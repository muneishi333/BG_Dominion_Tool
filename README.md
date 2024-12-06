# BG_Dominion_Tool

"Dominion" is one of the most popular Game.
This code is an application for Dominion's randomizer.

There are 2 menu in this application. 
 - "ランダマイザー"：Computer randomly selects which card to use for the game
 - "闇市場"：Computer randomly selects 3 cards

Default extension set to use (BG_Dominion_Tool.py 320-424)
(ex) If you want to use "冒険"
 useset.append(30)    #冒険
 usespset.append(20)
 totalC += 30
 totalSC += 20
 for i in range(30):
     usecard.append(0)
 for i in range(20):
     usespcard.append(0)
(ex) If you don't want to use "冒険"
 useset.append(-30)    #冒険
 usespset.append(-20)
 totalC += 30
 totalSC += 20
 for i in range(30):
     usecard.append(-1)
 for i in range(20):
     usespcard.append(-1)
