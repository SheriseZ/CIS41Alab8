# lab 8
# Zhubo Deng, Shiyu Zhang
# Data stucture: A dictionary: key=classNumber; value=a list[classTitle, a list of 4 boolean[True,True,True,True]
#ex: {"2":["Computer and Society",[True,True,True,True]]}

import re
FILE_NAME = "lab8_no_blankline.txt"


class CISclasseses:
    def __init__(self) :
        try :
            with open(FILE_NAME) as infile :
                self._classDict = {}                
                for line in infile :
                    line = line.rstrip()              # remove whitespace which is \n                        
                    
                    classNum = None
                    className = None
                    
                    if ">CIS " in line :
                        
                        # class number
                        print(line)
                        classNum = re.search("CIS (\d+(\w+)?)", line)
                        print(classNum.group(1))                                                
                        classNum = classNum.group(1)
                        
                        line = infile.readline()
                        line = line.rstrip()
                        print(line)
                    
                        
                        # title
                        print(line)
                        className = re.search("\">(.*)</[as]", line)    # </a> or </span>
                        print(className.group(1))                        
                        className = className.group(1)
                        
                        
                        # boolean: 4 QUARTERS
                        #m = re.search("\w(?=<)",s2)
                        quarterLIst = []
                        for i in range(4) :
                            line = infile.readline()
                            line = line.rstrip()                            
                            m = re.search(">(x)<", line)
                            status = False if m==None else True
                            quarterLIst.append(status)
                            print(quarterLIst)
                                         
                    '''
                    self._classDict[classNum] = className
                    print(self._classDict)
                    '''
                    
                    if (classNum != None and className != None and quarterLIst != None) :                        
                        self._classDict[classNum] = [className, quarterLIst]
                    print(self._classDict)
                       
                        
                      
                
                
                
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
