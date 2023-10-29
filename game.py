import world
import copy


def exits():
    current_room = world.data["current_state"]["room"]
    s = ""
    for direction in world.data["rooms"][current_room]["exits"].keys():
        s += direction
        s += " "
    world.data["output"] = "You can go: " + s


def inventory():
    s = ""
    items = world.data["current_state"]["inventory"]
    for item in items:
        if items[item]:
            s += item
            s += " "
    if s == "":
        world.data["output"] = "You are not carrying anything."
    else:
        world.data["output"] = "You are carrying: " + s


def look():
    output = ""
    room = world.data["current_state"]["room"]
    output += world.data["rooms"][room]["description"] + " "
    objects_around = world.data["rooms"][room]["objects"]
    l = []
    for obj in objects_around:
        if objects_around[obj]:
            l.append(obj)
    if len(l) == 0:
        output += "There is nothing around here."
    elif len(l) == 1:
        output += "There is a {obj} here.".format(obj=l[0])
    else:
        output += "There is a "
        for pos, elt in enumerate(l):
            if pos != len(l) - 1:
                output += "{thing} and a ".format(thing=elt)
            else:
                output += "{thing} here.".format(thing=elt)

    world.data["output"] = output


def examine(obj):
    inv = world.data["current_state"]["inventory"]
    room = world.data["current_state"]["room"]
    items_in_room = world.data["rooms"][room]["objects"]

    if obj is None:
        world.data["output"] = "What should I examine?"
        return

    if obj in inv and inv[obj]:
        world.data["output"] = world.data["objects"][obj]["description"]
    elif obj in items_in_room and items_in_room[obj]:
        world.data["output"] = world.data["objects"][obj]["description"]
    else:
        world.data["output"] = "There is no such thing around"


def take(obj):
    room = world.data["current_state"]["room"]
    items_in_room = world.data["rooms"][room]["objects"]
    inv = world.data["current_state"]["inventory"]

    if obj is None:
        world.data["output"] = "What should I take?"
        return

    if obj in items_in_room and items_in_room[obj]:
        if obj == "sigil":
            if "necklace" in items_in_room and items_in_room[obj]:
                items_in_room[obj] = False
                inv[obj] = True
                world.data["output"] = "You take the {obj}!".format(obj=obj)
            else:
                world.data[
                    "output"
                ] = "You cannot take the sigil yet. Solve the riddle first."
        elif obj != "mirror":
            items_in_room[obj] = False
            inv[obj] = True
            world.data["output"] = "You take the {obj}!".format(obj=obj)
            if obj == "necklace":
                world.data["output"] = "Maybe I should bring this to the slime..."
        else:
            world.data[
                "output"
            ] = "You cannot take this object. Its presence makes you feel uneasy."
    else:
        world.data["output"] = "I don't see a {obj} here.".format(obj=obj)


def drop(obj):
    room = world.data["current_state"]["room"]
    items_in_room = world.data["rooms"][room]["objects"]
    inv = world.data["current_state"]["inventory"]

    if obj is None:
        world.data["output"] = "What should I drop?"
        return

    if obj in inv and inv[obj]:
        inv[obj] = False
        items_in_room[obj] = True
        world.data["output"] = "You drop the {obj}".format(obj=obj)
        if room=="cemetery" and "ghost" in items_in_room and items_in_room["ghost"]:
            print("Thank you, human! You may slay the evil witch by using a bow and a silver arrow!")
        if obj == "necklace" and "sigil" in items_in_room and items_in_room["sigil"]:
            take("sigil")
    else:
        world.data["output"] = "You don't have this item in your inventory"

def ininv(object):
    inventory = world.data["current_state"]["inventory"]
    return object in inventory and inventory[object]

def kill(entity):
    current_room = world.data["current_state"]["room"]
    inventory = world.data["current_state"]["inventory"]
    room = world.data["rooms"][current_room]

    if entity is None:
        world.data["output"] = "Who should I kill?"
        return

    if entity == "witch":
        if entity in room["objects"]:
            if ininv("lake"): 
                 world.data["output"] = """You've vanquished the malevolent witch and 
                                        brought peace to the land. 
                                        As the murky waters of the cursed lake swallow her, 
                                        the world is finally free from her wicked grasp. You win!"""
            elif (ininv("bow") and ininv("arrow")):
                world.data["output"] = """You accurately land an arrow on the witch's head. 
                                        The witch slowly collapses to the ground. You win!"""
            elif ininv("bow"):
                 world.data["output"] = "I need to find an arrow to use with my bow..."
            elif ininv("arrow"):
                 world.data["output"] = "I need to find a bow to use with my arrow..."
            else:
                world.data["output"] = """I don't have a powerful enough weapon for this... 
                                        maybe I should go back and find one."""
        else:
            world.data["output"] = f"The %s is not here..." % entity
    else:
        world.data["output"] = f"I cannot kill %s!" % entity


def help():
    output = "Actions: || "
    output += "exits || "
    output += "go [direction] || "
    output += "inventory || "
    output += "take [object] || "
    output += "drop [object] || "
    output += "examine [object] || "
    output += "look || "
    output += "talk [creature] || "
    output += "kill [creature] || "
    output += "quit"

    world.data["output"] = output


def go(direction):
    room = world.data["current_state"]["room"]
    items_in_room = world.data["rooms"][room]["objects"]
    directions = world.data["rooms"][room]["exits"]

    if direction is None:
        world.data["output"] = "'go' where?"
        return

    if direction in directions:
        if room == "bridge" and direction == "north":
            if "sigil" in items_in_room:
                world.data["current_state"]["room"] = directions[direction]
                look()
            else:
                world.data["output"] = "You cannot cross yet."
        elif direction != "treehouse":
            world.data["current_state"]["room"] = directions[direction]
            look()
            # output += "You are now in the {place}.".format(place=directions[direction]))
        else:
            world.data["current_state"]["room"] = directions[direction]
            look()
            quit()
    else:
        world.data["output"] = "You cannot go there!   Use 'exits' to view exits."


def start():
    world.data["current_state"]["playing"] = True


def quit():
    world.data["current_state"]["playing"] = False


def talk(obj):
    if obj is None:
        world.data["output"] = "Who should I talk to?"
        return
    
    if obj == "witch" or obj == "slime" or obj == "ghost":
        examine(obj)
    else:
        world.data["output"] = "You cannot talk to this object."


def do(act, something=None):
    actions = {
        "inventory": inventory,
        "exits": exits,
        "quit": quit,
        "start": start,
        "look": look,
        "help": help,
    }

    actions_one_noun = {
        "talk": talk,
        "kill": kill,
        "examine": examine,
        "go": go,
        "take": take,
        "drop": drop,
    }
    if act in actions:
        return actions[act]()
    elif act in actions_one_noun:
        if not (something is None):
            return actions_one_noun[act](something)
        elif act == "go":
            world.data["output"] = "You must specify a direction to go to."
        elif act == "talk":
            world.data["output"] = "You must specify a creature to talk to."
        else:
            world.data["output"] = f"You must specify an object to %s." % act
    else:
        world.data["output"] = f"I don't know how to %s." % act
        #world.data["output"] = "I cannot do that."


def user_input(prompt):
    room_name = world.data["current_state"]["room"]
    room = world.data["rooms"][room_name]
    if prompt == "start":
        world.data = copy.deepcopy(world.data_copy)
        world.data["current_state"]["playing"] = True
        go("north")

    elif world.data["current_state"]["playing"] == False:
        pass

    elif room_name == "hell":
        world.data["output"] = """It's game over.. 
                                    you can only restart using 'start' now."""

    elif prompt == "quit":
        world.data = copy.deepcopy(world.data_copy)
        desc = "Thank you for playing!"
        world.data["current_state"]["playing"] = False
        world.data["output"] = "Ty for playing! Type 'start' to restart."
    else:
        prompt = prompt.split()
        if len(prompt) == 1:
            do(prompt[0])
        elif len(prompt) == 2:
            do(prompt[0], prompt[1])
        else:
            world.data["output"] = "I cannot take such long commands unfortunately..."
