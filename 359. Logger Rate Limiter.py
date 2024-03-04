class Logger(object):

    def __init__(self):
        self.time_dict = dict()

        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.time_dict :
            self.time_dict[message] = timestamp
            return True
        # If exist
        if timestamp < self.time_dict[message] + 10 : # PREVENT
            return False
        else :
            # IT'S OKAYYY, update timestamp
            self.time_dict[message] = timestamp
            return True

        


        
        
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)