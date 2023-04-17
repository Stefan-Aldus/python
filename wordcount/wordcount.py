# Promts the user for a sentence
user_sentence = input("Enter your sentence you want to count words from: ")

# Creates a list of numbers
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for x in numbers:
    user_sentence = user_sentence.replace(x, "")

# Strips and trailing whilespaces
stripped_user_sentence = user_sentence.strip()


# Splits the sentence into words
split_user_sentence_whitespace = stripped_user_sentence.split(" ")
wordcount_whitespace = len(split_user_sentence_whitespace)

split_user_sentence_hiphon = stripped_user_sentence.split("-")
wordcount_hiphon = len(split_user_sentence_hiphon)

# Checks the length
wordcount = round(
    (wordcount_hiphon + wordcount_whitespace) - 1)

# Print the result
print("The wordcount in your sentence \"%s\" is: %s" %
      (user_sentence, wordcount))
