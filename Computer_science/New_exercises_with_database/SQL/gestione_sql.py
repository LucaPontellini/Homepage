import os
import sqlite3
import re

# 📁 Percorso dinamico: cartella dove si trova lo script
sql_folder = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(sql_folder, "db.sqlite")

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
    # 📄 Mostra i file .sql disponibili
    sql_files = [f for f in os.listdir(sql_folder) if f.endswith(".sql")]
    print("\n📄 File SQL disponibili:")
    for i, file in enumerate(sql_files, 1):
        print(f"{i}. {file}")

    # 📥 Chiedi quale file eseguire
    scelta = input("\nInserisci il numero o il nome del file da eseguire (o 'esci' per uscire): ").strip()

    if scelta.lower() == "esci":
        break

    if scelta.isdigit():
        scelta_index = int(scelta) - 1
        if 0 <= scelta_index < len(sql_files):
            selected_file = sql_files[scelta_index]
        else:
            print("❌ Numero fuori intervallo.")
            continue
    elif scelta in sql_files:
        selected_file = scelta
    else:
        print("❌ Scelta non valida.")
        continue

    file_path = os.path.join(sql_folder, selected_file)

    if not controlla_sql(file_path):
        conferma = input("Vuoi comunque eseguire il file? (sì/no): ").strip().lower()
        if conferma not in ["sì", "si", "y", "yes"]:
            print("⏭️ File saltato.")
            continue

    # 🔄 Reset del database prima di eseguire il file selezionato
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
            print(f"\n✅ {selected_file} eseguito con successo su db.sqlite.")
            print("✅ Il server è pronto. Tutte le tabelle necessarie sono presenti.")

    riepilogo_tabelle(cursor)
    conn.commit()
    conn.close()

# 🧹 Elimina il database alla fine della sessione
elimina_database()

print("\n👋 Fine sessione. Il database è stato eliminato per evitare residui dalle esecuzioni precedenti.")