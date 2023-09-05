#!/bin/bash

# Source bash profile to get the environment variables
source /home/pi/.bashrc

# Add the path to the thermalprinter module to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:/home/pi/.local/lib/python3.9/site-packages

# Navigate to the directory
cd /home/pi/PoemOMatic/

# Run the Python script
/usr/bin/python3 /home/pi/PoemOMatic/PoemMain2023.py >> /home/pi/cronjoblog 2>&1
