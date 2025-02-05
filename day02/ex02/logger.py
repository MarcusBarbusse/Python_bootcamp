import time 
import getpass
from random import randint
from time import process_time 

def log(function):
    user = getpass.getuser()
    def inner(*args, **kwargs):
        start = time.process_time()
        res = function(*args, **kwargs)
        total = time.process_time() - start
        with open("machine.log", "a+") as f:
            if (total > 0.001):
                f.write(f"({user})Running: {function.__name__:40s} [ exec-time = {total:3f} s ]\n")
            elif (total < 0.001):
                f.write(f"({user})Running: {function.__name__:40s} [ exec-time = {total * 1000:3} ms ]\n")
        return res
    return inner

class CoffeeMachine(): 
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20: 
            return True
        else:
            print("Please add water!") 
            return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine(): 
            for _ in range(20): 
                time.sleep(0.1)
                self.water_level -= 1 
            print(self.boil_water()) 
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5)) 
        self.water_level += water_level 
        print("Blub blub blub...")
    
if __name__ == "__main__":

        machine = CoffeeMachine() 
        for i in range(0, 5):
            machine.make_coffee()

        machine.make_coffee() 
        machine.add_water(70)