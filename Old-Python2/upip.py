#!/usr/bin/python

from subprocess import check_output
from  printer import *
import printer
import time

time.sleep(10) # delays for 5 seconds
#This delay is here for slow DHCP Servers
ipAddr = check_output(["hostname", "-I"])
print 'IP Address: ' + ipAddr + "\n"
p=printer.ThermalPrinter(serialport="/dev/ttyAMA0")
p.linefeed()
p.print_text('IP Address: ' + ipAddr + "\n")
p.linefeed()
p.print_text('The Poem-O-Matic is Ready       ')
p.print_text('Ready Player 1                  ')
p.print_text('@MarioCruz 2016 ')
p.linefeed()
p.linefeed()
p.linefeed()
p.linefeed()

