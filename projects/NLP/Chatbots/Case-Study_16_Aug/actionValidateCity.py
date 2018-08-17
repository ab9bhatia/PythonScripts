from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import UserUttered
from rasa_core.events import BotUttered


class ValidateCity(Action):
    def name(self):
        return 'action_validate_city'
    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('location')
        citylist=['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune', 'agra', 'ajmer', 'aligarh', 
				'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 
				'bhubaneswar', 'bikaner', 'bokarosteelcity', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilainagar', 
				'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati‚gwalior', 
				'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 
				'kanpur', 'kakinada', 'kochi', 'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 
				'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 
				'palakkad', 'patna', 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 
				'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 
				'vadodara', 'varanasi', 'vasai-virarcity', 'vijayawada', 'visakhapatnam', 'warangal']
        if location.lower() in citylist:
            UserUttered("/utter_ask_cuisine", intent={'name': 'utter_ask_cuisine', 'confidence': 1.0}),
            return [SlotSet("location", location )]
        else:
            dispatcher.utter_message("We don't serve in " + location +" city " )
            UserUttered("/utter_goodbye", intent={'name': 'utter_goodbye', 'confidence': 1.0}),
            return [SlotSet("location", None)]