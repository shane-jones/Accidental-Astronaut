#Shuttle

label to_shuttle:
  "You have arrived on the shuttle."

label shuttle_in_cargo_hold:

label inside_shuttle_transfer:

  menu:
    
    "Transfer HANC to the shuttle.":
      jump hanc_transferred_aboard
    
    "Do not transfer HANC to the shuttle.":
      jump leaving_cargo_hold

label hanc_transferred_aboard:

label hanc_takes_control:
  "End."
  return

label leaving_cargo_hold:
  
  menu:
  
    "Give Jinx the code.":
      jump jinx_gets_the_code
    
    "Keep the code secret.":
      jump preparing_for_orbita

label jinx_gets_the_code:

label jinx_kills_holloway:
  "End."
  return

label preparing_for_orbita:

label turning_towards_orbita:

label landing_on_orbita:

"Happy ending."
return