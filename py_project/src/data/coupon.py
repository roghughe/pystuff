'''

Parse a line of data and return as a list of pairs

Created on 23 Nov 2017

@author: Roger
'''

#Given a line of data, split it into an array of lists
def generate(line):

    retVal = []

    # Creates a list of sub-strings
    list1 = line.split(";")

    for item in list1:
        pair = item.split("=")
        if len(pair) > 1:
            kv = [pair[0], pair[1]]
        else: 
            kv = [pair[0],"NULL"]
        retVal.append(kv)          

    return retVal

