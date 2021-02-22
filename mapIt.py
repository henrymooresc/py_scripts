# Launches google maps using address from the command line or clipboard
import webbrowser, sys, pyperclip

def main():
    # If no command line arg, uses clipboard
    if len(sys.argv) > 1:
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()
    
    # Opens the map
    webbrowser.open('https://www.google.com/maps/place/' + address)

main()