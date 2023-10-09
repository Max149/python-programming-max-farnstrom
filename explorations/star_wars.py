class Empire:
    def __init__(self, name, special_ability):
        self.name = name
        self.special_ability = special_ability

class siths:
    def __init__(self, name, sith, s1, s2):
        self.name = name
        self.sith = sith
        self.s1 = s1
        self.s2 = s2

       

class inquisitors:
    def __init__(self, name):
        pass
        

s1 = siths(name = "Darth Vader")
print(s1)
s2 = siths(name = "Darth Sidious")
print(s2)