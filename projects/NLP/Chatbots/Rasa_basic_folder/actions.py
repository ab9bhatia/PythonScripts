from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pprint
import re

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
	
	# Function to get the lowest & highest values from the budget string.
	def getBudget(d,budget):
		bud_range = re.findall(r"\d+", budget)
		bud_range = [int(i) for i in bud_range]

		if (len(bud_range) >=2):
			lowest = min(bud_range)
			highest = max(bud_range)
		else:
			bud_words = [x.lower() for x in bud.split()]
			low = ['low','lower','lesser','ends','from']
			high = ['high','higher','greater','starts','to','limit']
			match_low = [i for i in low if i in bud_words]
			match_high = [i for i in high if i in bud_words]
			if (len(match_low) >= 0):
				lowest = min([restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']])
				highest = bud_range[0]
			elif(len(match_high) >= 0):
				lowest = bud_range[0]
				highest = max([restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']])
		return lowest,highest
	
	def run(self, dispatcher, tracker, domain):
	
		# provide API key and initialise a 'zomato app' object
		config={ "user_key": "78c87a6483c0723fb0743bb4e9ab417d"}
		zomato = zomatopy.initialize_app(config)
		
		# get details of location, cuisine & budget
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		bud= tracker.get_slot('budget')

		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 15)
		d = json.loads(results)
		
		# Custom logic to get the lowest & highest range from the budget
		lowest, highest = getBudget(d,budget=bud)

		response=[]
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				price = restaurant['restaurant']['average_cost_for_two']
				if((price >=lowest) & (price <= highest)):
					#print(price)
					response.append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ \
                            " with an average cost for two  " +str(price))
							
		dispatcher.utter_message("-----"+str(response[:5]))
		return [SlotSet('location',loc)]
