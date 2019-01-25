class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.last_elements=[0 for i in range(size)]
        self.flag=0
        self.counter=0
        self.truncated_counter=0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        #add the element
        self.last_elements[self.truncated_counter]=val
        self.truncated_counter+=1
        self.counter+=1
        if self.flag==0:
            res=1.0*sum(self.last_elements)/self.counter
        else:
            res=1.0*sum(self.last_elements)/len(self.last_elements)
        if self.counter>=len(self.last_elements):
            self.flag=1
            self.truncated_counter=self.counter%len(self.last_elements)
        return res#%self.last_elements, self.truncated_counter


# Your MovingAverage object will be i+nstantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

#This is the basic implementation
# more obvious choice of implementation would be a FIFO: A queue
# Remove the latest, while size>3
# Else don't remove
#return mean of all

#Queue Approach
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue=[]
        self.size=size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        if len(self.queue)>self.size:
            self.queue.pop(0)
        # print(self.queue)
        return 1.0*sum(self.queue)/len(self.queue)
        

#Using queues through collections would be faster
#collections has deque() which can be used as stacks and queues, using pop() and popleft()
class MovingAverage(object):
    import collections 
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue=collections.deque()
        self.size=size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        if len(self.queue)>self.size:
            self.queue.popleft()
        # print(self.queue)
        return 1.0*sum(self.queue)/len(self.queue)
         
