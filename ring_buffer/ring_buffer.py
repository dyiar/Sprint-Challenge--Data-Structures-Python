class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

    # class __Full:
    #   def append(self, x):
    #     self.storage[self.current] = x
    #     self.current = (self.current +1) & self.capacity
    #   def get(self):
    #     return self.storage[self.current:]+self.storage[:self.current]

  def append(self, item):
    # self.storage.append(item)
    # print(self.storage)
    # if len(self.storage) == self.capacity:
    #   self.current = 0
      # self.__class__ = self.__Full

    self.storage[self.current] = item
    if self.current+1 <= len(self.storage)-1:
      self.current +=1
    else:
      self.current = 0

  def get(self):
    temp = []
    for i in self.storage:
      if i is not None:
        temp.append(i)
    return temp
    # return self.storage[self.current:]+self.storage[:self.current]