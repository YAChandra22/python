'''def is_Prime(n):
    if n > 1:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return "Given number is not a prime"
        else:
            return f'Given number {n} is prime'
    else:
        return "Given number is not a prime"

def prime_No(n):
    return is_Prime(n)
print(prime_No(13))'''
#Armstrong Number
'''def is_Armstrong(n):
    l=len(str(n))
    s=0
    d=n
    while d>0:
        rem=d%10
        d=n//10
        s+=rem**l
    if s==n:
        return f'given number {n} is armstrong number'
def armstrong(n):
    return is_Armstrong(n)
print(armstrong(153))
'''
# Simple simulation game for Codeville Adventure

import random

# Basic classes for OOP concepts

class Building:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"{self.name} (Cost: {self.cost})"

class City:
    def __init__(self):
        self.resources = 1000
        self.buildings = []

    def add_building(self, building):
        if self.resources >= building.cost:
            self.buildings.append(building)
            self.resources -= building.cost
            print(f"Built {building.name}. Remaining resources: {self.resources}")
        else:
            print("Not enough resources to build.")

    def collect_resources(self):
        collected = random.randint(50, 150)
        self.resources += collected
        print(f"Collected {collected} resources. Total resources: {self.resources}")

def main():
    city = City()

    # Sample buildings
    farm = Building("Farm", 300)
    factory = Building("Factory", 500)

    # Game loop
    while True:
        print("\nWelcome to Codeville Adventure!")
        print("1. Collect resources")
        print("2. Build a Farm")
        print("3. Build a Factory")
        print("4. Check Resources")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            city.collect_resources()
        elif choice == "2":
            city.add_building(farm)
        elif choice == "3":
            city.add_building(factory)
        elif choice == "4":
            print(f"Current resources: {city.resources}")
        elif choice == "5":
            print("Exiting game.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()



















