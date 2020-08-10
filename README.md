<h1 align="center">Consultant Review Scheduler </h1>

This program schedules consultants and supervisors for a Consultant Review meeting based on location, number of hours worked, and availability.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
- [Installation](#installation)
- [Documentation](#documentation)
  - [Content](#content)
  - [Definitions](#definitions)
  - [create_Shift()](#create_shift)
  - [convert24()](#convert24)
  - [populate2D()](#populate2d)
  - [search()](#search)
  - [readCons()](#readcons)
  - [readSups()](#readsups)
  - [prioritizeConultants()](#prioritizeconultants)
  - [Assignment()](#assignment)
  - [ranking()](#ranking)
  - [setConflicts()](#setconflicts)
  - [getSITS()](#getsits)
  - [main()](#main)

## Requirements

- Have the latest version of [Python](https://www.python.org/downloads/) installed. This program is written in `Python 3.8.2`.
- Install [Git](https://git-scm.com/) to clone this repository and update live changes to the script.
- Install a [Text Editor or an IDE](https://www.fullstackpython.com/text-editors-ides.html) to edit the program. The team recommends: [Visual Studio Code](https://code.visualstudio.com/) or [Pycharm](https://www.jetbrains.com/pycharm/).

## Installation

After installing the requirements, use your terminal/IDE to install the program by simply cloning the repository:

```
git clone https://github.com/loej/CR-Scheduler.git
```

Navigate to the created folder:

```
cd CR-Scheduler
```

List all the files in the CR-Scheduler directory:

```
ls
```

Now you should be able to view all the files. The file with the script is `main.py`. You can now open this file using your IDE/Text editor of choice.

The csv files that are currently in this repository are just examples to run with the current script. To run your own csv files name each csv appropriatley but with its respective information.

## Documentation

While you review the program the team highly recommends having an understanding of basic programming concepts. Please visit the [Python Documentation](https://docs.python.org/3/) if any concepts remain unclear.

### Content

The CR Scheduler program contains:

- 3 Classes

  - class Cons:
  - class Sups:
  - class Shift:

- 10 Methods

  - [create_Shift()](#create_shift)
  - [convert24()](#convert24)
  - [populate2D()](#populate2d)
  - [search()](#search)
  - [readCons()](#readcons)
  - [readSups()](#readsups)
  - [prioritizeConultants()](#prioritizeconultants) 
  - [Assignment()](#assignment)
  - [ranking()](#ranking)
  - [setConflicts()](#setconflicts)

Each class and method will be documented thoroughly.

### Definitions

Day of the Week:

- 0 = Sunday
- 1 = Monday
- 2 = Tuesday
- 3 = Wednesday
- 4= Thursday
- 5 = Friday
- 6 = Saturday

Locations :

- 0 = ARC
- 1 = BEST
- 2 = Kessler
- 3 = LSM

### create_Shift()

- ```create_Shift()``` takes in the location, day of week, and the start and end of a shift. It filters each location and translates it to a numerical value as shown above. This method simply takes each case as a day of the week and translates it. Towards the end you should see that it converts the start and end dat to a 24-hour format. Finally, it returns the refined location, dayofWeek, and start and end in a 24-hour format as one list. 

### convert24()

- ```convert24()``` takes in a string and a time check. The string 'time' is indicated if the time is either the start or end. Conventionally, start = 1 and end = 0. The hour variable is an integer from the start of the list up to but not including the colon index. The minute starts from the colonIndex up to but not including -2 index of the list. The first if - else block checks if the index -2 contains "PM". If it doesn't it switches the boolean from T/F. The second if-else block uses the boolean check to convert the hours into a 24 hour format. 

### populate2D()

- ```populate2D()``` populates an array for the supervisor schedules. It starts by converting the start and end time of the shifts to a 24-hour format using ```convert24()```. For each day there is a a 2D array with both index representing the day. The first index is the day of the week starting with Sunday. The for-loop loops through the array index of j and sets all of j index to 1.

### search()

- ```search()``` is a helper method that takes in a target and a roster. It loops through the roster and if the target's netID is located then it returns the roster's index. If it doesn't it returns None and the last items in the list. 

### readCons()

- ```readCons()``` is a method that reads the Cons.csv. Using a for-loop, the iterated file checks for empty indexes, empty columns, and repeated netIDs. Once it completes each check it appends the netID, schedule, and hours to the consRoster. After, a new.NetID is initialized in ```row[0]``` and also creates a new list of the schedule. A list of temporary values are assigned to the ```create_shift()``` method to populate the rows. Then it is appended to the new schedule. 
 
### readSups()
- ```readSups()``` reads the sups.csv file. It initiates the hours count, a temporary list, temporary index, and temporary netID. The next two lines initiate the rows and columns for the csv file; the list also uses two for loops to fill in the rows and columns. ```readSups()``` then reads the Sups.csv file and loops through the list from 1 to the length of the supervisor list. ```line 231```. After, the script checks for the following cases: if the ``supList[idx][0] == ""`` is empty, if ``supList[idx][0] in sitRoster`` contains an SIT, and finally the last else statement populates the 2D array. 

### prioritizeConultants()

- Prioritize  Consultants takes in the list ```consRoster[]``` and schedules them off of location, dayofWeek, startingShift, and endShift. It sorts both types of consultants: ```scheduled[]``` and ```unscheduled[]``` consultants. Unscheduled consultants are not able to meet the criteria to meet a supervisor between the times they work. This method return a list of both scheduled and unscheduled consultants: ```[scheduledConsultants, unscheduledConsultants]```.

### Assignment()

- ```Assignment()``` accesses the amount of consultants every supervisor can be assigned to; this method divides the length of supervisor and cons to get the threshold for each supervisor. ```Assignment()``` uses ```prioritizeCons()``` to prioritize the ```consRoster``` list. The first for-loop loops through the list to use ```ranking()``` on the scheduled consultants. Then, it appends the supervisor roster the assigned consultants. For **any** unscheduled consultant, a list is crated in order to filter out the unscheduled consultants. Finally, the last for- loop sorts the supervisor roster ```sup.assignedCons.sort()```.  The final block puts adds the results to a new csv file called ```Results.csv```. 

### ranking()

- The ```ranking()``` method takes in the ```consultant``` object. The first variable floors and divides the length of both the ```consRoster``` and ```supRoster```. Every location/site is weighed in a rank from ```10, 4, 6, and 8```. The first for-loop checks if the consultant netID is on the ```supRoster[i].noGoodCons```. If not it sets the list to ```rankingArray[i] + (consultantThreshold - len(supRoster[i].assignedCons)) * 25```. After, the second for-loop loops through the consultant schedule and the supervisor count. The third for-loop checks if the supervisor hour in the day of the week matches. It updates the ```rankingArray``` with the information once the shift location is set. Finally, the ``supIndex`` variable is updated with the ``rankingArray``. 
  
### setConflicts()

- The `setConflicts()` method iterates through every single conflict set by the user. It reads the csv and iterates through every row. It checks for the length of the row and appends the conflicts: `tempSup.noGoodCons.append(r[b])`.


###  getSITS()

- For current SITs, we need to filter them at the beginning of the process. ```getSITS()``` does this task by having the user input the netID's of the SITs. Then a while-loop is used with a try-catch error that then appends all of the SIT's netID's to the sitRoster. 

### main()

- The main method is what the user uses to input any information; e.g. SITs or consultant conflicts. It also reminds the user to double check if the folder in which the executable is in has important csv files. The main method also calls the methods from above to run the program  and check for any errors. 