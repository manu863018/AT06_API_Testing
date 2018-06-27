def extractURL(text):
    if ("http://" not in text): return text
    firstText = text[text.find("http://") : len(text)]
    if (" " not in firstText): return firstText
    return firstText[0 : firstText.find(" ")]


print(extractURL("this is an example of an http://someurl.com as a new url"))
print(extractURL("this is an example of an http://someurl.com"))
print(extractURL("http://someurl.com is a new url"))
print(extractURL("http://someurl.com "))
print(extractURL("ttp://someurl.com "))
print(extractURL("some text"))