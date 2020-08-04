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
  - [readCSV()](#readcsv)
  - [ranking()](#ranking)
  - [setConflicts()](#setconflicts)

## Requirements

- Have the latest version of [Python](https://www.python.org/downloads/) installed. This program is written in `Python 3.8.X`.
- Install [Git](https://git-scm.com/) to clone this repository and update live changes to the script.
- Install a [Text Editor or an IDE](https://www.fullstackpython.com/text-editors-ides.html) to edit the program. The team recommends: [Visual Studio Code](https://code.visualstudio.com/) or [Pycharm](https://www.jetbrains.com/pycharm/).

## Installation

After installing the requirements, use the terminal to install the program by simply cloning the repository:

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

Each class and method will be documented thorouhgly.

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

- create_Shift() takes in the location, day of week, and the start and end of a shift. It filters each location and translates it to a numerical value as shown above. This method simply takes each case as a day of the week and translates it. Towards the end you should see that it converts the start and end dat to a 24-hour format. Finally, it returns the refined location, dayofWeek, and start and end in a 24-hour format as one list. 

### convert24()

- convert24() takes in a string and a time check. The string 'time' is indicated if the time is either the start or end. Conventionally, start = 1 and end = 0. The hour variable is an integer from the start of the list up to but not including the colon index. The minute starts from the colonIndex up to but not including -2 index of the list. The first if - else block checks if the index -2 contains "PM". If it doesn't it switches the boolean from T/F. The second if-else block uses the boolean check to convert the hours into a 24 hurs format. 

### populate2D()

- populate2D() populates an array for the supervisor schedules. It starts by converting the start and end time of the shifts to a 24-hour format using convert24(). For each day there is a a 2D array with both index representing the day. The first index is the day of the week starting with Sunday. The for-loop loops through the array index of j and sets all of j index to 1.

### search()

- search() is a helper method that takes in a target and a roster. It loops through the roster and if the target's netID is located then it returns the roster's index. If it doesn't it returns None and the last items in the list. 

### readCons()

- readCons() is a method that reads the Cons.csv. Using a for-loop, the iterated file checks for empty indexes, empty columns, and repeated netIDs. Once it completes each check it appends the netID, schedule, and hours to the consRoster. After, a new.NetID is initialized in row[0] and also creates a new list of the schedule. A list of temporary values are assigned to the create_shift() method to populate the rows. Then it is appended to the new schedule. 
 
### readSups()
- wip

### prioritizeConultants()

- Proritize Consultants takes in the list consRoster[] and schedules them off of location, dayofWeek, startingShift, and endShift. It sorts both types of consultants: scheduled[] and unscheduled[] consultants. Unscheduled consultants are not able to meet the criteria to meet a supervisor between the times they work. This method return a list of both scheduled and unscheduled consultants: [scheduledConsultants, unscheduledConsultants].

### Assignment()

- wip

### readCSV()

- wip

### ranking()

- wip

### setConflicts()

- wip
