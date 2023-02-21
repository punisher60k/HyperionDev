#***

import spacy

'''
en_core_web_sm is a smaller model and contains no word vectors. Using this instead of "en_core_web_md" gives wildly different comparison results in all 3 exercises.
For example, exercise 1 gives the comparison between a monkey and banana as the highest while cat and monkey are the lowest.

In exercise 3, while the most similar sentence is still "Hello, there is my car", confidence in the results generally is much lower.
'''
nlp = spacy.load('en_core_web_md')
print("Example 1:\n")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
Out from above print statements:

0.5929930274321619 
0.40415016164997786
0.22358825939615987

It is interesting to note that spacy considers the similarity between a cat and monkey stronger than other comparisons.

It can be argued that a monkey is more synonymous with a banana, given their depictions is popular stories/imagery, than a cat. Therefore, it would appear the strength in relationship as being animals is given more weighting than food sources.

While not unsurprising, cat and banana appear quite dissimilar. While both could be considered food depending on the world location, this data source spacy is pulling from is likely western in origin.
Consequently, western based cultures would find the idea of eating cat abhorrent. It would be an interesting exercise if whatever data source was from a South Korea.
'''

print("Example 2:\n")

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("Example 3:\n")

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go", 
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)