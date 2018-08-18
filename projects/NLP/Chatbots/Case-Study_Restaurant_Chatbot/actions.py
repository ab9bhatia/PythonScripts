from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pprint
import re
from rasa_core.events import UserUttered
from rasa_core.events import BotUttered
import smtplib
import yaml
from email.mime.text import MIMEText
import pandas as pd

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
	
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"b150e50385939f3d2fca77c2cca1e072"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		bud= tracker.get_slot('budget')
		tmp = next(tracker.get_latest_entity_values('budget'), None)
		#print (tmp)
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 15)
		d = json.loads(results)
		
		# Logic to get the lowest & highest value from the budget
		bud_range = re.findall(r"\d+", bud)
		bud_range = [int(i) for i in bud_range]
		if (len(bud_range) >=2):
			lowest = min(bud_range)
			highest = max(bud_range)
		else:
			if ((bud_range[0])<=300):
				lowest = 0
				highest = bud_range[0]
			elif(((bud_range[0])>300) & (((bud_range[0])<=700))):
				lowest = 301
				highest = 700
			elif ((bud_range[0])>700):
				lowest = 701
				highest = max([restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']])
		response=[]
		r = pd.DataFrame(columns=['Restaurant Name','Location','Average Cost for Two'])
		if d['results_found'] == 0:
			print('No Results')
		else:
			for restaurant in d['restaurants']:
				price = restaurant['restaurant']['average_cost_for_two']
				if((price >=lowest) & (price <= highest)):
					#print(price)
					response.append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ \
									" with an average cost for two  " +str(price))
		msgBody = '\n'.join(response[:10])
		dispatcher.utter_message(msgBody)
		
		# Logic to Send Email
		dispatcher.utter_message('\n'+"Do you want details of the top restaurants on email?, Enter Yes/No" )
		emailResponse = input()
		if (emailResponse.lower() == 'yes'):
			isInValidEmail = True
			while(isInValidEmail):
				dispatcher.utter_message("Please provide one or more Email address" )
				emailString = input()
				emailAddress = re.findall(r'[\w\.-]+@[\w\.-]+', emailString)
				if(len(emailAddress) > 0):
					isInValidEmail = False
				else:
					print('Invalid Email IDs')
			# creates SMTP session
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			# start TLS for security
			server.starttls()
			
			# Reading credentials from config file
			conf = yaml.load(open('./email.yml'))
			email = conf['user']['email']
			pwd = conf['user']['password']
			# Email Structure
			recipients = emailAddress
			msg = MIMEText(msgBody)
			msg['Subject'] = "Chatbot! Here is your Favorite Restaurants in "+loc
			msg['From'] = str('Chatbot Help <helpchatbot0@gmail.com.com>')
			msg['To'] = ','.join(recipients)
			
			# Authentication
			server.login(email,pwd)
			server.sendmail(email, recipients, msg.as_string())
			server.quit()
			dispatcher.utter_message("Email has been successfully sent to " + msg['To'] )
		return [SlotSet('location',loc)]

