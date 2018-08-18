from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import UserUttered
from rasa_core.events import BotUttered
import smtplib
import yaml
from email.mime.text import MIMEText

class SendEmail(Action):
	def name(self):
		return 'action_SendEmail'
	def run(self, dispatcher, tracker, domain):
		emailAddress = tracker.get_slot('emailAddress')
		dispatcher.utter_message("Do you want details of the top 10 restaurants on email?, Enter Yes/No" )
		emailResponse = input()
		if (emailResponse == 'Yes'):
			dispatcher.utter_message("Please provide your email address" )
			emailAddress = input()
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
			#recipients = ['ab9.bhatia@gmail.com','engg.saurabhsaxena@gmail.com','contactamarpal@gmail.com']
			recipients = [emailAddress]
			msg = MIMEText('body')
			msg['Subject'] = "Python! This message is from Jupyter Notebook"
			msg['From'] = str('Chatbot Help <helpchatbot0@gmail.com.com>')
			msg['To'] = ", ".join(recipients)
			
			# Authentication
			server.login(email,pwd)
			server.sendmail(email, recipients, msg.as_string())
			server.quit()
			dispatcher.utter_message("Email has been successfully sent to " + emailAddress )
		UserUttered("/utter_goodbye", intent={'name': 'utter_goodbye', 'confidence': 1.0}),
		return [SlotSet("emailAddress", emailAddress)]