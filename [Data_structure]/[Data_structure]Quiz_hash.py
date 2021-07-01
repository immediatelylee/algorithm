class HashSet:
    def __init__(self, table_size=16, hash_fnc=None):
        if hash_fnc is None:
            self.hash_fnc = hash
        else:
            self.hash_fnc = hash_fnc

        self.table_size = table_size
        self.table = [None]*table_size

    def add(self, data):
        ind = self.hash_fnc(data) % self.table_size
        if self.table[ind] is None or self.table[ind] == data:
            self.table[ind] = data
        else:
            pass

    def search(self, data):
        ind = self.hash_fnc(data) % self.table_size
        prob_ind = ind
        while self.table[prob_ind]:
            if self.table[prob_ind] == data:
                return True
            prob_ind = (prob_ind + 1) % self.table_size
            if prob_ind == ind:
                break
        return False


hs = HashSet(hash_fnc=lambda x: 1)
hs.add('abc')
hs.add('bcd')
hs.add('cde')
print(hs.search('abc'), end=' ')
print(hs.search('bcd'), end=' ')
print(hs.search('cde'), end=' ')
