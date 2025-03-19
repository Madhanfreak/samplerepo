class dad:
    def action(self):
        print("Head of family")
        self.__private_function()


    def __private_function(self):
        print("im private")    

class son(dad):
    def elder(self):
        print("Legal powers")


final = son()
final.elder() 
final.action() #acess the class Dad using clss son


