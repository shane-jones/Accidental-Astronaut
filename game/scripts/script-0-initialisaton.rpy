# Run the declartions.
call declarations from _call_declarations

# The game starts here.

label start:
  
  # Temporary menu for debugging.
  
  menu:
  
    "Start at airlock.":
      jump to_airlock
    
    "Start at EVA.":
      
      menu:
        
        "Start at to_eva":
          jump to_eva
        
        "Start at two_tethers":
          jump two_tethers
        
        "Start at a_sign_of_life with has_two_tethers":
          $ has_two_tethers = True
          jump a_sign_of_life
    
        "Start at a_sign_of_life with !has_two_tethers":
          $ has_two_tethers = False
          jump a_sign_of_life
          
        "Start at label slammed":  
          jump slammed          
        
        "Start at label jinx_makes_plans":  
          jump jinx_makes_plans

    "Start at Bridge.":
      jump to_bridge
    
    "Start at Cargo Hold.":
      jump to_cargo_hold
    
    "Start at Shuttle.":
      jump to_shuttle
      
    "Start at Bye":
      jump landing_on_orbita 
    
    "Start at Debugging.":
      jump to_debugging

return
