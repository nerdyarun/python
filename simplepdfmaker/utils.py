# simplepdfmaker/utils.py

import pandas as pd
import json
import os

UPLOADS_DIR = "uploads"
OUTPUTS_DIR = "outputs"

def ensure_folders():
    """Ensure uploads and outputs folders exist."""
    for folder in [UPLOADS_DIR, OUTPUTS_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✅ Created '{folder}/' folder.")

def parse_uploaded_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.endswith('.csv'):
        try:
            df = pd.read_csv(file_path)
        except pd.errors.EmptyDataError:
            raise ValueError("Uploaded CSV file is empty!")
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.json'):
        with open(file_path, 'r') as f:
            data = json.load(f)
        if isinstance(data, dict):
            data = [data]
        return data
    else:
        raise ValueError("Unsupported file format! Please upload CSV, XLSX, or JSON.")

    if df.empty:
        raise ValueError("Uploaded file is empty or invalid!")

    return df.to_dict(orient="records")