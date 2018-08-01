import sys
from st2actions.runners.pythonrunner import Action

class CreateTicket(Action):
    def run(self, param1, param2, param3):
        print('param1 ')
        #print("param1 " + str(param1))
        #print("param1 " + str(param1))
        return (True, "Action run is successfull")


