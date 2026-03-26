import argparse
import csv
import os

def process_file(file_path, save_summary=False):
    if not os.path.exists(file_path):
        print("❌ El archivo no existe")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    total_rows = len(rows) - 1  # sin header
    total_columns = len(rows[0]) if rows else 0

    print(f"📄 Archivo: {file_path}")
    print(f"🔢 Filas: {total_rows}")
    print(f"📊 Columnas: {total_columns}")

    if save_summary:
        with open("summary.txt", "w") as f:
            f.write(f"Archivo: {file_path}\n")
            f.write(f"Filas: {total_rows}\n")
            f.write(f"Columnas: {total_columns}\n")

        print("✅ Resumen guardado en summary.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesar un CSV local")

    parser.add_argument("file", help="Ruta del archivo CSV")
    parser.add_argument("--save", action="store_true", help="Guardar resumen en archivo")

    args = parser.parse_args()

    process_file(args.file, args.save)