from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import os


def create_text_on_image(image_path, d_json, font_size=110, pad=(0, 0, 0, 0), font_path="font/Arial.ttf"):
    dst_rgb = create_new_image_from_mask(image_path, d_json)
    dst_rgb_pil = Image.fromarray(dst_rgb)
    draw = ImageDraw.Draw(dst_rgb_pil)
    font_size = font_size  # Font size
    font = ImageFont.truetype(font_path, font_size)

    for annotation_data in d_json:
        for annotation in annotation_data['annotations']:
            for result in annotation['result']:
                if 'text' in result['value'] and result['value']['text'].lower() != 'image':
                    text = result['value']['text']
                    x = int(result['value']['x'] / 100 *
                            result['original_width'])
                    y = int(result['value']['y'] / 100 *
                            result['original_height'])

                    # Calculate the text dimensions
                    # Convert to integer
                    text_width = int(draw.textlength(text, font=font))
                    text_height = int(font_size)  # Convert to integer

                    # Create a transparent image for the text
                    text_image = Image.new(
                        'RGBA', (text_width, text_height), (255, 255, 255, 0))
                    draw_text = ImageDraw.Draw(text_image)
                    draw_text.text((0, 0), text, font=font, fill=(0, 0, 0))

                    if result['value']['rectanglelabels'][0] == 'cardId':
                        text_image = text_image.rotate(90, expand=1)

                    dst_rgb_pil.paste(
                        text_image, (x+pad[0]-pad[1], y+pad[2]-pad[3]), text_image)

    return dst_rgb_pil


def create_new_image_from_mask(img_path, json_data):
    print("Reading original image...")
    img = cv2.imread(img_path)
    height, width = img.shape[:2]
    print(f"Image dimensions: {width}x{height}")

    print("Creating mask from JSON data...")
    mask = create_mask_from_json(json_data, width, height)

    print("Performing inpainting...")
    dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    print("Converting image to RGB...")
    dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    return dst_rgb


def save_pil_image(image):
    try:
        print("Generating file path...")
        filepath = generate_file_path('results/cv', 'jpg')
        print(f"Saving image to {filepath}...")

        # Assuming 'image' is already a PIL Image object
        image.save(filepath, format='JPEG')  # Explicitly setting the format
        return f"Image saved successfully at {filepath}."
    except Exception as e:
        return f"Error in saving the image: {e}"


def generate_file_path(base_path, extension, max_tries=100):
    folder, base_filename = os.path.split(base_path)
    if not os.path.exists(folder):
        print(f"Creating folder: {folder}")
        os.makedirs(folder)

    for i in range(1, max_tries + 1):
        file_path = os.path.join(folder, f"{base_filename}_{i}.{extension}")
        if not os.path.exists(file_path):
            print(f"File path available: {file_path}")
            return file_path
    return None


def create_mask_from_json(json_data, image_width, image_height):
    # Create a black mask
    mask_image = np.zeros((image_height, image_width), dtype=np.uint8)

    # Process each annotation result
    for annotation in json_data[0]['annotations']:
        for result in annotation['result']:
            value = result['value']

            # Calculate the coordinates for the rectangle
            x = int(value['x'] / 100 * image_width)
            y = int(value['y'] / 100 * image_height)
            width = int(value['width'] / 100 * image_width)
            height = int(value['height'] / 100 * image_height)

            # Draw a white rectangle on the mask
            mask_image = cv2.rectangle(
                mask_image, (x, y), (x + width, y + height), 255, -1)

    return mask_image
