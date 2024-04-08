import random
from datetime import datetime
import json

def generate_date():
    random_date = datetime.strptime('{} {}'.format(random.randint(1, 366), 2024), '%j %Y')
    formatted_date = random_date.strftime('%d/%m/%Y')
    print(f"Generated Date: {formatted_date}")
    return 'émise le '+formatted_date

def generate_firstname():
    first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen"]
    random_first_name = random.choice(first_names)
    print(f"Generated First Name: {random_first_name}")
    return random_first_name

def generate_lastname():
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
    random_last_name = random.choice(last_names)
    print(f"Generated Last Name: {random_last_name}")
    return random_last_name

def generate_insurance_code():
    parts = [
        str(1),
        f"{random.randint(80, 99)}",
        f"{random.randint(1, 12)}",
        f"{random.randint(80, 99)}",
        f"{random.randint(100, 999)}",
        f"{random.randint(100, 999)}",
        f"{random.randint(10, 99)}"
    ]
    insurance_code = ' '.join(parts)
    print(f"Generated Insurance Code: {insurance_code}")
    return insurance_code

def generate_card_id():
    part1 = ''.join(str(random.randint(0, 9)) for _ in range(10))
    part2 = ''.join(str(random.randint(0, 9)) for _ in range(10))
    part3 = str(random.randint(0, 9))

    card_id = f"{part1} {part2} {part3}"
    print(f"Generated Card ID: {card_id}")
    return card_id

def read_json_from_path(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f"Read data from {file_path}")
        return data
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return str(e)

def add_key_to_values(json_data, key, value):
    for annotation in json_data[0]['annotations']:
        for result in annotation['result']:
            if result['value']['rectanglelabels'][0] == key:
                result['value']['text'] = value
                print(f"Added {key}: {value}")
    return json_data

def generate_dict_with_replacement(path):
    d_json = read_json_from_path(path)

    d_json = add_key_to_values(d_json, 'Date', generate_date())
    d_json = add_key_to_values(d_json, 'LastName', generate_lastname())
    d_json = add_key_to_values(d_json, 'FirstName', generate_firstname())
    d_json = add_key_to_values(d_json, 'InsuranceCode', generate_insurance_code())
    d_json = add_key_to_values(d_json, 'cardId', generate_card_id())
    return d_json

# Example usage (be sure to provide an actual file path)
# path_to_json = 'path_to_your_json_file.json'
# updated_json = generate_dict_with_replacement(path_to_json)
