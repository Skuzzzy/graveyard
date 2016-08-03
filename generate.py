import random
from sys import stdin

rand = random.random
randint = random.randint

class CountDict(object):

    def __init__(self):
        self.counts = {}
        self.total = 0

    def add(self, word):
        self.total += 1
        if not self.counts.get(word):
            self.counts[word] = 1
        else:
            self.counts[word] += 1

    def convert_to_proba(self):
        new_proba = ProbaList()
        low = 0.0
        for key in self.counts:
            high = low + float(self.counts[key])/self.total
            new_proba.add_key_proba(key, (low, high))
            low = high
        return new_proba

class ProbaList(object):

    def __init__(self):
        self.data = []

    def obtain_rand(self):
        proba_roll = rand()
        for each in self.data:
            if each[1][0] <= proba_roll and proba_roll < each[1][1]:
                return each[0]
        raise Exception

    def add_key_proba(self, key, proba_range):
        self.data.append((key, proba_range))

if __name__ == '__main__':
    count_data = {}
    lines = [line.rstrip().upper().split() for line in stdin]
    for title in lines:
        for index, word in enumerate(title):
            if not count_data.get(word):
                count_data[word] = CountDict()
            if index < len(title)-1:
                count_data[word].add(title[index+1])
            else:
                count_data[word].add('eol')


    probas = {key: count_data[key].convert_to_proba() for key in count_data}

    for _ in range(10):
        title = []
        # Seed
        # keys = probas.keys()
        # current = keys[randint(0,len(keys))]
        current = 'THE'
        title.append(current)

        while current != 'eol':
            current = probas[current].obtain_rand()
            title.append(current)

        # for _ in range(10):
            # current = probas[current].obtain_rand()
            # if current == 'eol':
                # keys = probas.keys()
                # current = keys[randint(0,len(keys))]
            # title.append(current)

        print ' '.join(title)
    # for each in probas:
        # print each, probas[each].data
