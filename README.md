Python Random List and Phone Number Converter
Overview
This Python script offers two primary functions: generating a random list of integers and converting a phone number into a corresponding string of words. It consists of two tasks, each providing a unique utility.

Task 1: Random List Generation
Generates a list of random integers based on user input.
Calculates and displays the average value of the integers in the list.
Task 2: Phone Number to Text Conversion
Converts a user-inputted phone number in the format XXX-XXX-XXXX to a string of words.
Each digit is translated to its corresponding word (e.g., 1 becomes 'one').
Requirements
Python 3.x
No external libraries are required as the script uses the built-in random module.
Usage
Running the Script
Execute the script in a Python environment.
Use the command python script_name.py if running from a command-line interface.
Task 1: Random List Generation
When prompted, enter the desired size of the random list (as an integer).
Enter the maximum integer value to be included in the list.
The script will display the generated random list and its average value.
Task 2: Phone Number to Text Conversion
When prompted, enter a phone number in the format XXX-XXX-XXXX.
The script will display the phone number as a list of individual characters, then as a list of corresponding words, and finally as a string of words connected by '->'.
Exiting the Script
Press enter when prompted to exit the script.
Notes
The random list in Task 1 is generated using random.sample, ensuring that all integers in the list are unique.
The phone number conversion in Task 2 uses a predefined dictionary to map digits and the dash symbol to words.
Limitations
Task 1 requires that the maximum integer value be equal to or greater than the list size, as it relies on sampling without replacement.
Task 2 strictly expects the phone number format to be XXX-XXX-XXXX, including dashes.
Author Melika Sherafat
