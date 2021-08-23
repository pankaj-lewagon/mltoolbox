from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stopwords(text, lang='english'):
    stop_words = set(stopwords.words(lang))

    word_tokens = word_tokenize(text)

    text = [w for w in word_tokens if not w in stop_words]
    return text


def lemmastizer_text(text):

    lemmatizer = WordNetLemmatizer()

    text = ' '.join([lemmatizer.lemmatize(word) for word in text])

    return text
