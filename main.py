class HashTable:
  def __init__(self,size):
    self.size = size
    self.hashTbl = [None] * self.size
  
  def _hash(self, key): 
    hash = 0
    for i in range(len(key)):
        hash = (hash + ord(key[i])*i) % self.size
    return hash

  def set(self,key, value):
    address = self._hash(key)
    if not self.hashTbl[address]:
      self.hashTbl[address] = [[key,value]]
    else:
      self.hashTbl[address].append([key,value])

  def get(self,key):
    address = self._hash(key)
    for item in self.hashTbl[address]:
      if item[0] == key:
        print(item[1])
        return item[1]

  def keys(self):
    keysArray = []
    for item in self.hashTbl:
      if item:
        for subArr in item:
          if subArr:
            keysArray.append(subArr[0])
    print(keysArray)






# myTable = HashTable(50)

# myTable.set('apple',25)
# myTable.set('orange',55)
# myTable.set('banana',5)

# myTable.get('orange')

# myTable.keys()