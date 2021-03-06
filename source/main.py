# OIT CR Scheduler
# Documentation at README.md: https://github.com/loej/CR-Scheduler/blob/master/README.md
# Imports
import csv
import math
# More information: https://docs.python.org/3/library/operator.html
import operator
import sys


class Cons:

    # Instance attributes
    def __init__(self, netID, schedule, totalHours):
        self.netID = netID
        self.schedule = schedule
        self.totalHours = totalHours


class Sups:
    # Instance attributes
    def __init__(self, netID, schedule):
        self.netID = netID
        self.schedule = schedule
        self.assignedCons = []
        self.noGoodCons = []


class Shift:

    # Instance attributes; all integers.
    def __init__(self, location, dayofWeek, start, end):
        self.location = location
        self.dayofWeek = dayofWeek
        self.start = start
        self.end = end

    def copy(self, shiftCopy):
        self.location = shiftCopy.location
        self.dayofWeek = shiftCopy.dayofWeek
        self.start = shiftCopy.start
        self.end = shiftCopy.end


# Global Variables
startTime = 8
endTime = 22
supRoster = []
consRoster = []
sitRoster = []


# Creates shift based off of location, day of the week, and start and end time of shifts.
def create_Shift(location, dayofWeek, start, end):
    s = Shift
    # Assigning Location
    if "ARC" in location:
        s.location = 0
    if "BEST" in location:
        s.location = 1
    if "RBHS" in location:
        s.location = 2
    if "LSM" in location:
        s.location = 3
    # Assigning DayofWeek
    if dayofWeek == "Sunday":
        s.dayofWeek = 0
    if dayofWeek == "Monday":
        s.dayofWeek = 1
    if dayofWeek == "Tuesday":
        s.dayofWeek = 2
    if dayofWeek == "Wednesday":
        s.dayofWeek = 3
    if dayofWeek == "Thursday":
        s.dayofWeek = 4
    if dayofWeek == "Friday":
        s.dayofWeek = 5
    if dayofWeek == "Saturday":
        s.dayofWeek = 6
    # Converts start and end time to 24 hours
    s.start = convert24(start, 1)
    s.end = convert24(end, 0)
    # Returns data into one list
    return [s.location, s.dayofWeek, s.start, s.end]


# This code is no longer being used
def convert24DEPRECATED(str1, check):
    # Checking if last two elements of time is AM
    if str1[-2:] == "PM":
        # add 12 to hours and remove PM
        if str1[:-5] == "11":
            return 23
        # print(str1[:-5])
        if str1[:-5] == "12":
            return 12
        str2 = str(int(str1[:-5]) + 12)
        # Check if Sart Time, then go to Ceiling
        if check == 1:
            x = int(str1[-4:-2])
            if int(str1[-4:-2]) > 0:
                return int(str2) + 1
        return int(str2)
    elif int(str1[:colonIndex]) < 8:
        return 23;
    # Check if Start Time, then go to Ceiling
    if check == 1:
        if int(str1[-4:-2]) > 0:
            return int(str1[:-5]) + 1
    return int(str1[:-5])


def convert24(time, check):
    # start = 1 and end = 0
    colonIndex = time.index(":")
    hour = int(time[:colonIndex])
    minute = int(time[colonIndex + 1:-2])
    if time[-2:] == "PM":
        noon = True
    else:
        noon = False
    # Checks if a shift ends in the morning when supervisors are not working
    if (check == 0 and not noon and hour < 7) or (not noon and hour == 12):
        return 23
    if noon and hour == 12:
        return 12
    if minute > 30:
        if noon:
            return hour + 13
        else:
            return hour + 1
    else:
        if noon:
            return hour + 12
        else:
            return hour


# Populate2D Array for Sups.Schedule
def populate2D(arr, location, day, start, end):
    start = convert24(start, 1)
    end = convert24(end, 0)
    i = 0
    if "BEST" in location:
        return
    if day == "Sunday":
        arr[0][0] = 1
    if day == "Monday":
        arr[1][0] = 1
        i = 1
    if day == "Tuesday":
        arr[2][0] = 1
        i = 2
    if day == "Wednesday":
        arr[3][0] = 1
        i = 3
    if day == "Thursday":
        arr[4][0] = 1
        i = 4
    if day == "Friday":
        arr[5][0] = 1
        i = 5
    if day == "Saturday":
        arr[6][0] = 1
        i = 6
    for j in range(start + 1, end + 1):
        arr[i][j] = 1


#
def search(target, roster):
    for i in range(0, len(roster)):
        if target == roster[i].netID:
            return [roster[i], i]
    return [None, -1]


# ------------------------------------->
# Hassaan
# Reads CSV and creates Array of Workers #
# def read_CSV() :
# ---------------------------------------------READING CONS --------------------------------->
def readCons():
    with open(".\\Cons.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        prev = ""
        hoursCount = 0
        for row in csv_reader:  # Iterate through every row
            if line_count != 0:  # Make sure not the Top Column
                # print(row[0])
                if row[0] == "":  # Error check in case netID field is empty
                    line_count += 1
                    # print("hello world")
                    continue
                if row[0] != prev:  # NetID is the same as last row
                    if prev != "":
                        consRoster.append(Cons(new.netID, new.schedule, hoursCount))
                        hoursCount = 0
                        prev = new.netID
                    new = Cons
                    #   print(row[0])
                    new.netID = row[0]  # Initialize netID
                    new.schedule = []
                [temp1, temp2, temp3, temp4] = create_Shift(row[1], row[3], row[4], row[5])
                new.schedule.append(Shift(temp1, temp2, temp3, temp4))  # Add Shift to the Schedule Array
                hoursCount += temp4 - temp3
                prev = new.netID
            line_count += 1
        consRoster.append(Cons(new.netID, new.schedule, hoursCount))
        hoursCount = 0


# Reads sups.csv file
def readSups():
    hoursCount = 0
    tempList = []
    tempIdx = 0
    tempNetID = 0
    rows, cols = (7, 25)
    tempListDouble = [[0 for i in range(cols)] for j in range(rows)]
    with open(".\\Sups.csv", 'r') as csv_file2:
        supListRaw = csv.reader(csv_file2, delimiter=',')
        line_count = 0
        prev = ""
        tempCount = 0
        supList = list(supListRaw)
        for idx in range(1, len(supList)):
            if supList[idx][0] == "":
                continue
            if supList[idx][0] in sitRoster:
                [temp1, temp2, temp3, temp4] = create_Shift(supList[idx][1], supList[idx][3], supList[idx][4],
                                                            supList[idx][5])
                tempList.append(Shift(temp1, temp2, temp3, temp4))
                hoursCount += temp4 - temp3
                if idx + 1 == len(supList) or supList[idx + 1][0] != supList[idx][0]:
                    [tempNetID, tempIdx] = search(supList[idx][0], consRoster)
                    if tempNetID is None:
                        consRoster.append(Cons(supList[idx][0], tempList, hoursCount))
                    else:
                        consRoster[tempIdx].schedule.extend(tempList)
                        consRoster[tempIdx].totalHours += hoursCount
                    tempList = []
                    hoursCount = 0
            else:
                populate2D(tempListDouble, supList[idx][1], supList[idx][3], supList[idx][4], supList[idx][5])
                if idx + 1 == len(supList) or supList[idx + 1][0] != supList[idx][0]:
                    supRoster.append(Sups(supList[idx][0], tempListDouble))
                    tempListDouble = [[0 for i in range(cols)] for j in range(rows)]


# Prioritizes consultants using consRoster list.
def priorotizeConsultants(lstCons):
    tempSched = []
    tempSITSched = []
    # List of all Scheduled consultants
    scheduledConsultants = []
    # List of all Unscheduled consultants
    unscheduledConsultants = []
    # Boolean value that is set to show if a supervisor works during valid hours.
    workingDuringSup = False
    # Empty dictionary to be populated below.
    consDictionary = {}
    # This for loop iterates through lstCons which in this case it's the @consRoster list
    for obj in range(len(lstCons)):
        # Variable that holds the schedule from the Cons() class
        iterate = lstCons[obj].schedule
        # Variable that holds the netID from the Cons() class
        objNetid = lstCons[obj].netID
        # Checks for errors if the list is empty.
        if iterate is None:
            return 'ERROR: Please check the csv file.'
        for i in range(len(iterate)):
            # Points to the list inside consRoster. This is part of the Shift() class.
            # This section points to the location, day of the week, and start and end time.
            location = iterate[i].location
            dayofWeek = iterate[i].dayofWeek
            startingShift = iterate[i].start
            endShift = iterate[i].end
            # Checks for errors if the list is empty.
            if (location and dayofWeek and startingShift and endShift) is None:
                return 'ERROR: Please check the csv file.'
            # Checks for the threshold if a consultant is between working Supervisor hours.
            elif startingShift < endTime:
                workingDuringSup = True
        # Appends unscheduled Consultants netID, schedule, and total hours.
        if not workingDuringSup:
            unscheduledConsultants.append(Cons(lstCons[obj].netID, lstCons[obj].schedule, lstCons[obj].totalHours))
        else:
            # Populates the empty dictionary with the netID and total hours.
            consDictionary[objNetid] = lstCons[obj].totalHours
            workingDuringSup = False
    # Sorts the values inside the dictionary.
    sortedCons = dict(sorted(consDictionary.items(), key=operator.itemgetter(1)))
    # This for loop appends the keys from the dictionary into the scheduled consultants.
    for cons in sortedCons.keys():
        for i in range(len(lstCons)):
            if cons == lstCons[i].netID:
                scheduledConsultants.append(Cons(lstCons[i].netID, lstCons[i].schedule, lstCons[i].totalHours))
                break
    # returns both lists inside a list.
    return [scheduledConsultants, unscheduledConsultants]


# Assignment ()
# Divide lengths of Sup and Cons to get threshold  for each supervisor
# Go through cons list sequentially. For each cons, go through supervisor list.
def Assignment():
    [schedCons, unschedCons] = priorotizeConsultants(consRoster)
    [tempIdx,tempMin] = [-1,-1]
    for i in range(0, len(schedCons)):
        supFocusedIndex = ranking(schedCons[i])
        supRoster[supFocusedIndex].assignedCons.append(schedCons[i].netID)
    for cons in unschedCons:
        [tempIdx, tempMin] = [-1, sys.maxsize]
        for idx in range(0, len(supRoster)):
            if len(supRoster[idx].assignedCons) < tempMin:
                tempMin = len(supRoster[idx].assignedCons)
                tempIdx = idx
        supRoster[tempIdx].assignedCons.append(cons.netID)
    for sup in supRoster:
        sup.assignedCons.sort()
    # Outputs the results in a csv file.
    with open('Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0, len(supRoster)):
            print(supRoster[i].netID, ':', end=" ")
            print(*supRoster[i].assignedCons, sep=", ")
            writer.writerow([supRoster[i].netID, *supRoster[i].assignedCons])


def ranking(consultant):
    consultantThreshold = math.floor(len(consRoster) / len(supRoster))
    # print("Threshold",consultantThreshold);
    supCount = len(supRoster)
    rankingArray = [0] * supCount
    siteWeight = [10, 4, 6, 8]
    # initalvalues for rankingArray
    for i in range(0, supCount):
        if consultant.netID in supRoster[i].noGoodCons:
            rankingArray[i] = -999999
        else:
            rankingArray[i] = rankingArray[i] + (consultantThreshold - len(supRoster[i].assignedCons)) * 25
    for i in range(0, len(consultant.schedule)):
        focusedShift = consultant.schedule[i]
        for a in range(0, supCount):
            if 1 == supRoster[a].schedule[focusedShift.dayofWeek][0]:
                for hour in range(focusedShift.start + 1, focusedShift.end + 1):
                    if supRoster[a].schedule[focusedShift.dayofWeek][hour]:
                        rankingArray[a] = rankingArray[a] + 1 + siteWeight[focusedShift.location]
    supIndex = rankingArray.index(max(rankingArray))
    return supIndex


def setConflicts():
    tempSup = Sups
    tempIdx = 0
    with open(".\\Conflicts.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for r in csv_reader:  # Iterate through every row
            if len(r) < 1:
                return
            if r[0] in sitRoster:
                continue
            [tempSup, tempIdx] = search(r[0], supRoster)
            if tempSup is None:
                raise ValueError(r[0].strip())
            else:
                for b in range(1, len(r)):
                    if r[b] != "":
                        tempSup.noGoodCons.append(r[b])



def getSITS():
    inputSITS = ""
    inputSITS = input("Input this semseter's SITs (separated by commas): ")
    commaIndex = -1
    count = 0
    gucci = True
    while gucci:
        try:
            commaIndex = inputSITS.index(',')
        except ValueError:
            gucci = False
            sitRoster.append(inputSITS[:].replace(" ", ""))
            return
        sitRoster.append(inputSITS[:commaIndex].replace(" ", ""))
        inputSITS = inputSITS[commaIndex + 1:]


if __name__ == '__main__':
    errorList = []
    print("Welcome to the CR Scheduler!!!")
    print("By: emo66, hs770, jfm203")
    print("Last update: emo66 July 25, 2020\n")
    print("Ensure the following files are in the same folder as the executable:")
    print("\nCons.csv")
    print("\tZed Report of Assigned Shifts of Consultants")
    print("\nSups.csv")
    print("\tZed Report of Assigned Shifts of Supervisors")
    print("\tAny SITs on this list must be moved to Cons.csv")
    print("\nConflicts.csv")
    print("\tContains conflicts of interest between supervisors and consultants")
    print("\tCreate a csv and enter a supervisor into the first cell of a row and input the conflicting consultants")
    print("\t\tinto the following cells on the same row. Repeat for other supervisors who have conflicts")
    print("\t\tone supervisor per row.")
    input("\nPress ENTER to continue\n")
    getSITS()
    print("")
    try:
        readCons()
    except FileNotFoundError:
        errorList.append("ERROR: Cons.csv Not Found")
    except Exception as x:
        errorList.append("UNKNOWN ERROR C" + x)
    try:
        readSups()
    except FileNotFoundError:
        errorList.append("ERROR: Sups.csv Not Found")
    except Exception as x:
        errorList.append("UNKNOWN ERROR S" + x)
    try:
        setConflicts()
    except FileNotFoundError:
        print("WARNING: Conflicts.csv Not Found")
    except ValueError as sup:
        print("\nWARNING: Supervisor", sup, "does not exist in Roster. Please check Conflicts.csv and Sups.csv")
    except Exception as x:
        errorList.append("UNKNOWN ERROR CF" + x)
    try:
        if len(errorList) == 0:
            Assignment()
    except PermissionError:
        errorList.append("ERROR: Unable to write to Results.csv. Close Results.csv if open.")
    except Exception as x:
        errorList.append("UNKNOWN ERROR A" + x)
    for err in errorList:
        print(err)
    input("\nPress ENTER to exit")
    if len(errorList) == 0:
        sys.exit(0)
    else:
        sys.exit(len(errorList))
