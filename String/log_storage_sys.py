#You are given several logs that each log contains a unique id and timestamp.
# Timestamp is a string that has the following format: 
#Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. 
#All domains are zero-padded decimal numbers.
#Design a log storage system to implement the following functions:
#void Put(int id, string timestamp): Given a log's unique id and timestamp, 
#store the log in your storage system.
#int[] Retrieve(String start, String end, String granularity): Return the id of
#logs whose timestamps are within the range from start to end. Start and end 
#all have the same format as timestamp. However, granularity means the time 
#level for consideration. For example, start = "2017:01:01:23:59:59", 
#end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to 
#find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017
class LogSystem(object):

    def __init__(self):
        self.log_dict={}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.log_dict[id]=timestamp
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        res=[]
        if gra=="Year":
            start_idx=0
            end_idx=4
        elif gra=="Month":
            start_idx=5
            end_idx=7
        elif gra=="Day":
            start_idx=8
            end_idx=10
        elif gra=="Hour":
            start_idx=11
            end_idx=13
        elif gra=="Minute":
            start_idx=14
            end_idx=16
        elif gra=="Second":
            start_idx=17
            end_idx=19
        for key,val in self.log_dict.items():
            # print(s,val,e,key)
            if val[:end_idx]>=s[:end_idx] and val[:end_idx]<=e[:end_idx]:
                res.append(key)
        return res
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)


#Here, we use the string comparison easily inbuilt in python
# otherwise we can convert the timestamp to a unique time as
# 60*60*HH + 60*MM + SS
# and compare only upto the required position

