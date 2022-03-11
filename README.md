# ioet_test

Ioet selection process' challenge solution

# Statement

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday

00:01 - 09:00 25 USD

09:01 - 18:00 15 USD

18:01 - 00:00 20 USD

Saturday and Sunday

00:01 - 09:00 30 USD

09:01 - 18:00 20 USD

18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday

TU: Tuesday

WE: Wednesday

TH: Thursday

FR: Friday

SA: Saturday

SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD

# Asumptions

* Worked hours input start and end in 00 (0 minutes)
* If a worker completes a day and still working (e.g Monday 23:00 - Tuesday 01:00), this counts as working two separated days for input purposes (Monday 23:00 - 23:59 AND Tuesday 00:00 - 01:00)
* Since for right limit time, 00:00 and 24:00 belongs to the next day, the correct way to denote a work worked until 00:00 of next day is using 23:59, anyway using 24:00 will work as well. 00:00 will not work according to what is pointed on the previous two points
* If a worker works in two separated time intervals, this is considered as two different input sections (e.g Monday 12:00 - 13:00 AND 14:00 - 15:00, this should be input like Monday 12:00 - 13:00 AND Monday 14:00 - 15:00)

# Considerations

A GIGO approach is used, which means for bad inputs (specially, with bad format), script will return garbage results

# Solution description

Solution is very simple and it works the following way:

* Defines constants (weekdays, working intervals and payments)
* Reads input file from stdin (argv[1])
* Parses input strings (with in statement format)
* Extract indexes from limit times
* Uses indexing to select a sublist from interval payments list
* Performs a sum() of earnings of each day
* Returns sum() result with corresponding ping

# Requirements

Solution's script doesn't rely on any external library, anyway **for testing purposes** `mypy`, `flake8` and `pytest` are required, those can be installed using:

```
pip install -r requirements_dev.txt
```

# Running

Example input strings are contained on hours.txt file, so assuming we want to read this input we run calculate_payments.py in `src/payhours` folder running (from this folder): 

```
python calculate_payments.py ../../hours.txt
```

# Testing

For running tests, with installed requirements run:

For installing script as package:
```
pip install -e .
```
For running mypy tests:
```
mypy src
```
For running flake8 tests:
```
flake8 src
```
For running pytest tests:
```
pytest
```
For testing in different environments with different python versions, run:
```
tox
```

Github actions are configured as well, so automated tests will run with every pull request :)
