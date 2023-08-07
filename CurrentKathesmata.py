import time

current_time = time.localtime()
print(current_time)
print(current_time.tm_hour)
print(current_time.tm_wday)


if current_time.tm_hour >= 8 and current_time.tm_hour < 19: #checks whether it is evening or it is morning
    matins()
else:
    vespers()


def matins(): #defines the early morning service
    if current_time.tm_wday == 0: #Monday
        print("The Fourth Kathisma:")
        fourth_kathisma()
        print("The Fifth Kathisma:")
        fifth_kathisma()
    if current_time.tm_wday == 1: #Tuesday
        print("The Seventh Kathisma:")
        seventh_kathisma()
        print("The Eighth Kathisma:")
        eighth_kathisma()
    if current_time.tm_wday == 2: #Wednesday
        print("The Tenth Kathisma:")
        tenth_kathisma()
        print("The Eleventh Kathisma:")
        eleventh_kathisma()
    if current_time.tm_wday == 3: #Thursday
        print("The Thirteenth Kathisma:")
        thirteenth_kathisma()
        print("The Forteenth Kathisma:")
        forteenth_kathisma()
    if current_time.tm_wday == 4: #Friday
        print("The Ninteenth Kathisma:")
        ninteenth_kathisma()
        print("The Twentith Kathisma:")
        twentith_kathisma()
    if current_time.tm_wday == 5: #Saturday
        print("The Sixteenth Kathisma:")
        sixteenth_kathisma()
        print("The Seventeenth Kathisma:")
        seventeenth_kathisma()
    if current_time.tm_wday == 6: #Sunday
        print("The Second Kathisma:")
        second_kathisma()
        print("The Third Kathisma:")
        third_kathisma()

def vespers():  #defines the early evening service
    if current_time.tm_wday == 0: #Monday
        print("The Sixth Kathisma:")
        sixth_kathisma()
    if current_time.tm_wday == 1: #Tuesday
        print("The Ninth Kathisma:")
        ninth_kathisma()
    if current_time.tm_wday == 2: #Wednesday
        print("The Twelth Kathisma:")
        twelth_kathisma()
    if current_time.tm_wday == 3: #Thursday
        print("The Fifteenth Kathisma:")
        fifteenth_kathisma()
    if current_time.tm_wday == 4: #Friday
        print("The Eighteenth Kathisma:")
        eighteenth_kathisma()
    if current_time.tm_wday == 5: #Saturday
        print("The First Kathisma:")
        first_kathisma()
    if current_time.tm_wday == 6: #Sunday
        no_kathisma()

def first_kathisma():
    file = open("src/001.txt", 'r')
    print(file.read())
    file.close()
    
    file = open("src/002.txt", 'r')
    print(file.read())
    file.close()
    
    file = open("src/003.txt", 'r')
    print(file.read())
    file.close()
    
    file = open("src/004.txt", 'r')
    print(file.read())
    file.close()
    
    file = open("src/005.txt", 'r')
    print(file.read())
    file.close()
    
    file = open("src/006.txt", 'r')
    print(file.read())
    file.close()
    
    file = open("src/007.txt", 'r')
    print(file.read())
    file.close()
    
    file = open("src/008.txt", 'r')
    print(file.read())
    file.close()
    
    file = open("src/009.txt", 'r')
    print(file.read())
    file.close()
   
    
def second_kathisma():
    pass

def third_kathisma():
    pass

def fourth_kathisma():
    pass

def fifth_kathisma():
    pass

def sixth_kathisma():
    pass

def seventh_kathisma():
    pass

def eighth_kathisma():
    pass

def ninth_kathisma():
    pass

def tenth_kathisma():
    pass

def eleventh_kathisma():
    pass

def twelth_kathisma():
    pass

def thirteenth_kathisma():
    pass

def forteenth_kathisma():
    pass

def fifteenth_kathisma():
    pass

def sixteenth_kathisma():
    pass

def seventeenth_kathisma():
    pass

def eighteenth_kathisma():
    pass

def ninteenth_kathisma():
    pass

def twentith_kathisma():
    pass

def no_kathisma():
    for i in range(99):
        print("O Lord Jesus Christ, have mercy on me, the sinner!")




def read_psalm(filename)





'''
try:
    file = open("src/001.txt", 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found.")
'''