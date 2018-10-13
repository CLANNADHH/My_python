import time
import re


class Change_Time(object):
    def __init__(self,time_str=time.time()):
        self.time_format = '%Y-%m-%d %H:%M:%S'
        self.time_str = time_str
   
    def timetypetest(self):
        if(isinstance(self.time_str,float)):
            self.time_str = int(self.time_str)
        
        result = re.match(r'\d{10}',str(self.time_str))
        if result is not None:
            print(result.group())
            self.time_str = int(result.group())
            return self.stamp2time()
        return "你给的不是时间戳数据"
    
    def stamp2time(self):
        return time.strftime(self.time_format, time.localtime(self.time_str))

if __name__ == "__main__":
  stamp_change = Change_Time()
  # 默认不输入时间戳就会取当前时间戳
  print(stamp_chamge())
