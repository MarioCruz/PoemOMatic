# (c) 2023 Mario Cruz Python3
# please credit me if you modify and/or use this code
# not for commercial use

import os
import glob
import json
import random
import textwrap
import thermalprinter
from PIL import Image
from thermalprinter import ThermalPrinter
from time import sleep
import RPi.GPIO as GPIO

DEBOUNCE_TIME = 0.5  # 0.5 second debounce time
MAX_RETRIES = 3  # Set this to the number of retry attempts you want
PRINTER_WIDTH = 384  # Adjust based on your printer's specifications

def load_random_poem(poem_directory):
    """Load a random poem from the specified directory."""
    path = os.path.join(poem_directory, "*.json")
    poem_files = glob.glob(path)
    if not poem_files:
        print("No poem files found.")
        return None

    random_file = random.choice(poem_files)
    try:
        with open(random_file, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Failed to decode JSON from {random_file}")
        return None

def console_print(poem):
    """Print poem details to the console."""
    print(poem['title'])
    print("by " + poem['author'])
    print("\n".join(poem['text']))

def printer_print(printer, poem):
    """Print poem details using a thermal printer."""
    # Print title centered
    printer.justify('C')
    printer.double_height(True)
    printer.bold(True)
    printer.underline(True)
    printer.out(poem['title'] + "\n")
    printer.bold(False)
    printer.underline(False)
    printer.double_height(False)

    # Print poem text left-aligned
    printer.justify('L')
    wrapped_text = textwrap.fill("\n".join(poem['text']), 32)
    printer.out(wrapped_text + "\n")

    # Print author centered
    printer.bold(True)
    printer.justify('C')
    printer.out("\n" + poem['author'] + "\n")
    printer.bold(False)
    
def center_image(img_path, canvas_width):
    """Center the image on a canvas of specified width."""
    img = Image.open(img_path)
    img_width, img_height = img.size

    padding = (canvas_width - img_width) // 2
    centered_img = Image.new('RGB', (canvas_width, img_height), (255, 255, 255))  # Assuming a white background
    centered_img.paste(img, (padding, 0))

    return centered_img

def initialization_printout():
    """Print an initialization message indicating that the machine is ready."""
    try:
        with ThermalPrinter(port="/dev/serial0", heat_time=100) as printer:
            printer.flush()
            printer.justify('C')
            printer.out("Initialization\n")
            printer.out("======================\n")
            printer.out("Poem-o-matic is ready!\n")
            printer.feed(3)
    except Exception as e:
        print(f"Failed to print initialization message due to: {e}")

def print_poem_with_retry():
    LOGO_O = "o.png"
    POEM_DIRECTORY = os.path.join(os.getcwd(), "PoemJson")

    for attempt in range(MAX_RETRIES):
        try:
            with ThermalPrinter(port="/dev/serial0") as printer:
                
                # Flush the printer buffer
                printer.flush()

                # Print the centered Logo
                centered_logo = center_image(LOGO_O, PRINTER_WIDTH)
                printer.image(centered_logo)
                printer.feed(1)

                # Print the Random Poem
                poem = load_random_poem(POEM_DIRECTORY)
                if poem:
                    console_print(poem)
                    printer_print(printer, poem)

                # Print The Footer
                printer.bold(True)
                printer.justify('C')  # The footer centered
                printer.out("Tag Us")
                printer.out("Poem-o-matic 2023 by @mariocruz")
                printer.out("@OMiamiFestival @MarioTheMaker")
                printer.out("#OPoemOMatic #MarioTheMaker")
                printer.bold(False)
                printer.feed(3)

            # If printing succeeded, break out of the loop
            break

        except Exception as e:
            print(f"Printing failed on attempt {attempt + 1} due to: {e}")
            if attempt < MAX_RETRIES - 1:  # Don't print the following message on the last attempt
                print("Retrying...")

            # Optional: Add a sleep here if you want a delay between retries
            # sleep(5)

if __name__ == "__main__":
    # Print initialization message
    initialization_printout()

    # GPIO setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)

    while True:
        if GPIO.input(23) == False:
            print("Printing")
            print_poem_with_retry()
            print("Printed")
            sleep(DEBOUNCE_TIME)  # debounce delay
        sleep(0.1)  # regular sleep to avoid busy-waiting
