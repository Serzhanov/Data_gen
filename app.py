import streamlit as st
import os
from PIL import Image
from augmente_script import augment_images_in_folder
import utils
import generator
# Assurez-vous d'inclure vos fonctions de génération d'images ici
import re


def generate_carte_vitale_images(number_of_images):
    image_path = 'carte_vitale.jpg'
    json_path = 'carte_vitale.json'
    for i in range(number_of_images):
        print(f"Generating image {i+1}")
        d_json = generator.generate_dict_with_replacement(json_path)
        image = utils.create_text_on_image(image_path, d_json)
        save_status = utils.save_pil_image(image)
        print(save_status)


def display_images_from_folder_result(folder_path, number_of_last_images=1):
    if not os.listdir(folder_path):
        print(f"No files found in {folder_path}")
        return

    # Extract and sort files by the numeric part in their names
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    image_files.sort(key=lambda x: int(re.findall(r"(\d+)", x)[0]))

    # Display only the last 'number_of_last_images' images
    for image_file in image_files[-number_of_last_images:]:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        st.image(image, caption=image_file)


def display_images_from_folder_augmented(folder_path, number_of_last_images=1):
    if not os.listdir(folder_path):
        print(f"No files found in {folder_path}")
        return

    # Extract and sort files by the numeric part in their names
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    image_files.sort(key=lambda x: int(re.findall(r"(\d+)", x)[0]))

    # Display only the last 'number_of_last_images' images
    for image_file in image_files[-number_of_last_images:]:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        st.image(image, caption=image_file)


if 'generated_images' not in st.session_state:
    st.session_state['generated_images'] = []
if 'augmented_images' not in st.session_state:
    st.session_state['augmented_images'] = []


def update_image_list(folder_path, image_list_name, number_of_last_images):
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    image_files.sort(key=lambda x: int(re.findall(r"(\d+)", x)[0]))
    st.session_state[image_list_name] = image_files[-number_of_last_images:]


def display_images(image_list, folder_path):
    for image_file in image_list:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        st.image(image, caption=image_file)


# Streamlit interface
st.title("Générateur de Carte Vitale")

number = st.number_input(
    "Combien de cartes vitale voulez-vous générer?", min_value=1, max_value=100, value=1)
folder_res = 'results'
backup_folder = 'backup'
augmented_folder = 'augmented_data'

# Display generated images
st.header("Images Générées")
if st.button('Générer des Images'):
    generate_carte_vitale_images(number)
    update_image_list(folder_res, 'generated_images', number)
display_images(st.session_state['generated_images'], folder_path=folder_res)

# Display augmented images
st.header("Images Augmentées")
if st.button('Générer des Images Augmentées'):
    augment_images_in_folder(folder_res, augmented_folder, backup_folder)
    update_image_list(augmented_folder, 'augmented_images', number)
display_images(st.session_state['augmented_images'],
               folder_path=augmented_folder)
