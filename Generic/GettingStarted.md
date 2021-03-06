Introduction
------------

These are the steps required to get the ERLTGenericSpeaker working on Windows/Mac/Linux

The ERLTGenericSpeaker uses the python package pyttsx, a cross platform text-to-speech package.
The version 1.2 of pyttsx works on the following platforms;

    SAPI5 on Windows XP, Windows Vista, and Windows 7
    NSSpeechSynthesizer on Mac OS X 10.5 (Leopard), 10.6 (Snow Leopard), 10.7 (Lion), and 10.8 (Mountain Lion).
    espeak on 32-bit Ubuntu Desktop Edition 8.10 (Intrepid), 9.04 (Jaunty), 9.10 (Karmic), and 12.04 (Precise).

Before You Start
----------------
Make sure you are using one of the supported platforms previously listed. Make sure your device is on the same network as the EasyRaceLapTimer raspberry pi. Make sure you can browse the Monitor tab of the EasyRaceLapTimer webserver, (http://192.168.42.1/monitor for default image and wifi setup). Make sure you are getting updates when transponders pass the sensor array or when a new race session is created.

Installation
------------

**Step 1:**
Install Python 2.7 (latest)
ERLTGenericSpeaker was developed using Python 2.7.11. 
The required pyttsx package does not work with Python3 at the time of development.
Download Python2.7 here https://www.python.org/downloads/

**Step 2:**
Install pyttsx using the OS specific instructions found here, http://pyttsx.readthedocs.org/en/latest/install.html

**Step 3:**
Install requests using the instructions here http://docs.python-requests.org/en/master/user/install/#install

**Step 4:**
Open a browser. Download the .cfg and .py files located here. https://github.com/SSPW/ERLTSpeaker/tree/master/Generic
Place them in a new folder ERLTGenericSpeaker.

Configuration
----------
**Step 1:**
open ERLTGenericSpeaker.cfg a text editor.

**Step 2:**
Edit the first line to reflect the the transponder id you want to monitor.

**Step 3:**
If you are not using the default EasyRaceLapTimer pi image and network setup, then edit the second line to reflect the ip address for the raspberry pi

Execution (windows)
----------

**Step 1:**
Double click on ERLTGenericSpeaker.py or right-click and select open


Execution (mac/linux)
----------

http://pythoncentral.io/execute-python-script-file-shell/





Coming Soon
-----------
See youtube video for run time behavior and other configuration settings

