## Happy Path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location" : "delhi"}
    - slot{"location" : "delhi"}
    - action_validate_city
    - utter_ask_cuisine
* restaurant_search{"cuisine" : "chinese"}
    - slot{"cuisine" : "chinese"}
    - utter_ask_budget
* restaurant_search[budget= 800]
	- slot{"budget" : 800}	
	- action_restaurant	
	- utter_goodbye

## Generated Stories
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location" : "delhi"}
    - slot{"location" : "delhi"}
    - action_validate_city
    - utter_ask_cuisine
* restaurant_search{"cuisine" : "chinese"}
    - slot{"cuisine" : "chinese"}
    - utter_ask_budget
* restaurant_search[budget= "more than 400"]
	- slot{"budget" : "more than 400"}	
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
	- utter_goodbye

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
* restaurant_search{"budget": "300 to 700"}
	- slot{"budget": "300 to 700"} 
	- action_restaurant	
	- utter_goodbye

## Generated Story 5607610188699372090
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "300 - 700"}
    - slot{"budget": "300 - 700"}
	- action_restaurant	
	- utter_goodbye
	
## Generated Story 5607610188699372091
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
	- action_restaurant	
	- utter_goodbye
## Generated Story 5607610188699372091
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "less than 300"}
    - slot{"budget": "less than 300"}
	- action_restaurant	
	- utter_goodbye
	
## Generated Story -4687699300234469408
* greet
    - utter_greet
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - action_validate_city
    - slot{"location": null}
    - utter_goodbye
    - export

