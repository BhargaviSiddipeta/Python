import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.util import ngrams


f= open("input.txt","w+", encoding="utf-8")

# Assigning link to a variable
myLink = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Opens the URL
getLink=urllib.request.urlopen(myLink)

# Converts to HTML
soup = BeautifulSoup(getLink,  "html.parser")
text1 = soup.get_text()
text2 = soup.h1.text
print("----------Heading--------------")
print(text2)
f.write(soup.get_text())

# Tokenization the text in the URL given
stokens = nltk.sent_tokenize(text2)
wtokens = nltk.word_tokenize(text2)

# Printing Tokenized Sentences
print("-----------------Tokenized sentences--------------------")
for s in stokens:
    print(s)
# Printing Tokenized Words
print("-------------------Tokenized words--------------------------")
for w in wtokens:
    print(w)

# Stemming the text in the URL given
ps = PorterStemmer()
ls = LancasterStemmer()
ss = SnowballStemmer('english')
print("------------------Stemming Output------------------------")
for words in wtokens:
    print("Porter stemming Output: ", ps.stem(words))
    print("Lancaster stemming Output: ",ls.stem(words))
    print("Snowball stemming Output: ", ss.stem(words))


# Lemmatization
lemmatizer = WordNetLemmatizer()
print("----------------Lemmatized Output-------------------")
print(lemmatizer.lemmatize(text2))

# Parts of speech
print("-------------------POS output-------------------")
for w in wtokens:
    mysen = nltk.word_tokenize(text1)
print(nltk.pos_tag(mysen))

# Named Entity Recognition
sentence = text1
print(ne_chunk(pos_tag(word_tokenize(sentence))))

# Trigram ( 3 words as a set)
print('--------------Trigram----------------')
mySentence = "Hi How are you? i am fine and you"
token=nltk.word_tokenize(mySentence)
trigram = ngrams(token,3)
for t in trigram:
    print(t)