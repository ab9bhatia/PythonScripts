from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import UserUttered
from rasa_core.events import BotUttered


class CheckEmail(Action):
	def name(self):
		return 'action_CheckEmail'
	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')
		emailAddress = tracker.get_slot('emailAddress')
		print(email)
		print(emailAddress)
		if email.lower() =='yes':
			UserUttered("/utter_ask_emailAddress", intent={'name': 'utter_ask_emailAddress', 'confidence': 1.0}),
			return [SlotSet("email", email)]
		else:
			UserUttered("/utter_goodbye", intent={'name': 'utter_goodbye', 'confidence': 1.0}),
			return [SlotSet("email", email)]