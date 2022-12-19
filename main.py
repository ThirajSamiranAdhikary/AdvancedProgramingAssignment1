import csv
mylist = [] #global variable to store datta

def readFile(): # to read csv file as dictionary mode
    global mylist
    with open('abc.csv') as f:
        myread = csv.DictReader(f)
        for x in myread:
            mylist.append(x)


def updateFile(): #to update students marks and average
    global mylist
    exam1sum = 0
    exam2sum = 0
    finalExam = 0
    overallExam = 0

    while True: #to continue a loop to enter and update marks
        stdnum = int(input('Enter student number: (Amal - 0),(Nimal-1),(Saman-2),(Kamal-3)'))
        exmnum = int(input('Enter exam mark : (Exam1 - 1),(Exam2 - 2),(Final Exam-3)'))
        exmark = int(input('Enter marks:'))
        if exmark<=100 and exmark>=0:
            if exmnum == 1 and stdnum in (0, 1, 2, 3):
                mylist[stdnum]['Exam1'] = exmark
            elif exmnum == 2 and stdnum in (0, 1, 2, 3):
                mylist[stdnum]['Exam2'] = exmark
            elif exmnum == 3 and stdnum in (0, 1, 2, 3):
                mylist[stdnum]['Final Exam'] = exmark
            else:
                print('Not a valid  exam')
        else:
            print('Marks should be within 0 and 100')
            continue
        jump=int(input('Press 1 if you want update  marks: Press 0 if you want to leave:'))
        if jump==0:
            break
        else:
            continue

    for i in (0, 1, 2, 3):
        mylist[i]['Overall Grade'] = (int(mylist[i]['Exam1']) + int(mylist[i]['Exam2']) + int(
            mylist[i]['Final Exam'])) / 3

    for i in (0, 1, 2, 3):
        exam1sum = exam1sum + int(mylist[i]['Exam1'])
        exam2sum = exam2sum + int(mylist[i]['Exam2'])
        finalExam = finalExam + int(mylist[i]['Final Exam'])
        overallExam = overallExam + int(mylist[i]['Overall Grade'])

    mylist[5]['Exam1'] = exam1sum / 4
    mylist[5]['Exam2'] = exam2sum / 4
    mylist[5]['Final Exam'] = finalExam / 4
    mylist[5]['Overall Grade'] = overallExam / 4


def writeFile(): #to write to csv file
    with open('abc.csv', 'w', newline='') as f:
        fieldnames = ['Name', 'Exam1', 'Exam2', 'Final Exam', 'Overall Grade']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in mylist:
            writer.writerow(i)

#call functions
readFile()

updateFile()

writeFile()







