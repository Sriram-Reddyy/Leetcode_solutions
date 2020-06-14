"""
380. Insert Delete GetRandom O(1)
Medium

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""

class RandomizedSet:
    def __init__(self):
        self.d1 = defaultdict(int)
        self.count = 0
        self.list1 = []
    def insert(self, val: int) -> bool:
        if(self.d1[val]==0):
            self.d1[val]+=1
            self.list1.append(val)
            self.count+=1
            return True
    def remove(self, val: int) -> bool:
        if(self.d1[val]):
            self.d1[val]-=1
            self.list1.remove(val)
            self.count-=1
            return True
        
    def getRandom(self) -> int:
        r = random.randint(0,self.count-1)
        return self.list1[r]
