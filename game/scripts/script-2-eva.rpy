# EVA

label to_eva:
  stop music fadeout 5.0
  
  scene black
  with dissolve
  
  pause 0.5
  
  # interpolation warpers https://www.renpy.org/doc/html/atl.html#interpolation-statement
  show bg eva-empty-space:
    zoom 1.0
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    easein 3.0 xpos 0.49
    pause 1.0
    ease 6.0 xpos 0.51
    pause 1.0
    easeout 3.0 xpos 0.5
    repeat
  
  show helmet-black
  
  with dissolve
  
  h "I move out of the airlock; a bit too fast. Maybe I shouldn’t have jumped."
  
  h "I’ve never been in free space before."
  
  scene bg eva-empty-space
  
  show helmet-black:
    zoom 1.0
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    linear 0.1 xpos 0.49 zoom 1.02
    linear 0.1 xpos 0.5 zoom 1.0
    linear 0.1 xpos 0.51 zoom 1.02
    linear 0.1 xpos 0.5 zoom 1.0
    repeat 5
    
  with dissolve
  
  queue sound [ tether_snap_sound, pained_grunt_sound ]
  
  "The tether has snapped taught."
  
  h "At least I’ve stopped. I turn around."

# 2.0.0. OUTSIDE ##############################################################
label outside:
   
# 2.0.1. THE SHIP #############################################################
label the_ship:

  show bg eva-with-planet:
    zoom 1.0
    xpos 0.7
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    
  show long-rope-2:  
    zoom 1.0
    xpos 0.7
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
  
  show helmet-black
  
  with dissolve
  
  h "This ship is really beaten up."
  
  h "There’s scaffolding on the hull and an “A” frame with a large metal plate attached. So that must be where the damage is."
  
  hide long-rope-2
  with None
  
  show bg eva-open-airlock
  show two-tethers
  show helmet-black
  
  with dissolve
  
  h "The airlock is still open. I should just go back in and wait for help."
  
  show bg eva-open-airlock:
    zoom 1.0
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 3.0 zoom 1.1 xpos 0.3 ypos 0.55
  
  show two-tethers:
    zoom 1.0
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 3.0 zoom 1.1 xpos 0.3 ypos 0.55
  
  with dissolve
  
  h "But if I make it to the scaffolding, I might be able to repair the hull."
    
  hide two-tethers
  with None
  
  show bg eva-with-planet:
    zoom 1.0
    xpos 0.7
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    pause 0.5
    ease 3.0 zoom 1.2 xpos 0.8
    
  show long-rope-2:
    zoom 1.0
    xpos 0.7
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    pause 0.5
    ease 3.0 zoom 1.2 xpos 0.8
    
  show helmet-black
  
  with dissolve
  
  "Holloway slowly pulls on the tether and moves towards the airlock."
  
  hide long-rope-2
  with None
  
  show bg eva-open-airlock:
    zoom 1.5
    xpos 0.3
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
  
  show two-tethers:
    zoom 1.5
    xpos 0.3
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
  
  show helmet-black
  
  with dissolve
    
  h "Look, there are some climbing grabs on the hull above the airlock hatch."
  
  h "I can use the grabs to pull myself up the side and over the top of the hull to get to the scaffolding."
  
  "Holloway clicks on the radio button."
  
  h "HANC. What do I do now?"
  
  play sound beep_sound
  $ renpy.pause(1.0)
  play sound hanc_2_0_1_sound
  $ renpy.pause(1.0)
    
  H radio "What can you see? Describe it."
  
  h "Surely this suit has a camera. Can’t I just send images via the radio system to you?"

# 2.0.2. TWO TETHERS ##########################################################
label two_tethers:

  show bg eva-open-airlock:
    zoom 1.5
    xpos 0.3
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 2.0 zoom 1.0 
  
  show two-tethers:
    zoom 1.5
    xpos 0.3
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 2.0 zoom 1.0 
    
  show helmet-black
  
  with dissolve
  
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
    
  show bg eva-open-airlock:
    zoom 1.0
    xpos 0.3
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 2.0 zoom 1.5 xpos 0.1 ypos 0.7 
  
  show two-tethers:
    zoom 1.0
    xpos 0.3
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 2.0 zoom 1.5 xpos 0.1 ypos 0.7 
    
  with dissolve
  
  h "I make my way up to the repair rig."

# 2.0.3. THE REPAIR ###########################################################
label the_repair:

  # [ Background image - Close up image of repair rig. ]
  
  "The radio splutters back into action."
  
  h "HANC. I’m at the repair site. What do I do with this oversized manhole cover?"
  
  play sound beep_sound
  $ renpy.pause(1.0)
  play sound hanc_2_0_3_sound
  $ renpy.pause(1.0)
  
  H radio "Maneuver the plate over the breach using the controls on the rig. Once you've got it there you have to fire the six explosive bolts fixed around the perimeter of the plate to lock it to the hull."
  
  # [ Sound music - Ominous music while the plate fits it into place. ]
  
  h "Okay HANC. It’s in position. How do I work these bolts."
  
  play sound beep_sound
  $ renpy.pause(1.0)
  play sound hanc_2_0_3b_sound
  $ renpy.pause(1.0)

  H radio "Just press on the firing pins."
  
  "Holloway makes his way around the plate, pressing the firing pins, one at a time."
  
  # [ Sound effect - Three explosions. ]

  play sound explosive_bolt_sound
  $ renpy.pause(1.0)
  
  "The hull vibrates violently underfoot with each bolt smashing into the hull."
  
  play sound explosive_bolt_sound
  $ renpy.pause(1.0)
  
  h "That's two."

  play sound explosive_bolt_sound
  $ renpy.pause(1.0)

# 2.1.0. A SIGN OF LIFE #######################################################
label a_sign_of_life:

  scene black
  with dissolve
  
  scene bg cargo-hold-f
  
  show shuttle-clear-windows
  
  show jinx listening:
  
  with dissolve
  
  $ renpy.pause(1.0)
  
  play sound distant_explosive_bolt_sound
  
  j "Someone is alive and outside but I have no space suit. I need whoever it is to pressurise the hull, and soon."
    
  $ renpy.pause(1.0)
  
  play sound distant_explosive_bolt_sound
  
  $ renpy.pause(2.0)

# 2.2.0. THE SHIP IS SEALED ###################################################
label the_ship_is_sealed:

  # [ Background image - Close up image of repair rig. ]
  
  scene black
  with dissolve
  
  scene bg eva-bolts-fired:
    zoom 1.0
    xpos 0.4
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
  
  show helmet-black
  
  with dissolve
  
  h "HANC, the last bolt failed."
  
  play sound beep_sound
  $ renpy.pause(1.0)
  play sound hanc_2_2_0_sound
  $ renpy.pause(1.0)
  
  H radio "The seal is tight. I am going to begin pressurising the ship."
  
  "HANC begins the checklist to return atmosphere to the ship."

# 2.2.1. BACK TO THE SHIP #####################################################
label back_to_the_ship:

  h "25 minutes oxygen. Good."
  
  show bg eva-open-airlock:
    zoom 1.5
    xpos 0.3
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 2.0 zoom 1.0
    
  show two-tethers:
    zoom 1.5
    xpos 0.3
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 2.0 zoom 1.0
      
  show helmet-black
  
  with dissolve
  
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
  
  scene bg airlock-door-open
  
  with dissolve
  
  "Completely exhausted, Holloway falls to the floor."
  
  play sound hanc_2_2_2_sound
  $ renpy.pause(1.0)
  
  H "Closing the hatch. Please remain clear."
  
  scene bg airlock-door-closed
  
  with dissolve
  
  h "HANC, why didn’t you open it like that for me earlier?"
  
  play sound hanc_2_2_2b_sound
  $ renpy.pause(1.0)
  
  H "You didn’t ask."
  
  "Holloway does not feel at ease with HANC’s response, again."
  
  jump pressurising

# 2.2.3. NOT ENOUGH ROPE ######################################################
label not_enough_rope:
  
  # [ Background image - Empty space. ]
  
  h "I can’t reach. 20 minutes oxygen."
  
  scene bg eva-empty-space:
    zoom 0.75
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5

  show holloway floating:
    zoom 0.5
    xpos 0.8
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    easeout 3.0 xpos 0.2 

  show airlock-door-open-transparent
  
  with dissolve

  "Holloway struggles to reach the hatch. He makes a desperate leap but misses. 20 minutes later, in orbit around the planet below, he runs out of air and life."
  
  "The end."
  return

# 2.3.0. PRESSURISING #########################################################
label pressurising:

  play sound hanc_2_3_0_sound
  $ renpy.pause(1.0)
  
  H "The pressurisation checklist is complete. Hull atmosphere is being restored."
  
  play music repressurisation
  
  "The ship’s hull protests as it fills with air. The creaking sound of stressed metal is cause for concern."
  
  h "I hope that steel plate holds with only nine bolts."
  
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
  
  scene bg airlock-door-closed
  
  with dissolve
  
  "Unfortunately for Holloway, he opened the door too soon. He is slammed into the opening airlock door, caused by the pressure differential, and is severely injured."
  
  stop music
  play sound door_release
  
  show holloway slammed:
    zoom 0.8
    xpos 0.5
    ypos 0.4
    xanchor 0.5
    yanchor 0.5
    easein 0.1 xpos 0.75
    linear 0.1 xpos 0.5 ypos 0.8
  
  "No-one can help him. As he lay unconscious for hours on the airlock floor the ship sinks into the planet’s atmosphere and is destroyed."

  "The end."
  return

# 2.3.2. 60 MORE SECONDS ######################################################
label sixty_more_seconds:

  h "I just push that button to get in. I better check."
  
  h "HANC, is it okay to enter?"
  
  play sound hanc_2_3_2_sound
  $ renpy.pause(1.0)
  
  H "Not yet. Wait 60 more seconds."
  
  "Holloway waits 60 seconds."
  
  play sound hanc_2_3_2b_sound
  $ renpy.pause(1.0)
  
  stop music fadeout 3.0
  
  H "The pressure is equal. Opening the door. Please remain clear."
    
  "Holloway removes his helmet and enjoys the rich warm air of the ship."
  
  play music audio.space_main_theme fadein 3.0
  
  H "The ship’s orbit is decaying. You need to make your way to the bridge"
  
# 2.4.0. JINX MAKES PLANS #####################################################
label jinx_makes_plans:
  
  scene black
  with dissolve
  
  scene bg cargo-hold-f
  
  show shuttle-clear-windows
  
  show jinx standing_thinking:
    zoom 0.75
    xpos 0.35
    ypos 0.75
    xanchor 0.5
    yanchor 0.5
  
  with dissolve 
  
  "Jinx notices the pressure change and knows that someone has to get to the bridge to transfer shuttle locks and control from there to the cargo hold so she can take the shuttle."
  
  scene black
  with dissolve
  
  $ renpy.pause(1.0)  
  
jump to_bridge 
