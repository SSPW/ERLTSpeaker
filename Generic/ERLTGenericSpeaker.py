# EasyRaceLapTimer Python Client with Speech
# Version for Windows (using pyttsx, see https://pyttsx.readthedocs.org/en/latest/)
#
# Author: John Craven
#
# This is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with Foobar. If not, see http://www.gnu.org/licenses/.

# coding: utf-8

from time import sleep
import requests
import json
import pyttsx

def readline_stripped(f):
	return f.readline().replace('\n','').replace('\r','')
	
def writevalueline(f, val):
	f.write('%s\n' %(val))
	
def replacevalue(m, pattern, replacement):
	return m.replace(pattern, '{}'.format(replacement))

def initSpeech(wpm, voice):
        #start speech engine
        e = pyttsx.init()
        e.setProperty('rate', wpm)
        e.setProperty('voice', voice)
        return e;

def speakMessage(e, message):
        e.say(message)
        e.runAndWait()

#---------------------------------------------------------
        
try:
	f1 = open('ERLTGenericSpeaker.cfg','r')
	token = readline_stripped(f1)
	ip = readline_stripped(f1)
	interval = readline_stripped(f1)
	timeout = readline_stripped(f1)
	speech_speed = readline_stripped(f1)
	time_precision = readline_stripped(f1)
	best_time_phrase = readline_stripped(f1)
	message_format = readline_stripped(f1)
	f1.close()
	
except Exception:
	token = '1'
	ip = '192.168.42.1'
	interval = '2'
	timeout = '1'
	speech_speed = '150'
	time_precision = '2'
	best_time_phrase = 'fastest'
	message_format = 'lap {6} time {7} {11}'
	
engine = initSpeech(int(speech_speed), 'en-US')

url = r'http://' + ip + r'/api/v1/monitor'

print("starting to monitor token = {}".format(token))
print("")

last_lap_count = ""
last_session = ""

while True:
	sleep(float(interval))
	
	try:
		# get monitor update
		response = requests.get(url, timeout = float(timeout))
	
		# chevk for good response
		if (response.status_code == requests.codes.ok):
			# load response in a json object
			monitor = response.json()
	
			# get race session info
			session = monitor.get("session")
			session_title = session.get("title")
			session_lap_count = session.get("current_lap_count") 
	
			# check for new session (or race)
			if (session_title != last_session):
				last_session = session_title
				print("%s \r\n" % (session_title))
				speakMessage(engine, "new race, " + session_title)
	
			# get data for pilots and times
			data = monitor.get("data")

			# loop for each pilot
			for item in data:
				# get pilot transponder token
				pilot = item.get("pilot")
				pilot_transponder_token = pilot.get("transponder_token")
		
				# continue if token matches 
				if (pilot_transponder_token == token):
					# get current lap
					lap_count = item.get("lap_count")
					# continue if new lap
					if (lap_count != last_lap_count):
						last_lap_count = lap_count
						# get the remaining of the info for pilot and lap
						position = item.get("position")
						pilot_name = pilot.get("name")
						pilot_quad = pilot.get("quad")
						pilot_team = pilot.get("team")
					
						avg_lap_time = float(item.get("avg_lap_time"))
						fastest_lap = item.get("fastest_lap")
						fastest_lap_num = fastest_lap.get("lap_num")
						fastest_lap_time = float(fastest_lap.get("lap_time"))
						last_lap = item.get("last_lap")
						last_lap_num = last_lap.get("lap_num")
						last_lap_time = float(last_lap.get("lap_time"))
						latest_tracked = item.get("latest_tracked")
				
						last_lap_is_fastest = (last_lap_time == fastest_lap_time)

						#number of digits for time formatting
						tp = int(time_precision)
						
						message = message_format
						#message = message.replace("{1}", str(position))
						message = replacevalue(message, '{1}', str(position))
						message = replacevalue(message, '{2}', pilot_name)
						message = replacevalue(message, '{3}', str(pilot_transponder_token))
						message = replacevalue(message, '{4}', pilot_quad)
						message = replacevalue(message, '{5}', pilot_team)
						message = replacevalue(message, '{6}', str(last_lap_num))
						message = replacevalue(message, '{7}', '{}'.format(round(last_lap_time / 1000, tp)))
						message = replacevalue(message, '{8}', str(fastest_lap_num))
						message = replacevalue(message, '{9}', '{}'.format(round(fastest_lap_time / 1000, tp)))
						message = replacevalue(message, '{10}', '{}'.format(round(avg_lap_time / 1000, tp)))
						
						if (last_lap_is_fastest):
							message = replacevalue(message, '{11}', best_time_phrase)
						else:
							message = replacevalue(message, '{11}', '')
							
						#print message
						print(message)
						print("")

						#speak message
						speakMessage(engine, message)
						
						break
						
	except requests.exceptions.Timeout:
		print(".")
	except requests.exceptions.ConnectionError:
		print("connection error")
	except Exception as e:
		print(e.message)
		print(e.args)
		
