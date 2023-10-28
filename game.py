from world import world

class Game:
    def __init__(self):
        self.world = world
        self.description = self.describe()
        
    def describe(self):
        room = world["current_state"]["room"] 
        rooms = world["rooms"]
        
        description = rooms[room]["description"]
        # print out each object
        for obj in rooms[room]["objects"]:
            description += " There is a {object} here.".format(object=obj)
            
        return description
    
    def actions(self, verb):
        actions = {}
        return actions[verb]()
    
g = Game()