import pygame

score = 0

def HighestScore():
    with open("Highest score.txt", "r") as f:
        return f.read()

try:
    highestScore = int(HighestScore())
except:
    highestScore = 0

if(highestScore < score):
    highestScore = score
with open("Highest score.txt", "w") as f:
    f.write(str(highestScore))