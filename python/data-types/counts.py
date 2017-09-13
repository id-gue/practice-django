"""
run it with:

ipython3 -i counts.py
(close and open ipython aver changes in the file)

%time f1(words)
%timeit f1(words)
"""

# prepare out data
text = open('sample.txt', 'r').read()
text.split()
words = text.split()


# compare word by word
def f1(words):
    for word in words:
        count = 0
        for words2 in words:
            if word == words2:
                count += 1
        # print("word: {}, count {}".format(word, count))


# faster version using a list
def f2(words):
    seen_words = []
    for word in words:
        if word in seen_words:
            # ignore it when you already seen it and continue with next word
            continue
        seen_words.append(word)
        count = 0
        for words2 in words:
            if word == words2:
                count += 1
        # print("word: {}, count {}".format(word, count))


# use a set instead of a list
def f3(words):
    seen_words = set()
    for word in words:
        if word in seen_words:
            continue
        seen_words.add(word)
        count = 0
        for words2 in words:
            if word == words2:
                count += 1


# ugly version with a touple (just to see why to )
def f4(words):
    word_counts = []

    for word in words:
        word_was_seen = False
        position = 0
        for (word2, count) in word_counts:
            if word == word2:
                count += 1
                word_was_seen = True
                word_counts[position] = (word, count)
                break
            else:
                position += 1
        if not word_was_seen:
            word_counts.append((word, 1))

    # print(word_counts)


# nicer version with dictionary
def f5(words):
    word_counts = {}

    for word in words:
        if word in word_counts:
            count = word_counts.get(word)
            count += 1
            word_counts[word] = count
        else:
            count = 0


# dictionary - shorter
def f6(words):
    word_counts = {}

    for word in words:
        cur_count = word_counts.get(word, 0)
        cur_count += 1
        word_counts[word] = cur_count


# dictionary - shorter 2
def f7(words):
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

"""
or: just don't code - use other peoples code
from collection import Counter

def f8(words):
    Counter(words)
"""
