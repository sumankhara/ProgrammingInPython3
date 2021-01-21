import random

articles = ["the", "a", "an"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped"]
adverbs = ["loudly", "quietly", "well", "badly"]

for _ in (1, 2, 3, 4, 5):
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)

    sentence_structure = random.randint(0, 1)
    if sentence_structure:
        print(article, subject, verb, adverb)
    else:
        print(article, subject, verb)