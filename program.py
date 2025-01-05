import ctypes
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import pyautogui
import time

# Paths
ORIGINAL_IMAGE_PATH = "/mnt/data/IMG_1043.png"  # Uploaded image path
BMP_IMAGE_PATH = "IMG_1043.bmp"  # Converted BMP image for wallpaper

def convert_to_bmp(original_image_path, bmp_image_path):
    """Convert an image to BMP format (required for some Windows versions)."""
    try:
        with Image.open(original_image_path) as img:
            img = img.convert("RGB")  # Ensure it's in RGB mode, cuz it fucking need to </3
            img.save(bmp_image_path, "BMP")
    except Exception as e:
        print(f"Error converting image to BMP: {e}")

def change_wallpaper(bmp_image_path):
    """Change the desktop wallpaper to the given BMP image."""
    try:
        abs_path = os.path.abspath(bmp_image_path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)  # SPI_SETDESKWALLPAPER = 20
        print("Wallpaper changed successfully.")
    except Exception as e:
        print(f"Error changing wallpaper: {e}")

def open_notepad_and_type():
    """Open Notepad and type something silly."""
    try:
        subprocess.Popen(["notepad.exe"])  # Open Notepad
        time.sleep(2)  # Wait for Notepad to open
        pyautogui.typewrite("You thought you could close me, but I'm everywhere! :3", interval=0.1)
        print("Text typed in Notepad.")
    except Exception as e:
        print(f"Error opening Notepad or typing: {e}")

def show_error_dialog():
    """Show a fake error dialog."""
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the main tkinter window
        messagebox.showerror("Critical Error", "An unknown error occurred. Press OK to continue.")
        print("Error dialog shown.")
    except Exception as e:
        print(f"Error showing dialog: {e}")

# Main execution
if __name__ == "__main__":
    try:
        # Convert the uploaded image to BMP format
        convert_to_bmp(ORIGINAL_IMAGE_PATH, BMP_IMAGE_PATH)

        # Show fake error dialog
        show_error_dialog()

        # Regardless of user input, execute the payload
        change_wallpaper(BMP_IMAGE_PATH)
        open_notepad_and_type()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Cleanup the BMP image
        if os.path.exists(BMP_IMAGE_PATH):
            os.remove(BMP_IMAGE_PATH)
            print("Temporary BMP file removed.")
