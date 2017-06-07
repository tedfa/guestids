# guestids

These scripts were created to simplify the repetative process of resetting guest log-ins for use by visitors at Hodges Library. 

These scripts were written in Python3.

* logins.py - creates the dictionary where the log-in information is stored.
* dictlook.py - just allows user to see current passwords and has commented out code to change a single (or more) password in the local data structure.
* webscripts.py - function that utilizes the selenium module to navigate to OIT password reset website and actually change the passwords for each guest ID.
* gid4.py - This script is the main flow of control. It prompts the user for which IDs to reset, calls the selenium function, and creates the file that is printed and then handed out to guest users in the library.
 

To use:

1. Download all scripts to a single directory.
2. Make sure you have a mark down editor like MacDown. 
3. Run logins.py to initialize data structure. 
4. Open dictlook.py in text editor to make appropriate updates to the current passwords.
5. Run gid4.py
6. Open login.md file and print