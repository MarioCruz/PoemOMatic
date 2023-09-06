
import textwrap, sys
from PIL import Image
import thermalprinter
from thermalprinter import ThermalPrinter
from PIL import Image
#Here is a test with all the things I got working on an Adafruit Thermal printer
#more things to try here https://thermalprinter.readthedocs.io/usage.html 

with ThermalPrinter(port="/dev/serial0") as printer: 
    unwrapped_text = "\n From My Poem-O-Matic, Roses are red, violets are blue, I'm seeing a future filled with Poems and you!\n"
    wrapped_text = textwrap.fill(unwrapped_text, 32)
    printer.feed(2)
    printer.out(wrapped_text, bold=True)
    printer.feed(1)
    printer.out("Thermal Printer Test", bold=True)
    printer.image(Image.open("MTM.png"))
    printer.out("Mario The Maker",underline=1)
    printer.out("2023", inverse=True)
    printer.feed(3)
                