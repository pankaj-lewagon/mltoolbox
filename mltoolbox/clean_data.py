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


if __name__ == '__main__':
    print remove_num("121212 Pankaj 121212")
    print remove_punctuation("12121?????2 Pank2!!!aj 121212????")
    print lowercase("12121?????2 Pank2!!!aj XXXXXXXXX121212????")
