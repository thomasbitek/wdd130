"""
#CSE 110: Text-Based Adventure Game
#TITLE: THOMAS BITEK THE ALIEN KILLER
#CREATIVITY ADDITIONS: Action-focused sci-fi thriller with tactical choices,
#weapon selection, stealth or brute force approaches, multiple endings including a 
#secret heroic sacrifice ending.
"""

print("=" * 60)
print("WELCOME TO: THOMAS BITEK - THE ALIEN KILLER")
print("=" * 60)
print()
print("Colonial outpost Vega-9 is under siege. Alien creatures swarm the perimeter.")
print("You are Thomas Bitek, a veteran hunter with a reputation for getting the job done.")
print("A distress beacon blares; command says hold the line until extraction.")
print()

choice1 = input("Do you GRAB a RIFLE, a SHOTGUN, or a SNIPER rifle? ").strip().upper()

if choice1 == "RIFLE":
    print()
    print("You shoulder a reliable assault rifle with a steady rate of fire.")
    print("Your squadmates nod; you'll need to cover the main corridor.")
    print()

    choice2 = input("Do you TAKE point, COVER the rear, or SCOUT ahead? ").strip().upper()

    if choice2 == "TAKE":
        print()
        print("You lead the squad into the corridor. Aliens pour out of vents.")
        print("You lay down suppression fire, buying time for the others.")
        print()

        choice3 = input("Do you THROW a grenade, AIM for the swarm, or FALL back? ").strip().upper()

        if choice3 == "THROW":
            print()
            print("The grenade obliterates a nest. You clear a path to the comm tower.")
            print()
            choice4 = input("Do you CLIMB the tower or RETRIEVE wounded? ").strip().upper()

            if choice4 == "CLIMB":
                print()
                print("From the tower, you call in orbital strikes. The outpost is saved.")
                print()
                print("★ VICTORY! You became a legend.")
                print()
            else:
                print()
                print("You attempt to retrieve the wounded but are ambushed. The squad is lost.")
                print()
                print("✗ DEFEAT. Your bravery was noble but fatal.")
                print()

        elif choice3 == "AIM":
            print()
            print("Your precision drops the swarm, but more are coming.")
            print()
            print("You hold until extraction arrives. You're celebrated for discipline.")
            print()
            print("✓ SURVIVAL. You lived to fight another day.")
            print()

        else:
            print()
            print("You fall back and regroup, but the aliens overrun the corridor.")
            print()
            print("✗ DEFEAT. Retreat led to collapse.")
            print()

    elif choice2 == "COVER":
        print()
        print("You watch the rear. A breach opens behind you; a lone alien slips through.")
        print()
        choice3 = input("Do you AMBUSH it, SET a trap, or IGNORE and focus forward? ").strip().upper()

        if choice3 == "AMBUSH":
            print()
            print("You take it down silently. Your squad doesn't even notice the threat.")
            print()
            print("✓ SURVIVAL. Stealth kept the team alive.")
            print()
        elif choice3 == "SET":
            print()
            print("The trap triggers but also alerts nearby aliens. A swarm overwhelms you.")
            print()
            print("✗ DEFEAT. The trap backfired.")
            print()
        else:
            print()
            print("You ignore it; later, the alien returns with reinforcements.")
            print()
            print("✗ DEFEAT. Neglect had consequences.")
            print()

    else:
        print()
        print("You scout ahead and find the alien queen's lair entrance.")
        print()
        choice3 = input("Do you STEALTH to plant charges or RUSH in guns blazing? ").strip().upper()

        if choice3 == "STEALTH":
            print()
            print("You plant charges and slip away unseen. The explosion collapses the lair.")
            print()
            print("★ VICTORY! You crippled the hive without losing your team.")
            print()
        else:
            print()
            print("Guns blazing drew too much attention. The queen awoke and retaliated.")
            print()
            print("✗ DEFEAT. Recklessness ended the mission.")
            print()

elif choice1 == "SHOTGUN":
    print()
    print("You equip a shotgun—devastating at close range but heavy.")
    print("You're assigned to the storage bay where breaches are likely.")
    print()

    choice2 = input("Do you BARRICADE the door, AMBUSH nearby, or SEARCH for supplies? ").strip().upper()

    if choice2 == "BARRICADE":
        print()
        print("You fortify the door with crates. Aliens batter it but cannot break through.")
        print()
        print("You hold until reinforcements arrive. The outpost stands.")
        print()
        print("✓ SURVIVAL. Defense worked as planned.")
        print()

    elif choice2 == "AMBUSH":
        print()
        print("You lure aliens into kill zones. Your shotgun tears through them.")
        print()
        print("However, the ammo runs low and you must make a hard choice.")
        print()
        choice3 = input("Do you SEND a messenger for ammo or CONSERVE shells? ").strip().upper()

        if choice3 == "SEND":
            print()
            print("The messenger is lost, but you get enough ammo to continue the fight.")
            print()
            print("✓ SURVIVAL. Risk brought reward.")
            print()
        else:
            print()
            print("Conserving was wise, but eventually the aliens push through.")
            print()
            print("✗ DEFEAT. Resource scarcity doomed you.")
            print()

    else:
        print()
        print("You search for supplies and discover an alien artifact humming softly.")
        print()
        choice3 = input("Do you ACTIVATE it, STUDY it, or DESTROY it? ").strip().upper()

        if choice3 == "ACTIVATE":
            print()
            print("It grants you temporary enhanced vision and strength.")
            print("With it, you lead a counterattack and win the day.")
            print()
            print("★ VICTORY! The artifact turned the tide.")
            print()
        elif choice3 == "STUDY":
            print()
            print("You are fascinated but the artifact floods your mind with alien thoughts.")
            print()
            print("✗ DEFEAT. Curiosity became possession.")
            print()
        else:
            print()
            print("You destroy it, but doing so releases a pulse that enrages nearby aliens.")
            print()
            print("✗ DEFEAT. Destruction had costs.")
            print()

else:
    print()
    print("You choose the SNIPER rifle, preferring distance and precision.")
    print("You're placed on the outer rampart to pick off threats.")
    print()

    choice2 = input("Do you HOLD position, RELOCATE for a better angle, or AIM for the commander? ").strip().upper()

    if choice2 == "HOLD":
        print()
        print("From your perch you pick off charging aliens expertly.")
        print("An incoming dropship signals extraction within the hour.")
        print()
        print("✓ SURVIVAL. Patience paid off.")
        print()

    elif choice2 == "RELOCATE":
        print()
        print("You move to a new vantage and spot a hidden cloaked alien flanker.")
        print("You take it down, saving the entire extraction group.")
        print()
        print("★ VICTORY! Your movement saved many lives.")
        print()

    else:
        print()
        print("You aim for the alien commander. Your shot hits true and cripples its command link.")
        print("The hive falls into chaos and retreats.")
        print()
        print("★ VICTORY! Targeted precision won the battle.")
        print()

# Secret ending trigger: special input path
print()
secret = input("Type `SACRIFICE` to trigger a secret ending, or press Enter to finish: ").strip().upper()
if secret == "SACRIFICE":
    print()
    print("You manually override the outpost's reactor to create a localized implosion.")
    print("The blast kills you but destroys the hive. Your name becomes legend.")
    print()
    print("★ HEROIC SACRIFICE! You saved countless lives at the cost of your own. ★")
    print()

print()
print("=" * 60)
print("THANKS FOR PLAYING: THOMAS BITEK - THE ALIEN KILLER")
print("=" * 60)
