class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity=capacity
        self.capacity_used = 0
        self.lru=[]
        self.keymap={}
        

    # @return an integer
    def get(self, key):
        if self.keymap.has_key(key):
            self.lru.remove(key)
            self.lru.append(key)
            return self.keymap[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.keymap.has_key(key) == False:
            if self.capacity_used == self.capacity:
                # insert new key by first making room for it
                del self.keymap[self.lru[0]]
                self.lru.remove(self.lru[0])
                self.keymap[key]=value
                self.lru.append(key)
            else:
                # insert a new key when there is still room
                self.keymap[key]=value
                self.lru.append(key)
                self.capacity_used+=1    

        else:
            # I overide a key that I already have
            self.keymap[key]=value
            self.lru.remove(key)
            self.lru.append(key)