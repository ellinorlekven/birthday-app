
"""
age_utils.py

This module contains utility functions for processing family-related data, 
such as calculating ages, dates of birth, and jubilees for family members.

The module includes the following functions:
- get_age_in_days(birthdate): Calculate the age in days from a given birthdate to the current date.
- date_2_doy(input_date): Convert a given date to the day of the year (DOY).
- doy_2_date(day_of_year, year): Convert the day of the year (DOY) 
  to a specific date in the given year.
- get_average_dob(family_dict): Calculate the average date of birth for a family.
- get_total_age(family_dict): Calculate the total age of a family in years, weeks, and days.
- get_average_age(family_dict): Calculate the average age of a family in years, weeks, and days.
- get_familiy_jubilee(family_dict, jubilee_dict): Calculate family jubilees based on a jubilee dictionary.
- get_converted_age(family_dict): Convert the ages of family members into a human-readable format.

Note: This module uses the `datetime` module for date-related calculations.

Author: Your Name
Date: Date of creation or last modification
"""

from datetime import date, timedelta, datetime

def get_age_in_days(birthdate):
    """Calculate the age in days from the birthdate to the current date.

    Parameters:
    birthdate (datetime.date): The birthdate of the person.

    Returns:
    int: The age in days.
    """
    current_year = datetime.now().date()
    age = (current_year - birthdate).days
    return age


def date_2_doy(input_date):
    """Convert a given date to the day of the year (DOY) starting from 0.

    Parameters:
    input_date (datetime.date): The input date.

    Returns:
    int: The day of the year (DOY) starting from 0.
    """
    day_of_year = input_date.timetuple().tm_yday - 1
    return day_of_year


def doy_2_date(day_of_year, year = datetime.now().year):
    """Convert the day of the year (DOY) back to the date.

    Parameters:
    day_of_year (int): The day of the year (DOY) starting from 0.
    year (int): The year for which to calculate the date (optional, default is the current year).

    Returns:
    str: The result date in "YYYY-MM-DD" format.
    """
    first_day = datetime(year, 1, 1)
    date_of_year = first_day + timedelta(days=day_of_year - 1)
    result_date = date_of_year.strftime("%Y-%m-%d")
    return result_date


def get_average_dob(family_dict):
    """Calculate the average date of birth for a given family.

    Parameters:
    family_dict (dict): A dictionary containing family members' names 
    as keys and their birthdates as values.

    Returns:
    tuple: A tuple containing a string with the output message and t
    he average date of birth in "YYYY-MM-DD" format.
    """
    dob_lst = []
    for member in family_dict:
        birthdate = family_dict.get(member)
        dob = date_2_doy(birthdate)
        dob_lst.append(dob)
    lst_sum = sum(dob_lst)
    lst_length = len(dob_lst)
    if lst_length == 0:
        return 0  # To avoid division by zero for an empty list
    average = round(lst_sum/lst_length)
    average_dob = doy_2_date(average)
    output_message = f'The family\'s average date of birth is {average_dob}'
    return output_message, average_dob



def get_total_age(family_dict):
    """Calculate the total age of a given family.

    Parameters:
    family_dict (dict): A dictionary containing family members' names 
    as keys and their birthdates as values.

    Returns:
    tuple: A tuple containing the total years, weeks, days, and total age in days.
    """
    age_lst = []
    for member in family_dict:
        birthdate = family_dict.get(member)
        age_in_days = get_age_in_days(birthdate)
        age_lst.append(age_in_days)
    total_age_in_days = sum(age_lst)
    # Total year in:
    years = int(total_age_in_days/365.242199)
    weeks = int((total_age_in_days%365.242199)/7)
    days = int((total_age_in_days%365.242199)%7)
    return (years, weeks, days, total_age_in_days)

def get_average_age(family_dict):
    """Calculate the average age of a given family.

    Parameters:
    family_dict (dict): A dictionary containing family members' names 
    as keys and their birthdates as values.

    Returns:
    tuple: A tuple containing the average years, weeks, days, and average age in days.
    """

    age_lst = []
    for member in family_dict:
        birthdate = family_dict.get(member)
        age_in_days = get_age_in_days(birthdate)
        age_lst.append(age_in_days)
    total_age_in_days = sum(age_lst)
    family_members = len(family_dict)
    average_age_in_days = round(total_age_in_days/family_members)
    # Average age in:
    years = int(average_age_in_days/365.242199)
    weeks = int((average_age_in_days%365.242199)/7)
    days = int((average_age_in_days%365.242199)%7)
    # if family_dict == 0:
    #     output_message = f'There are no birthdays in the list {family_dict}'
    # else:
    return (years, weeks, days, average_age_in_days)


def get_familiy_jubilee(family_dict, jubilee_dict):
    """Find family members who will reach certain jubilee ages.

    Parameters:
    family_dict (dict): A dictionary containing family members' names 
    as keys and their birthdates as values.
    jubilee_dict (dict): A dictionary containing jubilee age thresholds 
    as keys and the corresponding days as values.

    Returns:
    dict: A dictionary containing family members' names as keys and 
    tuples with days until jubilee and jubilee dates as values.
    """
    jub_dict = {}
    today =  date.today()
    fam_age_days = get_total_age(family_dict)[3]
    dev = len(family_dict)
    for key, value in jubilee_dict.items():
        if value > fam_age_days:
            diff = value - fam_age_days
            days_until_jub = round(diff/dev)
            jub_date = today + timedelta(days= days_until_jub)
            jub_dict[key] = (days_until_jub, jub_date)
    return jub_dict

def get_converted_age(family_dict):
    """Convert the ages of family members into formatted age strings.

    Parameters:
    family_dict (dict): A dictionary containing family members' names 
    as keys and their birthdates as values.

    Returns:
    dict: A dictionary with formatted age strings for each family member.
    """
    today = date.today()
    age_data = {} # Empty dict
    for member in family_dict:
        birthdate = family_dict.get(member)
        age_in_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        months = (today.month - birthdate.month - (today.day < birthdate.day)) %12
        age = today - birthdate
        age_in_days = age.days
        if age_in_years >= 80:
            formatted_age = "80 years or older"
        elif age_in_years >= 12:
            formatted_age = f"{age_in_years} years"
        elif age_in_years >= 2:
            half = 'and a half ' if months > 6 else ''
            formatted_age = f"{age_in_years} {half}years"
        elif months >= 6:
            formatted_age = f"{months} months"
        elif age_in_days >= 14:
            formatted_age = f"{age_in_days // 7} weeks"
        else:
            formatted_age = f"{age_in_days} days"

        age_data[member] = formatted_age # Fill dict

    return age_data