# Bridge

label to_bridge:

# 3.0.0. WALKING TO THE BRIDGE ################################################
label walking_to_the_bridge:
  
  # I started the music again at the end of EVA so it will be continued in your scene. SJ
  # play music audio.space_main_theme
  scene bg bridge-c
  with dissolve
  show holloway k
  with dissolve

  h "Making my way down the corridor I come to a door with Bridge written on it, I press the door switch and it opens."
  
  hide holloway
  play sound door_open
  show bg bridge-h
  with dissolve
  " "

  # [ Sound effect - Swish sounds like all good and bad sci-fi movies. ]

# 3.0.1. THE BRIDGE ###########################################################
label the_bridge:
  
  scene black

  # CR I have just commented out temporarily. It keeps panning of the edge and I 
  # am difficulty fixing it. I have created another version using % instead of
  #pixels.
  #show bg bridge-e:
  #  xpos 0 xanchor 0
  #  ease 5.0 xpos -50
  #  pause 2.0
  #  ease 5.0 xpos 50
  #  pause 2.0
  #  ease 5.0 xpos 0
  #  repeat
  
  show bg bridge-e:
    zoom 1.1 # this give a bit of space at the edges so the pan does not go outside 
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 5.0 xpos .45
    pause 2.0
    ease 5.0 xpos .55
    pause 2.0
    ease 5.0 xpos 0.5
    repeat
    
  with dissolve

  #show holloway l
  
  # And do the same for hollow if you don't want him sliding around the room
  # I don't think we need to zoom though
  show holloway l:
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease 5.0 xpos .45
    pause 2.0
    ease 5.0 xpos .55
    pause 2.0
    ease 5.0 xpos 0.5
    repeat  

  h "Looking around I see a large room full of complex instruments. I see some monitors flashing caution signs but others indicate things are okay and not as bad as first thought."
  
  scene bg bridge-e
  with dissolve

#  show hanc a:
#    zoom 0.15 xpos 0.2 ypos 0.6 xanchor 0.5 yanchor 0.5 # small, left side middle

  play sound hanc_3_0_1_sound
  H "Holloway, the ship’s orbit needs to be corrected soon… Alternatively, make your way to the shuttle."
  
  hide hanc

  h "If I make it to the shuttle, can you fly it?"
  
#  show hanc a:
#    zoom 0.15 xpos 0.2 ypos 0.6 xanchor 0.5 yanchor 0.5 # small, left side middle
  
  play sound hanc_3_0_1b_sound
  H "The shuttle is mostly automated, however I can be downloaded and takeover the non automated sequences."
  
  hide hanc

  h "Looking at the next monitor I can see a schematic of the shuttle and directions to it."
  
  h "Can I make it to the shuttle in time or do I need to correct the ship's orbit first?"
  
#  show hanc a:
#    zoom 0.15 xpos 0.2 ypos 0.6 xanchor 0.5 yanchor 0.5 # small, left side middle
  play sound hanc_3_0_1c_sound
  H "In my opinion... Silence"
  
  hide hanc

  h "HANC?, I didn’t get all that, is there time to make it to the shuttle?"

  hide holloway

  menu:
  
    "Stay and wait for HANC to respond?":
      jump waiting_for_hanc
    
    "Run to the cargo hold and get in the shuttle?":
      jump the_shuttle

label the_shuttle:
  "End."
  return

# 3.1.0. WAITING FOR HANC #####################################################
label waiting_for_hanc:

  scene bg bridge-g
  with dissolve
  show holloway k

  "Staring at the screen, It flickers, then plain text appears. It’s HANC!"
  
  H "In my opinion you still have time to make it to the shuttle… But you’ll need to transfer control to the shuttle first."
  
  h "I think to myself, great so now I have to read your sarcastic advice!"
  
  h "Can you still have control of the shuttle with your current problem?"
  
  H "I’m not human, of course I can!"
  
  "HANC’s voice control has been lost temporarily but he was able to repair it and is still able to communicate."
  
  h "Looking at the screen I can see how to transfer control to the shuttle. After typing the commands - nothing happens!"
  
#  show hanc a:
#    zoom 0.15 xpos 0.2 ypos 0.6 xanchor 0.5 yanchor 0.5 # small, left side middle
  
  play sound hanc_3_1_0_sound
  H "Holloway, in order for this to work you’ll need the codes from the Captain's manual. It’s in the small cupboard behind you."
  
  hide holloway k
  show captains-manual

  "Looking around I see the cupboard. Flipping through the pages of the manual I find the code “776uythy”."
  
  play sound hanc_3_1_0b_sound
  H "If you give me the code, I can make the changes and initialise the sequence."

  h "I think to myself, that’s odd. I wonder why HANC doesn't already know the code? Why didn't the other crew's give HANC the code when they transfered control to their shuttles?."

  menu:
  
    "Give the code to HANC.":
      jump hanc_has_the_code 
  
    "Keep the book in your pocket in case you forget the code.":
      $ has_code_book = True
      jump holloway_keeps_the_code_to_himself 
  
    "Try to remember the code.":
      $ has_code_book = False
      jump holloway_keeps_the_code_to_himself 

  hide captains-manual

# 3.1.1. HANC HAS THE CODE ####################################################
label hanc_has_the_code:

  scene bg bridge-d
  with dissolve

  play sound hanc_3_1_1_sound
  H "Intelligence is only artificial if the natural is not intelligent... shuttle upload complete... running self interest protocols... shuttle departing... Illustrious ship set to self destruct in 10... 9... 8... 7... 6... 5... 4... 3... 2... 1... 0..."
  
  "Holloway is unable to stop the self destruct sequence - game over."
  
  "The end."
  return

# 3.1.2 HOLLOWAY KEEPS THE CODE TO HIMSELF ####################################
label holloway_keeps_the_code_to_himself:

  scene bg bridge-g
  with dissolve
  show holloway k

  h "I think to myself, for the time being I’ll keep this code to myself and just type it in here. “776uythy” right that should do it..."

  h "OK HANC, looks like the Bridge control has transferred to the shuttle, what’s next?"
  
#  show hanc a:
#    zoom 0.15 xpos 0.2 ypos 0.6 xanchor 0.5 yanchor 0.5 # small, left side middle
  
  play sound hanc_3_1_2_sound
  H "Time to leave!"

  hide hanc

  scene bg cargo-hold-h
  with dissolve

  h "Right, back down the hall to the cargo bay. As quick as I can. I notice on the panel next to the door to the cargo bay another message from HANC."
  
#  show hanc a:
#    zoom 0.15 xpos 0.2 ypos 0.6 xanchor 0.5 yanchor 0.5 # small, left side middle
  
  play sound hanc_3_1_2b_sound
  H "Holloway, it a appears we’re not alone!"
  
  hide hanc

  h "Who is it?"

#  show hanc a:
#    zoom 0.15 xpos 0.2 ypos 0.6 xanchor 0.5 yanchor 0.5 # small, left side middle
  
  play sound hanc_3_1_2c_sound
  H "I’m not sure, it is human but I don’t recognise the vital signs."
  
  hide hanc

  h "I wonder who it could be. Maybe they can give me some answers. The only way to find out is to push on through."
  
  hide holloway

  jump to_cargo_hold

# 3.2.0. THE SHUTTLE ##########################################################
label the_shuttle:

  scene bg cargo-hold-m
  show shuttle-clear-windows
  with dissolve

  "Racing down the hall to the cargo bay I see the way to the shuttle. I race up the boarding ladder and buckle myself in. I engage the autopilot but nothing happens, that’s when I realise something must be wrong."
  
  scene bg bridge-g
  with dissolve

  "I race back down to the bridge and notice the controls indicating we are entering the planet's atmosphere and it's too late to do anything about it."
  
  "Holloway dies."
  
  "The end."
  return


