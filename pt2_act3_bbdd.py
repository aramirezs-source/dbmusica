import sqlite3
import os

# Ruta absoluta al mateix directori que l'script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, "grups_musica.db")

# Crea la taula si no existeix
def crear_taula():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_grup TEXT NOT NULL,
            any_inici INTEGER,
            tipus_musica TEXT,
            num_integrants INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Afegeix un nou grup
def afegir_grup(nom_grup, any_inici, tipus_musica, num_integrants):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO grups (nom_grup, any_inici, tipus_musica, num_integrants)
        VALUES (?, ?, ?, ?)
    ''', (nom_grup, any_inici, tipus_musica, num_integrants))
    conn.commit()
    conn.close()
    print(f"Grup '{nom_grup}' afegit correctament.")

# Mostra tots els grups
def mostrar_grups():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grups')
    grups = cursor.fetchall()
    conn.close()

    if grups:
        print("\nLlista de grups:")
        for grup in grups:
            print(f"ID: {grup[0]}, Nom: {grup[1]}, Any inici: {grup[2]}, Tipus: {grup[3]}, Integrants: {grup[4]}")
    else:
        print("\nNo hi ha grups a la base de dades.")

# Actualitza un grup pel nom
def actualitzar_grup(nom_grup, nou_nom_grup=None, any_inici=None, tipus_musica=None, num_integrants=None):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    nom_grup_original = nom_grup

    if nou_nom_grup:
        cursor.execute('UPDATE grups SET nom_grup = ? WHERE nom_grup = ?', (nou_nom_grup, nom_grup_original))
        nom_grup_original = nou_nom_grup 

    if any_inici:
        cursor.execute('UPDATE grups SET any_inici = ? WHERE nom_grup = ?', (any_inici, nom_grup_original))
    if tipus_musica:
        cursor.execute('UPDATE grups SET tipus_musica = ? WHERE nom_grup = ?', (tipus_musica, nom_grup_original))
    if num_integrants:
        cursor.execute('UPDATE grups SET num_integrants = ? WHERE nom_grup = ?', (num_integrants, nom_grup_original))

    conn.commit()
    conn.close()
    print(f"Grup amb nom '{nom_grup}' actualitzat correctament.")

# Elimina un grup pel nom
def eliminar_grup(nom_grup):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM grups WHERE nom_grup = ?', (nom_grup,))
    conn.commit()
    conn.close()
    print(f"Grup amb nom '{nom_grup}' eliminat correctament.")

# Menú principal
def menu():
    crear_taula()
    while True:
        print("###################################################################")
        print("#################### GRUPS DE MÚSICA en CATALÀ ####################")
        print("###################################################################")
        print("\n--- Menú ---")
        print("1. Afegir un nou grup de música en català")
        print("2. Mostrar tots els grups de música en català")
        print("3. Actualitza un  grup de música en català")
        print("4. Elimina un dels grups de música en català")
        print("0. Sortir")
        opcio = input("Tria una opció: ")

        if opcio == "1":
            nom = input("Nom del grup: ")
            any_inici = int(input("Any d'inici: "))
            tipus = input("Tipus de música: ")
            integrants = int(input("Nombre d'integrants: "))
            afegir_grup(nom, any_inici, tipus, integrants)
        elif opcio == "2":
            mostrar_grups()
        elif opcio == "3":
            actualitzar_grup(nom_grup=input("Nom del grup a actualitzar: "),
                            nou_nom_grup=input("Nou nom del grup (deixeu en blanc per no canviar): "),
                            any_inici=input("Nou any d'inici (deixeu en blanc per no canviar): "),
                            tipus_musica=input("Nou tipus de música (deixeu en blanc per no canviar): "),
                            num_integrants=input("Nou nombre d'integrants (deixeu en blanc per no canviar): "))
        elif opcio == "4":
            eliminar_grup(input("Nom del grup a eliminar: "))
        elif opcio == "0":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Torna-ho a provar.")

if __name__ == "__main__":
    menu()