# lab 8
# Zhubo Deng, Shiyu Zhang

class CISclasseses:
    def __init__(self):
        filename1 = "lab8input.txt"
        filename2 = "lab8_no_blankline.txt"
        try:
            with open(filename2,'r') as fin:
                for line in fin:
                    line = line.strip()
                    print(line)
        except IOError as e1:
            print(str(e1))
            return None
        
        
# classes = CISclasseses()
