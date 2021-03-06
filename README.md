# O, Miami Poem-O-Matic

## What
Poem-o-matic is a friendly "bot-in-a-box" that prints out a keepsake poem just for you when you press the button. We hope you'll snap an Instagram of your poem and share it with your social network.

#### Status
The very first (and at this time, only) Poem-o-matic was created for the 2016 [O, Miami Poetry Festival](http://www.omiami.org/) at the [Moonlighter Makerspace](http://moonlighter.co/), where fine Miami nerds come together to make cool things.

#### Screenshots and Press

![Composite photo of the Poem-O-Matic, with poems](https://pbs.twimg.com/media/CeCSeLtVAAAc_ZA.jpg)

- Video at work: https://www.facebook.com/cryptocoder/videos/10153924795386827/
- https://twitter.com/mariocruz/status/715596679215464451

## Why

Poem-o-matic was created for the 2016 [O, Miami Poetry Festival](http://www.omiami.org/). The mission of the festival is for every single person in Miami-Dade County to encounter a poem during the month of April. O, Miami is a Knight Foundation-funded organization that expands and advances literary culture in Greater Miami, FL.

## Who

Poem-o-matic is a project by Mario Cruz, with negligible spiritual support from Cristina Solana and Rebekah Monson. Ernie Hsiung assisted with the documentation.

Additional inspiration, research and some code lifted and referenced from these two sites:

- [Carrie Anne Philbin](http://geekgurldiaries.blogspot.co.uk/2012/12/part-2.html) @Geekgurldiaries 
- [Giles Booth](http://www.suppertime.co.uk/blogmywiki/2012/12/pi-poems/) @blogmywiki

## How
#### Materials

- [Raspberry Pi 2 or 3](https://www.adafruit.com/category/105)
- [Breadboard](http://www.amazon.com/microtivity-IB400-400-point-Experiment-Breadboard/dp/B0084A7PI8)
- [Thermal Printer kit](https://www.adafruit.com/product/600)
- [6 Breadboard Wires](https://www.adafruit.com/product/153) 
- [A 10k resistor](http://www.amazon.com/E-Projects-10k-Resistors-Watt-Pieces/dp/B00BWYS9BA)

Note: This document assumes you can get a Raspberry Pi up and running. If not, [try this link](https://www.raspberrypi.org/help/quick-start-guide/).

#### Setup the Raspberry Pi
SSH into your Raspbery Pi or - via monitor and keyboard - open a terminal. We will need to install the required files by typing the following into a terminal window on your Pi:

```
sudo apt-get update
sudo apt-get upgrade
```

Install the needed packages:
```
sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio
sudo apt-get install python-serial 
sudo apt-get install python-imaging-tk
sudo apt-get install python-unidecode
sudo apt-get install gcc 
```

Next give the serial port permission to be used:
```
sudo usermod -a -G dialout pi
```

Now reboot, to make sure everything is okay:
```
sudo shutdown -r now
```

If everything boots correctly please make an image backup of your SD / Raspberry PI with [Apple Pi-Baker Mac](http://www.tweaking4all.com/hardware/raspberry-pi/macosx-apple-pi-baker/) or an app of your choice like [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/) (Note: I have not used this.)

Changes to your `cmdline.txt` could render your Pi useless until you re-image your SD.

Then we need to change the Pi serial port. These changes keep the printer from spewing garbage when you first set it up. The serial port is set up for terminal use, so we need to turn that off.

```
sudo nano /boot/cmdline.txt
```

In the file, change:
 `console=ttyAMA0,115200` to
 `console=tty1` 

Reboot to make sure it’s all working:
```
sudo shutdown -r now
``` 

#### Project Wiring 

![poem-o-matic_-_google_docs](https://cloud.githubusercontent.com/assets/33945/14189971/37ef71ca-f75e-11e5-8f26-1458b4edf840.jpg)

##### Install the printer

Take the green/yellow/black cable and cut the green cable. You don’t need it and it can it can short out your Pi.

Now connect it to the TTL socket in the back of the printer: the black cable goes into the GND, and the yellow into the RX, and the green wire should just be a stub.

To connect the printer we make use of the pin #6 (Ground) and the pin #8 (GPIO14). 

![12910189_10153972478171827_1459247504_n](https://cloud.githubusercontent.com/assets/33945/14190358/50039ae6-f760-11e5-9735-6d77677f73dc.jpg)


![12939506_10153972446901827_483233786_n](https://cloud.githubusercontent.com/assets/33945/14190201/789ee1f0-f75f-11e5-8548-70cf512f329e.png)

Now, let's connect the power. Attach the printer’s red/black wires to the 2.1mm jack adapter:

![](https://learn.adafruit.com/system/assets/assets/000/001/944/original/components_poweradapt.jpg?1396777663)


##### Power up the printer

Plug the 5V 2A power supply into the 2.1 mm DC jack adapter provided with the kit. 

Reboot:
```
sudo shutdown -r now
```

If your printer starts spewing gibberish when it reboots, check `/boot/cmdline.txt` files to make sure the changes were saved from above.

Next we need to download the python files needed to print and Poem-O-Matic files to run from github. 

First you will need to install `git-core` onto your pi using:

```
sudo apt-get install git-core
git clone git://github.com/MarioCruz/PoemOMatic
```

Now we are ready for a test print: 
```
python test.py

TestIMAGE
```

This a poem to verify this works:

```
Python PoemMain.py
```

You should get a random poem.

On the PI3 the Serial Port is named "ttyS0" and not "ttyAMA0" 
If you are using a Raspberry Pi 3

Comment 
   p = printer.ThermalPrinter(serialport="/dev/ttyAMA0")

and uncomment 
   p = printer.ThermalPrinter(serialport="/dev/ttyS0")


#### Connect the switch 

Connect one side of the push button to pin 14 GND on the Raspberry Pi. Connect the the other side of the button to pin 16 on the Pi (GPIO 23). You also need to connect the same side of the switch that’s connected to GPIO 23 via a 10k ohm resistor to pin 1 of the Raspberry Pi (which supplies 3.3 volts of electricity).

![12419284_10153924767736827_3342091426751050788_o](https://cloud.githubusercontent.com/assets/33945/14190119/1cd6f75e-f75f-11e5-83d2-7eded4b730ed.jpg)

Finally, we want the PoemOMatic program to run whenever the Pi is started and the button is pushed. Therefore we need to modify the `/etc/rc.local` file to reflect this by using a terminal window:

```
sudo nano /etc/rc.local

# Change to the Poem Directory
cd /home/pi/PoemOMatic

# Tell me the system is up and the IP (if connected)
python upip.py

# Listening for the Switch to be pressed
python GPIORUN.py

exit 0
```

##### Save and Reboot

Once you have tested that it all works, transfer your Pi, printer, and breadboard into the custom box and make sure everything is plugged in and sits well. Power it all up, give a few minutes, if it all works the printer should say it is ready with an IP if connected.  

![12948437_10153972496991827_1152713091_o](https://cloud.githubusercontent.com/assets/33945/14190472/f7fe626c-f760-11e5-941a-30776f6bb99f.jpg)

Press the button and receive a poem:

![12941008_10153972497251827_319633202_o](https://cloud.githubusercontent.com/assets/33945/14190534/5617ce9c-f761-11e5-86f2-b6d1f083d8b9.jpg)


I modified the box to be screwless and added the O' Miami logo using [Adafruit IOT Printer box /via Thingiverse](http://www.thingiverse.com/thing:18319/#files) as my starting source source and cut it on [Moonlighters Wood CNC](http://moonlighter.co) .

![10989503_10153924767551827_6255215138792160131_o](https://cloud.githubusercontent.com/assets/33945/14190165/532c437c-f75f-11e5-9ce5-00918ff05490.jpg)


#### Updating poems 

```
{"title": "Fire and Ice",
 "author": "Robert Frost",
 "text": ["Some say the world will end in       fire,",
          "Some say in ice.",
          "From what I've tasted of desire,",
          "I hold with those who favor fire.",
          "But if I had to perish twice,",
          "I think I know enough of hate",
          "To say that for destruction ice",
          "Is also great",
          "And would suffice."]}
```

The poems themselves are in the `PoemJson` directory in a JSON structure. Make any changes or add poems and use a SFTP program i.e. Transit, Cyberduck, etc to upload into the Raspberry Pi.

Plug an ethernet cable into the Raspberry Pi, power the Pi and if ethernet settings are correct the IP address will be shown at the top of the ready print slip:

If you get no IP reboot and try again.

![12948437_10153972496991827_1152713091_o](https://cloud.githubusercontent.com/assets/33945/14190472/f7fe626c-f760-11e5-941a-30776f6bb99f.jpg)

SFTP in to the PI using the IP  User: PI Password:raspberry

Add new poems into the /PoemOMatic/PoemJson/ with a .json extension.
   You may want to valdidate your JSON files using a vilidator before uploading 
   i.e. https://jsonformatter.curiousconcept.com
   
 ##### Things to make better
   1. Use textwrap.fill  Json data
   2. Use escape for ' issues in JSON data.  "'" crashes when pritnig 
  

