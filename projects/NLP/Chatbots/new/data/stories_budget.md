## Happy Path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location" : "delhi"}
    - slot{"location" : "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine" : "chinese"}
    - slot{"cuisine" : "chinese"}
    - utter_ask_budget
* restaurant_search[budget=800]
	- slot{"budget" : "800"}
	- action_restaurant
	- utter_goodbye

## Generated Stories
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location" : "delhi"}
    - slot{"location" : "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine" : "chinese"}
    - slot{"cuisine" : "chinese"}
    - utter_ask_budget
* restaurant_search
	- slot{"budget" : "Less than 800"}
	- action_restaurant
	- utter_goodbye

## Generated Story -1339624582499543471
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location" : "pune"}
	- slot{"location" : "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
	- slot{"budget": ">700"} 
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## Generated Story -1339624582439543471
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location" : "pune"}
	- slot{"location" : "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
	- slot{"budget": "300-700"} 
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_goodbye
    - export