# showmap.py - Launches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip, urllib.parse
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

print("Address:", address)

url = 'https://www.openstreetmap.org/search?query=' + urllib.parse.quote(address)

print("Opening:", url)

webbrowser.open(url)

input("Press Enter to exit...")