# lab 8
# Zhubo Deng, Shiyu Zhang
# Data stucture: A dictionary: key=classNumber; value=a list[classTitle, a list of 4 boolean[True,True,True,True]
#ex: {"2":["Computer and Society",[True,True,True,True]]}


import re
FILE_NAME = "lab8_no_blankline.txt"


class CISclasses:
    def __init__(self) :
        '''a constucture to read file and store data in our data stucture describled at the top of the file'''
        try :
            with open(FILE_NAME) as infile :
                self._classDict = {}                
                for line in infile :
                    line = line.rstrip()              # remove whitespace which is \n                        
                    
                    classNum = None
                    className = None
                    
                    if ">CIS " in line :
                        
                        # class number
                        classNum = re.search("CIS (\d+(\w+)?)", line)
                        #print(classNum.group(1))                                                
                        classNum = classNum.group(1)
                        
                        line = infile.readline()
                        line = line.rstrip()
                    
                        
                        # title
                        className = re.search('">([\w(].*)</[as]', line)                      
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
                            #print(quarterLIst)
                                         
                    
                    if (classNum != None and className != None) :                 
                        self._classDict[classNum] = [className, quarterLIst]
                #print(self._classDict)

                
        except FileNotFoundError as e :
            print("File not found")
            raise SystemExit

    def searchByNumber(self, classNum) :
        '''  a method to search classes by class number '''
        if classNum in self._classDict :        # if key in dict then print
            if self._classDict[classNum][1] [::]== [False,False,False,False]:
                print("CIS", classNum, self._classDict[classNum][0])
            else:
                print("CIS", classNum, self._classDict[classNum][0] + ":", 
                      "Fall" if self._classDict[classNum][1][0] == True else "",
                      "Winter" if self._classDict[classNum][1][1] == True else "", 
                      "Spring" if self._classDict[classNum][1][2] == True else "", 
                      "Summer" if self._classDict[classNum][1][3] == True else "")
        else:
            print("No such a class Number!!!")
 
    
    
    def searchByTopic(self, topic) :
        '''a method to search classe by topic'''

        flag = False
        for classNum in sorted(self._classDict, key=self._classDict.get) :   # traverse dict  
                        
            if topic == "C++" :
                regex = "C\+\+"
            elif topic == "C+":
                regex = "C\+\\b"
            elif topic == "C#" :
                regex = "C\#"
            elif topic == "C" :
                regex = "\\bC\\b[^+#]"
            else :
                regex = topic + "\\b"

            if re.search(regex, self._classDict[classNum][0], re.I) != None :
                flag = True
                print("CIS", classNum, self._classDict[classNum][0])
        
        if flag == False :
            print('No class matching topic:',topic)
            
        
    def searchByTopicQuarter(self, topic, quarter) :
        '''a method to search classes by a combination of topic and quarter'''
        flag = False
        for classNum in sorted(self._classDict, key=self._classDict.get) :   # traverse dict      # can we use sorted??????????????????
            
            if topic == "C++" :
                regex = "C\+\+"
            elif topic == "C#" :
                regex = "C\#"
            elif topic == "C" :
                regex = "\\bC\\b[^+#]"
            else :
                regex = topic + "\\b"
                        
            if re.search(regex, self._classDict[classNum][0], re.I) != None :      # if substr in str(value of the key) then print
                
                if (quarter == "Fall" and self._classDict[classNum][1][0] == True) :
                    flag = True
                    print("CIS", classNum, self._classDict[classNum][0])
                elif (quarter == "Winter" and self._classDict[classNum][1][1] == True) :
                    flag = True
                    print("CIS", classNum, self._classDict[classNum][0])
                elif (quarter == "Spring" and self._classDict[classNum][1][2] == True) :
                    flag = True
                    print("CIS", classNum, self._classDict[classNum][0])
                elif (quarter == "Summer" and self._classDict[classNum][1][3] == True) :
                    flag = True
                    print("CIS", classNum, self._classDict[classNum][0])
                
        if flag == False :
            print('No class of topic '+'"'+topic+'"'+ ' in '+ quarter +' quarter!!!')


'''
# unit test
classes = CISclasses()
print()
classes.searchByNumber("50")
print()
classes.searchByTopic("C!")     
print()
classes.searchByTopicQuarter("Assembly", "Summer")      
'''