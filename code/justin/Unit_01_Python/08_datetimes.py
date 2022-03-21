# Full Stack Bootcamp - Unit 01 Practice 08
# Justin Hammond, 01/05/2022

from datetime import date, datetime


# Create Date ==================================================================
# Write a function that creates and returns a new datetime given the components

def create_date(month, day, year):
    return f"{datetime(year, month, day)}"

def test_create_date():
    assert create_date(4, 20, 2021) == '2021-04-20 00:00:00'

# print(create_date(4, 20, 2021)) # 2021-04-20 00:00:00


# Get Year =====================================================================
# Write a function that returns the year of a given datetime

def get_year(dt):
    return dt.year

def test_get_year():
    assert get_year(datetime(2021, 4, 20)) == 2021

# print(get_year(datetime(2021, 4, 20))) # 2021


# Parse Date ===================================================================
# Write a function that converts the given string into a datetime

def parse_date(date_string):
    date_format = "%B %d, %Y"
    return f"{datetime.strptime(date_string, date_format)}"

def test_parse_date():
    assert parse_date('April 20, 2021') ==  '2021-04-20 00:00:00'
# print(parse_date('April 20, 2021')) # 2021-04-20 00:00:00


# Parse Datetime ===============================================================
# Write a function that converts a given string into a datetime
def parse_datetime(date_string):
    date_format = "%B %d, %Y %I:%M %p"
    return f"{datetime.strptime(date_string, date_format)}"

def test_parse_datetime():
    assert parse_datetime('April 20, 2021 09:30 AM') == '2021-04-20 09:30:00'
# print(parse_datetime('April 20, 2021 09:30 AM')) # 2021-04-20 09:30:00


# Format Datetime ==============================================================
# Write a function that converts the given datetime into a string
def format_datetime(dt):
    return f"{dt}"

def test_format_datetime():
    format_datetime(datetime(2021, 4, 20, 9, 30)) == '2021-04-20 09:30:00'
# print(format_datetime(datetime(2021, 4, 20, 9, 30)))