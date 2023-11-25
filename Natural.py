NLP
import nltk
nltk.download('punkt')#Tokenizing
from nltk.tokenize import *
text="""A newspaper is the strongest medium for news. People are reading newspapersfordecades.Ithasahugecontributionto globalization.Rightnowbecauseofeasy
internet connection, people don’t read printed newspapers often. They read the onlineversion."""
print("Sample text : \n ",text,"\n")sent_tokenized=sent_tokenize(text)
print("Tokenizing by sentence : \n",sent_tokenized,"\n")word_tokenized=word_tokenize(text)
print("Tokenizing by word : \n ",word_tokenized,"\n")
