# EasyRaceLapTimer Python Client with Speech
# Version for Windows (using pyttsx, see https://pyttsx.readthedocs.org/en/latest/)
#
# Author: John Craven
#
# This is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with Foobar. If not, see http://www.gnu.org/licenses/.

from time import sleep
import requests
import json
import pyttsx

#transponder of interest
mytoken = 33

#url for monitor api
#url = 'http://192.168.1.231/api/v1/monitor'
url = 'http://192.168.42.1/api/v1/monitor'

#polling interval
interval = 2
# speech speed (words per minute)
wpm = 200

mylap = ""
mysession = ""

#start speeck engine
engine = pyttsx.init()
engine.setProperty('rate', wpm)

while True:
    sleep(interval)
    
    # get monitor update
    response = requests.get(url)
    
    # load response in a json object
    monitor = response.json()
    
    # get race session info
    session = monitor.get("session")
    session_title = session.get("title")
    session_lap_count = session.get("current_lap_count")
    
    # check for new session (or race)
    if (session_title != mysession):
        mysession = session_title
        print("%s \r\n" % (session_title))
        engine.say("new race, " + session_title)
        engine.runAndWait()
    
    # get data for pilots and times
    data = monitor.get("data")
    
    # loop for each pilot
    for item in data:
        # get pilot transponder token
        pilot = item.get("pilot")
        pilot_transponder_token = pilot.get("transponder_token")
        
        # continue if token matches 
        if (int(pilot_transponder_token) == mytoken):
            # get current lap
            lap_count = item.get("lap_count")
            # continue if new lap
            if (lap_count != mylap):
                mylap = lap_count 
                # get the remaining of the info for pilot and lap
                position = item.get("position")
                pilot_name = pilot.get("name")
                pilot_quad = pilot.get("quad")
                pilot_team = pilot.get("team")
                avg_lap_time = float(item.get("avg_lap_time")) / 1000
                fastest_lap_num = item.get("fastest_lap").get("lap_num")
                fastest_lap_time = float(item.get("fastest_lap").get("lap_time")) / 1000
                last_lap_num = item.get("last_lap").get("lap_num")
                last_lap_time = float(item.get("last_lap").get("lap_time")) / 1000
                latest_tracked = item.get("latest_tracked")
                
                last_lap_is_fastest = (last_lap_time == fastest_lap_time)
                
                # print the info 
                print("%s, %s, %s, %s, %s, %s" % (position, pilot_name, pilot_transponder_token, pilot_quad, pilot_team, latest_tracked))
                print("%s, %s" % (lap_count, avg_lap_time)) 
                print("%s, %s" % (fastest_lap_num, fastest_lap_time)) 
                print("%s, %s, %s" % (last_lap_num, last_lap_time, last_lap_is_fastest)) 
                print("")
                
                #build base message
                message = pilot_name
                message = message + ", lap {}".format(last_lap_num)
                message = message + ", time {:5.2f}".format(last_lap_time)
                    
                #add flag if fastest
                if (last_lap_is_fastest):
                    message = message +  " best"
                    
                #speak message
                engine.say(message)
                engine.runAndWait()
        
                break
