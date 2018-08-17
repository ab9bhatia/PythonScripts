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
* restaurant_search[budget=800]
	- slot{"budget" : "800"}
	- utter_ask_email
* restaurant_search[email="Yes"]
	- slot{"email" : "Yes"}
	- utter_ask_emailAddress
* restaurant_search[emailAddress="abc@gmail.com"]
	- slot{"emailAddress" : "abc@gmail.com"}
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
* restaurant_search
	- slot{"budget" : "Less than 800"}
	- utter_ask_email
* restaurant_search[email="Yes"]
	- slot{"email" : "Yes"}
	- utter_ask_emailAddress
* restaurant_search[emailAddress="abc@gmail.com"]
	- slot{"emailAddress" : "abc@gmail.com"}
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
	- utter_ask_email
* restaurant_search[email="Yes"]
	- slot{"email" : "Yes"}
	- utter_ask_emailAddress
* restaurant_search[emailAddress="abc@gmail.com"]
	- slot{"emailAddress" : "abc@gmail.com"}
	- action_restaurant
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
	- utter_ask_email
* restaurant_search[email="No"]
	- action_restaurant
	- utter_goodbye
    - export

## Generated Story 5607610188699372090
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300 - 700"}
    - slot{"budget": "300 - 700"}
    - action_restaurant
	- utter_ask_email
* restaurant_search[email="No"]
	- action_restaurant
	- utter_goodbye
    - export

## Generated Story -4687699300234469408
* greet
    - utter_greet
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - action_validate_city
    - slot{"location": null}
    - utter_goodbye
    - export

