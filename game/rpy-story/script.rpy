## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define f = Character('Frank')
define PC = Character('...')
define LOG = Character('LOG...')
define HANC = Character('HANC')

## The game starts here.

#SJ test comment

label start:
    
    stop music

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg room

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show Frank

    ## These display lines of dialogue.
    
    play music "breathing-sound.mp3"

    f "Ughh....."

    f "W....where..am I..??."

    f "How did I get here?...."
    
    f "Oh no!! That red flashing light isnt a good sign, the oxygen levels are low. I... I need to get up.., ive got to bring up these oxygen
       levels some how."
    
    f "M...maybe this door can get me out.."
    play music "Ice-Sound.mp3" fadein 2 fadeout 2
    
    f "....The ice has jammed the door...."
    f " The windows on the door is foggy and icy, I.. I cant see anything.."
       
    
    
    stop music fadeout 3
    
    f "Ive got to find another way out, but how?.."
    
    
    
    menu introduction:
        "Do nothing, wait for help":
            f "I just hope help arrives soon, but I can't sit here and do nothing"
            jump introduction
        
        "Force airlock":
            f "Thats crazy!!.. I dont want to die.."
            jump introduction
        
        "Maybe that strange device on the wall can help":
            f "Lets turn this thing on..."
            
            play music "Beep-Sound.mp3"
            f ".....*beep*...."
            stop music
            
            
    f "Oh... it looks like a...a recording of some type!.."
    
    
    LOG "We have abandoned the illustrious with all souls accounted for except one who could not be found - Civilian
            Frank Holloway, a research Astrobiologist." 
            
    LOG "We searched but were unable to look any longer and left with diminishing air supplies.This ship was hit by debris from an
            asteroid and is in orbit around a planet called and that it can sustain life"
    
    LOG "Holloway, if you read this, needs to get there. Several problems exist though. This ship can't be flown to the surface without 
         being destroyed passing through the atmosphere  as it’s a freighter and not capable of landing on a planet and would burn up 
         entering the atmosphere"
    
    LOG "Additionally, the ship is not very stable in the current orbit due to the explosion and is slowly drifting towards the planet. 
         There is a one shuttle left in the cargo bay. The ship is unpressurised the hull must be repaired and then possibly attempt to 
         stabilise the ship from the bridge to buy more time."
    
    LOG "There is also an onboard computer called HANC who can help, HANC has suffered some logic damage but appears to be operating 
         properly"
    
    LOG "LOG END"
    
    f "Wow!.."
    f "W...Well it looks like this HANC could be useful"
    f "*Frank presses HANC button*"
    play music "Beep-Sound.mp3"
    PC "*beep*"
    stop music
    
    LOG "Booting...Please wait...."
    
    f "W...Whats my situation HANC?"
    PC "*30 seconds later.....*"
    
    HANC "Hi Sir"
    HANC "I am analysing the situation now"
    HANC "I will attempt to power up and pressurise the rest of the ship"
    PC "...*minutes later...*"
    HANC "I can't get enough power to run the ship properly until it can be sealed"
    HANC "You will need to go outside, better you than me"
    HANC "The ship has no oxygen due to a hole in the hull which must be repaired."
    HANC "After the collision, a crew member attempted to repair the hole but was lost after being hit by a small debris field"
    HANC "The crew could not pressurise the ship and therefore only had the oxygen in their suits. They were forced to abandon
          the ship but could not locate you and ran out of time"
    HANC "They took one of the two shuttles and left. They fired the engines away from the mothership but something happened and they
          never made it to the surface below"
    HANC "They did not make radio contact with anyone so there will be no help, at this point."
    HANC "The illustrious is still orbiting the planet Orta which is a trading partner. Its populated with people that are civilised
          but still not capable of spaceflight"
    HANC "The atmosphere is suitable and there is plenty of food and water. They are friendly and helpful"
    
    
    
    
    
    
    ## This ends the game.

    return
