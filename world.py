data = {
    # update this state as the game progresses
    "current_state": {"room": "witch_house",
                      "inventory": { "coins":True,"knife":True,"chains":True,"ring":True},  # the things they carried
                      "playing": False  # flag: True until the player quits
                      },

    # these are objects in the world, and their properties
    "objects": {
        "coins": {"description": "I discovered a handful of rusty old coins in my pocket, their once-shiny surfaces now tarnished with time and weathered by countless hands."},
        "vial": {"description": "I stumbled upon a small, suspicious vial hidden in my pocket, its contents a mystery, wrapped in an aura of uncertainty."},
        "knife": {"description": "I unearthed a rusty, yet remarkably sharp knife from my leg sheath, a relic of age with an unexpected edge."},
        "herbs": {"description": "On the table, I discovered an array of magical herbs, each leaf and petal shimmering with an otherworldly glow, their enchanting fragrance filling the air."},
        "cauldron": {"description": "In the center of the room, there stood a cauldron, its metal surface stained with vibrant shades of purple, hinting at the potent brews that had once bubbled within."},
        "potion": {"description": "The mysterious antimagnetic potion was a shimmering, iridescent liquid that seemed to defy the laws of attraction, promising to ward off even the strongest magnetic forces."},
        "wand": {"description": "The old magical wand exuded an aura of ancient power, but its twisted, gnarled wood and eerie engravings sent a shiver down my spine, leaving me with an unsettling sense of unease."},
        "mirror": {"description": "A magical mirror that reflects everything in the room except for my own reflection, leaving me with a sense of both wonder and curiosity."},
        "parchment": {"description": "An old, fragile parchment. It says: <<Beware, for you have invoked my ire. A curse now binds your fate, and darkness shall be your constant companion. Each step you take, every breath you draw, will be a struggle. My magic will haunt your days and torment your nights.>> Frightening."},
        "chains": {"description": "The old, rusty magic chains, their surface marred by time, retained an unbreakable strength, a testament to their enduring enchantment."},
        "ring": {"description": "The magic gold ring, adorned with intricate runes, clung to my finger like an unyielding bond, defying all attempts to remove it."},
        "torch": {"descrption": "A charred torch."},
        "sign" : {"description" : "ÐU NE WILLCUMEN GEONDGAN."},
        "lake": {"description": "The magical lake, its pristine waters shimmering with an ethereal glow, denied touch and reflection, holding secrets beyond the grasp of mortal curiosity."}
    },

    # these are the rooms in the world
    "rooms": {
        "witch_house": {
            "description": "A haunted witch house, shrouded in eerie mists, echoes with ghostly whispers and flickering candles, where spells of the past linger.",
            "exits": {
                "north": "swamp_main"
            },
            "img_url":"",
            "objects": {"herbs":True , "potion":True , "wand":True , "mirror":True , "cauldron":True
            },
        },
        "swamp_main": {
            "description": "In the heart of the eerie, dark swamp, murky waters hide secrets, tangled roots beckon the curious, and shadows dance mysteriously.",
            "objects": { "sign":True, "lake": True
            },
            "exits": {"south": "witch_house", "north": "bridge" , "west" : "cave" , "east" : "church"},
        },
        "church": {
            "description": "Within the dark, abandoned church, decaying pews crumble under ghostly shadows, and a spectral chill lingers, whispering tales of the past.",
            "objects": {
            },
            "exits": {"west": "swamp_main"},
        },
        "cave": {
            "description": "Inside the foreboding cave, darkness envelops, broken only by sporadic glimmers of distant phosphorescent fungi. Eerie echoes reverberate, while a strange, luminescent slime creature beckons silently. Its pulsating form creates an uncanny ambiance, both intriguing and unsettling, as it lures with an otherworldly call that tugs at curiosity and fear.",
            "objects": {

            },
            "exits": {"east": "swamp_main"},
        },
        "bridge": {
            "description": "Upon the bridge, an enigmatic invisible barrier halts progress. When you reach out, magic particles swirl around your fingers, revealing an arcane force that defies explanation and beckons further exploration.",
            "objects": {
            },
            "exits": {"north" : "after_bridge"},
        }

    },

}