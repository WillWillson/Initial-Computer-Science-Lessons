
import sys

# this blueprint for a room
class Room:

    # the constructor
    def __init__(self, name):
        self.name = name             # name
        self.exits = []              # exits
        self.exitLocations = []      # exitLocations
        self.items = []              # items
        self.itemDescriptions = []   # descriptions for each item
        self.grabbables = []         # grabables, things for our inventory

    # getters and setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # addExit method
    def addExit(self, exit, room):
        """
        Adds an exit to the room
        exit is a string
        room is an instance of a room
        """
        self._exits.append(exit)
        self._exitLocations.append(room)

    # addItem method
    def addItem(self, item, desc):
        """
        Adds an item to the room
        item is a string
        desc is a string, describes the item
        """
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # addGrabbable
    def addGrabbable(self, item):
        """
        adds a grabbable item to the room
        item is a string
        """
        self._grabbables.append(item)

    # delGrabbable
    def delGrabbables(self, item):
        """
        removes a grabbable item from the list of grabbables
        item is a sting
        """
        self._grabbables.remove(item)

    # __str__ function
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the items in the room are
        s += "You see: "
        for items in self.items:
            s += items + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        s += "\n"

        return s

# create rooms function
def createRoom():
    # currentRoom global var
    global currentRoom

    # create each room
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Room 5")

    # handle room 1
    # add the exits
    r1.addExit("east", r2)
    r1.addExit("south",r3)

    # add grabbables
    r1.addGrabbable("key")

    # add items
    r1.addItem("chair", "It is made of wicker and no one is sitting on it")
    r1.addItem("table", "It is made of oak. A gold key rests on it.")

    # handle room 2
    # add exits
    r2.addExit("west", r1)
    r2.addExit("south", r4)

    # add items
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes.")
    
    # handle room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addExit("west", r5)

    # add grabbables
    r3.addGrabbable("book")

    # add items
    r3.addItem("bookshelves", "They are empty. Go figure")
    r3.addItem("statue", "There is nothig special about it.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")

    # handle room 4
    # add exits
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None)        # game over/death scenario

    # add grabbables
    r4.addGrabbable("6-pack")

    # add items
    r4.addItem("brew_rig", "Jean Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")

    # handle room 5
    # add exits
    r5.addExit("east", r3)

    # add items
    r5.addItem("chest", "A weird wodden chest is sitting in the corner with to code locks.")

    # set current room to room 1
    currentRoom = r1

# death picture

def death():
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 +"\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7+ "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" +"$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$"* 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")

# key picture

def key():
    print(" " * 17 + "u" * 5)
    print(" " * 15 + "u" * 3 + " " * 3 + "u" * 3)
    print(" " * 13 + "u" * 3 + " " * 7 + "u" * 3)
    print(" " * 11 + "u" * 3 + " " * 11 + "u" * 3)
    print(" " * 11 + "u" * 3 + " " * 11 + "u" * 3)
    print(" " * 11 + "u" * 3 + " " * 11 + "u" * 3)
    print(" " * 13 + "u" * 3 + " " * 7 + "u" * 3)
    print(" " * 15 + "u" * 3 + " " * 3 + "u" * 3)
    print(" " * 17 + "u" * 5)
    print(" " * 17 + "u" * 5)
    print(" " * 17 + "u" * 2 + "4" * 1 + "u" * 2)
    print(" " * 17 + "u" * 5)
    print(" " * 17 + "u" * 2 + "9" * 1 + "u" * 2)
    print(" " * 17 + "u" * 5)
    print(" " * 17 + "u" * 2 + "2" * 1 + "u" * 2)
    print(" " * 16 + "u" * 6)
    print(" " * 15 + "u" * 7)
    print(" " * 17 + "u" * 4)
    print(" " * 17 + "u" * 5)
    print(" " * 18 + "u" * 4)
    print(" " * 17 + "u" * 5)
    print(" " * 18 + "u" * 4)
    print(" " * 19 + "u" * 3)
    print(" " * 20 + "u" * 2)
    print(" " * 21 + "u" * 1)
    
# book picture

def book():
    print(" " * 17 + "T" * 17 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 1 + "  Computers" * 1 + " " * 3 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 1 + "  For Older" * 1 + " " * 3 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 1 + "    People " * 1 + " " * 3 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + "_______________" * 1 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 1 + "  Turning on" * 1 + " " * 2 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 1 + "   Computers" * 1 + " " * 2 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + "_____Step 1____" * 1 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 15 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 1 + " Press Power" * 1 + " " * 2 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 15 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 1 + " Wait to Load" * 1 + " " * 1 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 15 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 1 + "Type Password" * 1 + " " * 1 + "1" * 1 + "I" * 1)
    print(" " * 17 + "1" * 1 + " " * 3 + "   815      " + "1" * 1 + "I" * 1)
    print(" " * 17 + "T" * 17 + "I" * 1)

# win picture

def win():
    print(" " * 10 + "W" * 7 + " " * 35 + "W" * 8)
    print(" " * 11 + "W" * 7 + " " * 33 + "W" * 8)
    print(" " * 12 + "W" * 7 + " " * 13 + "W" * 3 + "W" * 2 + " " * 13 + "W" * 8)
    print(" " * 13 + "W" * 7 + " " * 11 + "W" * 5 + "W" * 2 + " " * 11 + "W" * 8)
    print(" " * 14 + "W" * 7 + " " * 9 + "W" * 7 + "W" * 2 + " " * 9 + "W" * 8)
    print(" " * 15 + "W" * 7 + " " * 7 + "W" * 9 + "W" * 2 + " " * 7 + "W" * 8)
    print(" " * 16 + "W" * 7 + " " * 5 + "W" * 11 + "W" * 2 + " " * 5 + "W" * 8)
    print(" " * 17 + "W" * 7 + " " * 3 + "W" * 13 + "W" * 2 + " " * 3 + "W" * 8)
    print(" " * 18 + "W" * 7 + " " * 1 + "W" * 17 + " " * 1 + "W" * 8)
    print(" " * 19 + "W" * 7 + "W" * 7 + " " * 4 + "W" * 14)
    print(" " * 20 + "W" * 7 + "W" * 5 + " " * 6 + "W" * 12)
    print(" " * 21 + "W" * 7 + "W" * 3 + " " * 8 + "W" * 10)

# code lock for chest

def main():
    while True:
        print(" ")
        CodeLock1 = input ("Enter Code 1: ")
        CodeLock2 = input ("Enter Code 2: ")

        if CodeLock1 == "492" and CodeLock2 == "815":
            print(" ")
            print ("Those codes worked! You have won the game! ")
            print(" ")
            win()
            sys.exit()

        else:
            print ("Password did not match!")
            break

    

###################################################################
# Start the game
inventory = [] # nothing in the inventory
createRoom()


# play until the player dies or asks to quit
while True:

    # set status
    status = "{} \n You are carrying: {}\n".format(currentRoom, inventory)
    # check for death
    if currentRoom == None:
        status = "You are dead"
    # provide status update
    print("===========================================================================")
    print(status)

    if currentRoom == None:
        death()
        break
    
    # add user input suport
    action = input("What to do? ")
    action = action.lower()
    if (action == "quit" or action == "exit" or action == "bye"):
        break
    
    # parse player's input for verb/noun format
    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take."
    words = action.split()

    if len(words) == 2:
        verb = words[0]
        noun = words[1]
    
        # support for verb go
        if verb == "go":
            response = "Invalid exit."
            for i in range(len(currentRoom.exits)):
                if noun == currentRoom.exits[i]:
                    currentRoom = currentRoom.exitLocations[i]
                    response = "Room changed."
                    break
                
        # support for verb look
        elif verb == "look":
            response = "I don't see that item."
            for i in range(len(currentRoom.items)):
                if noun == currentRoom.items[i]:
                    response = currentRoom.itemDescriptions[i]
                    break
                    
        # support for verb take
        elif verb == "take":
            response = "I don't see that item."
            for grabbable in currentRoom.grabbables:
                if noun == grabbable:
                    inventory.append(grabbable)
                    currentRoom.delGrabbables(grabbable)
                    response = "Item grabbed."
                    break

        # support for phrase inspect key 
        elif verb == "inspect":
            response = "I can't inspect this item."
            for i in range(len(currentRoom.items)):
                if noun == "key":
                    key()
                    response = "There is something on this item."
                    break
                if noun == "book":
                    book()
                    response = "There is something on this item."
                    break

        # Code Locks for the chest
        elif verb == "open":
            response = "I can't inspect this item."
            for i in range(len(currentRoom.items)):
                if noun == "chest":
                    response = "There is two locks that need to be opened."
                    main()
                    break
                
                
    # display the response
    print("\n{}".format(response))
        
    
