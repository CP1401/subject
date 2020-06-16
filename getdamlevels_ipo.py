"""
Get Townsville Ross River Dam Level from Website
Author: Lindsay Ward
This program demonstrates using the requests library to get a website as text
Part of the text is in JSON (JavaScript Object Notation)
so it can easily be converted to a Python dictionary by the json library.
Various string functions are used to extract the desired value, which is printed.

This version shows which parts of the program are Input, Processing and Output.
"""

import json
import requests

URL = "https://mitownsville.service-now.com/webapps/dam_levels.do"
START_STRING = "var ross_last_reading"
DISTANCE_TO_VALUES = 4


def main():
    # INPUT - only the first line
    # Get response text from Council website
    response = requests.get(URL)

    # PROCESSING - we find and extract only the interesting part
    text = response.text
    # print(text)  # Left in for potential debugging to confirm what response is received
    # Extract just the JSON-like string that contains the current data
    start_index = text.find(START_STRING) + len(START_STRING) + DISTANCE_TO_VALUES
    finish_index = text.find("}", start_index) + 1
    section = text[start_index:finish_index].replace("\\", "")
    # Convert JSON text to dictionary
    data = json.loads(section)
    # data looks like {'date': '01/03/2018 09:00:00', 'percent': '63%', 'volume': '146124 ML'}
    # Get the value without the final '%'
    value = data["percent"][:-1]

    # OUTPUT - After all the processing, we can just display the result
    print(value)


main()
