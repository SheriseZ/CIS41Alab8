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
                    
                    if (classNum != None and className != None) :               # comfirm or don't need to?  
                        self._classDict[classNum] = [className, quarterLIst]
                    print(self._classDict)
                       
                        
                      
                
                
                
        except FileNotFoundError as e :
            print("File not found")
            raise SystemExit

    def searchByNumber(self, classNum) :
        '''  41A '''
        if classNum in self._classDict :        # if key in dict then print
            print("CIS", classNum, self._classDict[classNum][0] + ":", 
                  "Fall" if self._classDict[classNum][1][0] == True else "",
                  "Winter" if self._classDict[classNum][1][1] == True else "", 
                  "Spring" if self._classDict[classNum][1][2] == True else "", 
                  "Summer" if self._classDict[classNum][1][3] == True else "")
        
    
    
    def searchByTopic(self, topic) :
        
        
        # iterator dict??? sequence?????????????
        
        for classNum, classList in sorted(self._classDict.items()) :   # traverse dict      # can we use sorted??????????????????
            if topic in self._classDict[classNum][0] :      # if substr in str(value of the key) then print
                print("CIS", classNum, self._classDict[classNum][0])
                
        
    def searchByTopicQuarter(self, topic, quarter) :
        
        for classNum, classList in sorted(self._classDict.items()) :   # traverse dict      # can we use sorted??????????????????
            if topic in self._classDict[classNum][0] :      # if substr in str(value of the key) then print
                
                if (quarter == "Fall" and self._classDict[classNum][1][0] == True) :
                    print("CIS", classNum, self._classDict[classNum][0])
                if (quarter == "Winter" and self._classDict[classNum][1][1] == True) :
                    print("CIS", classNum, self._classDict[classNum][0])
                if (quarter == "Spring" and self._classDict[classNum][1][2] == True) :
                    print("CIS", classNum, self._classDict[classNum][0])
                if (quarter == "Summer" and self._classDict[classNum][1][3] == True) :
                    print("CIS", classNum, self._classDict[classNum][0])
                
                    
                '''
                print("CIS", classNum, self._classDict[classNum][0], 
                      quarter if (quarter == "Fall" and self._classDict[classNum][1][0] == True) else "", 
                      quarter if (quarter == "Winter" and self._classDict[classNum][1][1] == True) else "", 
                      quarter if (quarter == "Spring" and self._classDict[classNum][1][2] == True) else "", 
                      quarter if (quarter == "Summer" and self._classDict[classNum][1][3] == True) else "")
                '''
        
        
            

classes = CISclasseses()
print()
classes.searchByNumber("170F")
print()
classes.searchByTopic("Java")     # unsolved; capitalize; alphabe sequence; error msg; java??, javascript??
print()
classes.searchByTopicQuarter("C++", "Spring")       # no need sequence here???????