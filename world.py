import copy

data = {
    # update this state as the game progresses
    "current_state": {"room": "main_menu",
                      "inventory": { "coins":True,"knife":True,"chains":True,"ring":True},  # the things they carried
                      "playing": False  # flag: True until the player quits
                      },

    "output":"Type in START to begin your adventure",

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
        "slime": {"description" : "<<I'm hidden within a place of worship so grand, With jewels and gems, I'm carefully planned. Adorning the neck, in a sacred embrace, Where am I found, in this hallowed place?>> Drop this object at my feet and I shall help you."},
        "axe": {"description": "ÐU NE WILLCUMEN GEONDGAN."},
        "note": {"description": "You may cross only once the sigil is bound to you."},
        "ghost": {"description": "BOOOOO, Trick or Treat dear traveller! Bring me the candy if you want to know how to slay the evil witch!"},
        "bow": {"description": "A magical bow, adorned with ethereal glow, rests solemnly atop a hallowed grave. Its presence pays tribute to a departed soul, a poignant reminder of the enchanted legacy left behind, even in the realm beyond."},
        "arrow": {"description": "A silver arrow, gleaming with a pristine, moonlit sheen, embodies precision and power. Crafted for the purpose of vanquishing monsters, it promises a swift and decisive end to even the most formidable of foes."},
        "candy": {"description": "Just a bag of candy..."},
        "pumpkin": {"description": "A jack-o'-lantern, carved with a sinister grin, harbors a spectral secret within. Its flickering candlelight dances with the restless soul trapped within, casting an eerie glow that speaks of unending Halloween nights."},
        "candle": {"description": "A magical candle, shimmering softly, radiates an aura of enchantment. Its wax, infused with mystic energies, dances with ethereal light, promising to ignite the secrets of the arcane with each flickering flame."},
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
            "img_url":"static/images/witchy_room.jpeg",
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
            "img_url": "static/images/celler.jpeg",
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
            "exits": {"north" : "after_bridge", "south":"swamp_main"},
        },
        "after_bridge": {
            "description": "<<Salutations, wanderer!>> proclaims the Mystical Cockroach Man with a timeless wisdom. <<Now that you have traversed this realm, you stand at the crossroads of salvation. You may embark upon the short yet perilous western path, or you may opt for the elongated but tranquil eastern journey. The decision, traveler, rests with you, guided by the eternal flow of time.>>",
            "objects": {
                        },
            "img_url": "static/images/cockroach_man.jpeg",
            "exits": {"west": "statue" , "east":"treehouse", "south":"bridge"},
        },
        "cemetery": {
            "description": "In the heart of the enchanted forest, a mighty, ethereal cemetery stands as a testament to bygone wizards and mystical beings. Ancient tombstones, adorned with symbols of power, stretch into the misty horizon. A benevolent ghost, wreathed in soft, haunting light, drifts gracefully among the hallowed grounds, guarding the secrets of those who rest in eternal slumber.",
            "objects": { "ghost":True , "pumpkin":True , "candle":True , "bow":True
            },
            "img_url": "static/images/cemetery.jpeg",
            "exits": {"west": "forest"},
        },
        "forest": {
            "description": "Within the heart of the mystical forest, a single towering tree stands, its gnarled roots delving deep into enchanted soil. The malevolent witch, her dark essence forever bound, is imprisoned within its ancient, twisted trunk. The tree exudes an eerie aura, guarding the wicked secrets of her entrapment for all eternity.",
            "objects": {
            },
            "img_url": "static/images/final_forest.jpeg",
            "exits": {"east": "cemetery"},
        },
        "statue": {
            "description": "Beneath the luminous embrace of the shining moon, a mystical statue stands, bathed in celestial light. Its form is an exquisite fusion of ethereal grace and otherworldly beauty, an enigmatic sentinel that seems to hold the secrets of the night within its stone heart.",
            "objects": { "candy":True, "arrow" : True
            },
            "img_url": "static/images/statue.jpeg",
            "exits": {"north": "cemetery"},
        },
        "hell": {
            "description": "YOU FOOL! YOU HAVE PICKED THE SHORT PATH...YOUR FATE IS ETERNAL DAMNATION!!In the shivering silence, I felt a searing surge within, my essence twisting into something monstrous. Crimson tendrils snaked across my skin, horns sprouted from my temples, and eyes glowed with infernal fervor. Terror gripped my heart as I began a slow descent into the very earth, my existence melding with the shadows below. In that terrifying moment, I realized I had become a demon, forever bound to the depths, my humanity fading like a distant, vanishing whisper. In the realm of eternal torment, Hell's relentless embrace gradually consumes a writhing demon. The abyssal maw, a seething void of suffering, hungrily devours the creature's malevolent essence, leaving naught but a fading echo of its wickedness in its relentless descent into oblivion.",
            "objects": {
            },
            "img_url": "static/images/hell.jpeg",
            "exits": {},
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

data_copy = copy.deepcopy(data)