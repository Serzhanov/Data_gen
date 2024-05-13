import utils
import generator
import streamlit as st
import os
from PIL import Image


def generate_carte_vitale_images(number_of_images):
    image_path = 'carte_vitale.jpg'
    json_path = 'carte_vitale.json'
    for i in range(number_of_images):
        print(f"Generating image {i+1}")
        d_json = generator.generate_dict_with_replacement(json_path)
        image = utils.create_text_on_image(image_path, d_json)
        save_status = utils.save_pil_image(image)
        print(save_status)


def gemerate_residence_card_images(number_of_images):
    image_path = 'titre_sej_n.jpg'
    json_path = 'titre_sej.json'
    for i in range(number_of_images):
        print(f"Generating image {i+1}")
        d_json = generator.generate_dict_with_replacement_carte_resid(
            json_path)
        image = utils.create_text_on_image(
            image_path, d_json, 25, pad=(0, 0, 0, 5))
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


gemerate_residence_card_images(1)
display_images_from_folder('results')
# augmente_script.augment_images_in_folder('results','augmented_data','backup')
