import world


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

    if obj in inv and inv[obj]:
        inv[obj] = False
        items_in_room[obj] = True
        world.data["output"] = "You drop the {obj}".format(obj=obj)
        if obj == "necklace" and "sigil" in items_in_room and items_in_room["sigil"]:
            take("sigil")
    else:
        world.data["output"] = "You don't have this item in your inventory"

def kill(entity):
    current_room = world.data["current_state"]["room"]
    inventory = world.data["current_state"]["inventory"]
    room = world.data["rooms"][current_room]

    if entity == "witch":
        if entity in room["objects"]:
            pass # check for bow and arrow (or lake)
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
    output += "talk [entity] || "
    output += "quit"

    world.data["output"] = output

def go(direction):
    room = world.data["current_state"]["room"]
    items_in_room = world.data["rooms"][room]["objects"]
    directions = world.data["rooms"][room]["exits"]

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
        world.data["output"] = "You cannot go there!"


def start():
    world.data["current_state"]["playing"] = True


def quit():
    world.data["current_state"]["playing"] = False


def talk(obj):
    if obj == "witch" or obj == "slime" or obj == "ghost":
        examine(obj)
    else:
        world.data["output"] = "You cannot talk to this object."


def do(act, something=None):
    actions = {
        "go": go,
        "inventory": inventory,
        "exits": exits,
        "take": take,
        "drop": drop,
        "examine": examine,
        "quit": quit,
        "start": start,
        "look": look,
        "talk": talk,
        "help": help,
    }
    if act in actions:
        if something is None:
            return actions[act]()
        else:
            return actions[act](something)
    else:
        world.data["output"] = "I cannot do that."


def user_input(prompt):
    if prompt == "start":
        world.data["current_state"]["playing"] = True
        go("north")

    elif world.data["current_state"]["playing"] == False:
        pass

    elif prompt == "quit":
        desc = "Thank you for playing!"
        world.data["current_state"]["playing"] = False
        world.data["output"] = "Ty for playing"
    else:
        prompt = prompt.split()
        if len(prompt) == 1:
            do(prompt[0])
        elif len(prompt) == 2:
            do(prompt[0], prompt[1])
        else:
            world.data["output"] = "I cannot take such long commands unfortunately..."
