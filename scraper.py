import pyautogui
import easyocr
from PIL import ImageGrab
import numpy as np

def scrape_text(left, top, right, bottom):
    # Create an OCR reader
    reader = easyocr.Reader(['en'])

    # Take a screenshot of the current screen
    screenshot = ImageGrab.grab()

    # Define the region where the Notepad application is located (adjust these coordinates according to your screen resolution)
    notepad_region = (left, top, right, bottom)  # Example: (left, top, width, height)

    # Crop the screenshot to the region of the Notepad application
    notepad_screenshot = screenshot.crop(notepad_region)

    # Convert the cropped screenshot to grayscale
    notepad_screenshot_gray = notepad_screenshot.convert('L')

    # Convert the cropped screenshot to a NumPy array
    notepad_screenshot_array = np.array(notepad_screenshot_gray)

    # Perform OCR on the NumPy array
    results = reader.readtext(notepad_screenshot_array)


    
    return results
