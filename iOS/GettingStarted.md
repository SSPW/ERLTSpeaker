Introduction

This is the steps required to get the ERLTSpeaker app working on iOS.

Before You Start
make sure your iOS is on the same network as the EasyRaceLapTimer raspberry pi
make sure you can load the monitor tab of the EasyRaceLapTimer webserver, at http://192.168.42.1/monitor (for default wifi setup)
make sure you are getting updates when transponders pass the sensor array

Installation

Step 1:
Python is not included with iOS so you need to buy it.
Purchase Pythonista at the app store and install it.
Its $10 for the app. It works on both ipad and iphone. 
http://omz-software.com/pythonista/
https://itunes.apple.com/app/pythonista/id528579881

Step 2:
once you have pythonista running
hit the + at the bottom of the library (left) pane
create a folder called EasyRaceLapTimer (or whatever you want, name is not critical)
hit + again
create an empty script, check your new folder, and name the script ERLTSpeaker.py
this will create the new script and show its code in the code (right) pane

Step 3:
goto safari
open https://raw.githubusercontent.com/SSPW/ERLTSpeaker/master/iOS/ERLTSpeaker.py
select all and copy

Step 4:
go back to pythonista
paste the clip into the ERLTSpeaker.py code pane
changes are saved automatically


Execution:

Step 1:
Open Pythonista

Step 2:
Browse the library pane to the EasyRaceLapTimer folder and the ERLTSpeaker.py script
click on the script
this will open the code (left) pane and open the Console (right) pane

Step 3:
hit the run (play) button at the top of the ERLTSpeaker.py code pane

Step 4:
the configuration dialog pops up every time the app starts
if you have run the app and configured it and it worked and you want the same settings, just hit done at thats it.
if not, goto step 5

Step 5:
If you are not using the default EasyRaceLapTimer image and network
Change the ip address for the raspberry pi

Step 6:
Set the Token to the transponder id you want to monitor.

Step 7: 
hit done

See youtube video for run time behaviour and configuration
Coming Soon




