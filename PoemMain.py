# (c) 2016  Mario Cruz
# please credit me if you modify and/or use this code
# not for commercial use
# help from Giles Booth @blogmywiki site (inspiration and lots of instructions)
# and Christian Romney @christianromney (Made the poems manageable w/ JSON files) 

import os
import glob
import json
import random
import printer, textwrap

from PIL import Image
from StringIO import StringIO
 
def random_poem():
    path = os.path.join(os.getcwd(), "PoemJson/*.json")
    list = glob.glob(path)
    if (0 < len(list)):
        idx = random.randrange(0, len(list))
        with open(list[idx]) as f:
            return json.load(f)
    else:
        return None
    
def poem_text(poem):
    return "\n".join(poem['text'])
    
def console_print(poem):
   
    print(poem['title'])
    print("by " + poem['author'])
    print(poem_text(poem)) 

def printer_print(p, poem):
    p.bold()
    p.inverse()
    p.print_text(poem['title'])
    p.linefeed()
    p.bold(False)
    p.inverse(False)
    p.justify("L")
    p.print_text(poem_text(poem))
      
    p.linefeed()
    p.justify("R")
    p.linefeed()
    p.bold()
    p.print_text(poem['author'])
    p.justify("L")
    p.bold(False)

# Run the program
if __name__ == "__main__":
    p = printer.ThermalPrinter(serialport="/dev/ttyAMA0")

# Print the Logo
    i = Image.open("o.png")
    data = list(i.getdata())
    w, h = i.size
    p.print_bitmap(data, w, h, False)
    p.linefeed() 
# Print the Random Poem
    poem  = random_poem()
    if (poem is not None):   
        console_print(poem)
        printer_print(p, poem)
        p.linefeed()

#Print The Footer
p.font_b()
p.print_text("Poem-o-matic 2016 by @mariocruz          ")          
p.print_text(" @codeformiami @OMiamiFestival           ")
p.print_text("      HashTag OPoemOMatic            ")
p.font_b(False)
p.linefeed()
p.linefeed()
p.linefeed()


