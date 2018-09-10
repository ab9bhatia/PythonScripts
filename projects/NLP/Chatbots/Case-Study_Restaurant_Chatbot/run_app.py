from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-416133588359-415099094818-420034981543-fce2b3ed7e7da5d8ba75cb518adbf834', #app verification token
							'xoxb-416133588359-420334838470-8webzIM7OLD6jdMKqxJAJqfr', # bot verification token
							'ADRtxEif3aiezm8zx4zfCZ1R', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))