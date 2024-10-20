def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are two paths ahead.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    print("3. Look around.")
    
    choice = input("Which action will you take? (1/2/3): ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    elif choice == "3":
        look_around()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        start_game()
        
def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are two paths ahead.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    print("3. Look around.")
    
    choice = input("Which action will you take? (1/2/3): ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    elif choice == "3":
        look_around()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        start_game()

def left_path():
    print("\nYou take the left path and walk for a while. The forest is dense, and the air is thick with mist.")
    print("1. Continue walking forward.")
    print("2. Stop and listen to your surroundings.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        print("\nYou continue walking forward, but the mist grows thicker.")
        print("Suddenly, you stumble upon an old, abandoned cabin.")
        print("1. Enter the cabin.")
        print("2. Walk around the cabin.")
        
        choice = input("What will you do? (1/2): ")
        
        if choice == "1":
            enter_cabin()
        elif choice == "2":
            walk_around_cabin()
        else:
            print("Invalid choice. Please choose 1 or 2.")
            left_path()
    
    elif choice == "2":
        print("\nYou stop and listen carefully. The forest is eerily quiet, except for a faint rustling in the bushes.")
        print("1. Investigate the bushes.")
        print("2. Continue on the path.")
        
        choice = input("What will you do? (1/2): ")
        
        if choice == "1":
            investigate_bushes()
        elif choice == "2":
            continue_on_path()
        else:
            print("Invalid choice. Please choose 1 or 2.")
            left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        left_path()

def enter_cabin():
    print("\nYou cautiously enter the cabin. The air inside is cold and stale.")
    print("You see a dusty table with an old, tattered book on it.")
    print("1. Read the book.")
    print("2. Leave the cabin.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        read_book()
    elif choice == "2":
        print("\nYou leave the cabin and continue your journey on the path.")
        left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        enter_cabin()

def read_book():
    print("\nYou open the book and begin to read. The pages are filled with strange symbols and illustrations.")
    print("Suddenly, you feel a cold breeze, and the symbols start glowing.")
    print("1. Continue reading.")
    print("2. Close the book and leave the cabin.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        print("\nAs you continue reading, the symbols lift off the page and swirl around you.")
        print("You feel a surge of energy as the book's magic infuses you.")
        print("You have gained a new magical ability!")
        # Continue the adventure with new abilities
    elif choice == "2":
        print("\nYou quickly close the book and leave the cabin.")
        left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        read_book()

def walk_around_cabin():
    print("\nYou walk around the cabin and find an old well behind it.")
    print("The well is covered in moss, and a faint glow emanates from within.")
    print("1. Look inside the well.")
    print("2. Ignore the well and return to the path.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        look_inside_well()
    elif choice == "2":
        print("\nYou ignore the well and return to the path.")
        left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        walk_around_cabin()

def look_inside_well():
    print("\nYou peer into the well and see something shimmering at the bottom.")
    print("1. Climb down the well.")
    print("2. Throw a rock into the well.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        climb_down_well()
    elif choice == "2":
        print("\nYou throw a rock into the well. The rock hits the bottom with a splash, but nothing else happens.")
        left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        look_inside_well()

def climb_down_well():
    print("\nYou carefully climb down the well, using the old, slippery stones as handholds.")
    print("At the bottom, you find a glowing crystal embedded in the wall.")
    print("1. Take the crystal.")
    print("2. Leave the crystal and climb back up.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        print("\nYou take the crystal, and as you do, the well begins to shake.")
        print("You quickly climb back up and escape just as the well collapses.")
        print("You have gained a mysterious glowing crystal!")
        # Continue the adventure with the crystal
    elif choice == "2":
        print("\nYou decide to leave the crystal and climb back up the well.")
        left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        climb_down_well()

def investigate_bushes():
    print("\nYou approach the bushes cautiously and see a small creature scurrying away.")
    print("1. Chase after the creature.")
    print("2. Return to the path.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        chase_creature()
    elif choice == "2":
        print("\nYou decide not to pursue the creature and return to the path.")
        left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        investigate_bushes()

def chase_creature():
    print("\nYou chase after the creature and follow it into a hidden clearing.")
    print("In the clearing, you find an ancient stone altar with strange markings.")
    print("1. Investigate the altar.")
    print("2. Leave the clearing and return to the path.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        investigate_altar()
    elif choice == "2":
        print("\nYou decide to leave the clearing and return to the path.")
        left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        chase_creature()

def investigate_altar():
    print("\nYou approach the altar and notice that one of the markings resembles a handprint.")
    print("1. Place your hand on the handprint.")
    print("2. Step back and observe.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        place_hand_on_altar()
    elif choice == "2":
        print("\nYou decide to observe the altar from a distance, but nothing happens.")
        left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        investigate_altar()

def place_hand_on_altar():
    print("\nYou place your hand on the handprint, and the markings on the altar begin to glow.")
    print("A portal opens up in front of you, leading to an unknown realm.")
    print("1. Step through the portal.")
    print("2. Step back and close the portal.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        enter_portal()
    elif choice == "2":
        print("\nYou step back, and the portal closes, leaving you in the clearing.")
        left_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        place_hand_on_altar()

def enter_portal():
    print("\nYou step through the portal and find yourself in a mysterious, glowing cave filled with ancient treasures.")
    print("You have discovered a hidden realm with endless possibilities!")


def continue_on_path():
    print("\nYou decide to continue walking along the path, leaving the rustling bushes behind.")
    print("The mist starts to clear, and you find yourself in a serene, sunlit grove.")
    print("In the center of the grove, there is a large, ancient tree with golden leaves.")
    print("1. Approach the tree.")
    print("2. Sit down and rest by the tree.")
    print("3. Explore the grove.")

    choice = input("What will you do? (1/2/3): ")
    
    if choice == "1":
        approach_tree()
    elif choice == "2":
        rest_by_tree()
    elif choice == "3":
        explore_grove()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        continue_on_path()

def approach_tree():
    print("\nYou walk up to the ancient tree and notice that the bark is covered in strange, glowing runes.")
    print("The tree seems to hum with energy, and you feel a strong connection to it.")
    print("1. Touch the tree.")
    print("2. Step back and observe the tree.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        print("\nAs you touch the tree, a warm energy flows through you.")
        print("You feel your strength and vitality increase. The tree has blessed you with its ancient power!")
        # The player gains a permanent stat boost or ability.
    elif choice == "2":
        print("\nYou decide to observe the tree from a distance. The glowing runes tell a story of an ancient civilization.")
        print("You gain knowledge about the history of this land.")
        # The player gains lore knowledge or insight.
    else:
        print("Invalid choice. Please choose 1 or 2.")
        approach_tree()

def rest_by_tree():
    print("\nYou sit down and rest by the tree, feeling a deep sense of peace and calm.")
    print("As you relax, you hear the gentle rustling of the leaves and feel a refreshing breeze.")
    print("You fall into a deep, restorative sleep and wake up feeling rejuvenated.")
    print("Your health and energy are fully restored!")
    # The player recovers health and energy, allowing for continued exploration.

def explore_grove():
    print("\nYou decide to explore the grove further and discover a hidden pond behind the ancient tree.")
    print("The water in the pond is crystal clear, and you can see your reflection perfectly.")
    print("1. Drink from the pond.")
    print("2. Throw a stone into the pond.")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        print("\nYou drink from the pond and feel a surge of energy flow through your body.")
        print("The water has magical properties, and you feel stronger and more alert.")
        # The player gains a temporary boost to strength or alertness.
    elif choice == "2":
        print("\nYou throw a stone into the pond, and the water ripples gently.")
        print("As the ripples fade, you notice something shimmering at the bottom of the pond.")
        print("You reach into the water and pull out a small, glowing gemstone.")
        # The player finds a magical item or key.
    else:
        print("Invalid choice. Please choose 1 or 2.")
        explore_grove()


def right_path():
    print("\nYou chose to take the right path. The forest seems darker here.")
    print("As you walk further, the trees become denser, and you start to hear strange noises.")
    print("1. Continue walking cautiously.")
    print("2. Try to find the source of the noises.")
    print("3. Turn back to the starting point.")

    choice = input("What will you do? (1/2/3): ")

    if choice == "1":
        print("\nYou decide to continue walking cautiously. The path gets narrower, and the noises grow louder.")
        print("Suddenly, you stumble upon a hidden cave entrance, covered by thick vines.")
        print("1. Enter the cave.")
        print("2. Ignore the cave and continue on the path.")
        
        choice = input("What will you do? (1/2): ")

        if choice == "1":
            print("\nYou carefully enter the cave. It's dark and damp, but you see a faint light deeper inside.")
            print("As you move towards the light, you find an ancient chest.")
            print("1. Open the chest.")
            print("2. Leave the chest and explore deeper into the cave.")

            choice = input("What will you do? (1/2): ")

            if choice == "1":
                print("\nYou open the chest and find a mystical artifact that glows with an otherworldly light.")
                print("The artifact grants you a special ability to communicate with the forest creatures.")
                print("1. Use the artifact to communicate with the forest creatures.")
                print("2. Keep the artifact and leave the cave.")

                choice = input("What will you do? (1/2): ")

                if choice == "1":
                    print("\nYou use the artifact to communicate with the forest creatures.")
                    print("They tell you of a hidden treasure deep within the forest and guide you to it.")
                    print("You follow their directions and eventually find the treasure, becoming a legendary explorer!")
                elif choice == "2":
                    print("\nYou decide to keep the artifact and leave the cave.")
                    print("As you step out, you notice the forest seems to recognize your presence.")
                    print("You continue your journey with the newfound power, unlocking the secrets of the forest.")

            elif choice == "2":
                print("\nYou decide to leave the chest and explore deeper into the cave.")
                print("As you venture further, you find a hidden passage that leads you out of the cave.")
                print("The passage opens into a hidden valley, untouched by time.")
                print("1. Explore the valley.")
                print("2. Mark the location and return to the forest.")

                choice = input("What will you do? (1/2): ")

                if choice == "1":
                    print("\nYou decide to explore the valley. It's filled with rare plants and animals.")
                    print("You discover ancient ruins that tell the story of a lost civilization.")
                    print("You document your findings and become famous for your discovery.")
                elif choice == "2":
                    print("\nYou decide to mark the location and return to the forest.")
                    print("You plan to return later with more resources to fully explore the valley.")
                    print("As you leave, you feel a sense of accomplishment and anticipation for future adventures.")

        elif choice == "2":
            print("\nYou ignore the cave and continue on the path.")
            print("The path eventually leads you to a clearing where you find an abandoned campsite.")
            print("1. Investigate the campsite.")
            print("2. Set up your own camp for the night.")

            choice = input("What will you do? (1/2): ")

            if choice == "1":
                print("\nYou investigate the campsite and find clues that suggest someone was here recently.")
                print("You decide to follow the trail left behind, hoping to find the previous campers.")
                print("After a few hours, you find a group of explorers who got lost in the forest.")
                print("You help them find their way out, and they reward you with valuable supplies.")
            elif choice == "2":
                print("\nYou decide to set up your own camp for the night.")
                print("As you rest, you hear rustling in the bushes.")
                print("You prepare yourself for an encounter, but it turns out to be a friendly forest creature.")
                print("The creature shares food with you, and you spend a peaceful night in the forest.")

    elif choice == "2":
        print("\nYou decide to find the source of the noises.")
        print("You carefully move towards the sound and discover a group of bandits hiding in the forest.")
        print("1. Confront the bandits.")
        print("2. Avoid them and continue on the path.")

        choice = input("What will you do? (1/2): ")

        if choice == "1":
            print("\nYou bravely confront the bandits, demanding to know their intentions.")
            print("They initially threaten you, but you manage to outsmart them and convince them to leave the forest.")
            print("The forest becomes safer because of your actions, and you are hailed as a hero.")
        elif choice == "2":
            print("\nYou decide to avoid the bandits and continue on the path.")
            print("You eventually reach a peaceful clearing where you can rest and reflect on your journey.")
            print("The forest seems less menacing now, and you feel a sense of calm.")

    elif choice == "3":
        print("\nYou decide to turn back to the starting point.")
        print("The forest is dense, but you manage to retrace your steps.")
        print("You return safely, but the mystery of the right path lingers in your mind.")
        print("Perhaps one day you'll return to uncover its secrets.")


def look_around():
    print("\nYou decide to look around before choosing a path.")
    print("The forest is quiet, with only the sound of rustling leaves.")
    print("As you examine your surroundings, you notice a few interesting things:")
    print("1. A strange marking on a nearby tree.")
    print("2. A glint of something shiny partially buried in the ground.")
    print("3. A faint trail of smoke rising in the distance.")
    
    choice = input("Which one will you investigate? (1/2/3): ")

    if choice == "1":
        print("\nYou walk over to the tree with the strange marking.")
        print("The marking resembles an ancient symbol, glowing faintly in the dark.")
        print("1. Touch the marking.")
        print("2. Try to decipher the symbol.")
        print("3. Leave the tree and look for other clues.")

        choice = input("What will you do? (1/2/3): ")

        if choice == "1":
            print("\nYou reach out and touch the marking. Suddenly, the forest around you changes.")
            print("You find yourself transported to a different location, a mysterious glade bathed in moonlight.")
            print("1. Explore the glade.")
            print("2. Try to find a way back to the forest.")

            choice = input("What will you do? (1/2): ")

            if choice == "1":
                print("\nYou explore the glade and discover it is a place of ancient power.")
                print("You find a stone altar with an inscription that speaks of a hidden treasure.")
                print("You decide to search for the treasure, knowing it could hold great value.")
            elif choice == "2":
                print("\nYou try to find a way back to the forest, but the glade seems to have no exit.")
                print("As you search, you discover a hidden portal that leads you back to the forest.")
                print("You realize the marking was a gateway to another world, and you vow to return someday.")

        elif choice == "2":
            print("\nYou study the symbol closely and manage to decipher its meaning.")
            print("It appears to be a protective ward, placed here to guard something nearby.")
            print("1. Search the area for what the symbol is guarding.")
            print("2. Leave the area, not wanting to disturb the ancient magic.")

            choice = input("What will you do? (1/2): ")

            if choice == "1":
                print("\nYou search the area and find a hidden trapdoor beneath the tree.")
                print("The trapdoor leads to an underground chamber filled with ancient artifacts.")
                print("You take a valuable artifact and leave, feeling the weight of the ward's protection lift.")
            elif choice == "2":
                print("\nYou decide not to disturb the ancient magic and leave the area.")
                print("As you walk away, you feel a sense of respect for the forest's ancient mysteries.")

        elif choice == "3":
            print("\nYou decide to leave the tree and look for other clues.")
            print("As you walk away, the marking slowly fades, and the forest seems to shift back to normal.")
            print("You continue to explore, wondering what other secrets the forest might hold.")

    elif choice == "2":
        print("\nYou decide to investigate the shiny object partially buried in the ground.")
        print("You dig it out and find a small, intricately designed box.")
        print("The box has a lock, but there is no key in sight.")
        print("1. Try to open the box.")
        print("2. Look for a key nearby.")
        print("3. Keep the box and continue exploring.")

        choice = input("What will you do? (1/2/3): ")

        if choice == "1":
            print("\nYou try to open the box, but it won't budge.")
            print("As you struggle with the lock, the box suddenly opens on its own, revealing a mysterious scroll.")
            print("The scroll contains a map of the forest, with a marked location that seems important.")
            print("You decide to follow the map, hoping it will lead to something valuable.")
        elif choice == "2":
            print("\nYou look around for a key, searching the area thoroughly.")
            print("After a while, you find a small key hidden under a nearby rock.")
            print("You use the key to open the box, revealing a magical amulet inside.")
            print("The amulet glows with a soft light, and you feel its power resonate within you.")
            print("You decide to wear the amulet, knowing it will protect you on your journey.")
        elif choice == "3":
            print("\nYou decide to keep the box and continue exploring.")
            print("As you walk, you notice the box humming softly, as if it contains something alive.")
            print("You feel a connection to the box, wondering what secrets it might reveal later.")

    elif choice == "3":
        print("\nYou decide to investigate the trail of smoke rising in the distance.")
        print("As you approach, you find a small campsite, recently abandoned.")
        print("The fire is still smoldering, and there are footprints leading away from the site.")
        print("1. Follow the footprints.")
        print("2. Search the campsite for clues.")
        print("3. Put out the fire and leave the area.")

        choice = input("What will you do? (1/2/3): ")

        if choice == "1":
            print("\nYou decide to follow the footprints, tracking them through the forest.")
            print("After a short distance, you find a group of travelers who got lost in the woods.")
            print("You help them find their way out, and they reward you with supplies and a map of the forest.")
        elif choice == "2":
            print("\nYou search the campsite for clues and find a journal left behind by the previous campers.")
            print("The journal details their exploration of a hidden cave nearby, rumored to hold great treasure.")
            print("You decide to search for the cave, hoping to find the treasure yourself.")
        elif choice == "3":
            print("\nYou decide to put out the fire and leave the area.")
            print("As you walk away, you notice the forest growing darker, as if something is watching you.")
            print("You quicken your pace, eager to return to the safety of the main path.")


start_game()