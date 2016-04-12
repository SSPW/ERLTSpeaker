# coding: utf-8
from time import sleep
import requests
import json
import speech
import console
import dialogs

def readline_stripped(f):
	return f.readline().replace('\n','').replace('\r','')
	
def writevalueline(f, val):
	f.write('%s\n' %(val))
	
def replacevalue(m, pattern, replacement):
	return m.replace(pattern, '{}'.format(replacement))
	
try:
	f1 = open('ERLTconfig.csv','r')
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
	speech_speed = '0.5'
	time_precision = '2'
	best_time_phrase = 'fastest'
	message_format = 'lap {6}, time {7}, {11}'
	
dl = [{'type':'number','title':'Token','key':'token', 'value':token},{'type':'text','title':'Server IP','key':'ip', 'value':ip},{'type':'number','title':'Interval','key':'interval','value':interval},{'type':'number','title':'Timeout','key':'timeout','value':timeout},{'type':'number','title':'Speech Speed','key':'speechspeed','value':speech_speed},{'type':'number','title':'Time Precision','key':'timeprecision','value':time_precision},{'type':'text','title':'Best Time Phrase','key':'besttimephrase','value':best_time_phrase},{'type':'text','title':'Message Format','key':'messageformat','value':message_format}]

form = dialogs.form_dialog('ERLT Speech Monitor', dl)

if (form != None):
	token = form.get('token')
	ip = form.get('ip')
	interval = form.get('interval')
	timeout = form.get('timeout')
	speech_speed = form.get('speechspeed')
	time_precision = form.get('timeprecision')
	best_time_phrase = form.get('besttimephrase')
	message_format = form.get('messageformat')

	f2 = open('ERLTconfig.csv','w')
	writevalueline(f2, token)
	writevalueline(f2, ip)
	writevalueline(f2, interval)
	writevalueline(f2, timeout)
	writevalueline(f2, speech_speed)
	writevalueline(f2, time_precision)
	writevalueline(f2, best_time_phrase)
	writevalueline(f2, message_format)
	f2.close()

url = r'http://' + ip + r'/api/v1/monitor'

console.clear()
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
				console.clear()
				print("%s \r\n" % (session_title))
				speech.say("new race, " + session_title, 'en-US', float(speech_speed))
	
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
							
						#speak message
						speech.say(message, 'en-US', float(speech_speed))
		
						#print message
						print(message)
						print("")
						
						break
						
	except requests.exceptions.Timeout:
		print(".")
	except requests.exceptions.ConnectionError:
		print("connection error")
	except Exception as e:
		print(e.message)
		print(e.args)
		