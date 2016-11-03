# EVA

label to_eva:
  stop music
  scene bg eva-empty-space
  
  h "I move out of the airlock; a bit too fast. Maybe I shouldn’t have jumped."
  
  h "I’ve never been in free space before."
  
  # [ Sound effect - The sound of the tether snapping taught. ]
  # [ Sound effect - A pained grunt as Holloway suddenly stops. ]
  
  queue sound [ tether_snap_sound, pained_grunt_sound ]
  
  $ renpy.pause(2.0)
  
  h "At least I’ve stopped."

# 2.0.0. OUTSIDE ##############################################################
label outside:
   
# 2.0.1. THE SHIP #############################################################
label the_ship:

  # [ Background image - An old ship with a beaten up hull, from about 50 meters out. ]
  
  h "This ship is really beaten up."
  
  h "There’s scaffolding on the hull and an “A” frame with a large metal plate attached. So that must be where the damage is."
  
  h "The airlock is still open. I should just go back in and wait for help."
  
  h "But if I make it to the scaffolding, I might be able to repair the hull."
  
  "Holloway slowly pulls on the tether and moves towards the airlock."
  
  h "Look, there are some climbing grabs on the hull above the airlock hatch."
  
  h "I can use the grabs to pull myself up the side and over the top of the hull to get to the scaffolding."
  
  "Holloway clicks on the radio button."
  
  h "HANC. What do I do now?"
  
  H "What can you see? Describe it."
  
  h "Surely this suit has a camera. Can’t I just send images via the radio system to you?"

# 2.0.2. TWO TETHERS ##########################################################
label two_tethers:

  # [ Background image - Close in graphic of working area. ]
  
  h "There’s another tether."
  
  menu:
    "Hook this tether to your suit and release the other tether.":
      
      $ has_two_tethers = False
      
      "That was the tether back to the airlock."
      
      h "I see the tether peacefully float away. I have an uneasy feeling."
      
    "Hook this tether to your suit and keep the other tether attached.":
      
      $ has_two_tethers = True
      
      "Holloway hooks the second tether onto his suit."
      
      h "Feeling safer already."
  
  h "I make my way up to the repair rig."

# 2.0.3. THE REPAIR ###########################################################
label the_repair:

  # [ Background image - Close up image of repair rig. ]
  
  "The radio splutters back into action."
  
  h "HANC. I’m at the repair site. What do I do with this oversized manhole cover?"
  
  H "Maneuver the plate over the breach using the controls on the rig. Once you've got it there you have to fire the six explosive bolts fixed around the perimeter of the plate to lock it to the hull."
  
  # [ Sound music - Ominous music while the plate fits it into place. ]
  
  h "Okay HANC. It’s in position. How do I work these bolts."
  
  H "Just press on the firing pins."
  
  "Holloway makes his way around the plate, pressing the firing pins, one at a time."
  
  "The hull vibrates violently underfoot with each bolt smashing into the hull."
  
  # [ Sound effect - Three explosions. ]

# 2.1.0. A SIGN OF LIFE #######################################################
label a_sign_of_life:

  # [ Background image - Inside the shuttle. ]
  # [ Character image - Jinx sitting - straining to hear. ]
  # [ Sound effect - Two muffled explosions followed by a rattle. ]
  
  j "Someone is alive and outside but I have no space suit. I need whoever it is to pressurise the hull, and soon."

# 2.2.0. THE SHIP IS SEALED ###################################################
label the_ship_is_sealed:

  # [ Background image - Close up image of repair rig. ]
  
  h "HANC, the last bolt failed."
  
  H "The seal is tight. I am going to begin pressurising the ship."
  
  "HANC begins the checklist to return atmosphere to the ship."

# 2.2.1. BACK TO THE SHIP #####################################################
label back_to_the_ship:

  # [ Background image - Close in graphic of repair rig. ]
  
  h "25 minutes oxygen. Good."
  
  "Holloway makes his way back to the airlock using the grab points."
  
  "Three meters from the airlock the grab points run out. Holloway is above the airlock but there is nothing to hold onto."

  if has_two_tethers:
    jump enough_rope
  else:
    jump not_enough_rope
    
# 2.2.2 ENOUGH ROPE ###########################################################
label enough_rope:
  
  h "Lucky I kept the tether to the airlock."
  
  "Holloway releases the other line and pulls himself along the tether for the last few meters to the open hatch and climbs into the airlock."
  
  "Completely exhausted, Holloway falls to the floor."
  
  H "Closing the hatch. Please remain clear."
  
  h "HANC, why didn’t you open it like that for me earlier?"
  
  H "You didn’t ask."
  
  "Holloway does not feel at ease with HANC’s response, again."
  
  jump pressurising

# 2.2.3. NOT ENOUGH ROPE ######################################################
label not_enough_rope:
  
  # [ Background image - Empty space. ]
  
  h "I can’t reach. 20 minutes oxygen."
  
  "Holloway struggles to reach the hatch. He makes a desperate leap but misses. 20 minutes later, in orbit around the planet below, he runs out of air and life."
    
  "The end."
  return

# 2.3.0. PRESSURISING #########################################################
label pressurising:

  # [ Background image - The airlock. ]
  # [ Sound effect - creaking metal. ]
  
  H "The pressurisation checklist is complete. Hull atmosphere is being restored."
  
  "The ship’s hull protests as it fills with air. The creaking sound of stressed metal is cause for concern."
  
  h "I hope that steel plate holds with only five bolts."
  
  H "(Silence)"
  
  h "That gauge indicates that there is pressure on the other side."

  menu:
  
    "Push the button to open the door to go inside.":
      jump slammed

    "Ask HANC if it’s okay to open the door to go inside.":
      jump sixty_more_seconds

# 2.3.1. SLAMMED ##############################################################
label slammed:

  # [ Background image - The airlock. ]
  # [ Character image - Holloway - unconscious. ]
  # [ Sound effect - depressurisation and a loud thump. ]
  
  "Unfortunately for Holloway, he opened the door too soon. He is slammed into the opening airlock door, caused by the pressure differential, and is severely injured."
  
  "No-one can help him. As he lay unconscious for hours on the airlock floor the ship sinks into the planet’s atmosphere and is destroyed."

  "The end."
  return

# 2.3.2. 60 MORE SECONDS ######################################################
label sixty_more_seconds:

  h "I just push that button to get in. I better check."
  
  h "HANC, is it okay to enter?"
  
  H "Not yet. Wait 60 more seconds."
  
  "Holloway waits 60 seconds."
  
  H "The pressure is equal. Opening the door. Please remain clear."
  
  "Holloway removes his helmet and enjoys the rich warm air of the ship."
  
  h "The ship’s orbit is decaying. You need to make your way to the bridge"
  
# 2.4.0. JINX MAKES PLANS #####################################################
label jinx_makes_plans:
  
  # [ Background image - Inside the shuttle. ]
  # [ Character image - Jinx standing - thinking. ]
  
  "Jinx notices the pressure change and knows that someone has to get to the bridge to transfer shuttle locks and control from there to the cargo hold so she can take the shuttle."
  
jump to_bridge 
