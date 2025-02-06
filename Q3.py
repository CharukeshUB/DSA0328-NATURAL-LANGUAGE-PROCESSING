import nltk
nltk.download('punkt')
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Sample text
text = "The cats are running faster than the dogs. He studies hard for his exams."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stemming using Porter Stemmer
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]
print("Stemmed Words:", stemmed_words)

# Lemmatization using WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, pos="v") for word in tokens]  # 'v' for verb
print("Lemmatized Words:", lemmatized_words)
