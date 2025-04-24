# 🎶 Gestor de Grups de Música en Català

Aquest projecte és una aplicació de terminal feta amb **Python** i **SQLite** per gestionar una base de dades de grups de música. Permet afegir, consultar, modificar i eliminar informació sobre grups musicals catalans.

## 📁 Descripció del projecte

El programa ofereix un menú interactiu per:
- Afegir un nou grup de música.
- Consultar tots els grups.
- Actualitzar les dades d’un grup pel seu nom.
- Eliminar un grup pel seu nom.
- Validar la informació introduïda per l'usuari.

La informació es desa en una base de dades SQLite anomenada `grups_musica.db`.

## 🧱 Estructura del codi

- **`crear_taula()`**: Crea la taula a la base de dades si no existeix.
- **`afegir_grup()`**: Insereix un nou registre a la base de dades.
- **`mostrar_grups()`**: Llista tots els grups emmagatzemats.
- **`actualitzar_grup()`**: Actualitza les dades d’un grup identificat pel seu nom.
- **`eliminar_grup()`**: Esborra un grup pel nom.
- **`intro_dades()`**: Funció reutilitzable per introduir i validar dades, compatible amb l'afegit i l'actualització.
- **`menu()`**: Menú principal interactiu per executar les accions anteriors.

## ▶️ Instruccions d'ús

1. Assegura’t de tenir Python instal·lat.
2. Desa el codi en un fitxer `.py`, per exemple: `gestor_grups.py`
3. Executa el programa amb:
   ```bash
   python gestor_grups.py
   ```
4. Segueix el menú per introduir o consultar dades.

La base de dades `grups_musica.db` es crearà automàticament al primer ús.

## 👤 Crèdits i autoria

Aquest projecte ha estat desenvolupat com a pràctica educativa en programació amb Python i bases de dades SQLite.

**Autor/a**: *[El teu nom aquí]*  
**Data**: Abril 2025  
