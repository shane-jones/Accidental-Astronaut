# Bridge

label to_bridge:
  "You have arrived on the bridge."

label walking_to_the_bridge:

label the_bridge:

  menu:
  
    "Stay and wait for HANC to respond?":
      jump waiting_for_hanc
    
    "Run to the cargo hold and get in the shuttle?":
      jump the_shuttle

label the_shuttle:
  "End."
  return

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

label hanc_has_the_code:
  "End."
  return

label holloway_keeps_the_code_to_himself:
  if has_code_book:
    "You have the code book."
  else:
    "You do not have the code book."

"Jump to the cargo hold."
jump to_cargo_hold