import random 
class Dreidel:
    def __init__(self):
        self.actions = {
            1: {
                "face_name": "Gimmel",
                "meaning": "You win the whole pot!"
            },
            2: {
                "face_name": "Shin",
                "meaning": "Put 2 in the pot!"
            },
            3: {
                "face_name": "Hey",
                "meaning": "You win half the pot!"
            },
            4: {
                "face_name": "Nun",
                "meaning": "Do nothing..."
            }
        }
    
    def spin(self):
        random_index = random.randint(1, 5)
        random_side = self.actions[random_index]

        return random_side
