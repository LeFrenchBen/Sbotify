import math
import statistics

print("\nHey user! Sbotify has for purpose to tell you the probability of \
playing a song of the same album in a shuffled Spotify playlist. \n\

total_songs = int(input("\nEnter the total of your songs:"))

lst = []
num = int(input('Enter a number of albums: '))
for n in range(num):
    numbers = int(input('Enter number of song for each album: '))
    lst.append(numbers)
print("Sum of songs belonging to an album is :", sum(lst))
print(lst)

print("\nLet's find out the songs that don't belong to any album. This will be handy later:")

solo_songs = total_songs - sum(lst)
print(int(solo_songs))

# I'm afraid we need to use... **MATH**

print("Nice! Now we need to find out the probabilities of 2 songs of the same album playing back to back in shuffle mode")

#Each album needs to be considered 1 entity and to that, the solo_songs value needs to be multiplied by itself -1 until 0
#to respect the probability formula.


