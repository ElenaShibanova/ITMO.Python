from moduleLab5 import inputName, gameDice, winner

namePlayer1 = inputName(1)
namePlayer2 = inputName(2)
summPointsPlayers = gameDice(namePlayer1, namePlayer2)
winner (namePlayer1, namePlayer2, summPointsPlayers[0],summPointsPlayers[1])