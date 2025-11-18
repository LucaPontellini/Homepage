import os
import re
import subprocess
import sys
import platform
import hashlib
import requests

def choose_system():
    print("\n🌍 Seleziona il tuo sistema operativo:")
    print("  [1] Windows")
    print("  [2] Linux")
    print("  [3] macOS")
    choice = input("👉 Inserisci il numero corrispondente (o premi Invio per rilevamento automatico): ").strip()
    if choice == "1":
        return "Windows"
    elif choice == "2":
        return "Linux"
    elif choice == "3":
        return "Darwin"
    else:
        return platform.system()

def get_activate_command(env_name, system_override=None):
    system = system_override or platform.system()
    if system == "Windows":
        return f"{env_name}\\Scripts\\activate.bat"
    elif system in ["Linux", "Darwin"]:
        return f"source {env_name}/bin/activate"
    else:
        return f"<attivazione non definita per {system}>"

def detect_existing_venv():
    for item in os.listdir('.'):
        if os.path.isdir(item):
            if platform.system() == 'Windows':
                if os.path.exists(os.path.join(item, 'Scripts', 'activate.bat')):
                    return item
            else:
                if os.path.exists(os.path.join(item, 'bin', 'activate')):
                    return item
    return None

def python_path(env_name):
    return os.path.join(env_name, 'Scripts' if platform.system() == 'Windows' else 'bin', 'python')

def ensure_pip_in_venv(env_name):
    try:
        subprocess.run([python_path(env_name), '-m', 'ensurepip', '--upgrade'])
        subprocess.run([python_path(env_name), '-m', 'pip', 'install', '--upgrade', 'pip'])
    except Exception as e:
        print(f"⚠️ Errore durante ensurepip: {e}")

def create_virtualenv(env_name='venv'):
    subprocess.run([sys.executable, '-m', 'venv', env_name])
    print(f"✅ Ambiente virtuale creato: {env_name}")
    ensure_pip_in_venv(env_name)
    return env_name

def ensure_stdlib_list_installed(env_name):
    try:
        result = subprocess.run([python_path(env_name), '-m', 'pip', 'show', 'stdlib-list'], capture_output=True, text=True)
        if result.returncode != 0 or 'Name: stdlib-list' not in result.stdout:
            print("📦 stdlib-list non trovato. Lo installo...")
            subprocess.run([python_path(env_name), '-m', 'pip', 'install', 'stdlib-list'])
        else:
            print("✅ stdlib-list già presente.")
    except Exception as e:
        print(f"⚠️ Errore durante il controllo/installazione di stdlib-list: {e}")

def get_standard_modules():
    try:
        from stdlib_list import stdlib_list
        version = f"{sys.version_info.major}.{sys.version_info.minor}"
        try:
            return set(stdlib_list(version)).union(set(sys.builtin_module_names))
        except Exception:
            print("⚠️ stdlib-list non supporta questa versione, uso fallback 3.13")
            return set(stdlib_list("3.13")).union(set(sys.builtin_module_names))
    except Exception as e:
        print(f"❌ Errore durante l'import di stdlib_list: {e}")
        return set()

def is_pypi_package(package_name):
    try:
        response = requests.head(f"https://pypi.org/pypi/{package_name}/json", timeout=3)
        return response.status_code == 200
    except requests.RequestException:
        return False

EXCLUDED_MODULES = set()
MANUAL_MAP = {
    'OpenSSL': 'pyOpenSSL',
    'ConfigParser': 'configparser',
    'HTMLParser': 'html.parser',
    'odf': 'odfpy',
    'fpdf': 'fpdf',
    'openpyxl': 'openpyxl'
}

def find_imports(path):
    imports = set()
    pattern = re.compile(r'^\s*(?:import|from)\s+([a-zA-Z0-9_\.]+)')
    local_modules = set()
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                local_modules.add(os.path.splitext(file)[0])
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        for line in f:
                            match = pattern.match(line)
                            if match:
                                module = match.group(1).split('.')[0]
                                if module not in local_modules:
                                    imports.add(module)
                except Exception as e:
                    print(f"⚠️ Errore nel file {file}: {e}")
    return imports

def map_to_pypi(imports):
    ignored = []
    valid = []
    for pkg in imports:
        if pkg in EXCLUDED_MODULES or pkg.startswith('_') or len(pkg) <= 1:
            ignored.append(pkg)
        elif pkg in MANUAL_MAP:
            valid.append(MANUAL_MAP[pkg])
        else:
            valid.append(pkg)
    return sorted(set(valid)), sorted(set(ignored))

def get_installed_packages(env_name):
    try:
        result = subprocess.run([python_path(env_name), '-m', 'pip', 'freeze'], capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')
        packages = set()
        for line in lines:
            if '==' in line:
                pkg = line.split('==')[0].strip()
                packages.add(pkg)
        return packages
    except Exception as e:
        print(f"⚠️ Errore durante il rilevamento dei pacchetti installati: {e}")
        return set()

def hash_file(path):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def write_requirements(packages):
    new_content = '\n'.join(sorted(packages)) + '\n'
    old_hash = hash_file('requirements.txt')
    new_hash = hashlib.md5(new_content.encode()).hexdigest()
    if old_hash == new_hash:
        print("📦 requirements.txt invariato. Nessuna modifica necessaria.")
        return False
    with open('requirements.txt', 'w') as f:
        f.write(new_content)
    print("📦 requirements.txt aggiornato con", len(packages), "pacchetti.")
    return True

def install_requirements(env_name):
    print("📥 Installazione delle dipendenze in corso...")
    result = subprocess.run([python_path(env_name), '-m', 'pip', 'install', '-r', 'requirements.txt'], capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Tutte le dipendenze installate correttamente.")
        return

    print("⚠️ Errore durante l'installazione. Analizzo i pacchetti problematici...")
    failed = []
    for line in result.stderr.splitlines():
        if "No matching distribution found for" in line:
            pkg = line.split("for")[-1].strip()
            failed.append(pkg)

    if failed:
        print("🧹 Rimuovo i pacchetti non installabili:", ", ".join(failed))
        try:
            with open("requirements.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open("requirements.txt", "w", encoding="utf-8") as f:
                for line in lines:
                    if not any(pkg.lower() == line.strip().lower() for pkg in failed):
                        f.write(line)
            EXCLUDED_MODULES.update(failed)
            print("🔁 Riprovo l'installazione...")
            retry = subprocess.run([python_path(env_name), '-m', 'pip', 'install', '-r', 'requirements.txt'], capture_output=True, text=True)
            if retry.returncode == 0:
                print("✅ Installazione completata dopo la correzione automatica.")
            else:
                print("❌ Installazione fallita anche dopo la correzione. Controlla manualmente i pacchetti.")
        except Exception as e:
            print(f"❌ Errore durante la rimozione dei pacchetti non validi: {e}")
    else:
        print("❌ Errore non riconosciuto. Controlla manualmente l'output di pip.")

def main():
    print("🔧 Setup ambiente virtuale Python")
    system = choose_system()

    print("🔍 Analisi dei file Python in corso...")
    venv = detect_existing_venv()
    if venv:
        print(f"🧠 Ambiente virtuale rilevato: {venv}")
        ensure_pip_in_venv(venv)
    else:
        print("⚠️ Nessun ambiente virtuale trovato. Lo creo ora...")
        venv = create_virtualenv()

    # Controllo e installazione stdlib-list
    ensure_stdlib_list_installed(venv)

    # Gestione moduli standard
    global EXCLUDED_MODULES
    EXCLUDED_MODULES = get_standard_modules()
    EXCLUDED_MODULES.update({'Queue', 'StringIO', 'cgi', 'compression', 'distutils'})

    # Analisi degli import nei file Python
    imports = find_imports('.')
    valid, ignored = map_to_pypi(imports)
    installed = get_installed_packages(venv)

    print("🔎 Verifica dei pacchetti su PyPI...")
    combined = set(valid).union(installed)
    all_packages = {pkg for pkg in combined if is_pypi_package(pkg)}

    # Aggiornamento requirements.txt
    updated = write_requirements(all_packages)

    # Installazione pacchetti
    if updated:
        install_requirements(venv)
    else:
        print("📥 Nessuna installazione necessaria: ambiente già aggiornato.")

    # Comando di attivazione
    activate_cmd = get_activate_command(venv, system_override=system)
    print(f"\n🚀 Per attivare l'ambiente virtuale:\n{activate_cmd}")

    # Moduli ignorati
    if ignored:
        print("\n📄 Moduli ignorati (non installabili o locali):")
        for mod in ignored:
            print(" -", mod)

    # Comandi utili
    print("\n📘 Comandi utili per gestire il tuo ambiente virtuale:")
    print("────────────────────────────────────────────────────────")
    print("🔹 Attivazione:")
    print(f"    {activate_cmd}")
    print("🔹 Disattivazione:")
    print("    deactivate")
    print("🔹 Installazione pacchetti:")
    print("    python -m pip install nome_pacchetto")
    print("🔹 Aggiornamento requirements.txt:")
    print("    python setup_env.py")
    print("🔹 Ricostruzione ambiente da zero:")
    print("    python -m venv .venv")
    print("    python -m pip install -r requirements.txt")
    print("────────────────────────────────────────────────────────")

if __name__ == "__main__":
    main()