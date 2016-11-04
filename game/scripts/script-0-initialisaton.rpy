# Run the declartions.
call declaratons

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
        
        "Start at a_sign_of_life":
          jump a_sign_of_life
    
    "Start at Bridge.":
      jump to_bridge
    
    "Start at Cargo Hold.":
      jump to_cargo_hold
    
    "Start at Shuttle.":
      jump to_shuttle
    
    "Start at Debugging.":
      jump to_debugging

return
