'''class Bank:
    bank_name='sbi'
    bank_ifsc=1245
    bank_roi=6
    bank_address='kizikistan'
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
jaya=Bank('jayasree',223344,1234,'banglore')
suma=Bank('suma',334455,2345,'chennai')
print(jaya.name)
print(jaya.bank_name)
print(suma.balance)


class Car:
    def __init__(self,mk,mdl,yy,clr,eng_si,fl_typ,mx_sp):
        self.make=mk
        self.model=mdl
        self.year=yy
        self.color=clr
        self.engine_size=eng_si
        self.fuel_type=fl_typ
        self.milage=0
        self.max_speed=mx_sp
        self.current_speed=0
        self.fuel_level=100
        def start(self):
            print('car is started')
        def stop(self):
            print('car was stopped')
            self.current_speed=0
        def accelerate(self,amount):
            if current_speed+amount<=self.max_speed:
                self.current_speed+=amount
                print(f'car was accelerated to {self.current_speed} mph')
            else:
                self.current_speed=self.max_speed
                print(f'the car was reached max speed of {self.max_speed} mph')
        def brake(self,amount):
            if self.current_speed-amount>=0:
                self.current_speed-=amount
                print('The car was slowed down to {self.current_speed} mph')
            else:
                self.current_speed=0
                print('The car was stopped')
        def refuel(self,amount):
            if self.fuel_level+amount<=100:
                self.fuel_level+=amount
                print('The car was refueled to {self.fuel_level} %')
            else:
                self.fuel_level=100
                print('The fuel tank is full')
        def honk(self):
            print('honk! honk!')
        def turn(self,direction):
            print(f'turning {direction}')
        def get_info(self):
            return f'{self.year} {self.make} {self.model}, color:{self.color},Engine:{self.engine_size}L,fuel:{self.fuel_type}'
my_car=Car('Suzuki','Swift',2024,'Blue',5.6,'diesel',150)
print(my_car.get_info())
my_car.start()
my_car.accelerate(50)
my_car.turn('right')
my_car.breake(20)
my_car.honk()
my_car.stop()
my_car.refuel(50)
    
'''
'''
class Car:
    def __init__(self, make, model, year, color, engine_size, fuel_type, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_size = engine_size
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.current_speed = 0
        self.fuel_level = 100
        self.mileage = 0
    def start(self):
        print("Car started")
    
    def stop(self):
        print("Car stopped")
        self.current_speed = 0
    
    def accelerate(self, amount):
        if self.current_speed + amount <= self.max_speed:
            self.current_speed += amount
            print(f"Accelerated to {self.current_speed} mph")
        else:
            self.current_speed = self.max_speed
            print(f"Reached max speed of {self.max_speed} mph")
    
    def brake(self, amount):
        if self.current_speed - amount >= 0:
            self.current_speed -= amount
            print(f"Slowed down to {self.current_speed} mph")
        else:
            self.current_speed = 0
            print("Car stopped")
    
    def refuel(self, amount):
        if self.fuel_level + amount <= 100:
            self.fuel_level += amount
            print(f"Refueled to {self.fuel_level}%")
        else:
            self.fuel_level = 100
            print("Fuel tank is full")
    def honk(self):
        print("Honk! Honk!")
    
    def turn(self, direction):
        print(f"Turning {direction}")
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Color: {self.color}, Engine: {self.engine_size}L, Fuel: {self.fuel_type}"

# Example usage
my_car = Car("Toyota", "Corolla", 2020, "Blue", 1.8, "Gasoline", 120)
print(my_car.get_info())
my_car.start()
my_car.accelerate(30)
my_car.turn("left")
my_car.brake(10)
my_car.honk()
my_car.stop()
my_car.refuel(20)

class A:
    x=9
    _y=10
    ___=43
    @classmethod
    def display(cls):
        print(cls.__z)
print(A.x)
print(A._y)
print(A.___)

import random
OPTIONS = ['rock', 'paper', 'scissors']
class RockPaperScissorsSimulator:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None
    def get_computer_choice(self):
        self.computer_choice = random.choice(OPTIONS)
    def get_human_choice(self):
        choice_number = int(input('Enter the number of your choice: '))
        self.human_choice = OPTIONS[choice_number - 1]
    def print_options(self):
        print('\n'.join(f'({i}) {option.title()}' for i,
              option in enumerate(OPTIONS)))
    def print_choices(self):
        print(f'You chose {self.human_choice}')
        print(f'The computer chose {self.computer_choice}')
    def print_win_lose(self, human_beats, human_loses_to):
        if self.computer_choice == human_loses_to:
            print(f'Sorry, {self.computer_choice} beats {self.human_choice}')
        elif self.computer_choice == human_beats:
            print(f'Yes, {self.human_choice} beats {self.computer_choice}!')
    def print_result(self):
        if self.human_choice == self.computer_choice:
            print('Draw!')
        if self.human_choice == 'rock':
            self.print_win_lose('scissors', 'paper')
        elif self.human_choice == 'paper':
            self.print_win_lose('rock', 'scissors')
        elif self.human_choice == 'scissors':
            self.print_win_lose('paper', 'rock')
    def simulate(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        self.print_result()
RPS = RockPaperScissorsSimulator()
RPS.simulate()
'''
import re
product_review = '''This is a fine milk, but the product
line appears to be limited in available colors. I
could only find white.'''
sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
matches = sentence_pattern.findall(product_review)
sentences = [match[0] for match in matches]
word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    matches = word_pattern.findall(sentence)
    words = [match[0] for match in matches]
    print(words)







































