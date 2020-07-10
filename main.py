# OIT CR Scheduler

# Parent classes
import csv


class Cons:

    # Instance attributes
    def __init__(self, netID, schedule):
        self.netID = netID
        self.schedule = schedule


class Sups:
    # Instance attributes
    def __init__(self, netID, schedule):
        self.netID = netID
        self.schedule = schedule


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
startTime = 9
endTime = 22
supRoster = []
consRoster = []
#if __name__ == '__main__':
 #   rows, cols = (7, 25)
  #  x = [[0 for i in range(cols)] for j in range(rows)]
   # x[0][0] = 1
    #print(x)

# ------------------------------------->
# Helper Method.
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
    s.start = convert24(start, 1)
    s.end = convert24(end, 0)
    return [s.location, s.dayofWeek, s.start, s.end]


# ------------------------------------->
# Converting 12 Hour to 24 Hour Format
def convert24(str1, check):
    # Checking if last two elements of time is AM
    if str1[-2:] == "PM":
        # add 12 to hours and remove PM
        if str1[:-5] == "11":
            return 23
        print(str1[:-5])
        if str1[:-5] == "12":
            return 12
        str2 = str(int(str1[:-5]) + 12)
        if check == 1:  # Check if Start Time, then go to Ceiling
            x = int(str1[-4:-2])
            if int(str1[-4:-2]) > 0:
                return int(str2) + 1
        return int(str2)

    if check == 1:  # Check if Start Time, then go to Ceiling
        if int(str1[-4:-2]) > 0:
            return int(str1[:-5]) + 1
    return int(str1[:-5])


# ------------------------------------->
# Populate2D Array for Sups.Schedule
def populate2D (arr, location, day, start, end):
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
        arr[6][0]= 1
        i = 6
    for j in range(start+1, end+2):
            arr[i][j]=1

# ------------------------------------->
# Hassaan
# Reads CSV and creates Array of Workers #
# def read_CSV() :
#---------------------------------------------READING CONS --------------------------------->
with open(".\\Cons.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0
    prev = ""
    for row in csv_reader:  # Iterate through every row
        if line_count != 0:  # Make sure not the Top Column
            print(row[0])
            if row[0] == "":  # Error check in case netID field is empty
                line_count += 1
                # print("hello world")
                continue
            if row[0] != prev:  # NetID is the same as last row
                if prev != "":
                    consRoster.append(Cons(new.netID, new.schedule))
                    prev = new.netID
                new = Cons
                print(row[0])
                new.netID = row[0]  # Initialize netID
                new.schedule = []
            [temp1, temp2, temp3, temp4] = create_Shift(row[1], row[3], row[4], row[5])
            new.schedule.append(Shift(temp1, temp2, temp3, temp4))  # Add Shift to the Schedule Array
            prev = new.netID
        line_count += 1
    for x in consRoster:
        print(x.netID)
#------------------------------------------------------------------------------------->
#---------------------------------------------READING SUPS --------------------------------->
with open(".\\Sups.csv") as csv_file2:
    csv_reader = csv.reader(csv_file2, delimiter=',')
    line_count=0
    prev = ""
    for row in csv_reader:  # Iterate through every row
        if line_count != 0:  # Make sure not the Top Column
            print(row[0])
            if row[0] == "":  # Error check in case netID field is empty
                line_count += 1
                # print("hello world")
                continue
            if row[0] != prev:  # NetID is the same as last row
                if prev != "":
                    print(sched)
                    supRoster.append(Sups(netID, sched))
                    prev = new.netID
                print(row[0])
                netID = row[0]  # Initialize netID
                rows, cols = (7,25)
                sched = [[0 for i in range(cols)] for j in range(rows)]
            populate2D(sched,row[1], row[3], row[4], row[5])
            prev = netID
        line_count += 1

# ------------------------------------->
# Day of the Week:
# 0 = Sunday
# 1 =Monday
# 2 = Tuesday
# 3 = Wednesday
# 4= Thursday
# 5 = Friday
# 6 = Saturday
#
# Schedule:
# 0 = ARC
# 1 = BEST
# 2 = Kessler
# 3 = LSM
# Start/End:
# 4 digit 24 hour integer
# (0-23)
# i.e. 1:30PM = 1330

# ------------------------------------->
# Worker and Shift
# WORKER:
# + NetID (String)
# + Schedule (Array of Shifts)
# + Supervisor (bool)
# + addShift(shift): type

# SHIFT:
# + Location (Integer)
# + Day of the Week (Int)
# + Start (Integer)
# + End (Integer)
# + method(type): type


# ------------------------------------->

def priorotizeConsultants(lstCons):
    # List of all Scheduled consultants
    scheduledConsultants = []
    # List of all Unscheduled consultants
    unscheduledConsultants = []

    # print('The total amount of shifts are: ' + str(shiftCount) + '.')
    for obj in range(len(lstCons)):
        iterate = lstCons[obj].schedule
        objNetid = lstCons[obj].netID
        if iterate is None:
            return 'Please check the csv file.'
        for i in range(len(iterate)):
            location = iterate[i].location
            dayofWeek = iterate[i].dayofWeek
            startingShift = iterate[i].start
            endShift = iterate[i].end
            if (location and dayofWeek and startingShift and endShift) is None:
                return 'Please check the csv file'
            if (startingShift >= startTime) and (endShift <= endTime):
                hoursWorked = endShift - startingShift
                scheduledConsultants.append(objNetid)
                scheduledConsultants.append(hoursWorked)
            else:
                sep = 'Unscheduled Consultants: '
                unscheduledConsultants.append(sep)
                nightHoursWorked = endShift - startingShift
                unscheduledConsultants.append(objNetid)
                unscheduledConsultants.append(nightHoursWorked)

    return [scheduledConsultants, unscheduledConsultants]


# ------------------------------------->
# Assignment ()
# Divide lengths of Sup and Cons to get threshold  for each supervisor
# Go through cons list sequentially. For each cons, go through supervisor list.

# ------------------------------------->
def Assignment():
    supFocusedIndex = 0
    for i in range(0, len(consRoster)):
        supFocusedIndex = ranking(consRoster[i])
        supRoster[supFocusedIndex].assignedCons.append(consRoster[i].netID)
    for i in range(0, len(supRoster)):
        print(supRoster[i].netID, ': ', *supRoster[i].assignedCons, sep=", ")


# ------------------------------------->
# Edler:
# ranking()
# count overlapping hours
# between all supervisors and cons
#
# overlapping ARC? +10
# overlapping LSM? +8
# overlapping RBHS + 6
# overlapping BEST? +4
#
# difference in number of consultants assigned to supervisor and consultant threshold (x3)
#
# return index of highest ranking supervisor

def ranking(consultant):
    supCount = len(supRoster);
    rankingArray = [0] * supCount;
    siteWeight = [10, 4, 6, 8];
    tempMax = 0;
    max = 0;
    supIndex = 0;
    # initalvalues for rankingArray
    for i in range(0, supCount):
        rankingArray[i] = rankingArray[i] + (len(rankingArray[i].assignedCons) - consultantThreshold) * 3;
    for i in range(0, len(consultant.Schedule)):
        focusedShift = consultant.Schedule[i];
        for a in range(0, supCount):
            if (1 == supRoster[a].Schedule[focusedShift.Day][0]):
                for hour in range(focusedShift.start + 1, focusedShift.end + 1):
                    if (supRoster[a].Schedule[focusedShift.Day][hour]):
                        rankingArray[a] = rankingArray[a] + 1 + siteWeight[focusedShift.Location];
    supIndex, max = max(rankingArray, key=lambda item: item[1]);
    return supIndex;