# Run the declartions.
call declarations from _call_declarations

# The game starts here.

label start:
  
  # Temporary menu for debugging.
  
  menu:

    "Start at Airlock":
      jump to_airlock
        
    "Start at HANC.":
      jump hanc
    
    "Start at EVA.":
      
      menu:
        
        "Start at to_eva":
          jump to_eva
        
        "Start at two_tethers":
          stop music
          jump two_tethers
        
        "Start at a_sign_of_life with has_two_tethers":
          stop music
          $ has_two_tethers = True
          jump a_sign_of_life
    
        "Start at a_sign_of_life with !has_two_tethers":
          stop music
          $ has_two_tethers = False
          jump a_sign_of_life
          
        "Start at pressurising":  
          stop music
          jump pressurising
          
        "Start at label slammed":  
          stop music
          jump slammed          
        
        "Start at label jinx_makes_plans":  
          stop music
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
