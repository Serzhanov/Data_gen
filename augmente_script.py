import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from PIL import Image
import shutil

import os
import shutil
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from PIL import Image

def augment_images_in_folder(folder_path,dir_save=None, backup_folder_path=None, grayscale_probability=0.6):
    if backup_folder_path:
        if not os.path.exists(backup_folder_path):
            os.makedirs(backup_folder_path)
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"): 
                shutil.copy2(os.path.join(folder_path, filename), os.path.join(backup_folder_path, filename))

    data_gen = ImageDataGenerator(
        rotation_range=5,
        width_shift_range=0.01,
        height_shift_range=0.05,
        shear_range=0.01,
        zoom_range=0.1,
        fill_mode='nearest'
    )

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            image_path = os.path.join(folder_path, filename)
            img = load_img(image_path)
            img_array = img_to_array(img)
            img_array = img_array.reshape((1,) + img_array.shape)

            transformed_image = next(data_gen.flow(img_array, batch_size=1))[0]

            # Randomly convert to grayscale based on the specified probability
            if random.random() < grayscale_probability:
                transformed_image = Image.fromarray(transformed_image.astype('uint8')).convert('L')
            else:
                transformed_image = Image.fromarray(transformed_image.astype('uint8'), 'RGB')

            transformed_image.save(dir_save+'/'+filename)
