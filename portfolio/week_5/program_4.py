""" Write a program that takes a URL as a command-line argument and reports whether there
is a working website at that address.
Hint: You need to get the HTTP response code. Another Hint: StackOverflow is your friend. """

import sys
import requests

def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error! Enter valid url to check status.")
    else:
        url_check = sys.argv[1]
        if check_website(url_check):
            print(f"The website at {url_check} is working.")
        else:
            print(f"There is no working website at {url_check}.")