import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, Label, Button, Entry

ASCII_CHARS = "@%#*+=-:. "

class ASCIIArtConverter:
    def __init__(self, master):
        self.master = master
        master.title("ASCII Art Converter")

        self.label = Label(master, text="Enter image path:")
        self.label.pack()

        self.image_path_entry = Entry(master, width=50)  # Menambahkan parameter width untuk membuat Entry lebih panjang
        self.image_path_entry.pack()

        self.browse_button = Button(master, text="Browse", command=self.browse_image)
        self.browse_button.pack()

        self.convert_button = Button(master, text="Convert to ASCII", command=self.convert_and_save)
        self.convert_button.pack()

    def browse_image(self):
        file_path = filedialog.askopenfilename()
        self.image_path_entry.delete(0, tk.END)
        self.image_path_entry.insert(0, file_path)

    def convert_and_save(self):
        image_path = self.image_path_entry.get()
        try:
            image = Image.open(image_path)
            ascii_img = self.convert_image_to_ascii(image)
            self.display_ascii_art(ascii_img)
            self.save_ascii_to_text(ascii_img)
        except Exception as e:
            self.display_error(f"Failed to open the image: {e}")

    def convert_image_to_ascii(self, image):
        image = self.resize_image(image, new_width=100)
        image = self.grayscale(image)
        ascii_str = self.pixels_to_ascii(image)
        img_width = image.width
        ascii_img = ""
        for i in range(0, len(ascii_str), img_width):
            ascii_img += ascii_str[i:i+img_width] + "\n"
        return ascii_img

    def resize_image(self, image, new_width=100):
        width, height = image.size
        ratio = height / width / 1.65
        new_height = int(new_width * ratio)
        resized_image = image.resize((new_width, new_height))
        return resized_image

    def grayscale(self, image):
        return image.convert("L")

    def pixels_to_ascii(self, image):
        pixels = image.getdata()
        ascii_str = ""
        for pixel_value in pixels:
            ascii_str += ASCII_CHARS[pixel_value // 32]
        return ascii_str

    def display_ascii_art(self, ascii_art):
        ascii_window = tk.Toplevel(self.master)
        ascii_label = Label(ascii_window, text=ascii_art, font=("Courier", 8))
        ascii_label.pack()

    def save_ascii_to_text(self, ascii_art):
        folder_path = "generated"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if output_file:
            with open(output_file, "w") as file:
                file.write(ascii_art)
            self.display_info(f"ASCII art saved successfully to {output_file}")

    def display_error(self, message):
        error_label = Label(self.master, text=message, fg="red")
        error_label.pack()

    def display_info(self, message):
        info_label = Label(self.master, text=message, fg="green")
        info_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ASCIIArtConverter(root)
    root.mainloop()
