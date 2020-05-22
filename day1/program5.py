player1_run = int(input("enter the run scored by player 1 in 60 balls: "))
player2_run = int(input("enter the run scored by player 2 in 60 balls: "))
player3_run = int(input("enter the run scored by player 3 in 60 balls: "))
strikerate1 = player1_run * 100 / 60
strikerate2 = player2_run * 100 / 60
strikerate3 = player3_run * 100 / 60
print("strikerate of player 1 is", strikerate1)
print("strikerate of player 2 is", strikerate2)
print("strikerate of player 3 is", strikerate3)
print("run scored by player 1 if they played 60 more balls is", player1_run * 2)
print("run scored by player 2 if they played 60 more balls is", player2_run * 2)
print("run scored by player 3 if they played 60 more balls is", player3_run * 2)
print("maximum number of sixes player 1 could hit =", player1_run // 6)
print("maximum number of sixes player 2 could hit =", player2_run // 6)
print("maximum number of sixes player 3 could hit =", player3_run // 6)


