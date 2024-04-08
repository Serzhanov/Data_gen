import streamlit as st
import os
from PIL import Image

import utils
import generator
# Assurez-vous d'inclure vos fonctions de génération d'images ici


def generate_carte_vitale_images(number_of_images):
    image_path = 'carte_vitale.jpg'
    json_path = 'carte_vitale.json'
    for i in range(number_of_images):
        print(f"Generating image {i+1}")
        d_json = generator.generate_dict_with_replacement(json_path)
        image = utils.create_text_on_image(image_path, d_json)
        save_status = utils.save_pil_image(image)
        print(save_status)

def display_images_from_folder(folder_path):
    if not os.listdir(folder_path):
        print(f"No files found in {folder_path}")
    for image_file in os.listdir(folder_path):
        if image_file.endswith('.jpg'):
            image_path = os.path.join(folder_path, image_file)
            image = Image.open(image_path)
            st.image(image, caption=image_file)

# Streamlit interface
st.title("Générateur de Carte Vitale")

number = st.number_input("Combien de cartes vitale voulez-vous générer?", min_value=1, max_value=100, value=1)
folder_path = 'results' # Définissez le chemin de votre dossier d'images

if st.button('Générer des Images'):
    generate_carte_vitale_images(number)
    display_images_from_folder(folder_path)
