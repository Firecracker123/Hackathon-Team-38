data = {
    # update this state as the game progresses
    "current_state": {"room": "main_menu",
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
        "torch": {"description": "A charred torch."},
        "necklace": {"description": "The golden magical necklace gleamed with an enchanting radiance, a masterpiece of elegance and mystery."},
        "cloak": {"description": "The dirty but appealing and mysterious cloak bore the marks of countless journeys, its shabby exterior concealing a world of enigmatic charm and adventure within."},
        "slime" : {"description" : "<<I'm hidden within a place of worship so grand, With jewels and gems, I'm carefully planned. Adorning the neck, in a sacred embrace, Where am I found, in this hallowed place?>> Drop this object at my feet and I shall help you."},
        "axe": {"description": "ÐU NE WILLCUMEN GEONDGAN."},
        "note": {"description": "Release its power to the ground, let nature decide."},
        "sigil": {"description": "A sigil of liberation, etched in shimmering silver, emanates an aura of arcane potential. Its compact design is a tangle of interwoven lines and cryptic symbols, a key to unbind enchantments and break the chains of magic."},
        "sign": {"description": "The wooden handle, darkened by years of sweat and grit, still retains a sturdy resilience, despite the passage of time. This old sharp axe is a testament to the enduring craftsmanship of yesteryears"},
        "lake": {"description": "The magical lake, its pristine waters shimmering with an ethereal glow, denied touch and reflection, holding secrets beyond the grasp of mortal curiosity."}
    },

    # these are the rooms in the world
    "rooms": {
        "witch_house": {
            "description": "A haunted witch house, shrouded in eerie mists, echoes with ghostly whispers and flickering candles, where spells of the past linger.",
            "exits": {
                "outside": "swamp_main"
            },
            "img_url":"static/images/witchy_house.jpeg",
            "objects": {"herbs":True , "potion":True , "wand":True , "mirror":True , "cauldron":True
            },
        },
        "swamp_main": {
            "description": "In the heart of the eerie, dark swamp, murky waters hide secrets, tangled roots beckon the curious, and shadows dance mysteriously.",
            "objects": { "sign":True, "lake": True
            },
            "img_url":"static/images/swamp.jpeg",
            "exits": {"south": "witch_house", "north": "bridge" , "west" : "cave" , "east" : "church"},
        },
        "church": {
            "description": "Within the dark, abandoned church, decaying pews crumble under ghostly shadows, and a spectral chill lingers, whispering tales of the past.",
            "objects": {
            },
            "img_url": "static/images/church.jpeg",
            "exits": {"west": "swamp_main" , "down":"cellar"}
        },
        "cellar": {
            "description": "In the dark haunted cellar, an eerie gloom shrouded all, but a lone golden necklace emitted a hauntingly beautiful glow, its brilliance cutting through the shadows.",
            "objects": { "necklace":True , "cloak":True
            },
            "img_url": "static/images/church.jpeg",
            "exits": {"up": "church"},
        },
        "cave": {
            "description": "Inside the foreboding cave, darkness envelops, broken only by sporadic glimmers of distant phosphorescent fungi. Eerie echoes reverberate, while a strange, luminescent slime creature beckons silently. Its pulsating form creates an uncanny ambiance, both intriguing and unsettling, as it lures with an otherworldly call that tugs at curiosity and fear.",
            "objects": { "slime":True , "axe":True , "sigil":True
            },
            "img_url": "static/images/cave.jpeg",
            "exits": {"east": "swamp_main"},
        },
        "bridge": {
            "description": "Upon the bridge, an enigmatic invisible barrier halts progress. When you reach out, magic particles swirl around your fingers, revealing an arcane force that defies explanation and beckons further exploration.",
            "objects": { "note":True
            },
            "img_url": "static/images/bridge.jpeg",
            "exits": {"north" : "after_bridge", "south":"swamp"},
        },
        "after_bridge": {
            "description": "you have crossed",
            "objects": {
                        },
            "img_url": "static/images/after_bridge.jpeg",
            "exits": {"west": "path1" , "east":"path2", "south":"bridge"},
        },
        "main_menu": {
            "description": "Type in START to begin your adventure",
            "objects": {
            },
            "img_url": "static/images/main_menu.jpeg",
            "exits": {"north": "witch_house"},
        }
    },

}
