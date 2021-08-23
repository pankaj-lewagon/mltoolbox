from mltoolbox.clean_data import remove_num,remove_punctuation,lowercase
import string
import re

def test_remove_punctuation():
    text=remove_punctuation("hello's my name isn't pankaj!!! What, youe name??")
    text=text.replace(
        " ",
        "",
    )
    assert text.isalnum() == True


def test_lowercase():

    text=lowercase("AAVBBCCDDWEEFF")
    assert text.islower() == True

def test_remove_num():
    text=remove_num("hello's I am 21 years old in 2024")
    assert bool(re.search('\d',text)) != True
