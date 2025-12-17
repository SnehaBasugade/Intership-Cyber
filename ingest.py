import pandas as pd
from features import extract_features
from db import create_db, insert_url

# Make sure database exists
create_db()

# Function to ingest CSV file
def ingest_csv(file_path, label):
    df = pd.read_csv(file_path)  # CSV must have a column named 'url'
    for url in df['url']:
        features = extract_features(url)
        data = (url, label, *features, None)  # prediction=None
        insert_url(data)

# Function to insert a single URL
def insert_single_url(url, label):
    features = extract_features(url)
    data = (url, label, *features, None)
    insert_url(data)
    print(f"Inserted URL: {url}")