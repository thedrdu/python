def start():
    print "Welcome to 'Kingdom of Code', a text adventure!"
    print "You wake up in a cabin. There is a door and a large stick on the wall. What would you like to do?"
    print "Options: 'Take stick' or 'leave'"

    x = raw_input('What would you like to do?')
    if x.lower() != "take stick":
        print "You are about to leave, but you realize that a stick would probably come in handy."
        print "Options: 'Take stick'"
        x = raw_input("What would you like to do?")

    elif x.lower() != "leave":
        print "You grab the large stick. It's pretty hard to hold."
        print "Options: 'leave'"
        x = raw_input("What would you like to do?")

        if x.lower() == "leave":
            print "You see a forest and 2 paths. One is muddy and the other has thick trees."
            print "Options: 'Muddy path' or 'Woody path'"
            x = raw_input("What would you like to do?")

            if x.lower() != "woody path":
                print "You head down the muddy path, and encounter a beaver living nearby! It is angry!"
                print "Options: 'Fight' or 'Run'"
                x = raw_input("What would you like to do?")

                if x.lower() == "run":
                    print "You run away from the beaver; it has sharp teeth!"
                    x = raw_input("What would you like to do?")

                elif x.lower() == "fight":
                    print "You swing your stick around, and the beaver scurries off."
                    print "There is an arrow on the ground, and a distant castle. You pick the arrow up, and walk up to the walls."
                    print "Many guards stop you, and say that you cannot pass until you prove you have the skills of a warrior."
                    print "Options: 'Go back' or 'Fight guards'"
                    x = raw_input("What would you like to do?")

                    if x.lower() == "fight guards":
                        print "You hold the stick like a sword and swing it at the guards. They leap back and shout, \"What are you doing?\""
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

while start():
    pass
