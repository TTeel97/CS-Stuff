name = input("Type your name: ")
print("Welcome", name, "to this new adventure!")

answer = input(
    "You are on a long dirt road, but it has come to an end. You have two choices ahead you can go left or right. Which way do you go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can choose to swim across or try to walk around it. Type Swim or walk to choose ")

    if answer == "swim":
        print("You channeled your inner Michael Phelps and decided to swim, however you were eaten by a hippo. You lose")
    
    elif answer == "walk":
        print("You chose the safe route and decided to walk across, but then you fell and hit your head and died. You lose.")
        
elif answer == "right":
    decision = input("You come to an old creaky and wobbly bridge. It is missing planks. Do you attempt to cross it or do you backtrack? (cross/back) ").lower()
    if decision == "cross":
            sword_decision = input(
            "Going very slowly you decide to cross the bridge. Each plank creaking as you step on it. Somehow you make it across. You notice a sword laying on the ground. Do you pick it up, or leave it? (yes/no) ").lower()
            if sword_decision == "yes":
                    speak_decision = input("You pick up the sword. Ahead you notice someone standing in front of you. He looks angry. Do you speak to him? (yes/no) ").lower()
                    if speak_decision == "yes":
                        print("The man accuses you of stealing his family sword you hold in your hand. You give it back to him and he rewards you with a bag of gold and a ride home. It pays to be kind! You win!")
                    elif speak_decision == "no":
                        attack = input("The man accuses you of stealing his family sword held in your hand. Giving him the silent treatment angers him and he lunges toward you. Do you go on the offense or stay defensive? (offensive/defensive) ").lower()
                        if attack == "offensive":
                            mercy = input("You dodge the mans strike and the man quickly finds your blade at his neck. He begins to beg for mercy, but you cannot help but notice a large sack of valuables within his belongings. Do you grant the stranger mercy? (yes/no) ").lower()
                            if mercy == "yes":
                                print("The man thanks you. As a show of his gratitude he gives you the pack of valuables you saw in exchange for his life. Beyond him you see the One Piece. YOU WIN!")
                            elif mercy == "no":
                                print("You strike the man down in cold blood, leaving no valuables to rot with him. Inside his pack you locate the One Piece. YOU WIN!!....but at what cost..")
                            else:
                                print("That wasnt an option. You lose.")

                        elif attack == "defensive":
                            print("You dodge his strike and take a step back, however your lack of perception leads you to trip over your own feet. The man kills you. You lose.")
                        else:
                            print("That wasnt an option. You lose....again")
                    else:
                        print("That wasn't an option. You tripped and fell on your sword. You lose")    
            elif sword_decision == "no":
                    speak_decision2 = input("You decide not to take the sword. Ahead you notice someone standing in front of you. He looks upset. Do you speak to him? (yes/no) ").lower()
                    if speak_decision2 == "no":
                        print("The man takes offense to you ignoring him. He throws a grenade at you. You lose")
                    elif speak_decision2 == "yes":
                        print("The man accuses you of stealing his family sword. Likely the one you chose not to take, and because you didn't the man strikes you down with no issue. You lose")
            else:
                print("That isnt an option. You lose")
    elif decision == "back":
            print("There is no honor in being a coward. You attempted to backtrack but got lost and perished from hypothermia. You lose.")
    else:
            print("That wasn't an option. Your indecisiveness caused a stroke. You lose")
else:
    print("Not a valid option. You contracted listeria and died")