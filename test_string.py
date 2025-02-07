class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age
        
    def greet(self):
        print(f'Hellow my name is {self.name} and I am {self.age} years old')
        

def main():
        person1 = Person('Reslychen', 26)
        person1.greet()

        person2 = Person('Adrian', 25)
        person2.greet()

if __name__ == "__main__":

        main()