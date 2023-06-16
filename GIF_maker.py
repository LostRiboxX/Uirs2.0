import os
import re
import imageio

def create_gif_from_folders(folders, output_path):
    images = []
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        image_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')], key=lambda x: int(re.search(r'\d+', x).group()))

        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            image = imageio.imread(image_path)
            images.append(image)

    output_folder = os.path.dirname(output_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    imageio.mimsave(output_path, images, duration=0.1)


folders = ['rot0', 'line1', 'rot1', 'line2', 'rot2', 'line3', 'rot3']  # Массив с названиями папок
output_path = 'output/result.gif'  # Путь для сохранения GIF

create_gif_from_folders(folders, output_path)