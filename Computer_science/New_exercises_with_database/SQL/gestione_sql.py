import os
import sqlite3
import re

# 📁 Percorsi dinamici
base_folder = os.path.dirname(os.path.abspath(__file__))  # SQL/
sql_files_folder = os.path.join(base_folder, "folder_for_SQL_files")
python_files_folder = os.path.join(base_folder, "folder_for_Python_files")
db_path = os.path.join(base_folder, "db.sqlite")

def crea_database_se_manca():
    if not os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            conn.close()
            print("✅ Database creato all'avvio.")
        except Exception as e:
            print(f"❌ Errore nella creazione del database: {e}")
    else:
        print("ℹ️ Database già esistente.")

def elimina_database():
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
            print("🧹 Database eliminato.")
        except PermissionError:
            print("❌ Il file db.sqlite è aperto da un altro programma. Chiudilo e riprova.")
            exit()

def elimina_tutti_i_database_sqlite():
    for file in os.listdir(base_folder):
        if file.endswith(".sqlite"):
            try:
                os.remove(os.path.join(base_folder, file))
                print(f"🧹 Database eliminato: {file}")
            except PermissionError:
                print(f"❌ Impossibile eliminare {file}: è aperto da un altro programma.")

def ricrea_database():
    try:
        conn = sqlite3.connect(db_path)
        print("✅ Database ricreato correttamente.")
        return conn
    except Exception as e:
        print(f"❌ Errore nella creazione del database: {e}")
        return None

def controlla_sql(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        print("⚠️ Il file SQL è vuoto.")
        return False

    keywords = ["CREATE TABLE", "INSERT INTO", "SELECT", "UPDATE", "DELETE"]
    trovati = [kw for kw in keywords if kw.lower() in content.lower()]

    if not trovati:
        print("⚠️ Nessuna istruzione SQL rilevante trovata.")
        return False

    print(f"🔍 Il file contiene: {', '.join(trovati)}")
    return True

def riepilogo_tabelle(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    if not tables:
        print("📭 Nessuna tabella presente nel database.")
        return
    print("\n📊 Tabelle nel database:")
    for table_name in [t[0] for t in tables]:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"   - {table_name}: {count} righe")

def estrai_tabelle_da_sql(sql_text):
    pattern = r"\b(?:FROM|JOIN|UPDATE|INSERT INTO)\s+([a-zA-Z_][a-zA-Z0-9_]*)"
    return list(set(re.findall(pattern, sql_text, re.IGNORECASE)))

def check_tabelle_presenti(conn, tabelle_richieste):
    cursor = conn.cursor()
    cursor.execute("SELECT LOWER(name) FROM sqlite_master WHERE type='table';")
    tabelle_presenti = [row[0] for row in cursor.fetchall()]
    tabelle_mancanti = [t for t in tabelle_richieste if t.lower() not in tabelle_presenti]
    return tabelle_mancanti

# 📂 All'avvio: crea il database se non esiste
print("📂 Il database verrà resettato solo quando esegui un file SQL.")
print(f"📍 Percorso del database: {db_path}")
crea_database_se_manca()

while True:
    try:
        sql_files = [f for f in os.listdir(sql_files_folder) if f.endswith(".sql")]
    except FileNotFoundError:
        print(f"❌ Cartella dei file SQL non trovata: {sql_files_folder}")
        break

    try:
        py_files = [f for f in os.listdir(python_files_folder) if f.endswith(".py")]
    except FileNotFoundError:
        print(f"❌ Cartella dei file Python non trovata: {python_files_folder}")
        py_files = []

    if not sql_files and not py_files:
        print("📭 Nessun file SQL o Python trovato.")
        break

    # 🔢 Menu unificato
    print("\n📄 File disponibili:")
    file_menu = []
    for f in sql_files:
        file_menu.append(("sql", f))
    for f in py_files:
        file_menu.append(("py", f))

    for i, (tipo, nome) in enumerate(file_menu, 1):
        icona = "📄" if tipo == "sql" else "🐍"
        print(f"{i}. {icona} {nome}")

    scelta = input("\nInserisci il numero del file da eseguire (o 'esci' per uscire): ").strip()

    if scelta.lower() == "esci":
        break

    if not scelta.isdigit():
        print("❌ Inserimento non valido.")
        continue

    scelta_index = int(scelta) - 1
    if not (0 <= scelta_index < len(file_menu)):
        print("❌ Numero fuori intervallo.")
        continue

    tipo_file, nome_file = file_menu[scelta_index]

    if tipo_file == "py":
        os.system(f"python3 \"{os.path.join(python_files_folder, nome_file)}\"")
        elimina_tutti_i_database_sqlite()  # 🔥 Elimina eventuali database creati dallo script Python
        continue

    # SQL file selezionato
    file_path = os.path.join(sql_files_folder, nome_file)

    if not controlla_sql(file_path):
        conferma = input("Vuoi comunque eseguire il file? (sì/no): ").strip().lower()
        if conferma not in ["sì", "si", "y", "yes"]:
            print("⏭️ File saltato.")
            continue

    elimina_database()
    conn = ricrea_database()

    if conn is None:
        continue

    cursor = conn.cursor()

    with open(file_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

        tabelle_richieste = estrai_tabelle_da_sql(sql_script)
        try:
            cursor.executescript(sql_script)
        except Exception as e:
            print(f"\n❌ Errore durante l'esecuzione: {e}")
            conn.close()
            continue

        tabelle_mancanti = check_tabelle_presenti(conn, tabelle_richieste)
        if tabelle_mancanti:
            print("\n🚫 Il server ha eseguito il file, ma alcune tabelle richieste non sono presenti:")
            for tabella in tabelle_mancanti:
                print(f"❌ Tabella mancante: {tabella}")
        else:
            print(f"\n✅ {nome_file} eseguito con successo su db.sqlite.")
            print("✅ Il server è pronto. Tutte le tabelle necessarie sono presenti.")

    riepilogo_tabelle(cursor)
    conn.commit()
    conn.close()

# 🔚 Fine sessione: pulizia completa
elimina_tutti_i_database_sqlite()
print("\n👋 Fine sessione. Tutti i database .sqlite sono stati eliminati.")


#problema: i database creati dagli script python non vengono eliminati alla fine della sessione