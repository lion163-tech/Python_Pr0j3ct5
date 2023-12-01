#Original work, not seen b4
#Match simulator Manchester United vs Chelsea
#variables
timer = 0
def Start_match():
    mu_squad = ["De Gea,", "Diogo Dalot,", "Raphael Varane,", "Lisandro Martinez,", "Luke Shaw,", "Casemiro,", "Bruno Fernandes,","Kobby Mainoo,", "Marcus Rashford,", "Jadon Sancho,", "Wout Werghost"]
    ch_squad = ["Kepa Arrizabalaga,", "Thiago Silva,", ","]
    print("It's matchday at Old Trafford.Two rivals face off in the most bitterest game in Football's history;Manchester United face Chelsea")
    print("****")
    print("Here is the home side's line-up")
    print(mu_squad)
    print("The away side have chosen this line-up")
    print(ch_squad)
    print("****")
#Time for the real thing
def in_game():
    print("And we're off, this should be very entertaining")
    while timer < 90:
        return timer + 1
    player_choice = int(input())
    if timer == 21:
        print("Now here's a chance for United to strike from a counter")
        print("Choose:1.go on with the attack 2. wait for 5 of your players to go in")
        return player_choice
    if player_choice == 1:
        print("Oof, that's a bad despaerate tackle on the player by Chelsea, Free-kick from 40 yards out")
    else:
        print('And Chelsea have handled that chance by United well')
print(Start_match())
