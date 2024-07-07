import json

def load_test_data(file_path='test_data/login_data.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
