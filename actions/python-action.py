import sys
from st2actions.runners.pythonrunner import Action
#from st2common.runners.base_action import Action

class CreateTicket(Action):
    def run(self, message):
        print(message)
        #print("param1 " + str(param1))
        #print("param1 " + str(param1))
        return (True, "Action run is successfull")


