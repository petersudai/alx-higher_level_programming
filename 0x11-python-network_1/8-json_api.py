#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}

    try:
        response = requests.post(
            "http://0.0.0.0:5000/search_user",
            data=payload
        )
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
