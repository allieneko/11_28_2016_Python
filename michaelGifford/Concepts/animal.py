from animalModule import Animal

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        # print ('Dog')
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        # print ('Dragon')
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print ('This is a dragon!')
        super(Dragon, self).displayHealth()
        return self

fido = Dog('Fido').walk().walk().walk().run().run().pet().displayHealth()

puff = Dragon('Puff').walk().walk().walk().run().run().fly().fly().displayHealth()

monkey = Animal('George')
monkey.displayHealth().run().walk().displayHealth()