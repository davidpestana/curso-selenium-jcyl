import csv

def load_csv_data(file_path):
    """Carga los datos del CSV como lista de diccionarios"""
    data_rows = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row = {key: int(value) if value.isdigit() else value for key, value in row.items()}
            data_rows.append(row)
    return data_rows


