
from collections import Counter

'''Develop a program to print 10 most frequently appearing words in a text file.'''

# Open the text file
with open('file.txt', 'r') as file:
    # Read the contents of the file
    contents = file.read()


# Count the frequency of each word
word_counts = Counter(contents.split())

# Get the 10 most frequently appearing words
most_common_words = word_counts.most_common(10)
print(most_common_words)
# Print the most common words
for word, count in most_common_words:
    print(word, count)
