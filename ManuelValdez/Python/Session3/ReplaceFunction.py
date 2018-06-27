def replace(text, old, new):
    return new.join(text.split(old))


print(replace("this is a text to test replace function", "i", "I"))
print(replace("Mississippi", "i", "I"))
print(replace("spom", "om", "xxxx"))
print(replace("favorite", "o", "a"))
