# O, Miami Poem-O-Matic 2023

## What
Poem-o-matic is a friendly "bot-in-a-box" that prints out a keepsake poem just for you when you press the button. We hope you'll snap an Instagram of your poem and share it with your social network.

#### Status
The very first (and at this time, only) Poem-o-matic was created for the 2016 [O, Miami Poetry Festival](http://www.omiami.org/) at the [Moonlighter Makerspace](http://moonlighter.co/), where fine Miami nerds come together to make cool things.

#### Screenshots

![IMG_5500](https://github.com/MarioCruz/PoemOMatic/assets/1426877/2c9dc18f-8c3c-46c6-be8f-1155a3099bff)


#### Video 

https://github.com/MarioCruz/PoemOMatic/assets/1426877/8c90c99c-f934-47f5-93e1-09020cca742a

## Why

Poem-o-matic was created for the 2016 [O, Miami Poetry Festival](http://www.omiami.org/). The mission of the festival is for every single person in Miami-Dade County to encounter a poem during the month of April. O, Miami is a Knight Foundation-funded organization that expands and advances literary culture in Greater Miami, FL.

## Who

Poem-o-matic is a project by Mario Cruz, with negligible spiritual support from Cristina Solana and Rebekah Monson. Ernie Hsiung assisted with the documentation.

Orignial inspiration in 2016, research and referenced from these two sites:

- [Carrie Anne Philbin](http://geekgurldiaries.blogspot.co.uk/2012/12/part-2.html) @Geekgurldiaries 
- [Giles Booth](http://www.suppertime.co.uk/blogmywiki/2012/12/pi-poems/) @blogmywiki

## How
#### Materials

- [Raspberry Pi3](https://www.adafruit.com/category/105)
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
sudo apt install python3-pip
sudo apt-get install netatalk
python3 pip install thermalprinter
python3 pip install pillow
```

Next give the serial port permission to be used Disable Bluetooth:
Changes to your `cmdline.txt` could render your Pi useless make a Backup image of your SD.
```
sudo nano /boot/config.txt
# Disable Bluetooth
dtoverlay=disable-bt

sudo systemctl disable hciuart.service
sudo systemctl disable bluealsa.service
sudo systemctl disable bluetooth.service

```

Now reboot, to make sure everything is okay:
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


##### Power up the

First you will need to install `git-core` onto your pi using:

```
sudo apt-get install git-core
git clone git://github.com/MarioCruz/PoemOMatic
```

Now we are ready for a test print: 
```
python3 test2023.py

TestIMAGE
```
![IMG_5497 Large](https://github.com/MarioCruz/PoemOMatic/assets/1426877/5cb72d56-8d95-451b-9574-a4d72821a674)

This a poem to verify this works:

```
Python3 PoemMain2023.py
```

You should get a random poem.


#### Connect the switch 

Connect one side of the push button to pin 14 GND on the Raspberry Pi. Connect the the other side of the button to pin 16 on the Pi (GPIO 23). You also need to connect the same side of the switch that’s connected to GPIO 23 via a 10k ohm resistor to pin 1 of the Raspberry Pi (which supplies 3.3 volts of electricity).

![12419284_10153924767736827_3342091426751050788_o](https://cloud.githubusercontent.com/assets/33945/14190119/1cd6f75e-f75f-11e5-83d2-7eded4b730ed.jpg)

Finally, we want the PoemOMatic program to run whenever the Pi is started and the button is pushed. 


## Running PoemOMatic using a Bash script

To ensure the `PoemMain2023.py` script runs smoothly on boot using a Bash wrapper, follow these steps:

### 1. Create a new Bash script

Open a terminal and create the script using `nano`:

```bash
nano /home/pi/PoemOMatic/run_poemomatic.sh
```

### 2. Add the content to the script

Insert the following lines into the script:

```bash
#!/bin/bash

# Navigate to the directory (optional, but can help with relative paths in the script)
cd /home/pi/PoemOMatic/

# Run the Python script
/usr/bin/python3 /home/pi/PoemOMatic/PoemMain2023.py >> /home/pi/cronjoblog 2>&1
```

After entering the content, save and exit the editor. In `nano`, this is done by pressing `CTRL + X`, then `Y`, and finally `Enter`.

### 3. Make the Bash script executable

Provide the necessary permissions to the script so that it can be executed:

```bash
chmod +x /home/pi/PoemOMatic/run_poemomatic.sh
```

### 4. Update the `cron` job to run the Bash script

To make the Bash script run on boot, update your `crontab`:

```bash
sudo crontab -e
```

Replace the existing line (if you've set it up before) or add a new line with:

```bash
@reboot /home/pi/PoemOMatic/run_poemomatic.sh
```

### 5. Reboot

Reboot your Raspberry Pi to see the changes in effect:

```bash
sudo reboot


After the reboot, the Bash script will be executed, which will then run your Python script.
If any issues arise, they will be captured in the `/home/pi/cronjoblog` file for debugging.

```

##### Save and Reboot

Once you have tested that it all works, transfer your Pi, printer, and breadboard into the custom box and make sure everything is plugged in and sits well. Power it all up, give a few minutes, if it all works the printer should say it is ready with.  
![IMG_5490](https://github.com/MarioCruz/PoemOMatic/assets/1426877/efdcf7aa-4bc9-4952-bfac-2fab3350bcb9)


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

The poems themselves are in the `PoemJson` directory in a JSON structure. 

Plug an ethernet cable into the Raspberry Pi, power the Pi

On a Mac browse the network an connect to Pomeomatic to the PI the login is (in our case) User: PI Password:raspberry or
Make any changes or add poems and use a SFTP program i.e. Transit, Cyberduck, etc to upload into the Raspberry Pi.

Add new poems into the /PoemOMatic/PoemJson/ with a .json extension.
   You may want to valdidate your JSON files using a vilidator before uploading 
   i.e. https://jsonformatter.curiousconcept.com



2024 upgrade the Pi2 to Pi Zero W 2, Save space and We can add a Bigger SD card fro more poems.
   
 ##### Things to make better
  TBD, fixed all the old things in this area. 


  MarioTheMaker 2023
  

