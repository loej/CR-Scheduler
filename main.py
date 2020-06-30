# OIT CR Scheduler

# Parent classes
import this
import csv
import config

class Cons:

    #Instance attributes
    def __init__(netID,schedule):
        this.netID = netID
        this.schedule = schedule

class Shift:

    #Instance attributes
    def __init__(location,dayofWeek,start,end):
        this.location =location
        this.dayofWeek = dayofWeek
        this.start  = start
        this.end = end






# Hassaan:
# Reads CSV and creates Array of Workers #

#
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
#
# Start/End:
# 4 digit 24 hour integer
#
# i.e. 1:30PM = 1330

#----------------------------------------------------------------------#

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






#----------------------------------------------------------------------#
# Joel:
# prioritizeCons()
# Sorts cons array based on if they work during supervisor hours and how many shifts they have
#
# Use sort method based off length of worker Schedule Array
#
# Those who work outside of supervisor hours (2000 - 200 next day) can be moved to bottom of list

def prioritizeCons():
    global arr1[]






#----------------------------------------------------------------------#

# Assignment ()
# Divide lengths of Sup and Cons to get threshold  for each supervisor
#
# Go through cons list sequentially. For each cons, go through supervisor list.
def Assignment():
    supFocusedIndex=0;
    for i in range(0,len(consRoster)):
        supFocusedIndex=ranking(consRoster[i]);
        supRoster[supFocusedIndex].assignedCons.append(consRoster[i].netID);
    for i in range(0,len(supRoster)):
        print(supRoster[i].netID,': ',*supRoster[i].assignedCons,sep=", ");
#----------------------------------------------------------------------#

# Edler:
# ranking()
# count overlapping hours
#  between all supervisors and cons
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
    supCount=len(supRoster);
    rankingArray = [0]*supCount;
    siteWeight= [10,4,6,8];
    tempMax=0;
    max=0;
    supIndex=0;
    #initalvalues for rankingArray
    for i in range(0,supCount):
        rankingArray[i]=rankingArray[i]+(len(rankingArray[i].assignedCons)-consultantThreshold)*3;
    for i in range(0,len(consultant.Schedule)):
        focusedShift=consultant.Schedule[i];
        for a in range(0,supCount):
            if(1==supRoster[a].Schedule[focusedShift.Day][0]):
                for hour in range(focusedShift.start+1,focusedShift.end+1):
                    if(supRoster[a].Schedule[focusedShift.Day][hour]):
                        rankingArray[a]=rankingArray[a]+1+siteWeight[focusedShift.Location];
    supIndex,max=max(rankingArray,key=lambda item:item[1]);
    return supIndex;



