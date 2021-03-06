# Airlock!



label to_airlock:
  play music space_main_theme fadein (5.0)
  
  
  show bg eva-b
  with Dissolve (5.0)
  
  play sound illustrious_sound
  $ renpy.sound.set_volume (0.15)
  
  "It's 2425. The Illustrious, a Mega class freighter, is on a two year trading mission. The ship is a self sufficient craft capable of interstellar light speed and 
   is well equipped with the latest navigation and weapons systems. "
 
  "It can defend against any attempt to raid it's huge supply of goods and outrun any known enemy.
  
   The crew of 23 is very well trained and they are nearing the end of their tour of duty." 
 
  "It was hit by a large meteor that was not detected by the onboard Human Autonomous Network Computer (HANC).

   The Illustrious has been very badly damaged and HANC has also sustained circuit damage."
 
  "The entire crew had to abandon ship using one of the two shuttles on board."
 
  "Frank Holloway, an intern, was near the main airlock studying when the impact occured and could not be found by the crew. The ship was hit so hard that most of the compartments were depressurised."
 
  "Frank was knocked to the ground by the main impact. He crawled towards the airlock and fell inside and collapsed gasping for air. He managed to get a space suit on but couldn't locate the helmet."

  "As the ship lost it's oxygen supply Holloway fell unconscious. The various pressure doors including the airlock automatically closed. Holloway was deprived of oxygen for some time, causing some memory loss, but luckily the airlock is self contained."

  "When he wakes up he has an initial loss of memory due to a lack of oxygen."

  "You are Holloway - good luck with surviving what's ahead"

  scene black
  with Dissolve (2.0)

  stop sound fadeout (3.0)
  
  
# 1.0.0. WAKING UP IN THE AIRLOCK #############################################
label waking_up_in_the_airlock:

# [ Background image - Airlock. ] 
  scene bg airlock-a
  with dissolve
  
# [ Sound - Struggling to breath (background moody space music). ]
  play music breathing_sound fadein (2.0)
  
  ht "I wake up. Where am I? Why am I wearing a spacesuit? I try to stand up, confused, cold, and struggling for air."

  play music space_main_theme fadein (5.0)
  
  scene bg airlock-c

  ht "I can't lay around here forever. I get up, groggily,  and reach for the door. It's all covered in ice. I can’t see through and I can’t open it."

# 1.0.1. DECIDING WHAT TO DO ##################################################
label deciding_what_to_do:

  scene bg airlock-b

  "Holloway sees a red flashing light. The oxygen indicator, faintly blinking next to the red light shows that there is limited oxygen."

  "There is a monitor next to the door, but it is powered down."

  ht "What should I do?"

  menu:
  
    "Do nothing and wait for help.":
      jump wait_for_help
    
    "Force open the airlock.":
      jump force_open_the_airlock
    
    "Power up the monitor.":
      jump the_last_log

# 1.1.0. WAIT FOR HELP ########################################################
label wait_for_help:

  "Not a good idea. Help is on the way. Unfortunately for Holloway, it will take two years to arrive. Holloway dies waiting."

  "The end."
  return

# 1.2.0. FORCE OPEN THE AIRLOCK ###############################################
label force_open_the_airlock:

  "Holloway is desperate and acting irrationally. There is an emergency button that opens the outside door regardless of the pressure differential."
  
  "The airlock opens, but the remaining air that Holloway is breathing rushes into the vacuum on the other side. This also throws Holloway through the doorway. Holloway can’t breathe and dies."

  "The end."
  return

# 1.3.0. THE LAST LOG #########################################################
label the_last_log:
  
  "Holloway turns on the monitor. A LOG Menu appears on the screen."
  
  l "Log Ready.\nSelect Log. (Holloway selects the most recent log.)\nPlay. (Holloway taps the play button)\nHANC"

  scene bg airlock-g
  show abrahams b:
    zoom 1.3 
    xpos 0.45 
    ypos 1.0 
    xanchor 0.5 
    yanchor 0.5

  with dissolve
  
  "Captain Abrahams appears as a video recording."
  
  a "We have the abandoned the Illustrious with all souls accounted for except one who could not be found - civilian Frank Holloway, a research Astrobiologist."

  show abrahams c:
    zoom 1.0 
    xpos 0.50 
    ypos 1.0 
    xanchor 0.5 
    yanchor 0.5
 
  with Dissolve (1.5)

  a "We searched but were unable to look any longer and left with the air supply diminishing."
  
  a "This ship was hit by debris from an asteroid and is in orbit around Orbita, a planet that can sustain life."
  
  a "Holloway, if you read this, you need to get down there. Several problems exist though."
  
  a "This ship can't be flown to the surface without being destroyed as it passes through the atmosphere. It’s damaged and not capable of landing on a planet and would burn up entering the atmosphere."

  show abrahams d:
    zoom 1.2 
    xpos 0.50 
    ypos 0.90 
    xanchor 0.5 
    yanchor 0.5

  with Dissolve (1.5)  
  
  a "Additionally, the ship is not very stable in the current orbit due to the explosion and is slowly drifting towards the planet."
  
  a "There is a one shuttle left in the cargo bay. The Illustrious is unpressurised and the hull must be repaired and then you could possibly attempt to stabilise the ship from the bridge to buy more time."
  
  a "There is also an onboard computer called HANC who can help. HANC has suffered some logic damage but appears to be operating properly."
  
  l "Log end.\nReplay log.\nSelect log.\nPlay.\nHANC."
  
# 1.4.0. HANC #################################################################
label hanc:

  scene black
  with dissolve
  
  scene bg airlock-b
  with dissolve

  "After playing the LOG, Holloway presses a button labeled “HANC”. HANC (the console) boots up after 30 seconds and analyses the ship."

#  show hanc a:
#      zoom 0.15 xpos 0.2 xpos 0.6 xanchor 0.5 yanchor 0.5 #reduced size has the file is large
#       #25% of the way across the background
#       #80% of the way down the background
#       #using the centre of the character image
#       #using the centre of the character image 
      
  "HANC attempts to power up and pressurise the ship but it’s damaged with a hole and needs to be sealed first."
  
  "The illustrious is still orbiting around planet Orbita, a trading partner. It’s heavily populated so there’s definitely water and food down there."

  scene bg airlock-a

 
  play sound hanc_1_4_0_sound
  $ renpy.sound.set_volume (1.0)
  
  scene bg airlock-a
  
  H "Holloway, you must go outside and make a repair to the hull."

  
  
  ht "I look around for my suit helmet. If I go outside without it I will die and my eyes will explode; not necessarily in that order."
  
  h "HANC, where’s my helmet?"
  
  play sound hanc_1_4_0b_sound

  H "There's a small cabinet to your left that contains a helmet and a tether that you will need to fix the hole outside. Your suit has it's own oxygen supply."

# 1.5.0. THE LOCKER ###########################################################
label the_locker:

  ht "I go to the cabinet and put on my helmet with directions from HANC. The gauge in my helmet shows that I have 60 minutes of oxygen."

# 1.6.0. LEAVING THE AIRLOCK ##################################################
label leaving_the_airlock:

  ht "I return to the airlock and move towards the hatch."
  
  h "HANC, open the hatch."

  play sound hanc_1_6_0_sound
  
  H "Do you want me to equalise the pressure first?"
  
  h "Ah yes… Of course."
  
  h "HANC equalises the pressure but does not open the door. I move a heavy lever to an open position which requires lots of effort."
  
  ht "I pause before opening the hatch. What should I do now?"
    
  menu:
  
    "Open the airlock and go outside.":
      jump floating_away
      
    "Ponder on how to hold on outside and ask HANC what to do.":
      jump hancs_advice

# 1.7.0. FLOATING AWAY ########################################################
label floating_away:
  "Holloway just walks out of the airlock and floats away. Missing presumed dead."
  
  "The end."
  return

# 1.8.0. HANC’S ADVICE ########################################################
label hancs_advice:
  
  h "HANC, what should I do."

  play sound hanc_1_8_0_sound
  
  H "Take the tether and attach it to the lock point just outside the airlock."
  
  
  h "Why didn't you offer that advice before I was about to open the hatch."

  play sound hanc_1_8_0b_sound
  
  H "You didn't ask."
  
  ht "I feel uneasy about HANC’s less than helpful response."
  
  ht "I pause before jumping out into space. What should I do now?"
  menu:
    
    "Leave the ship.":
      jump radio_silence
    
    "Ask HANC about communications outside the ship.":
      jump radio_controls

# 1.9.0. RADIO SILENCE ########################################################
label radio_silence:
  
  "Holloway leaves the ship, but discovers that he does not know how to repair the hull and he has no communication with HANC."
  
  "Sadly he has spent too much time finding this out. In fact, this means that by the time Holloway returns to the Airlock finds out what to do to establish radio communication and go back to the repair site that he no longer has enough air to do the task."
    
  "The end."
  return

# 1.10.0. RADIO CONTROLS ######################################################
label radio_controls:
  
  h "How can we talk when I’m outside? I don’t know how to repair a spaceship."
 
  play sound hanc_1_10_0_sound
  
  H "We can communicate on the radio that’s built into your suit. Can you see it. Just power it up."
  
  h "Yeah. Sure, I see it now. Got it."

jump to_eva
