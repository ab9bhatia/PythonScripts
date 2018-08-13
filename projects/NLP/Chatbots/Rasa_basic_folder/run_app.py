from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput



nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-416133588359-415099094818-416419438838-be6c28bebce66dbbc70face9257a385d', #app verification token
							'xoxb-416133588359-416419439254-XqEL9I11gjBq5HH5NeZU7ftV', # bot verification token
							'w3hHBikLKgmocv4yGbb6zh7a', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))