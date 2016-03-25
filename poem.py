# (c) 2016  Mario Cruz
# please credit me if you modify and/or use this code
# not for commercial use
# lots of help from Giles Booth @blogmywiki


from random import *
from  printer import *
import printer
import random

p=printer.ThermalPrinter(serialport="/dev/ttyAMA0")


# the poem titles, text and authors are in 3 separate lists
# you force a new line with \n and \ at the end of a line
# allows you to continue defining a string on a new line

poemtitle = ['Full of Life, Now', 'The Sick Rose', 'This is just to say', 'Surprise']

poemtext = ['The apparition of these faces in the crowd;\n\
            Petals on a wet, black bough.',
            
            'FULL of life, now, compact, visible,\n\
            I, forty years old the Eighty-third Year of The States,\n\
            To one a century hence, or any number of centuries hence,\n\
            To you, yet unborn, these, seeking you.\n\
            \n\
            When you read these, I, that was visible, am become invisible;\n\
            Now it is you, compact, visible, realizing my poems, seeking me;\n\
            Fancying how happy you were, if I could be with you, and become your comrade;\n\
            Be it as if I were with you. (Be not too certain but I am now with you.)',
            'I have eaten\n\
            the plums\n\
            that were in\n\
            the icebox\n\n\
            and which\n\
            you were probably\n\
            saving\n\
            for breakfast\n\n\
            Forgive me\n\
            they were delicious\n\
            so sweet\n\
            and so cold','I lift the toilet seat\n\
            as if it were the nest of a bird\n\
            and i see cat tracks\n\
            all around the edge of the bowl.']

poemauthor = ['Walt Whitman\n', 'William Blake\n', 'William Carlos Williams\n', 'Richard Brautigan\n']


# this chooses a random poem number between 0 and 3
# (in the poem lists the 1st poem is poem number 0)
poem = random.randrange(0,4)

p.bold()
p.inverse()
p.print_text(poemtitle[poem])
p.linefeed()
p.bold(False)
p.inverse(False)
p.justify("L")
p.print_text(poemtext[poem])
p.linefeed()
p.justify("R")
p.print_text(poemauthor[poem])
p.justify("L")
p.linefeed()
from PIL import Image
i = Image.open("o.png")
data = list(i.getdata())
w, h = i.size
p.print_bitmap(data, w, h, True)
p.linefeed()

#FONT B IS THE TINY FONT
p.font_b()
p.print_text("O, Miami, Random Poems(c)2016 @mariocruz Code 4 Miami")
p.font_b(False)
p.linefeed()
p.linefeed()
p.linefeed()
