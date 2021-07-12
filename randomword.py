# Imports Requests, the library needed to get the wordlist.
import requests
# Imports BetterProfanity, the library used to filter out profanity.
from better_profanity import profanity
# Imports Random (Quite obvious, it's used to get a random word!)
import random


# Sets the link for the wordlist used.
link = "http://www.mieliestronk.com/corncob_lowercase.txt"

# Makes a request to the link above and registers it's text as a variable.
RequestText = requests.get(link).text

# Makes a list called WordList for us to use.
WordList = []

# Sets the list to have a new item for every word (Words are stored in new lines, so we split the text for each new line).
WordList = RequestText.split("\n")

# Sets the RandomWord variable to a random item in the list WordList.any
RandomWord = random.choice(WordList)

# Now that we have our word, it's time to make sure it doesn't contain profanity!

# Loads default censor words from the profanity package.
profanity.load_censor_words()

# Censors our random word and places the newly censored word in the RandomWord variable.
RandomWord = profanity.censor(RandomWord)

# Prints your new, censored random word!
print(RandomWord)