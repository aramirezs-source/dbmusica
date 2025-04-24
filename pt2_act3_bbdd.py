import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, "grups_musica.db")

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

from datetime import datetime

def intro_dades(nom=None):
    """
    Introdueix i valida les dades. 
    Si 'nom' és None → creació, tots els camps obligatoris.
    Si 'nom' té valor → actualització, es poden deixar camps en blanc.
    """
    actualitzant = nom is not None
    print(f"{'Actualització' if actualitzant else 'Creació'} de dades:")
    
    # Nom del grup
    while True:
        nou_nom = input("Nou nom del grup: " if actualitzant else "Nom del grup: ").strip()
        if not nou_nom and not actualitzant:
            print(" El nom no pot estar buit.")
        else:
            break

    # Any d'inici
    while True:
        any_inici_input = input("Nou any d'inici: " if actualitzant else "Any d'inici: ").strip()
        if not any_inici_input:
            any_inici = None if actualitzant else print(" L'any d'inici és obligatori.")
            if actualitzant: break
        else:
            try:
                any_inici = int(any_inici_input)
                any_actual = datetime.now().year
                if 1900 <= any_inici <= any_actual:
                    break
                else:
                    print(f" Introdueix un any entre 1900 i {any_actual}.")
            except ValueError:
                print(" L'any ha de ser un número enter.")

    # Tipus de música
    while True:
        tipus = input("Nou tipus de música: " if actualitzant else "Tipus de música: ").strip()
        if not tipus and not actualitzant:
            print(" El tipus de música és obligatori.")
        else:
            break

    # Nombre d'integrants
    while True:
        integrants_input = input("Nou nombre d'integrants: " if actualitzant else "Nombre d'integrants: ").strip()
        if not integrants_input:
            num_integrants = None if actualitzant else print("El nombre d'integrants és obligatori.")
            if actualitzant: break
        else:
            try:
                num_integrants = int(integrants_input)
                if num_integrants > 0:
                    break
                else:
                    print("El nombre d'integrants ha de ser major que zero.")
            except ValueError:
                print("El nombre d'integrants ha de ser un número enter.")

    return (nou_nom or None), any_inici, (tipus or None), num_integrants

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

def consultar_grup(nom_grup):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grups WHERE nom_grup = ?', (nom_grup,))
    grup = cursor.fetchone()
    conn.close()

    if grup:
        print(f"ID: {grup[0]}, Nom: {grup[1]}, Any inici: {grup[2]}, Tipus: {grup[3]}, Integrants: {grup[4]}")
    else:
        print(f"No s'ha trobat cap grup amb nom '{nom_grup}'.")

def actualitzar_grup(nom_grup):
    nou_nom, any_inici, tipus_musica, num_integrants = intro_dades(nom=nom_grup)

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    if nou_nom:
        cursor.execute('UPDATE grups SET nom_grup = ? WHERE nom_grup = ?', (nou_nom, nom_grup))
        nom_grup = nou_nom
    if any_inici is not None:
        cursor.execute('UPDATE grups SET any_inici = ? WHERE nom_grup = ?', (any_inici, nom_grup))
    if tipus_musica:
        cursor.execute('UPDATE grups SET tipus_musica = ? WHERE nom_grup = ?', (tipus_musica, nom_grup))
    if num_integrants is not None:
        cursor.execute('UPDATE grups SET num_integrants = ? WHERE nom_grup = ?', (num_integrants, nom_grup))

    conn.commit()
    conn.close()
    print(f"Grup '{nom_grup}' actualitzat correctament.")

def eliminar_grup(nom_grup):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM grups WHERE nom_grup = ?', (nom_grup,))
    conn.commit()
    conn.close()
    print(f"Grup '{nom_grup}' eliminat correctament.")

def menu():
    crear_taula()
    while True:
        print("###################################################################")
        print("#################### GRUPS DE MÚSICA en CATALÀ ####################")
        print("###################################################################")
        print("\n--- Menú ---")
        print("1. Afegir un nou grup de música en català")
        print("2. Mostrar tots els grups de música en català")
        print("3. Consultar un grup per nom")
        print("4. Actualitza un grup de música en català")
        print("5. Elimina un grup de música en català")
        print("0. Sortir")
        opcio = input("Tria una opció: ")

        if opcio == "1":
            nom, any_inici, tipus, integrants = intro_dades()
            if nom and any_inici and tipus and integrants:
                afegir_grup(nom, any_inici, tipus, integrants)
            else:
                print("Tots els camps són obligatoris per afegir un nou grup.")
        elif opcio == "2":
            mostrar_grups()
        elif opcio == "3":
            consultar_grup(input("Nom del grup a consultar: "))
        elif opcio == "4":
            actualitzar_grup(input("Nom del grup a actualitzar: "))
        elif opcio == "5":
            eliminar_grup(input("Nom del grup a eliminar: "))
        elif opcio == "0":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Torna-ho a provar.")

if __name__ == "__main__":
    menu()
