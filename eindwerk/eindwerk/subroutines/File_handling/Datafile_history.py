"""
This tracks the last 30 datafiles that are stored in datafile_history.txt .
Filtering is added to avoid duplicates.
"""

history_file = '../../resources/Files/datafile_history.txt'
max_nr_files = 30

import os
import csv

def test():
    testlist = ['Jan\r\n','Piet\r\n','Klaas\r\n']
    # testlist = ['Jan\n','Piet\n','Klaas\n']
    # testlist = [line.strip(os.linesep) for line in testlist]
    testlist = [line.strip() for line in testlist]
    print("testlist: ", testlist)

def Datafile_history(filepath):
    # Read the datafile_history
    with open(history_file, 'r') as f:
        history = f.readlines()
        history = [line.strip() for line in history]
        print("history :", history)
    # check that file is new and place it at beginning
    if filepath not in history:
        history.insert(0, filepath)
        surplus = len(history) - max_nr_files
        print('new file', history)
        # Cut file array if above max_nr_files
        if surplus >0:
            del history[-surplus:]
        # Add the EOLs again
        #history = [line+os.linesep for line in history]
        # history = '\n'.join(history)
        history = (os.linesep).join(history)
        print('updated file', history)
        # Write data back to file
        with open(history_file, 'w') as f:
            f.writelines(history)
    # f.close()

if __name__ == "__main__":
    filepath = 'C:/Users/mulderg/Downloads/10_October6.csv'
    # Datafile_history(filepath)
    test()
