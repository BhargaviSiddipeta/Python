
inputString = str(input("Please type a sentence: "))
#map  Applies function to every item of iterable and return a list of the results
print(*map(inputString.lower().count, "aeiou"))
vowels=0
for i in inputString:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)


def vowel_count(str):
    # Intializing count variable to 0
    count = 0

    # Creating a set of vowels
    vowel = set("aeiouAEIOU")

    # Loop to traverse the alphabet
    # in the given string
    for alphabet in str:

        # If alphabet is present
        # in set vowel
        if alphabet in vowel:
            count = count + 1

    print("No. of vowels :", count)


# Driver code
str = inputString

# Function Call
vowel_count(str)
