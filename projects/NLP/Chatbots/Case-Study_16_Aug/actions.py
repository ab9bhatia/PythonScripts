from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pprint

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"b150e50385939f3d2fca77c2cca1e072"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		bud= tracker.get_slot('budget')
		email = tracker.get_slot('email')
		emailAddress= tracker.get_slot('emailAddress')
		print(email)
		print(emailAddress)
		tmp = next(tracker.get_latest_entity_values('budget'), None)
		#print (tmp)
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 15)
		d = json.loads(results)
		response=[]
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				price=restaurant['restaurant']['average_cost_for_two']
				if("-" in bud):
    					lowbudget=int(bud[0:bud.index('-')])
    					highbudget=int(bud[bud.index('-')+1:])
    					if(lowbudget <= price & highbudget >= price):
    						print (lowbudget,highbudget)
    						response.append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " with an average cost for two  " +str(price))
				if(int(bud) < price):
					print (bud)
					response.append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " with an average cost for two  " +str(price))
				#if("<" in bud):
				#	if(int(bud) < price):
				#		print (bud)
				#		response.append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " with an average cost for two  " +str(price))

		dispatcher.utter_message("-----"+str(response[:5]))
		return [SlotSet('location',loc)]

