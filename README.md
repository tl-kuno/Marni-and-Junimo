# Marni-and-Junimo<br>

A text-based adventure game written for OSU Capstone Project<br>

## Game Parameters:<br>

### Summary: An adventure style, text based game

### "Rooms" - 10 different rooms
    - A paragraph description for first entry
    - A short description for returning entries
    - Ways to exit must be aluded to in the long and short form descriptions
    - (Optional) Explanations of occurances that happen while in the room
### "Objects" - 8 different objects
    - able to be acquired into a player inventory
    - must be able to drop item in any room
    - will stay in that room
    - able to be picked up later
    - (Optional) Can be fictionally overwritten for example
        - lava melts it
        - bread crumbs eaten
### "Verbs" - 10 primary actions
    - must be allowed to combine with each feature in each room
    - written response for each attempted feature

### Required phrases
    - look :: repeats the long form explanation (I like "look around" better) 
    - look at ___ :: fictionally interesting explanation of feature or object (includes inventory) 
    - go north | north | go dank-smelling staircase | dank-smelling staircase :: proceed to indicated exit 
    - (Optional) other room travel verbs implemented when logical like jump 
    - take :: acquire an object into your inventory 
    - help :: offers a list of verbs that the game understands 
    - main commands must be listed, but some commands may be hidden for user to discover
    - inventory :: lists all items in your inventory
    - savegame :: saves the state of the game to a file
    - loadgame :: confirms with the user that this is really desired and then

### Language Processing
    - research and implement Natural Langage Parsing
    - implement synonym phrases like "grab" for "take" etc.  

### Misc Requirements
    - Must submit a step-by-step solution for professor to be able to walk through entire game

### Technical Requirements
    - Must compile and run on the OSU flip servers
    - OOP, data about the game must be loaded from individual files
    - ie each room would have its own file, consider json structure
    - Note: if your game requires min width and height in characters, inform user,   exit if not met at load
