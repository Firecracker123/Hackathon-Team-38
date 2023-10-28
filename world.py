# Read this dictionary carefully, and understand how it is defining the world

world = {
    # update this state as the game progresses
    "current_state" : {"room":"dungeon", 
                       "inventory":{"hood":True}, # the things they carried
                       "playing":True # flag: True until the player quits
                      },
    
    # these are objects in the world, and their properties
    "objects" : {
        "hood":{"description":"A worn hood made of coarse, greyish fabric."},
        "quill":{"description":"An old-fashioned quill pen"},
        "parchment":{"description":"An oddly-stained parchment paper."},
        "carrot": {"description":"a fresh orange carrot"},
        "torch":{"descrption":"A charred torch"}
    },
    
    # these are the rooms in the world
    "rooms": {
        "dungeon": {
            "description": "A cold dark room with a wooden hatch and a ladder leading up to it.",
            "exits": {
                # direction : name of room to go to
                "up": "guard_room"
            },
            "objects": {
                # name : True if present (note: dictionary used as a set)
                "carrot":True
            },
        },
        "guard_room": {
            "description": "A small stone chamber with a candle burning on an empty desk. The room smells of tallow and straw.",
            "objects": {
                "quill": True,
                "parchment":True                
            },
            "exits": {"down": "dungeon", "north": "stone_corridor"},
        },
        "stone_corridor": {
            "description": "A dank, narrow chamber of coarse rock. Thick veins of nitre run down the walls. This way is blocked.",
            "objects": {"torch": True},
            "exits": {"south": "guard_room"},
        },
    },
  
}