from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re, string


# Lemmatization
lemmatizer = WordNetLemmatizer()
def lemmatize_words(words):
    
    return " ".join([lemmatizer.lemmatize(word) for word in words])


def text_prepare(corpus):
    
    # split into tokens
    sentence_splitted = corpus.split()
    
     # prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation)) # remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in sentence_splitted]
    
    # turn token to lowercase, Remove stop words
    filtered_tokens = [token.lower() for token in tokens if token.lower() not in stopwords.words('english')]
    
    # Lemmatize the filtered tokens
    lemmatized_tokens = lemmatize_words(filtered_tokens)

    # return the filtered tokens
    return lemmatized_tokens
