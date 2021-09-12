alienExperience = {
  "uuid": "F234C625-303F-4715-A594-7498ABAE18C3",
  "name": "Alien Experience",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631409365938,
  "passages": [
    {
      "name": "Bedroom - Awaken",
      "tags": "",
      "id": "1",
      "text": "You awake from a deep sleep aboard the commerical starship Nostromo.  Around you are your crewmates: Kane, Ash, Parker, Lambert, and Brett.  You are Ellen Ripley.  Checking the logs you notice cryosleep ended prematurely.\n\n[[DALLAS->Dallas]]\n[[DOORWAY->Science Hallway]]",
      "links": [
        {
          "linkText": "DALLAS",
          "passageName": "Dallas",
          "original": "[[DALLAS->Dallas]]"
        },
        {
          "linkText": "DOORWAY",
          "passageName": "Science Hallway",
          "original": "[[DOORWAY->Science Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "You awake from a deep sleep aboard the commerical starship Nostromo.  Around you are your crewmates: Kane, Ash, Parker, Lambert, and Brett.  You are Ellen Ripley.  Checking the logs you notice cryosleep ended prematurely."
    },
    {
      "name": "Dallas",
      "tags": "",
      "id": "2",
      "text": "Dallas is your Captain aboard the Nostromo.  He will know why the cryosleep awoke the crew.\n\n[[QUESTION->\"Why did Mother wake us, Dallas?\"]]\n[[LEAVE->Bedroom]]",
      "links": [
        {
          "linkText": "QUESTION",
          "passageName": "\"Why did Mother wake us, Dallas?\"",
          "original": "[[QUESTION->\"Why did Mother wake us, Dallas?\"]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "Bedroom",
          "original": "[[LEAVE->Bedroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "Dallas is your Captain aboard the Nostromo.  He will know why the cryosleep awoke the crew."
    },
    {
      "name": "Science Hallway",
      "tags": "",
      "id": "3",
      "text": "You enter the hallway connecting the dorm and lockerroom to the Science Lab and Lounge.\n\n[[LAB->Science Lab - Awaken]]\n[[LOUNGE->Lounge - Awaken]]",
      "links": [
        {
          "linkText": "LAB",
          "passageName": "Science Lab - Awaken",
          "original": "[[LAB->Science Lab - Awaken]]"
        },
        {
          "linkText": "LOUNGE",
          "passageName": "Lounge - Awaken",
          "original": "[[LOUNGE->Lounge - Awaken]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter the hallway connecting the dorm and lockerroom to the Science Lab and Lounge."
    },
    {
      "name": "\"Why did Mother wake us, Dallas?\"",
      "tags": "",
      "id": "4",
      "text": "Dallas trusts you as you are next in command.  He begins to tell you the message he received from Mother.  \n\n\"It seems as though our comms have intercepted a distress beacon.  Regulations say we must investigate.\" \n\nYou are annoyed.  Screw regulations, this was not apart of the mission.  Ash interrupts your thoughts saying how Mother's orders are not to be disobeyed.  The ship will land.\n\n[[LEAVE->Bedroom]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "Bedroom",
          "original": "[[LEAVE->Bedroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "Dallas trusts you as you are next in command.  He begins to tell you the message he received from Mother.  \n\n\"It seems as though our comms have intercepted a distress beacon.  Regulations say we must investigate.\" \n\nYou are annoyed.  Screw regulations, this was not apart of the mission.  Ash interrupts your thoughts saying how Mother's orders are not to be disobeyed.  The ship will land."
    },
    {
      "name": "Bedroom",
      "tags": "",
      "id": "5",
      "text": "The crew is still confused, nobody has addressed the issue with a real answer.\n\n[[DOORWAY->Science Hallway]]",
      "links": [
        {
          "linkText": "DOORWAY",
          "passageName": "Science Hallway",
          "original": "[[DOORWAY->Science Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "The crew is still confused, nobody has addressed the issue with a real answer."
    },
    {
      "name": "Science Lab - Awaken",
      "tags": "",
      "id": "6",
      "text": "Nothing is out of place.  Any equipment Ash was working on was put away before the crew entered cryosleep.\n\n[[BACK->Science Hallway]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway",
          "original": "[[BACK->Science Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "Nothing is out of place.  Any equipment Ash was working on was put away before the crew entered cryosleep."
    },
    {
      "name": "Lounge - Awaken",
      "tags": "",
      "id": "7",
      "text": "The lounge is as messy as you remember it.  Food  containers cover the table with magazines litering the furniture.  The only motion is the plastic bird decoration bobbing for water.  This room connects several other rooms, most of which are not accessible until the sleep cycle is manually ended by Dallas.\n\n[[BACK->Science Hallway]]\n[[FORWARD->Ship Control Center - Awaken]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway",
          "original": "[[BACK->Science Hallway]]"
        },
        {
          "linkText": "FORWARD",
          "passageName": "Ship Control Center - Awaken",
          "original": "[[FORWARD->Ship Control Center - Awaken]]"
        }
      ],
      "hooks": [],
      "cleanText": "The lounge is as messy as you remember it.  Food  containers cover the table with magazines litering the furniture.  The only motion is the plastic bird decoration bobbing for water.  This room connects several other rooms, most of which are not accessible until the sleep cycle is manually ended by Dallas."
    },
    {
      "name": "Ship Control Center - Awaken",
      "tags": "",
      "id": "8",
      "text": "From here the crew assesses their options.  Dallas, not wanting to disobey direct orders, decides it is best to entertain Mother's wishes.  The crew follows the procedures to land the ship.  The expeditionary crew members venture out to investigate the site and beacon.  They find a derelict ship, likely having been there for decades.  It is unknown what began the distress signal...\n\n[[CONTINUE->The Perfect Organism]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "The Perfect Organism",
          "original": "[[CONTINUE->The Perfect Organism]]"
        }
      ],
      "hooks": [],
      "cleanText": "From here the crew assesses their options.  Dallas, not wanting to disobey direct orders, decides it is best to entertain Mother's wishes.  The crew follows the procedures to land the ship.  The expeditionary crew members venture out to investigate the site and beacon.  They find a derelict ship, likely having been there for decades.  It is unknown what began the distress signal..."
    },
    {
      "name": "The Perfect Organism",
      "tags": "",
      "id": "9",
      "text": "Time has passed.  The expedition crew has returned, frantic.  A creature is attached to the helmet of Kane's suit.  Dallas and Lambert are holding him up while trying to convince you to let them.  Protocol says not to, as the whole ship would be at risk. Even though you were Commanding Officer in this situation - Dallas was on the expedition team, Ash disobeys orders and opens the doors.\n\nFor the sake of this experiment, time will lapse once more.  The creature attached to Kane's helmet must have laid an egg inside him as a small worm like monstrosity crawled its way out of his chest the next day.  Following this incident, the crew tried capturing the specimen to no avail.  Brett dies trying to find the crew's cat, Jones.  Dallas dies trying to kill the creature in the airducts with a flamethrower.  It is revealed Ash is a android, he is terminated after attacking you.\n\nIn a final attempt to kill this monster, you have instructed Lambert and Parker to try luring it towards the escape pod but they were not successful.  They were killed. It is left to you to now instead destroy the Nostromo and take the escape pod.  You will be starting on the control deck.  Start the self-destruct sequence by going down the ladder in the room out and to the right of the lounge.  The escape pod is to the left of the lounge with the dorm and science lab straight ahead.  \n\nGood luck!\n\n[[CONTINUE->Ship Control Center - The Escape]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Ship Control Center - The Escape",
          "original": "[[CONTINUE->Ship Control Center - The Escape]]"
        }
      ],
      "hooks": [],
      "cleanText": "Time has passed.  The expedition crew has returned, frantic.  A creature is attached to the helmet of Kane's suit.  Dallas and Lambert are holding him up while trying to convince you to let them.  Protocol says not to, as the whole ship would be at risk. Even though you were Commanding Officer in this situation - Dallas was on the expedition team, Ash disobeys orders and opens the doors.\n\nFor the sake of this experiment, time will lapse once more.  The creature attached to Kane's helmet must have laid an egg inside him as a small worm like monstrosity crawled its way out of his chest the next day.  Following this incident, the crew tried capturing the specimen to no avail.  Brett dies trying to find the crew's cat, Jones.  Dallas dies trying to kill the creature in the airducts with a flamethrower.  It is revealed Ash is a android, he is terminated after attacking you.\n\nIn a final attempt to kill this monster, you have instructed Lambert and Parker to try luring it towards the escape pod but they were not successful.  They were killed. It is left to you to now instead destroy the Nostromo and take the escape pod.  You will be starting on the control deck.  Start the self-destruct sequence by going down the ladder in the room out and to the right of the lounge.  The escape pod is to the left of the lounge with the dorm and science lab straight ahead.  \n\nGood luck!"
    },
    {
      "name": "Ship Control Center - The Escape",
      "tags": "",
      "id": "10",
      "text": "You look into the door to the terminal to talk to Mother and are angered by the very sight of it.  No one is left.  There is nothing in here to help you now.\n\n[[DOOR->Lounge - The Escape]]",
      "links": [
        {
          "linkText": "DOOR",
          "passageName": "Lounge - The Escape",
          "original": "[[DOOR->Lounge - The Escape]]"
        }
      ],
      "hooks": [],
      "cleanText": "You look into the door to the terminal to talk to Mother and are angered by the very sight of it.  No one is left.  There is nothing in here to help you now."
    },
    {
      "name": "Lounge - The Escape",
      "tags": "",
      "id": "11",
      "text": "The room is more of a mess than normal.  The table was cleared multiple times in the past 24 hours.  First for Kane.  Second when Ash attacked you.  Then again when planning the final mission.  Yet, things are still strewn about.  You think about your next move.\n\n[[FORWARD->Science Hallway - The Escape]]\n[[LEFT->Ladder Room]]\n[[RIGHT->Escape Pod Room]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Science Hallway - The Escape",
          "original": "[[FORWARD->Science Hallway - The Escape]]"
        },
        {
          "linkText": "LEFT",
          "passageName": "Ladder Room",
          "original": "[[LEFT->Ladder Room]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Escape Pod Room",
          "original": "[[RIGHT->Escape Pod Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The room is more of a mess than normal.  The table was cleared multiple times in the past 24 hours.  First for Kane.  Second when Ash attacked you.  Then again when planning the final mission.  Yet, things are still strewn about.  You think about your next move."
    },
    {
      "name": "Science Hallway - The Escape",
      "tags": "",
      "id": "12",
      "text": "You peer into the science lab, it is how you left it after Kane's death.  To your right is the bedroom, there is a hiss.\n\n[[RIGHT->Bedroom - The Escape]]\n[[DOOR->Science Lab - The Escape]]\n[[BACK->Lounge - The Escape]]",
      "links": [
        {
          "linkText": "RIGHT",
          "passageName": "Bedroom - The Escape",
          "original": "[[RIGHT->Bedroom - The Escape]]"
        },
        {
          "linkText": "DOOR",
          "passageName": "Science Lab - The Escape",
          "original": "[[DOOR->Science Lab - The Escape]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Lounge - The Escape",
          "original": "[[BACK->Lounge - The Escape]]"
        }
      ],
      "hooks": [],
      "cleanText": "You peer into the science lab, it is how you left it after Kane's death.  To your right is the bedroom, there is a hiss."
    },
    {
      "name": "Bedroom - The Escape",
      "tags": "",
      "id": "13",
      "text": "Despite being terrified, you manage to step towards the dorms.  Inside you find Jones, who hissed at you.  You pick him up and carry on.\n\n[[BACK->Science Hallway - The Escape (Jones Saved)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Jones Saved)",
          "original": "[[BACK->Science Hallway - The Escape (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "Despite being terrified, you manage to step towards the dorms.  Inside you find Jones, who hissed at you.  You pick him up and carry on.",
			"score":10
    },
    {
      "name": "Science Lab - The Escape",
      "tags": "",
      "id": "14",
      "text": "Stepping over the hole caused by the facehugger's acidic blood, you find Brett's tool he used as the ship's engineer.  Could be useful.\n\n[[BACK->Science Hallway - The Escape (Tool Acquired)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Tool Acquired)",
          "original": "[[BACK->Science Hallway - The Escape (Tool Acquired)]]"
        }
      ],
      "hooks": [],
      "cleanText": "Stepping over the hole caused by the facehugger's acidic blood, you find Brett's tool he used as the ship's engineer.  Could be useful.",
			"score": 10
    },
    {
      "name": "Science Hallway - The Escape (Tool Acquired)",
      "tags": "",
      "id": "15",
      "text": "You hear a hiss to your left coming from the bedroom again.  Time is running out.\n\n[[LEFT->Bedroom - The Escape (Tool Acquired)]]\n[[DOOR->Science Lab - The Escape (Tool Acquired)]]\n[[RIGHT->Lounge - The Escape (Tool Acquired)]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Bedroom - The Escape (Tool Acquired)",
          "original": "[[LEFT->Bedroom - The Escape (Tool Acquired)]]"
        },
        {
          "linkText": "DOOR",
          "passageName": "Science Lab - The Escape (Tool Acquired)",
          "original": "[[DOOR->Science Lab - The Escape (Tool Acquired)]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Lounge - The Escape (Tool Acquired)",
          "original": "[[RIGHT->Lounge - The Escape (Tool Acquired)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You hear a hiss to your left coming from the bedroom again.  Time is running out."
    },
    {
      "name": "Science Hallway - The Escape (Jones Saved)",
      "tags": "",
      "id": "16",
      "text": "The Lab is on your right.  Ahead is the lounge.\n\n[[BACK->Bedroom - The Escape (Jones Saved)]]\n[[RIGHT->Science Lab - The Escape (Jones Saved)]]\n[[FORWARD->Lounge - The Escape (Jones Saved)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Bedroom - The Escape (Jones Saved)",
          "original": "[[BACK->Bedroom - The Escape (Jones Saved)]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Science Lab - The Escape (Jones Saved)",
          "original": "[[RIGHT->Science Lab - The Escape (Jones Saved)]]"
        },
        {
          "linkText": "FORWARD",
          "passageName": "Lounge - The Escape (Jones Saved)",
          "original": "[[FORWARD->Lounge - The Escape (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Lab is on your right.  Ahead is the lounge."
    },
    {
      "name": "Science Lab - The Escape (Tool Acquired)",
      "tags": "",
      "id": "17",
      "text": "You are wasting time.  Leave while you still can!\n\n[[BACK->Science Hallway - The Escape (Tool Acquired)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Tool Acquired)",
          "original": "[[BACK->Science Hallway - The Escape (Tool Acquired)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are wasting time.  Leave while you still can!"
    },
    {
      "name": "Science Lab - The Escape (Jones Saved)",
      "tags": "",
      "id": "18",
      "text": "Stepping over the hole caused by the facehugger's acidic blood, you find Brett's tool he used as the ship's engineer.  Could be useful.\n\n[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "Stepping over the hole caused by the facehugger's acidic blood, you find Brett's tool he used as the ship's engineer.  Could be useful.",
			"score":10
    },
    {
      "name": "Science Hallway - The Escape (Tool Acquired, Jones Saved)",
      "tags": "",
      "id": "19",
      "text": "[[DOOR->Science Lab - The Escape (Tool Acquired, Jones Saved)]]\n[[DORM->Bedroom - The Escape (Tool Acquired, Jones Saved)]]\n[[LOUNGE->Lounge - The Escape (Tool Acquired, Jones Saved)]]",
      "links": [
        {
          "linkText": "DOOR",
          "passageName": "Science Lab - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[DOOR->Science Lab - The Escape (Tool Acquired, Jones Saved)]]"
        },
        {
          "linkText": "DORM",
          "passageName": "Bedroom - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[DORM->Bedroom - The Escape (Tool Acquired, Jones Saved)]]"
        },
        {
          "linkText": "LOUNGE",
          "passageName": "Lounge - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[LOUNGE->Lounge - The Escape (Tool Acquired, Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": ""
    },
    {
      "name": "Bedroom - The Escape (Tool Acquired)",
      "tags": "",
      "id": "20",
      "text": "Despite being terrified, you manage to step towards the dorms.  Inside you find Jones, who hissed at you.  You pick him up and carry on.\n\n[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "Despite being terrified, you manage to step towards the dorms.  Inside you find Jones, who hissed at you.  You pick him up and carry on.",
			"score":10
    },
    {
      "name": "Lounge - The Escape (Tool Acquired)",
      "tags": "",
      "id": "21",
      "text": "The room is still a mess.  The control deck is ahead of you, but you locked the door on your way out.  There are hallways to the left and right.\n[[LEFT->Ladder Room (Tool Acquired)]]\n[[BACK->Science Hallway - The Escape (Tool Acquired)]]\n[[RIGHT->Escape Pod Room (Tool Acquired)]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Ladder Room (Tool Acquired)",
          "original": "[[LEFT->Ladder Room (Tool Acquired)]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Tool Acquired)",
          "original": "[[BACK->Science Hallway - The Escape (Tool Acquired)]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Escape Pod Room (Tool Acquired)",
          "original": "[[RIGHT->Escape Pod Room (Tool Acquired)]]"
        }
      ],
      "hooks": [],
      "cleanText": "The room is still a mess.  The control deck is ahead of you, but you locked the door on your way out.  There are hallways to the left and right."
    },
    {
      "name": "Bedroom - The Escape (Jones Saved)",
      "tags": "",
      "id": "22",
      "text": "You are wasting time.  Leave while you still can!\n\n[[BACK->Science Hallway - The Escape (Jones Saved)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Jones Saved)",
          "original": "[[BACK->Science Hallway - The Escape (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are wasting time.  Leave while you still can!"
    },
    {
      "name": "Lounge - The Escape (Jones Saved)",
      "tags": "",
      "id": "23",
      "text": "The room is still a mess.  The control deck is ahead of you, but you locked the door on your way out.  There are hallways to the left and right.\n[[LEFT->Ladder Room (Jones Saved)]]\n[[BACK->Science Hallway - The Escape (Jones Saved)]]\n[[RIGHT->Escape Pod Room (Jones Saved)]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Ladder Room (Jones Saved)",
          "original": "[[LEFT->Ladder Room (Jones Saved)]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Jones Saved)",
          "original": "[[BACK->Science Hallway - The Escape (Jones Saved)]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Escape Pod Room (Jones Saved)",
          "original": "[[RIGHT->Escape Pod Room (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "The room is still a mess.  The control deck is ahead of you, but you locked the door on your way out.  There are hallways to the left and right."
    },
    {
      "name": "Science Lab - The Escape (Tool Acquired, Jones Saved)",
      "tags": "",
      "id": "24",
      "text": "You are wasting time.  Leave while you still can!\n\n[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are wasting time.  Leave while you still can!"
    },
    {
      "name": "Bedroom - The Escape (Tool Acquired, Jones Saved)",
      "tags": "",
      "id": "25",
      "text": "You are wasting time.  Leave while you still can!\n\n[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are wasting time.  Leave while you still can!"
    },
    {
      "name": "Lounge - The Escape (Tool Acquired, Jones Saved)",
      "tags": "",
      "id": "26",
      "text": "The room is still a mess.  The control deck is ahead of you, but you locked the door on your way out.  There are hallways to the left and right.\n[[LEFT->Ladder Room (Tool Acquired, Jones Saved)]]\n[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]\n[[RIGHT->Escape Pod Room (Tool Acquired, Jones Saved)]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Ladder Room (Tool Acquired, Jones Saved)",
          "original": "[[LEFT->Ladder Room (Tool Acquired, Jones Saved)]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Science Hallway - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[BACK->Science Hallway - The Escape (Tool Acquired, Jones Saved)]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Escape Pod Room (Tool Acquired, Jones Saved)",
          "original": "[[RIGHT->Escape Pod Room (Tool Acquired, Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "The room is still a mess.  The control deck is ahead of you, but you locked the door on your way out.  There are hallways to the left and right."
    },
    {
      "name": "Ladder Room (Tool Acquired)",
      "tags": "",
      "id": "27",
      "text": "This room has a ladder leading to the engine room that houses the self destruct mechanism.\n\n[[BACK->Lounge - The Escape (Tool Acquired)]] \n[[DOWN->Engine Room (Tool Acquired)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Lounge - The Escape (Tool Acquired)",
          "original": "[[BACK->Lounge - The Escape (Tool Acquired)]]"
        },
        {
          "linkText": "DOWN",
          "passageName": "Engine Room (Tool Acquired)",
          "original": "[[DOWN->Engine Room (Tool Acquired)]]"
        }
      ],
      "hooks": [],
      "cleanText": "This room has a ladder leading to the engine room that houses the self destruct mechanism."
    },
    {
      "name": "Engine Room (Tool Acquired)",
      "tags": "",
      "id": "28",
      "text": "You find the mechanism, but you hear a hissing off to your left.  Do you check out the noise or continue on the mission?\n\n[[INVESTIGATE->The Escape Death]]\n[[CONTINUE->Self Destruct Start (Tool Acquired)]]",
      "links": [
        {
          "linkText": "INVESTIGATE",
          "passageName": "The Escape Death",
          "original": "[[INVESTIGATE->The Escape Death]]"
        },
        {
          "linkText": "CONTINUE",
          "passageName": "Self Destruct Start (Tool Acquired)",
          "original": "[[CONTINUE->Self Destruct Start (Tool Acquired)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You find the mechanism, but you hear a hissing off to your left.  Do you check out the noise or continue on the mission?"
    },
    {
      "name": "The Escape Death",
      "tags": "",
      "id": "29",
      "text": "You have encountered the Xenomorph with nothing to fight him off.  He towers over you with massive claws, his tail wraps around your leg and in the blink of an eye, he attacks.  In space, no one can hear you scream...",
      "links": [],
      "hooks": [],
      "cleanText": "You have encountered the Xenomorph with nothing to fight him off.  He towers over you with massive claws, his tail wraps around your leg and in the blink of an eye, he attacks.  In space, no one can hear you scream..."
    },
    {
      "name": "Self Destruct Start (Tool Acquired)",
      "tags": "",
      "id": "30",
      "text": "You have begun the process.  Because you found Brett's tool, there were no snags along the way.  Proceed to the escape pod.\n\n[[PROCEED->Ladder Room - Self Destruct Commenced]]",
      "links": [
        {
          "linkText": "PROCEED",
          "passageName": "Ladder Room - Self Destruct Commenced",
          "original": "[[PROCEED->Ladder Room - Self Destruct Commenced]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have begun the process.  Because you found Brett's tool, there were no snags along the way.  Proceed to the escape pod."
    },
    {
      "name": "Ladder Room - Self Destruct Commenced",
      "tags": "",
      "id": "31",
      "text": "Lights are flashing everywhere.  A siren plays a loud, slow tone.\n\n[[FORWARD->Lounge - Self Destruct Commenced]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Lounge - Self Destruct Commenced",
          "original": "[[FORWARD->Lounge - Self Destruct Commenced]]"
        }
      ],
      "hooks": [],
      "cleanText": "Lights are flashing everywhere.  A siren plays a loud, slow tone."
    },
    {
      "name": "Lounge - Self Destruct Commenced",
      "tags": "",
      "id": "32",
      "text": "During the self destruct sequence only the door to the escape pods remain open.  This is the door ahead of you.\n\n[[FORWARD->Escape Pod Room - Self Destruct Commenced]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Escape Pod Room - Self Destruct Commenced",
          "original": "[[FORWARD->Escape Pod Room - Self Destruct Commenced]]"
        }
      ],
      "hooks": [],
      "cleanText": "During the self destruct sequence only the door to the escape pods remain open.  This is the door ahead of you."
    },
    {
      "name": "Escape Pod Room - Self Destruct Commenced",
      "tags": "",
      "id": "33",
      "text": "The Escape Pod is ahead of you,  now is your chance!\n\n[[ENTER->Escape Pod]]",
      "links": [
        {
          "linkText": "ENTER",
          "passageName": "Escape Pod",
          "original": "[[ENTER->Escape Pod]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Escape Pod is ahead of you,  now is your chance!"
    },
    {
      "name": "Escape Pod",
      "tags": "",
      "id": "34",
      "text": "You blast away from the ship.  As you enter your cryofreeze bed, you remember Jones.  He was a good cat.  Shame you could not save him.  You close the door to the bed when you see something move on the wall.  The Xenomorph!  You can either stay in the pod and hide or take a chance and fight.\n\n[[HIDE->The Bad Ending]]\n[[FIGHT->The Escape Death]]",
      "links": [
        {
          "linkText": "HIDE",
          "passageName": "The Bad Ending",
          "original": "[[HIDE->The Bad Ending]]"
        },
        {
          "linkText": "FIGHT",
          "passageName": "The Escape Death",
          "original": "[[FIGHT->The Escape Death]]"
        }
      ],
      "hooks": [],
      "cleanText": "You blast away from the ship.  As you enter your cryofreeze bed, you remember Jones.  He was a good cat.  Shame you could not save him.  You close the door to the bed when you see something move on the wall.  The Xenomorph!  You can either stay in the pod and hide or take a chance and fight."
    },
    {
      "name": "The Bad Ending",
      "tags": "",
      "id": "35",
      "text": "The good news: You survived.\n\nThe bad news: A ship found your pod several years after the events of the game and the Xenomorph with it.  The Xenomorph took over the station which is heading back to Earth.",
      "links": [],
      "hooks": [],
      "cleanText": "The good news: You survived.\n\nThe bad news: A ship found your pod several years after the events of the game and the Xenomorph with it.  The Xenomorph took over the station which is heading back to Earth."
    },
    {
      "name": "Ladder Room (Tool Acquired, Jones Saved)",
      "tags": "",
      "id": "36",
      "text": "This room has a ladder leading to the engine room that houses the self destruct mechanism.\n\n[[BACK->Lounge - The Escape (Tool Acquired, Jones Saved)]] \n[[DOWN->Engine Room (Tool Acquired, Jones Saved)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Lounge - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[BACK->Lounge - The Escape (Tool Acquired, Jones Saved)]]"
        },
        {
          "linkText": "DOWN",
          "passageName": "Engine Room (Tool Acquired, Jones Saved)",
          "original": "[[DOWN->Engine Room (Tool Acquired, Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "This room has a ladder leading to the engine room that houses the self destruct mechanism."
    },
    {
      "name": "Engine Room (Tool Acquired, Jones Saved)",
      "tags": "",
      "id": "37",
      "text": "You find the mechanism, but you hear a hissing off to your left.  Do you check out the noise or continue on the mission?\n\n[[INVESTIGATE->Investigate Safe]]\n[[CONTINUE->Self Destruct Start (Tool Acquired, Jones Saved)]]",
      "links": [
        {
          "linkText": "INVESTIGATE",
          "passageName": "Investigate Safe",
          "original": "[[INVESTIGATE->Investigate Safe]]"
        },
        {
          "linkText": "CONTINUE",
          "passageName": "Self Destruct Start (Tool Acquired, Jones Saved)",
          "original": "[[CONTINUE->Self Destruct Start (Tool Acquired, Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You find the mechanism, but you hear a hissing off to your left.  Do you check out the noise or continue on the mission?"
    },
    {
      "name": "Self Destruct Start (Tool Acquired, Jones Saved)",
      "tags": "",
      "id": "38",
      "text": "You have begun the process.  Because you found Brett's tool, there were no snags along the way.  Proceed to the escape pod.\n\n[[PROCEED->Ladder Room - Self Destruct Commenced (Jones Saved)]]",
      "links": [
        {
          "linkText": "PROCEED",
          "passageName": "Ladder Room - Self Destruct Commenced (Jones Saved)",
          "original": "[[PROCEED->Ladder Room - Self Destruct Commenced (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have begun the process.  Because you found Brett's tool, there were no snags along the way.  Proceed to the escape pod."
    },
    {
      "name": "Ladder Room - Self Destruct Commenced (Jones Saved)",
      "tags": "",
      "id": "39",
      "text": "Lights are flashing everywhere.  A siren plays a loud, slow tone.\n\n[[FORWARD->Lounge - Self Destruct Commenced (Jones Saved)]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Lounge - Self Destruct Commenced (Jones Saved)",
          "original": "[[FORWARD->Lounge - Self Destruct Commenced (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "Lights are flashing everywhere.  A siren plays a loud, slow tone."
    },
    {
      "name": "Lounge - Self Destruct Commenced (Jones Saved)",
      "tags": "",
      "id": "40",
      "text": "During the self destruct sequence only the door to the escape pods remain open.  This is the door ahead of you.\n\n[[FORWARD->Escape Pod Room - Self Destruct Commenced (Jones Saved)]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Escape Pod Room - Self Destruct Commenced (Jones Saved)",
          "original": "[[FORWARD->Escape Pod Room - Self Destruct Commenced (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "During the self destruct sequence only the door to the escape pods remain open.  This is the door ahead of you."
    },
    {
      "name": "Escape Pod Room - Self Destruct Commenced (Jones Saved)",
      "tags": "",
      "id": "41",
      "text": "The Escape Pod is ahead of you,  now is your chance!\n\n[[CONTINUE-> Escape Pod (Jones Saved)]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Escape Pod (Jones Saved)",
          "original": "[[CONTINUE-> Escape Pod (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Escape Pod is ahead of you,  now is your chance!"
    },
    {
      "name": "Escape Pod (Jones Saved)",
      "tags": "",
      "id": "42",
      "text": "You blast away from the ship.  As you enter your cryofreeze bed, you remember Jones.  He was a good cat.  Shame you could not find him.  You close the door to the bed when you see something move on the wall.  The Xenomorph!  You can either stay in the pod and hide or take a chance and fight.\n\n[[HIDE->The Bad Ending]]\n[[FIGHT->The Fight]]",
      "links": [
        {
          "linkText": "HIDE",
          "passageName": "The Bad Ending",
          "original": "[[HIDE->The Bad Ending]]"
        },
        {
          "linkText": "FIGHT",
          "passageName": "The Fight",
          "original": "[[FIGHT->The Fight]]"
        }
      ],
      "hooks": [],
      "cleanText": "You blast away from the ship.  As you enter your cryofreeze bed, you remember Jones.  He was a good cat.  Shame you could not find him.  You close the door to the bed when you see something move on the wall.  The Xenomorph!  You can either stay in the pod and hide or take a chance and fight."
    },
    {
      "name": "The Fight",
      "tags": "",
      "id": "43",
      "text": "You grab a metal crowbar that was next to the bed.  As you approach the monster, Jones attacks its leg, distracting it.  You hit it over the head and lunge for the airlock.  You manage to pull the lever.\n\n[[CONTINUE->Good Ending]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Good Ending",
          "original": "[[CONTINUE->Good Ending]]"
        }
      ],
      "hooks": [],
      "cleanText": "You grab a metal crowbar that was next to the bed.  As you approach the monster, Jones attacks its leg, distracting it.  You hit it over the head and lunge for the airlock.  You manage to pull the lever."
    },
    {
      "name": "Good Ending",
      "tags": "",
      "id": "44",
      "text": "The Alien gets sucked out the airlock as you grab Jones and close the door.  You record your final log: \"Final report, the commercial star-ship Nostromo. Third officer reporting. The other members of the crew—Kane, Lambert, Parker, Brett, Ash, and Captain Dallas—are dead. Cargo and ship destroyed. I should reach the frontier within six weeks. With a little luck the network will pick me up. This is Ripley, last survivor of the Nostromo, signing off.\"",
      "links": [],
      "hooks": [],
      "cleanText": "The Alien gets sucked out the airlock as you grab Jones and close the door.  You record your final log: \"Final report, the commercial star-ship Nostromo. Third officer reporting. The other members of the crew—Kane, Lambert, Parker, Brett, Ash, and Captain Dallas—are dead. Cargo and ship destroyed. I should reach the frontier within six weeks. With a little luck the network will pick me up. This is Ripley, last survivor of the Nostromo, signing off.\"",
			"score":100
    },
    {
      "name": "Escape Pod Room (Tool Acquired)",
      "tags": "",
      "id": "45",
      "text": "The escape pod is in front of you.  Do you want to leave without destroying the Alien and the ship?\n\n[[ENTER ->Escape Pod - No Self Destruct]]\n[[BACK->Lounge - The Escape (Tool Acquired)]]",
      "links": [
        {
          "linkText": "ENTER",
          "passageName": "Escape Pod - No Self Destruct",
          "original": "[[ENTER ->Escape Pod - No Self Destruct]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Lounge - The Escape (Tool Acquired)",
          "original": "[[BACK->Lounge - The Escape (Tool Acquired)]]"
        }
      ],
      "hooks": [],
      "cleanText": "The escape pod is in front of you.  Do you want to leave without destroying the Alien and the ship?"
    },
    {
      "name": "Escape Pod - No Self Destruct",
      "tags": "",
      "id": "46",
      "text": "You open the door to immediately get it with a blast of air.  You hear a hiss and wait for the fog to clear.\n\n[[CONTINUE->The Escape Death]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "The Escape Death",
          "original": "[[CONTINUE->The Escape Death]]"
        }
      ],
      "hooks": [],
      "cleanText": "You open the door to immediately get it with a blast of air.  You hear a hiss and wait for the fog to clear."
    },
    {
      "name": "Escape Pod Room (Tool Acquired, Jones Saved)",
      "tags": "",
      "id": "47",
      "text": "The escape pod is in front of you.  Do you want to leave without destroying the Alien and the ship?\n\n[[ENTER ->Escape Pod - No Self Destruct]]\n[[BACK->Lounge - The Escape (Tool Acquired, Jones Saved)]]",
      "links": [
        {
          "linkText": "ENTER",
          "passageName": "Escape Pod - No Self Destruct",
          "original": "[[ENTER ->Escape Pod - No Self Destruct]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Lounge - The Escape (Tool Acquired, Jones Saved)",
          "original": "[[BACK->Lounge - The Escape (Tool Acquired, Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "The escape pod is in front of you.  Do you want to leave without destroying the Alien and the ship?"
    },
    {
      "name": "Ladder Room (Jones Saved)",
      "tags": "",
      "id": "48",
      "text": "This room has a ladder leading to the engine room that houses the self destruct mechanism.\n\n[[BACK->Lounge - The Escape (Jones Saved)]] \n[[DOWN->Engine Room (Jones Saved)]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Lounge - The Escape (Jones Saved)",
          "original": "[[BACK->Lounge - The Escape (Jones Saved)]]"
        },
        {
          "linkText": "DOWN",
          "passageName": "Engine Room (Jones Saved)",
          "original": "[[DOWN->Engine Room (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "This room has a ladder leading to the engine room that houses the self destruct mechanism."
    },
    {
      "name": "Escape Pod Room (Jones Saved)",
      "tags": "",
      "id": "49",
      "text": "The escape pod is in front of you.  Do you want to leave without destroying the Alien and the ship?\n\n[[ENTER ->Escape Pod - No Self Destruct]]\n[[BACK->Lounge - The Escape (Jones Saved)]]",
      "links": [
        {
          "linkText": "ENTER",
          "passageName": "Escape Pod - No Self Destruct",
          "original": "[[ENTER ->Escape Pod - No Self Destruct]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Lounge - The Escape (Jones Saved)",
          "original": "[[BACK->Lounge - The Escape (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "The escape pod is in front of you.  Do you want to leave without destroying the Alien and the ship?"
    },
    {
      "name": "Engine Room (Jones Saved)",
      "tags": "",
      "id": "50",
      "text": "You find the mechanism, but you hear a hissing off to your left.  Do you check out the noise or continue on the mission?\n\n[[INVESTIGATE->Investigate Safe]]\n[[CONTINUE->Self Destruct Start (Jones Saved)]]",
      "links": [
        {
          "linkText": "INVESTIGATE",
          "passageName": "Investigate Safe",
          "original": "[[INVESTIGATE->Investigate Safe]]"
        },
        {
          "linkText": "CONTINUE",
          "passageName": "Self Destruct Start (Jones Saved)",
          "original": "[[CONTINUE->Self Destruct Start (Jones Saved)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You find the mechanism, but you hear a hissing off to your left.  Do you check out the noise or continue on the mission?"
    },
    {
      "name": "Self Destruct Start (Jones Saved)",
      "tags": "",
      "id": "51",
      "text": "The instructions require a tool to commence them.  While scrambling to find one you hear a noise behind you.  The Xenomorph is approaching, but Jones leaps to attack him.  You are able to find a blow torch to scare it away for now but Jones has died.  You pick up the tool you were looking for and continue.\n\n[[CONTINUE->Ladder Room - Self Destruct Commenced]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Ladder Room - Self Destruct Commenced",
          "original": "[[CONTINUE->Ladder Room - Self Destruct Commenced]]"
        }
      ],
      "hooks": [],
      "cleanText": "The instructions require a tool to commence them.  While scrambling to find one you hear a noise behind you.  The Xenomorph is approaching, but Jones leaps to attack him.  You are able to find a blow torch to scare it away for now but Jones has died.  You pick up the tool you were looking for and continue."
    },
    {
      "name": "Ladder Room",
      "tags": "",
      "id": "52",
      "text": "This room has a ladder leading to the engine room that houses the self destruct mechanism.\n\n[[BACK->Lounge - The Escape]] \n[[DOWN->Engine Room]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Lounge - The Escape",
          "original": "[[BACK->Lounge - The Escape]]"
        },
        {
          "linkText": "DOWN",
          "passageName": "Engine Room",
          "original": "[[DOWN->Engine Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "This room has a ladder leading to the engine room that houses the self destruct mechanism."
    },
    {
      "name": "Escape Pod Room",
      "tags": "",
      "id": "53",
      "text": "The escape pod is in front of you.  Do you want to leave without destroying the Alien and the ship?\n\n[[ENTER ->Escape Pod - No Self Destruct]]\n[[BACK->Lounge - The Escape]]",
      "links": [
        {
          "linkText": "ENTER",
          "passageName": "Escape Pod - No Self Destruct",
          "original": "[[ENTER ->Escape Pod - No Self Destruct]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Lounge - The Escape",
          "original": "[[BACK->Lounge - The Escape]]"
        }
      ],
      "hooks": [],
      "cleanText": "The escape pod is in front of you.  Do you want to leave without destroying the Alien and the ship?"
    },
    {
      "name": "Engine Room",
      "tags": "",
      "id": "54",
      "text": "You find the mechanism, but you hear a hissing off to your left.  Do you check out the noise or continue on the mission?\n\n[[INVESTIGATE->The Escape Death]]\n[[CONTINUE->Self Destruct Start]]",
      "links": [
        {
          "linkText": "INVESTIGATE",
          "passageName": "The Escape Death",
          "original": "[[INVESTIGATE->The Escape Death]]"
        },
        {
          "linkText": "CONTINUE",
          "passageName": "Self Destruct Start",
          "original": "[[CONTINUE->Self Destruct Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You find the mechanism, but you hear a hissing off to your left.  Do you check out the noise or continue on the mission?"
    },
    {
      "name": "Self Destruct Start",
      "tags": "",
      "id": "55",
      "text": "The instructions require a tool to commence them.  While scrambling to find one you hear a noise behind you.\n\n[[CONTINUE->The Escape Death]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "The Escape Death",
          "original": "[[CONTINUE->The Escape Death]]"
        }
      ],
      "hooks": [],
      "cleanText": "The instructions require a tool to commence them.  While scrambling to find one you hear a noise behind you."
    },
    {
      "name": "Investigate Safe",
      "tags": "",
      "id": "56",
      "text": "You find the Xenomorph!  He begins to approach, but Jones leaps to attack him.  You are able to bust a pipe with a screwdrive you found to scare it away for now but Jones has died.  You pick up the tool you were looking for and continue with the self destruct sequence.\n\n[[CONTINUE->Ladder Room - Self Destruct Commenced",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Ladder Room - Self Destruct Commenced",
          "original": "[[CONTINUE->Ladder Room - Self Destruct Commenced"
        }
      ],
      "hooks": [],
      "cleanText": "You find the Xenomorph!  He begins to approach, but Jones leaps to attack him.  You are able to bust a pipe with a screwdrive you found to scare it away for now but Jones has died.  You pick up the tool you were looking for and continue with the self destruct sequence."
    }
  ]
}

# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in alienExperience:
		for passage in alienExperience["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: {}, Score: {}".format(moves, score))
		print("You are at " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")
		for link in current_location["links"]:
			print(link["linkText"] + "\n")
def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Bedroom - Awaken"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves += 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score += current_location["score"]
	render(current_location, score, moves)
	response = get_input()