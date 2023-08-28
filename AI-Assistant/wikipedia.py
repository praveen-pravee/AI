# Wiki
import wikipedia

search = str(input("Wiki : "))
result = wikipedia.summary(query, sentences = 3)
print(result)

"""
It's works butI got some errors 
search = wikipedia.search('')
page = wikipedia.page('')
summary = wikipedia.summary('')
reference, title
"""
