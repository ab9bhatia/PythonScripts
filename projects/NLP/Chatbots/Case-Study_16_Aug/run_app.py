from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-412133759184-412851474258-417522628196-c6b665ff8b0efe3468fc5dd809d549db', #app verification token
							'xoxb-412133759184-413989836404-FJUCyTafX42oLGpDhdL3DSsJ', # bot verification token
							'9zpFsCmaRRJl1CiRmiWQhqjv', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))