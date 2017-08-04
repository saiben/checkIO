import unidecode
def checkio(in_string):
    "remove accents"
    print(in_string)
    print(unidecode(in_string).encode("ascii"))

    #return unicodedata.normalize('NFKD', in_string).decode('utf-8')

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio(u"préfèrent") == u"preferent"
    #assert checkio(u"loài trăn lớn") == u"loai tran lon"
    checkio(u"préfèrent")
    print('Done')
