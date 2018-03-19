# lab 8
# Zhubo Deng, Shiyu Zhang
'''
import re
FILENAME1 = "lab8input.txt"
FILENAME2 = "lab8_no_blankline.txt"

class CISclasseses:
    def __init__(self):
        try:
            with open(FILENAME2,'r') as fin:
                for line in fin:
                    line = line.strip()
                    print(line)
                    
                    
                    
        except IOError as e1:
            print(str(e1))
            return None
        
    def searchByNumber(self,classNum):
        
    
    def searchByTopic(self,classTopic):
        
    
    def searchByTopicQuarter(self):    
        
        
# classes = CISclasseses()
'''

import re
FILE_NAME = "lab8input.txt"


class CISclasseses:
    def __init__(self) :
        try :
            with open(FILE_NAME) as infile :
                self._classDict = {}
                for line in infile :
                    line = line.rstrip()              # remove whitespace which is \n    
                    #print(line)
                    
                    if ">CIS " in line :
                        print(line)
                        classNum = re.search("CIS (\d+)(\w+)?", line)
                        print(classNum.group())                        
                        n = classNum.group()
                        classNum = re.search("(\d+)(\w+)?", n)
                        print(classNum.group())
                        
                        # title
                    if "html" in line :
                        print(line)
                        className = re.search("^(Description\">)(\w+)(</a></td>)$", line)
                        print(className.group())
                        
                    #self._classDict[classNum] = className
                        
                        
                        #lassNum = re.search("^(CIS )(\d+?\w+?)</string>)$", line)
                        #m = classNum.group(1)
                        #print(classNum)
                        #_classDict[classNum] = 
                        # nowrap;"><strong>CIS 2</strong>
                        
                
                
                
        except FileNotFoundError as e :
            print("File not found")
            raise SystemExit

    def searchByNumber(self, classNum) :
        '''  41A '''
        if classNum in self._classDict :
            print("CIS", classNum, self._classDict[classNum], quarter)
        
    
    
    #def searchByTopic(self, topic) :
        
    #def searchByTopicQuarter() :
        
            

classes = CISclasseses()
