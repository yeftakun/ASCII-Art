import os
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 32]
    return ascii_str

def convert_image_to_ascii(image):
    image = resize_image(image, new_width=100)
    image = grayscale(image)
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    return ascii_img

def save_ascii_to_text(ascii_img):
    folder_path = "generated"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    output_file = input("Masukkan nama file untuk menyimpan hasil ASCII art: ")
    output_path = os.path.join(folder_path, output_file)
    with open(output_path, "w") as file:
        file.write(ascii_img)
    print(f"Hasil ASCII art berhasil disimpan dalam file {output_path}")

def main():
    image_path = input("Masukkan path ke file gambar: ")
    try:
        image = Image.open(image_path)
        ascii_img = convert_image_to_ascii(image)
        print(ascii_img)
        save_ascii_to_text(ascii_img)
    except Exception as e:
        print(f"Gagal membuka gambar: {e}")

if __name__ == "__main__":
    main()
