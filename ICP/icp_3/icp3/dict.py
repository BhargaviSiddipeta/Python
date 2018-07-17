
str=input('Enter any sentence of your choice \n')
# read input from the user
print(str)
# iterate through the sentence to find the count of each word
def word_count(str):
    counts = dict()
    words = str.split()
    words.sort()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count(str))
