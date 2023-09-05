
import printer, textwrap, sys 


 # Pi 1 and 2 
   p = printer.ThermalPrinter(serialport="/dev/ttyAMA0")
 
  # Pi 3
  #  p = printer.ThermalPrinter(serialport="/dev/ttyS0")

unwrapped_text = "\n From My Pi, Roses are red, violets are blue, I'm seeing a future filled with Poems and you!\n"
wrapped_text = textwrap.fill(unwrapped_text, 32) 
p.print_text(wrapped_text)
p.linefeed() 
p.linefeed() 
p.linefeed()
