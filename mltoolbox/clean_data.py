
import string

def remove_punctuation(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text


def lowercase(text):
    text = text.lower()
    return text


def remove_num(text):
    num_remove = ''.join(word for word in text if not word.isdigit())
    return num_remove
