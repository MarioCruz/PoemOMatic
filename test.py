
import printer, textwrap, sys 

p=printer.ThermalPrinter(serialport="/dev/ttyAMA0") 
unwrapped_text = "\nHello NightShift & RSM Good Morning from My Pi, Roses are red, violets are blue, I'm seeing a future filled with Poem and you!\n"
wrapped_text = textwrap.fill(unwrapped_text, 32) 
p.print_text(wrapped_text)
p.linefeed() 
p.linefeed() 
p.linefeed()
