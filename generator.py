import random
from datetime import datetime
import json
import random
import string


def generate_date(str_added=True):
    years = [2021, 2019, 2018, 2017, 2016, 2015, 2022, 2023, 2024]
    random_date = datetime.strptime('{} {}'.format(
        random.randint(1, 366),  random.choice(years)), '%j %Y')
    formatted_date = random_date.strftime('%d/%m/%Y')
    print(f"Generated Date: {formatted_date}")
    if str_added:
        return 'émise le '+formatted_date
    return formatted_date


def generate_firstname():
    first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William",
                   "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen"]
    random_first_name = random.choice(first_names)
    print(f"Generated First Name: {random_first_name}")
    return random_first_name


def generate_lastname():
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                  "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
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


def add_key_to_values(json_data, key, value, index_value=-1):
    if index_value != -1:
        for annotation in json_data[0]['annotations']:
            for idx, result in enumerate(annotation['result']):
                if idx == index_value and result['value']['rectanglelabels'][0] == key:
                    result['value']['text'] = value
                    print(f"Added {key}: {value}")
    else:
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
    d_json = add_key_to_values(
        d_json, 'InsuranceCode', generate_insurance_code())
    d_json = add_key_to_values(d_json, 'cardId', generate_card_id())
    return d_json


def generate_random_number(length):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def generate_sex_letter():
    return random.choice(['M', 'F'])


def generate_birth_date(start_year=1900, end_year=2023):
    # Generate a random year between start_year and end_year
    year = random.randint(start_year, end_year)

    # Generate a random month
    month = random.randint(1, 12)

    # Generate a random day based on month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:  # February
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)

    # Create a datetime object
    birth_date = datetime(year, month, day)

    # Return the date in dd/mm/yyyy format
    return birth_date.strftime("%d/%m/%Y")


def generate_random_number_with_letters(length, caps=False):
    # Combine the digits and ASCII letters for selection
    possible_characters = string.ascii_letters + string.digits

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(possible_characters)
                            for _ in range(length))

    # Convert to uppercase if caps is True
    if caps:
        random_string = random_string.upper()

    return random_string


def random_titre_de_sejour():
    titre_de_sejour_types = [
        "Salarié",
        "Visiteur",
        "Retraité",
        "Résident",
        "Permanent",
        "Travailleur",
        "Étudiant",
    ]

    # Return a random choice from the list
    return random.choice(titre_de_sejour_types)

    # Example usage (be sure to provide an actual file path)
    # path_to_json = 'path_to_your_json_file.json'
    # updated_json = generate_dict_with_replacement(path_to_json)


def generer_nationalite():
    nationalites = [
        "Afghane", "Albanaise", "Algérienne", "Américaine", "Andorrane", "Angolaise",
        "Antiguaise-et-Barbudienne", "Argentine", "Arménienne", "Australienne", "Autrichienne", "Azerbaïdjanaise",
        "Bahamienne", "Bahreïnienne", "Bangladaise", "Barbadienne", "Belge", "Bélizienne",
        "Béninoise", "Bhoutanaise", "Biélorusse", "Birmane", "Bolivienne", "Bosnienne",
        "Botswanaise", "Brésilienne", "Britannique", "Brunéienne", "Bulgare", "Burkinabée",
        "Burundaise", "Cambodgienne", "Camerounaise", "Canadienne", "Cap-verdienne",
        "Centrafricaine", "Chilienne", "Chinoise", "Chypriote", "Colombienne",
        "Comorienne", "Congolaise", "Costaricaine", "Croate", "Cubaine",
        "Danoise", "Djiboutienne", "Dominicaine", "Dominiquaise", "Égyptienne",
        "Émirienne", "Équato-guinéenne", "Équatorienne", "Érythréenne", "Espagnole",
        "Estonienne", "Américaine", "Éthiopienne", "Fidjienne", "Finlandaise",
        "Française", "Gabonaise", "Gambienne", "Géorgienne", "Ghanéenne",
        "Grecque", "Grenadienne", "Guatémaltèque", "Guinéenne", "Guinée-Bissau",
        "Guyanienne", "Haïtienne", "Hondurienne", "Hongroise", "Indienne",
        "Indonésienne", "Irakienne", "Iranienne", "Irlandaise", "Islandaise",
        "Israélienne", "Italienne", "Ivoirienne", "Jamaïcaine", "Japonaise",
        "Jordanienne", "Kazakhstanaise", "Kenyane", "Kirghize", "Kiribatienne",
        "Kosovare", "Koweïtienne", "Laotienne", "Lesothane", "Lettone",
        "Libanaise", "Libérienne", "Libyenne", "Liechtensteinoise", "Lituanienne",
        "Luxembourgeoise", "Macédonienne", "Malaisienne", "Malawienne", "Maldivienne",
        "Malgache", "Malienne", "Maltaise", "Marocaine", "Marshallaise",
        "Mauricienne", "Mauritanienne", "Mexicaine", "Micronésienne", "Moldave",
        "Monégasque", "Mongole", "Monténégrine", "Mozambicaine", "Namibienne",
        "Nauruane", "Néerlandaise", "Néo-Zélandaise", "Népalaise", "Nicaraguayenne",
        "Nigériane", "Nigérienne", "Nord-coréenne", "Norvégienne", "Omanaise",
        "Ougandaise", "Ouzbèke", "Pakistanaise", "Palauane", "Palestinienne",
        "Panaméenne", "Papouane-Néo-Guinéenne", "Paraguayenne", "Péruvienne", "Philippine",
        "Polonaise", "Portugaise", "Qatarienne", "Roumaine", "Russe",
        "Rwandaise", "Sainte-Lucienne", "Saint-Vincent-et-les Grenadines", "Salomonaise", "Salvadorienne",
        "Samoane", "Santoméenne", "Saoudienne", "Sénégalaise", "Serbe",
        "Seychelloise", "Sierra-Léonaise", "Singapourienne", "Slovaque", "Slovène",
        "Somalienne", "Soudanaise", "Sri-Lankaise", "Sud-Africaine", "Sud-coréenne",
        "Suédoise", "Suisse", "Surinamaise", "Swazie", "Syrienne",
        "Tadjike", "Tanzanienne", "Tchadienne", "Tchèque", "Thaïlandaise",
        "Togolaise", "Tongienne", "Trinidadienne", "Tunisienne", "Turkmène",
        "Turque", "Tuvaluane", "Ukrainienne", "Uruguayenne", "Vanuatuane",
        "Vénézuélienne", "Vietnamienne", "Yéménite", "Zambienne", "Zimbabwéenne"
    ]

    # Retourne un choix aléatoire de la liste
    return random.choice(nationalites)


def generate_dict_with_replacement_carte_resid(path):
    d_json = read_json_from_path(path)

    d_json = add_key_to_values(d_json, 'Date', generate_date(False), 3)
    d_json = add_key_to_values(d_json, 'LastName', generate_lastname())
    d_json = add_key_to_values(d_json, 'FirstName', generate_firstname())
    d_json = add_key_to_values(
        d_json, 'ResidenceType', random_titre_de_sejour())
    d_json = add_key_to_values(d_json, 'Date', generate_birth_date(), 2)
    d_json = add_key_to_values(d_json, 'Sex', generate_sex_letter())
    d_json = add_key_to_values(
        d_json, 'Number', generate_random_number_with_letters(10, True), 5)
    d_json = add_key_to_values(d_json, 'Number', generate_random_number(6), 6)
    d_json = add_key_to_values(d_json, 'Number', generate_random_number(9), 7)
    d_json = add_key_to_values(d_json, 'Number', generate_random_number(9), 8)
    d_json = add_key_to_values(d_json, 'Nationality', generer_nationalite())

    # d_json = add_key_to_values(
    #     d_json, 'InsuranceCode', generate_insurance_code())
    # d_json = add_key_to_values(d_json, 'cardId', generate_card_id())
    return d_json
