# OIT CR Scheduler

# Parent classes
import csv
import config
import array

worker = []


class Cons:

    # Instance attributes
    def __init__(self, netID, schedule):
        self.netID = netID
        self.schedule = schedule


class Shift:

    # Instance attributes
    def __init__(self, location, dayofWeek, start, end):
        self.location = location
        self.dayofWeek = dayofWeek
        self.start = start
        self.end = end


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

# ----------------------------------------------------------------------#

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


# ----------------------------------------------------------------------#
# Joel:
# prioritizeCons()
# Sorts cons array based on if they work during supervisor hours and how many shifts they have
#
# Use sort method based off length of worker Schedule Array
#

# Those who work outside of supervisor hours (2000 - 200 next day) can be moved to bottom of list

# Made Worker class and set the proper parameters

def prioritizecons(worker):

    # Conventional hours a supervisor would work in military time. (8:00am - 10:00pm)
    hourMorningSup = 800
    hourNightSup = 2200

    for i in worker:
        if (i >= hourMorningSup) and (i <= hourNightSup):
            conAvailable = netID
            message = "The consultant available during today's hours are: "
            print( message + str(conAvailable))
        else:
            conAvailable = netID
            message = "Find another time for these consultants: "
            print(message + str(conAvailable))



# ----------------------------------------------------------------------#
# Assignment ()
# Divide lengths of Sup and Cons to get threshold  for each supervisor
#
# Go through cons list sequentially. For each cons, go through supervisor list.

# ----------------------------------------------------------------------#

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
# return highest ranking supervisor
# OIT CR Scheduler


## Adding times and netIDs"
worker = ['albelee, 1100, 1200']
prioritizecons(worker)
