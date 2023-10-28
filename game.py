import world
def exits():
    current_room = world.data["current_state"]["room"]
    s = ""
    for direction in world.data["rooms"][current_room]["exits"].keys():
        s += direction
        s += " "
    print("You can go: " + s)


def inventory():
    s = ""
    items = world.data["current_state"]["inventory"]
    for item in items:
        if items[item]:
            s += item
            s += " "
    if (s == ""):
        print("You are not carrying anything.")
    else:
        print("You are carrying: " + s)


def look():
    room = world.data["current_state"]["room"]
    print(world.data["rooms"][room]["description"])
    objects_around = world.data["rooms"][room]["objects"]
    l = []
    for obj in objects_around:
        if objects_around[obj]:
            l.append(obj)
    if len(l) == 0:
        print("There is nothing around here.")
    elif len(l) == 1:
        print("There is a {obj} here.".format(obj=l[0]))
    else:
        print("There is a", end=" ")
        for pos, elt in enumerate(l):
            if pos != len(l) - 1:
                print("{thing} and a".format(thing=elt), end=" ")
            else:
                print("{thing} here.".format(thing=elt))


def examine(obj):
    inv = world.data["current_state"]["inventory"]
    room = world.data["current_state"]["room"]
    items_in_room = world.data["rooms"][room]["objects"]

    if obj in inv and inv[obj]:
        print(world.data["objects"][obj]["description"])
    elif obj in items_in_room and items_in_room[obj]:
        print(world.data["objects"][obj]["description"])
    else:
        print("There is no such thing around")


def take(obj):
    room = world.data["current_state"]["room"]
    items_in_room = world.data["rooms"][room]["objects"]
    inv = world.data["current_state"]["inventory"]

    if obj in items_in_room and items_in_room[obj]:
        if obj == "sigil":
            if "necklace" in items_in_room and items_in_room[obj]:
                items_in_room[obj] = False
                inv[obj] = True
                print("You take the {obj}!".format(obj=obj))
            else:
                print("You cannot take the sigil yet. Solve the riddle first.")
        elif obj != "mirror":
            items_in_room[obj] = False
            inv[obj] = True
            print("You take the {obj}!".format(obj=obj))
            if(obj == "necklace"):
                print("Maybe I should bring this to the slime...")
        else:
            print("You cannot take this object. Its presence makes you feel uneasy.")
    else:
        print("I don't see a {obj} here.".format(obj=obj))


def drop(obj):
    room = world.data["current_state"]["room"]
    items_in_room = world.data["rooms"][room]["objects"]
    inv = world.data["current_state"]["inventory"]

    if obj in inv and inv[obj]:
        inv[obj] = False
        items_in_room[obj] = True
        print("You drop the {obj}".format(obj=obj))
        take("sigil")
    else:
        print("You don't have this item in your inventory")


def go(direction):
    room = world.data["current_state"]["room"]
    items_in_room = world.data["rooms"][room]["objects"]
    directions = world.data["rooms"][room]["exits"]

    if direction in directions:
        if room == "bridge" and direction=="north":
            if "sigil" in items_in_room:
                world.data["current_state"]["room"] = directions[direction]
            else:
                print("You cannot cross yet.")
        else:
            world.data["current_state"]["room"] = directions[direction]
            look()
            # print("You are now in the {place}.".format(place=directions[direction]))
    else:
        print("You cannot go there!")

def start():
    world.data["current_state"]["playing"]=True

def quit():
    world.data["current_state"]["playing"]=False


def do(act, something=None):
    actions = {"go": go, "inventory": inventory,
               "exits": exits, "take": take, "drop": drop,
               "examine": examine, "quit": quit,
               "start" : start,
               "look": look}
    if act in actions:
        if something is None:
            return actions[act]()
        else:
            return actions[act](something)
    else:
        print("I cannot do that.")
def game():
    prompt=input()
    prompt=prompt.lower()
    while(True):
        if prompt == "start":
            world.data["current_state"]["playing"]=True
            go("north")

        elif world.data["current_state"]["playing"] == False:
            pass

        elif prompt=="quit":
            desc="Thank you for playing!"
            world.data["current_state"]["playing"]=False
            print("Ty for playing")
            break
        else:
            prompt = prompt.split()
            if len(prompt) == 1:
                do(prompt[0])
            elif len(prompt) == 2:
                do(prompt[0], prompt[1])
            else:
                print("I cannot take such long commands unfortunately...")
        prompt=input()
        prompt=prompt.lower()
        #game()

def user_input(prompt):
    if prompt == "start":
        world.data["current_state"]["playing"]=True
        go("north")

    elif world.data["current_state"]["playing"] == False:
        pass

    elif prompt=="quit":
        desc="Thank you for playing!"
        world.data["current_state"]["playing"]=False
        print("Ty for playing")
    else:
        prompt = prompt.split()
        if len(prompt) == 1:
            do(prompt[0])
        elif len(prompt) == 2:
            do(prompt[0], prompt[1])
        else:
            print("I cannot take such long commands unfortunately...")
