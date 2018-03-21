# lab 8
# Shiyu Zhang, Zhubo Deng
# Write an application that helps a user look up CIS classes. 
# The app uses data from this CIS web page, which has been saved into a text file called lab8input.txt. 
# The app lets the user look up CIS classes by entering a class number, or a CIS topic, or a CIS topic and a quarter.
# Data stucture: A dictionary: key=classNumber; value=a list[classTitle, a list of 4 boolean[True,True,True,True]
#ex: {"2":["Computer and Society",[True,True,True,True]]}

from cisclasses import CISclasses 

class UI:
    def __init__(self):
        '''constuctor for UI class, automatically create a cisclasses object'''
        self._classes = CISclasses ()
        
    def run(self):
        '''run method displays menu and ask users for their choice'''
        prompt = "1. Search by number\n2. Search by topic\n3. Search by topic and quarter\n4. End search\nEnter a number: "
        process = False
        while not process:
            try:
                userChoice = input(prompt)
                if  (userChoice.isdigit()==False) or (int(userChoice)<=0) or (int(userChoice)>=5):
                    raise ValueError("Must be an int from 1-4!!!")  
                choice = int(userChoice)
                if choice == 4:
                    process = True                    
                elif choice == 1:
                    classNum = input("Enter a class number: ")
                    
                    self._classes.searchByNumber(classNum.upper())
                    #print('choice #1')
                    print()
                elif choice == 2:
                    classTopic = input("Enter a CIS topic: ")
                    self._classes.searchByTopic(classTopic.title())
                    #print('choice #2')
                    print()
                elif choice == 3:
                    classTopic = input("Enter a CIS topic: ")
                    status = False
                    while not status:
                        try:    
                            classQuart = input("Enter a quarter: ")
                            classQuart = classQuart.title()
                            if not (classQuart=="Spring" or classQuart == "Summer" or classQuart=="Fall" or classQuart=="Winter"):
                                raise ValueError("Please enter a valid quarter!!! 'FALL, WINTER, SPRING, SUMMER only!'")
                            else:
                                self._classes.searchByTopicQuarter(classTopic.title(),classQuart)
                                #print('choice #3')
                                status = True
                        except ValueError as e2:
                            print(str(e2))
                    print()
            except ValueError as e1:
                print()
                print(str(e1))        

app = UI()
app.run()
