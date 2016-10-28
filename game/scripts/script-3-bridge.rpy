# Bridge

label to_bridge:
  "You have arrived on the bridge."

# 3.0.0. WALKING TO THE BRIDGE ################################################
label walking_to_the_bridge:

# 3.0.1. THE BRIDGE ###########################################################
label the_bridge:

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
  "End."
  return

# 3.1.2 HOLLOWAY KEEPS THE CODE TO HIMSELF ####################################
label holloway_keeps_the_code_to_himself:
  if has_code_book:
    "You have the code book."
  else:
    "You do not have the code book."

# 3.2.0. THE SHUTTLE ##########################################################
label the_shuttle:

"Jump to the cargo hold."
jump to_cargo_hold