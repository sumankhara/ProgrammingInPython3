import random
import sys

articles = ["the", "a"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped"]
adverbs = ["loudly", "quietly", "well", "badly"]
loop = 5

if len(sys.argv) >= 2:
    try:
        if 1 <= int(sys.argv[1]) <= 10:
            loop = int(sys.argv[1])
    except ValueError as error:
        print(error)

while True:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)

    sentence_structure = random.randint(0, 1)
    if sentence_structure:
        print(article, subject, verb, adverb)
    else:
        print(article, subject, verb)

    loop -= 1
    if loop <= 0:
        break
