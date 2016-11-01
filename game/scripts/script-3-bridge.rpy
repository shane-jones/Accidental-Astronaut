# Bridge
# Not sure there is anything left to do??? :)

label to_bridge:

# 3.0.0. WALKING TO THE BRIDGE ################################################
label walking_to_the_bridge:

  # [ Background image - Spaceship doors with control panel. ]
  
  h "Making my way down the corridor I come to a door with Bridge written on it, I press the door switch and it opens."
  
  # [ Sound effect - Swish sounds like all good and bad sci-fi movies. ]

# 3.0.1. THE BRIDGE ###########################################################
label the_bridge:

  # [ Background image - Ship’s bridge / control center. ]
  
  h "Looking around I see a large room full of complex instruments. I see some monitors flashing caution signs but others indicate things are okay and not as bad as first thought."
  
  H "Holloway, the ship’s orbit needs to be corrected soon… Alternatively, make your way to the shuttle."
  
  h "If I make it to the shuttle, can you fly it?"
  
  H "The shuttle is mostly automated, however I can be downloaded and takeover the non automated sequences."
  
  h "Looking at the next monitor I can see a schematic of the shuttle and directions to it."
  
  h "Can I make it to the shuttle in time or do I need to correct the ship's orbit first?"
  
  H "In my opinion..."
  
  h "HANC?, I didn’t get all that, is there time to make it to the shuttle?"
  
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

  h "Staring at the screen, It flickers, then plain text appears. It’s HANC!"
  
  H "In my opinion you still have time to make it to the shuttle… But you’ll need to transfer control to the shuttle first."
  
  h "I think to myself, great so now I have to read your sarcastic advice!"
  
  h "Can you still have control of the shuttle with your current problem?"
  
  H "I’m not human, of course I can!"
  
  "HANC’s voice control has been lost but he was able to repair it and is still able to communicate."
  
  h "Looking at the screen I can see how to transfer control to the shuttle. After typing the commands - nothing happens!"
  
  H "Holloway, in order for this to work you’ll need the codes from the Captain's manual. It’s in the small cupboard behind you."
  
  h "Looking around I see the cupboard. Flipping through the pages of the manual I find the code “776uythy”."
  
  H "If you give me the code, I can make the changes and initialise the sequence."
  
  h "I think to myself, that’s odd, I wonder why HANC doesn't already know the code, he seems to know everything else."

  menu:
  
    "Give the code to HANC.":
      jump hanc_has_the_code 
  
    "Keep the book in your pocket in case you forget the code.":
      $ has_code_book = True
      jump holloway_keeps_the_code_to_himself 
  
    "Try to remember the code.":
      $ has_code_book = False
      jump holloway_keeps_the_code_to_himself 

# 3.1.1. HANC HAS THE CODE ####################################################
label hanc_has_the_code:

  H "Intelligence is only artificial if the natural is not intelligent... shuttle upload complete... running self interest protocols... shuttle departing... Illustrious ship set to self destruct in 10... 9... 8... 7... 6... 5... 4... 3... 2... 1... 0..."
  
  "Holloway is unable to stop the self destruct sequence - game over."
  
  "The end."
  return

# 3.1.2 HOLLOWAY KEEPS THE CODE TO HIMSELF ####################################
label holloway_keeps_the_code_to_himself:

  h "I think to myself, for the time being I’ll keep this code to myself and just type it in here. “776uythy” right that should do it..."

  h "OK HANC, looks like the Bridge control has transferred to the shuttle, what’s next?"
  
  H "Time to leave!"
  
  h "Right, back down the hall to the cargo bay. As quick as I can. I notice on the panel next to the door to the cargo bay another message from HANC."
  
  H "Holloway, it a appears we’re not alone!"
  
  h "Who is it?"
  
  H "I’m not sure, it is human but I don’t recognise the vital signs."
  
  h "I wonder who it could be. Maybe they can give me some answers. The only way to find out is to push on through."
  
  jump to_cargo_hold

# 3.2.0. THE SHUTTLE ##########################################################
label the_shuttle:

  # [ Background image - Shuttle cockpit. ]
  
  h "Racing down the hall to the cargo bay I see the way to the shuttle. I race up the boarding ladder and buckle myself in. I engage the autopilot but nothing happens, that’s when I realise something must be wrong."
  
  # [ Background image - Ship’s bridge / control center. ]
  
  h "I race back down to the bridge and notice the controls indicating we are entering the planet's atmosphere and it's too late to do anything about it."
  
  "Holloway dies."
  
  "The end."
  return


