# OIT CR-SCHEDULER
# Documentation in the Github README.md: https://github.com/loej/CR-Scheduler/blob/master/README.md
#Imports:
import csv
import math
# More info: https://docs.python.org/3/library/operator.html
import operator


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
        self.assignedCons = [];
        self.noGoodCons = [];


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
# Sets global times.
startTime = 9
endTime = 22
# Empty lists for supervisor and consultant rosters.
supRoster = []
consRoster = []

# Creates shift based of location, day of week, and start and end shift times.
def create_Shift(location, dayofWeek, start, end):
    s = Shift
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
    s.start = convert24(start, 1)
    s.end = convert24(end, 0)
    return [s.location, s.dayofWeek, s.start, s.end]

# Converts from 12 hour format to 24 hour format.
def convert24(str1, check):
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

    # Check if Start Time, then go to Ceiling
    if check == 1:
        if int(str1[-4:-2]) > 0:
            return int(str1[:-5]) + 1
    return int(str1[:-5])

# Populate2D Array for Sups.Schedule.
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
    for j in range(start + 1, end + 2):
        arr[i][j] = 1

# Reads cons.csv file
with open(".\\Cons.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    prev = ""
    hoursCount = 0;
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
                    prev = new.netID
                new = Cons
                #   print(row[0])
                new.netID = row[0]  # Initialize netID
                new.schedule = []
            [temp1, temp2, temp3, temp4] = create_Shift(row[1], row[3], row[4], row[5])
            new.schedule.append(Shift(temp1, temp2, temp3, temp4))  # Add Shift to the Schedule Array
            hoursCount += temp4 - temp3;
            prev = new.netID
        line_count += 1
    consRoster.append(Cons(new.netID, new.schedule, hoursCount))
    hoursCount = 0;

# Reads Sups.csv file
with open(".\\Sups.csv") as csv_file2:
    csv_reader = csv.reader(csv_file2, delimiter=',')
    line_count = 0
    prev = ""
    for row in csv_reader:  # Iterate through every row
        if line_count != 0:  # Make sure not the Top Column
            # print(row[0])
            if row[0] == "":  # Error check in case netID field is empty
                line_count += 1
                # print("hello world")
                continue
            if row[0] != prev:  # NetID is the same as last row
                if prev != "":
                    #  print(sched)
                    supRoster.append(Sups(netID, sched))
                    prev = new.netID
                #   print(row[0])
                netID = row[0]  # Initialize netID
                rows, cols = (7, 25)
                sched = [[0 for i in range(cols)] for j in range(rows)]
            populate2D(sched, row[1], row[3], row[4], row[5])
            prev = netID
        line_count += 1
    supRoster.append(Sups(netID, sched))

# Sorts consultants to prioritize them
def priorotizeConsultants(lstCons):
    # List of all Scheduled consultants.
    scheduledConsultants = []
    # List of all Unscheduled consultants.
    unscheduledConsultants = []
    # Checks for a working supervisor. Set False by default.
    workingDuringSup = False
    # Empty dictionary that gets appended.
    consDictionary = {}
    # First for-loop that loops through any list; in this case it's the @consRoster list.
    for obj in range(len(lstCons)):
        # Variable that holds the schedule from the Cons() class.
        iterate = lstCons[obj].schedule
        # Variable that holds the netID from the Cons() class.
        objNetid = lstCons[obj].netID
        # Checks if the variable iterating holds no values.
        if iterate is None:
            return 'ERROR: There is an error in the CSV file.'
        # Second for-loop that loops through the list inside consRoster.
        for i in range(len(iterate)):
            # Every variable in this list points to a the location, day of week,
            # and the start end end of the shfit located in the Shift() class.
            location = iterate[i].location
            dayofWeek = iterate[i].dayofWeek
            startingShift = iterate[i].start
            endShift = iterate[i].end
            #  Checks if the variable iterating holds no values.
            if (location and dayofWeek and startingShift and endShift) is None:
                return 'ERROR: There is an error in the CSV file.'
            # Checks threshold if the consultants work from startingShift to endShift
            elif (startingShift >= startTime) and (endShift <= endTime):
                # If they pass the threshold the boolean value will
                workingDuringSup = True;
        # If the opposite is true, append the unscheduled consultants from the Cons() class.
        if (not (workingDuringSup)):
            unscheduledConsultants.append(Cons(lstCons[obj].netID, lstCons[obj].schedule, lstCons[obj].totalHours))
        else:
            consDictionary[objNetid] = lstCons[obj].totalHours;
            workingDuringSup = False;
    sortedCons = dict(sorted(consDictionary.items(), key=operator.itemgetter(1)));
    for cons in sortedCons.keys():
        for i in range(len(lstCons)):
            if (cons == lstCons[i].netID):
                scheduledConsultants.append(Cons(lstCons[i].netID, lstCons[i].schedule, lstCons[i].totalHours));
                break;
    return [scheduledConsultants, unscheduledConsultants]



# Assigns consultants to Supervisors.
def Assignment():
    [schedCons, unschedCons] = priorotizeConsultants(consRoster);
    supD = {};
    for i in range(0, len(schedCons)):
        supFocusedIndex = ranking(schedCons[i])
        supRoster[supFocusedIndex].assignedCons.append(schedCons[i].netID)
    for cons in unschedCons:
        for sup in supRoster:
            supD[sup.netID] = len(sup.assignedCons);
        sortedSupD = dict(sorted(supD.items(), key=operator.itemgetter(1)));
        for i in range(len(supRoster)):
            keyList = list(sortedSupD.keys())
            if (keyList[0] == supRoster[i].netID):
                supRoster[i].assignedCons.append(cons.netID);
                break;

    # Outputs information to CSV
    for i in range(0, len(supRoster)):
        print(supRoster[i].netID, ': ', *supRoster[i].assignedCons, sep=", ")

def ranking(consultant):
    consultantThreshold = math.floor(len(consRoster) / len(supRoster))
    supCount = len(supRoster)
    rankingArray = [0] * supCount
    siteWeight = [10, 4, 6, 8]
    tempMax = 0
    maxLOL = 0
    supIndex = 0
    # initalvalues for rankingArray
    for i in range(0, supCount):
        if (consultant.netID in supRoster[i].noGoodCons):
            rankingArray[i] = -999999;
        else:
            rankingArray[i] = rankingArray[i] + (consultantThreshold - len(supRoster[i].assignedCons)) * 20
    for i in range(0, len(consultant.schedule)):
        focusedShift = consultant.schedule[i]
        for a in range(0, supCount):
            if (1 == supRoster[a].schedule[focusedShift.dayofWeek][0]):
                for hour in range(focusedShift.start + 1, focusedShift.end + 1):
                    if (supRoster[a].schedule[focusedShift.dayofWeek][hour]):
                        rankingArray[a] = rankingArray[a] + 1 + siteWeight[focusedShift.location]
    # supIndex, max = max(rankingArray, key=lambda item: item[1]);
    supIndex = rankingArray.index(max(rankingArray))
    return supIndex

# Detects conflicts to manually input
def setConflicts():
    temp = "1";
    for i in range(0, len(supRoster)):
        while (temp != "0"):
            print("\nConflicting Consultants for ", supRoster[i].netID, ": ", supRoster[i].noGoodCons);
            temp = input("Input NetID of conflicting consultant with " + supRoster[
                i].netID + "\nif there are no further conflicts,enter 0\n");
            if (temp != "0"):
                supRoster[i].noGoodCons.append(temp);
        temp = "1";

# Main method
if __name__ == '__main__':
    setConflicts();
    Assignment();

