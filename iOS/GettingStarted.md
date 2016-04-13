Introduction
------------

These are the steps required to get the ERLTSpeaker working on iOS.

Before You Start
----------------

Make sure your iOS device is on the same network as the EasyRaceLapTimer raspberry pi. Make sure you can browse the Monitor tab of the EasyRaceLapTimer webserver, (http://192.168.42.1/monitor for default image and wifi setup). Make sure you are getting updates when transponders pass the sensor array or when a new race session is created.

Installation
------------

**Step 1:**
Python is not included with iOS so you need to buy it. Purchase Pythonista at the app store and install it. Its $10 for the app. It works on both ipad and iphone. see http://omz-software.com/pythonista/ and https://itunes.apple.com/app/pythonista/id528579881

**Step 2:**
Once you have Pythonista running. Hit the + at the bottom of the library (left) pane. Create a folder called EasyRaceLapTimer (or whatever you want, name is not critical). Hit + again. Create an empty script, check your new folder, and name the script "ERLTSpeaker.py". This will create the new script and show its code in the code (right) pane.

**Step 3:**
Open safari. Open https://raw.githubusercontent.com/SSPW/ERLTSpeaker/master/iOS/ERLTSpeaker.py. Select all and copy.

**Step 4:**
Go back to Pythonista. Paste the clip into the ERLTSpeaker.py code pane. Changes to the script are saved automatically.


Execution:
----------

**Step 1:**
Open Pythonista

**Step 2:**
Browse the library pane to the EasyRaceLapTimer folder and the ERLTSpeaker.py script. Click on the script. This will open the code (left) pane and open the Console (right) pane.

**Step 3:**
Hit the run (play) button at the top of the ERLTSpeaker.py code pane.

**Step 4:**
The ERLTSpeaker configuration dialog pops up every time the app starts. If you have run the app before and configured it and you want the same settings, just hit done. If not, goto step 5.

**Step 5:**
If you are not using the default EasyRaceLapTimer pi image and network setup, then change the ip address for the raspberry pi

**Step 6:**
Set the Token to the transponder id you want to monitor.

**Step 7:** 
Hit done to start monitoring

Coming Soon
-----------
See youtube video for run time behavior and configuration

