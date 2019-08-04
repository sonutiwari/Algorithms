class HashTable(object):
    def __init__(self):
        self.table = {}    
    # create a hashtable progressively
    # create a hashtable all at once
    def create_hash_table(self, items, has_multiple_item = False):
        self.table = {}
        if has_multiple_item:
            for key in items.keys():
                self.table[key] = items[key]
        else:
            self.table[key] = items[key]

    # replace an item
    def update_hash_table(self, key, value):
        self.table[key] = value
    
    def print(self):
        print(self.table)
        # iterate the keys and values in the dictionary
        for key, value in self.table.items():
            print("key: ", key, " value: ", value)

# try to access a nonexistent key
# print(items1["key6"])
ht = HashTable()
ht.create_hash_table(dict({"key1": 1, "key2": 2, "key3": "three"}), True)
ht.print()
