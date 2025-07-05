from PIL import Image
import numpy as np
import random
import os

def load_image(image_path):
    image = Image.open(image_path).convert('RGB')
    return np.array(image)

def save_image(np_array, output_path):
    encrypted_image = Image.fromarray(np_array.astype('uint8'), 'RGB')
    encrypted_image.save(output_path)
    print(f"Saved encrypted image to {output_path}")

def invert_colors(pixel_array):
    return 255 - pixel_array

def shuffle_pixels(pixel_array):
    original_shape = pixel_array.shape
    flat_pixels = pixel_array.reshape(-1, 3)
    np.random.shuffle(flat_pixels)
    return flat_pixels.reshape(original_shape)

def encrypt_image(image_path, output_path, method='invert'):
    pixels = load_image(image_path)

    if method == 'invert':
        encrypted_pixels = invert_colors(pixels)
    elif method == 'shuffle':
        encrypted_pixels = shuffle_pixels(pixels)
    else:
        raise ValueError("Unsupported encryption method. Use 'invert' or 'shuffle'.")

    save_image(encrypted_pixels, output_path)

# Example usage:
if __name__ == "__main__":
    input_image = "input.jpg"      # Replace with your image path
    output_image = "encrypted.jpg" # Output path

    # Choose 'invert' or 'shuffle'
    encrypt_image(input_image, output_image, method='invert')
