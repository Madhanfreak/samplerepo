class encapsulation:
    def public(self):
        print("public function")
        self._protected()            #call protected function


    def _protected(self):
        print("protected Function") 
        self.__private()            #call private function

    def __private(self):
        print("private Function")

result = encapsulation()        #using Object, Hiding the data(Encapsulation)
result.public()                       #call public function



