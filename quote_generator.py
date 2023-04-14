import random
import pyttsx3


quotes = ["Reality is wrong. Dreams are for real - Tupac Shakur", 
          "I'm living my best life, ain't going back and forth with you - Cardi B",
           "It ain't no fun if the homies can't have none -Snoop Dogg",
          "I believe that everything that you do bad comes back to you  - Nas",
          "I'm not a businessman, I'm a business, man - Jay-Z",
          "I'm the king of the world, on a boat like Leo - The Lonely Island feat. T-Pain",
          "Cause whatever you love can be taken away, so live like it's your dying day - Machine Gun Kelly",
          "The only way to change the world is to make a little noise -Chance The Rapper",
          "Life is a wheel of fortune and it's my turn to spin it - Tupac Shakur",
          "I'm trying to right my wrongs, but it's funny, these same wrongs helped me write this song- J. Cole",
          ]

#print(random.choice(quotes))

engine = pyttsx3.init()
engine.say(random.choice(quotes))
engine.runAndWait()