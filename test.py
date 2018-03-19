import re
s1 = '<td class="blue" style="white-space: nowrap;"><strong>CIS 2</strong></td>'
s2 = ''
'''
if 'CIS' in s1:
    cID = re.search('CIS:P(\d+*)',s1)
    print(cID.group())
    

print("first line\nsecond line\nthird line")
prompt = "1. Search by number\n2. Search by topic\n3. Search by topic and quarter\n4. End search"
print(prompt
'''
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
            print('choice #1')
            print()
            '''
        elif choice == 2:
            classTopic = input("Enter a CIS topic: ")
            #classes.searchByTopic(classTopic.title())
            print('choice #2')
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
                        #classes.searchByQuart(classTopic.title(),classQuart)
                        print('choice #3')
                        status = True
                except ValueError as e2:
                    print(str(e2))
            print()
            '''
    except ValueError as e1:
        print()
        print(str(e1))
        