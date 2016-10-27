# Cargo Hold

label to_cargo_hold:
  "You have arrived in the cargo hold"
  
label cargo_hold:

label jinx:

label preparations:

label secrets:

label the_code:

  menu:
    
    "Give Jinx the code.":
      jump jinx_gets_away
    
    "Give HANC the code.":
      jump hanc_has_the_code
    
    "Do not share the code.":
      jump smart_boy_holloway

label jinx_gets_away:

label container_mistage:
  "End."
  return

label smart_boy_holloway:
  "Play on."
  
label agreement:

"Jump to the shuttle."
jump to_shuttle