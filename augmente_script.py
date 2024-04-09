import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from PIL import Image
import shutil
import random
import numpy as np
import cv2
import os
import shutil
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from PIL import Image

# Custom preprocessing function for sharpening


def sharpen(img):
    if random.random() > 0.25:  # 75% chance to skip sharpening
        return img
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    img = cv2.filter2D(img, -1, kernel)
    return img

# Custom preprocessing function for random erasing


def random_erase(img):
    if random.random() > 0.25:  # 75% chance to skip cropping
        return img
    # Specify erasing parameters
    W, H = img.shape[1], img.shape[0]
    erase_percent = 0.1  # example proportion to erase

    # Compute area to erase
    Erase_area = int(erase_percent * W * H)

    # Randomly choose the location to start erasing
    x1 = np.random.randint(0, W)
    y1 = np.random.randint(0, H)

    # Calculate the dimensions of the rectangle
    h = np.random.randint(1, H - y1)
    w = Erase_area // h
    w = min(w, W - x1)
    h = min(h, Erase_area // w)

    img[y1:y1+h, x1:x1+w] = 0
    return img


def random_zoom(img):
    if random.random() > 0.25:  # 75% chance to skip zooming
        return img

    # Define zoom scale (example: zoom in by 20% to 40%)
    zoom_scale = random.uniform(1.2, 1.4)
    height, width = img.shape[:2]

    # Calculate the region to be cropped and resized (zoomed)
    new_height, new_width = int(height / zoom_scale), int(width / zoom_scale)
    start_x = np.random.randint(0, width - new_width)
    start_y = np.random.randint(0, height - new_height)
    zoomed_img = img[start_y:start_y + new_height, start_x:start_x + new_width]

    # Resize to original size
    return cv2.resize(zoomed_img, (width, height))


def augment_images_in_folder(folder_path, dir_save=None, backup_folder_path=None, grayscale_probability=0.6):
    if backup_folder_path:
        if not os.path.exists(backup_folder_path):
            os.makedirs(backup_folder_path)
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"):
                shutil.copy2(os.path.join(folder_path, filename),
                             os.path.join(backup_folder_path, filename))

    data_gen = ImageDataGenerator(
        rotation_range=5,
        width_shift_range=0.01,
        height_shift_range=0.05,
        shear_range=0.01,
        zoom_range=0.1,
        fill_mode='nearest',
        preprocessing_function=lambda img: sharpen(random_zoom(img))

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
                transformed_image = Image.fromarray(
                    transformed_image.astype('uint8')).convert('L')
            else:
                transformed_image = Image.fromarray(
                    transformed_image.astype('uint8'), 'RGB')

            transformed_image.save(dir_save+'/'+filename)
