import random 
class Spinner:
    def __init__(self):
        self.storage = {"default": []}
        self.current_basket = "default"

    def add(self, item):
        self.storage[self.current_basket].append(item)
    
    def remove(self, item):
        self.storage[self.current_basket].remove(item)
    
    def spin(self):
        random_index = random.randint(-100000, 100000) % len(self.storage[self.current_basket])

        return self.storage[self.current_basket][random_index]
    
    def info(self):
        output = ""
        output += f"{self.current_basket}\n"
        
        for item in self.storage[self.current_basket]:
            output += f"{item}\n"

        return output 

    def change_basket(self, basket_name):
        self.current_basket = basket_name

        if basket_name not in self.storage:
            self.storage[basket_name] = []
    
    def remove_basket(self, basket_name):
        del self.storage[basket_name]
        
        if basket_name == "default":
            self.storage[basket_name] = [] 
        
        self.change_basket("default")
        
    def info_basket(self):
        baskets = list(self.storage.keys())
        return "\n".join(baskets) 
 
    def coin(self):
        choices = ["heads", "tails"]
        return random.choice(choices)