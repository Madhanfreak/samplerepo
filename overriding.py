class dad:
    def action(self):
        print("Head of family")
        

class son(dad):
    def elder(self):
        print("Legal powers")
    
    def action(self):
        return super().action()
    print("Now im only Head")



final = son()

final.action() 