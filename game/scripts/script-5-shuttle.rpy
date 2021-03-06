#Shuttle

label to_shuttle:

# 5.0.0. SHUTTLE IN THE CARGO BAY #############################################
label shuttle_in_cargo_hold:

  scene black
  with dissolve

  # if you want to extend a dissolve use "with Dissolve (5.0)" NB upper-case 'D'
  
  scene bg shuttle-a
  with dissolve
    
  # [ Background Image - Largo cargo bay with the shuttle through an open door. ]
  
  "Jinx and Holloway make their way inside the shuttle and the door closes behind them."
  
  # [ Sound effect - Door Closing. ]

# 5.0.1. INSIDE THE SHUTTLE ###################################################
label inside_shuttle_transfer:
    
  
  scene black
  with dissolve
  
  scene bg cargo-hold-m
  
  show shuttle-clear-windows
  
  with dissolve
  

  # [ Background image - The shuttle internal area, several seats with two at the front like pilot seats. ]
  
  play sound hanc_5_0_1_sound
  
  
  H radio "Holloway, Please transfer me to the shuttle systems so I may help you."
  
  j "Holloway, HANC is not operating normally and I think it might be safer if you don't transfer him to the shuttle."
  
  "Holloway looks quite worried by this comment."
  
  "They have to decide whether to transfer HANC to the shuttle’s computer system."

  menu:
    
    "Transfer HANC to the shuttle.":
      jump hanc_transferred_aboard
    
    "Do not transfer HANC to the shuttle.":
      jump leaving_cargo_hold

# 5.1.0 HANC TRANSFERRED ABOARD ###############################################
label hanc_transferred_aboard:

  "Holloway agrees to upload HANC. There is a button on the console marked computer upload."
  
  h "Is the “upload” button the way to do this?"
  
  
  play sound hanc_5_1_0_sound
  
  
  H radio "Yes, just press and hold and I can do the rest."
  
  j "Are you sure Holloway?"
  
  show holloway-arm:
      zoom 1.8
      xpos 0.96         # 80 % of the way accross the background
      ypos 0.19         # 50 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
  
  
  
  "Holloway pushes and hold the “upload” button HANC begins to be downloaded on board the shuttle and populates the main computer."
  
  scene black
  with dissolve
  
  scene bg shuttle-d
  with dissolve
  
  # [ Background image - The computer's light up. ]

# 5.1.1. HANC TAKES CONTROL ###################################################
label hanc_takes_control:


  play sound hanc_5_1_1_1_sound
 
  H radio "Thankyou. Can I also have the code please. It will help."
  
  "Whether Holloway does or does not give HANC the code is irrelevant here. HANC locks them out of the systems and launches from the Illustrious. HANC aims the vessel away from the planet below and begins the journey towards High command."
  
  "If Holloway hands over the code it takes four weeks with interplanetary propulsion or two years with normal rockets. Either way Jinx and Holloway are dead after less than a week of Oxygen starvation."
  
  h "You can’t have the code perhaps the electrical systems will fail over the two years and your memory will be destroyed."
  
  
  
  play sound hanc_5_1_1_2_sound
 
  H radio "You won’t be around to find out."
  
  scene black
  with dissolve
  
  scene bg shuttle-g
  show jinx e:
      zoom 0.30         # 30 % size
      xpos 0.70         # 70 % of the way accross the background
      ypos 0.75         # 75 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      
  show holloway b:
      zoom 0.58         # 58 % size
      xpos 0.35         # 35 % of the way accross the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      
  with dissolve

  "The end."
  return

# 5.2.0. LEAVING THE CARGO HOLD ###############################################
label leaving_cargo_hold:
  
  scene black
  with dissolve
  
  scene bg shuttle-c
  with dissolve
  
  play sound launch_sound
  $ renpy.sound.set_volume (1.5)

  # [ Sound effect - Escape rockets firing under shuttle. ]
  
  
  "HANC realises they are leaving without him and he explosively decompresses the cargo bay in the hope of damaging the shuttle. But Jinx is too good a pilot and the shuttle moves out of the cargo bay."
  
  h "Sorry, HANC we can’t bring you with us. Good luck."
  
  j "Give me the code Holloway so I can fire these rockets."
  
  # [ Background music - Scary, uh oh: music. ]
  
  h "No! Remember our agreement. The code book is back there and the code is in my head."
  
  scene bg shuttle-i
  show shuttle-clear-windows
  
  show jinx o:
    zoom 0.90   # 95 % size
    xpos 0.30   # 20 % of the way across the background
    ypos 0.70   # 65 % of the way down the background
    xanchor 0.5 # using the centre of the character image
    yanchor 0.5 # using the centre of the character image
  
  "Holloway points to the Illustrious which is falling out of orbit."
  
  with dissolve
  
  # [ Background image - Illustrious front section burning as it moves slowly out of orbit and towards the planet. ]
  
  j "Tell me!!!."
  
  
  
  menu:
  
    "Give Jinx the code.":
      jump jinx_gets_the_code
    
    "Keep the code secret.":
      jump preparing_for_orbita

# 5.3.0. JINX GETS THE CODE ###################################################
label jinx_gets_the_code:
    
  scene black
  with dissolve
  
  show shuttle-clear-windows
  
  show jinx listening:
    zoom 0.65   # 65 % size
    xpos 0.25   # 25 % of the way across the background
    ypos 0.75   # 75 % of the way down the background
    xanchor 0.5 # using the centre of the character image
    yanchor 0.5 # using the centre of the character image
    
  
  
  
  
  # scene bg shuttle-h
  with dissolve
  # [ Background image - Inside the shuttle. ]
  
  h "The code is 776uythy."
  
  j "Thankyou, I will test these interplanetary systems for performance."
  
  # [ Character image - Jinx: smiling. ]
  
  "Jinx enters the code and starts the tests to ensure the systems will work and that Holloway gave her the correct code."
  
# 5.3.1. JINX KILLS HOLLOWAY ##################################################
label jinx_kills_holloway:

  scene black
  with dissolve  
  
  scene bg shuttle-g
  
  show jinx j:
      zoom 0.40
  show holloway a:
      zoom 0.68
      xpos 0.35         # 35 % of the way across the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      
  with dissolve
      
  j "Everything is great Holloway."
  
  "Everything works and then Jinx moves towards Holloway to hug him. But as she grabs him she snaps his neck killing him instantly."
  
  scene bg shuttle-g
  
  show holloway m
  
  show jinx i:
      zoom 0.40
      
  with dissolve
      
  
  # [ Character Image - Holloway neck broken - falling back ]
  
  # [ Sound effect - Snapping neck and gurgle sound. ]
  
  j "Sorry Holloway. Only enough air for one where I am going."
  
  scene bg shuttle-g:
     
  show holloway c:
      zoom 0.68
      xpos 0.50         # 50 % of the way across the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      
  with dissolve
  
  "The end."
  return

# 5.4.0 PREPARING FOR ORBITA ##################################################
label preparing_for_orbita:

  h "I will give it to you when we land down there on Orbita. You can take the shuttle and go wherever you want."
  
  
  
  # [ Character image - Jinx with a resigned look on her face. ]
  
  "They both then look at the Illustrious burning as it moves into the upper atmosphere."
  
  "HANC has now turned the huge defensive weapons towards the shuttle."
  
  scene bg shuttle-k
  show shuttle-clear-windows
  
  show jinx o:
    zoom 0.90   # 90 % size
    xpos 0.30   # 30 % of the way across the background
    ypos 0.70   # 70 % of the way down the background
    xanchor 0.5 # using the centre of the character image
    yanchor 0.5 # using the centre of the character image
  
  with dissolve
  
  # [ Background image - Illustrious front section red with flames - Through the shuttle windows. ]
  
  play sound beep_sound
  $ renpy.sound.set_volume (0.5)
  play sound hanc_5_4_0_sound
  
  
  H radio "Transfer me now! Or else I will destroy the shuttle."
  
  show jinx a
  
  "Jinx winks at Hollway."
  
  
  
  j "Go ahead HANC!"
  with dissolve
  
  "Holloway COVERS HIS EYES but nothing happens."
  
  # [ Character image - Holloway covering his face. ]
  
  j "The code is needed for HANC to fire any weapons."
  
  j "Ok let’s go down to Orbita. You had better give me the code down there. I can’t stay. As you know."
  
  scene bg shuttle-e
  show shuttle-clear-windows
  
  show jinx a:
    zoom 0.90   # 90% size
    xpos 0.30   # 30 % of the way across the background
    ypos 0.70   # 70 % of the way down the background
    xanchor 0.5 # using the centre of the character image
    yanchor 0.5 # using the centre of the character image
      
  
  with dissolve

        
  # [ Background image - Illustrious completely in flames. Aiming straight at the planet - Through the shuttle windows. ]
  
  
  "The Illustrious now falls deeper into the atmosphere and burns up."
  

# 5.4.1 TURNING TOWARD ORBITA #################################################
label turning_towards_orbita:

  "The interplanetary propulsion system is the only engine locked out by the code so the entry rockets work normally."

# 5.5.0 LANDING ON ORBITA #####################################################
label landing_on_orbita:

  scene bg shuttle-j
  with dissolve
  # [ Background image - Shuttle landed on a clearing of bush. ]
  
  "They enter the atmosphere and land."
  
  scene bg shuttle-g
  show jinx a:
      zoom 0.30
      xpos 0.50         # 50 % of the way across the background
      ypos 0.55         # 55 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      
      
  show holloway l:
      zoom 1.0
      xpos 0.60         # 60 % of the way across the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
  
  with dissolve
  
  # [ Background image - Holloway, leaving the shuttle and turning with a wink. ]
  
  
  "They get up from their seats and Jinx opens the shuttle hatch so that Holloway can leave the ship. He moves towards the exit and turns."
  
  
  scene bg shuttle-g
  show jinx a:
      zoom 0.30
      xpos 0.50         # 50 % of the way across the background
      ypos 0.55         # 55 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
  
  show holloway l:
      zoom 0.7
      xpos 0.55         # 55 % of the way across the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
  with dissolve
      
  "Holloway writes down the code for Jinx. He walks towards the exit of the shuttle. As he walks out:"
  scene bg shuttle-g
  show jinx a:
      zoom 0.30
      xpos 0.50         # 50 % of the way across the background
      ypos 0.55         # 55 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
  
  show holloway l:
      zoom 0.5
      xpos 0.50         # 50 % of the way across the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      
  with dissolve
      
  "He winks at Jinx. And says" 
  scene bg shuttle-g
  show jinx a:
      zoom 0.30
      xpos 0.50         # 50 % of the way across the background
      ypos 0.55         # 55 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
  
  show holloway l:
      zoom 0.45
      xpos 0.47         # 47 % of the way across the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      
  with dissolve
      
  
  h "I hope I remembered it correctly!!"
  scene bg shuttle-g
  show jinx a:
      zoom 0.30
      xpos 0.50         # 50 % of the way across the background
      ypos 0.55         # 55 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
  
  show holloway l:
      zoom 0.40
      xpos 0.44         # 44 % of the way across the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      
  j "I hope to see you around sometime"
  
  scene bg shuttle-l
   
   
   
"Congratulations Holloway you managed to live! Game over."
return
