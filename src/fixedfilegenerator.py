import json
import random
import string
import os

FIXED = 'fixed.txt'
CSV = 'snake.csv'
JSON = 'spec.json'



#This function is used to read the JSON file and return the python dictionary as a result set
def readJSON(jsonfile):
    with open(jsonfile) as jsonfile:
        try:
            return json.load(jsonfile)
        except Exception as e:
            print("Issue found", e)
            return None


#This function is used to generate a file with extension csv with the required delimiter provided
def generatecsvfile(columnwidths,delimiter=",",encoding=None):
    fxfile = None
    csvfile = None
    try:
        with open(FIXED) as fxfile:
            csvfile = open(CSV, 'w', encoding=encoding)
            for rec in fxfile.readlines():
                rec = splitstrascsv(rec, columnwidths,delimiter)
                csvfile.write(rec)
                csvfile.write("\n")
        return True
    except Exception as e:
        print("Issue found :", e)
        return False
    finally:
        if fxfile != None and csvfile != None:
            fxfile.close()
            csvfile.close()


# Logic to split the file and generate the delimiter record
def splitstrascsv(rec, columnwidths,delimiter=','):
    finalstr = ""
    for j in columnwidths:
        resultstr = rec[:int(j)]
        finalstr = finalstr + resultstr + delimiter
        rec = rec[int(j):]
    finalstr = finalstr[:len(finalstr) - len(delimiter)]
    return finalstr


# The below function is used to generate a fixed text file with the required specifications including headers

def generatefixedwidthfile(columnwidths, columnheadings, nooflines=1, encoding=None):
    fxdlenfile = None
    try:
        fxdlenfile = open(FIXED, "w", encoding=encoding)
        columnheaderswithoffsets = getfixedcolumnoffsets(columnwidths, columnheadings)
        fxdlenfile.write(columnheaderswithoffsets)
        fxdlenfile.write('\n')
        # iterate the number of records to be inserted
        for lines in range(nooflines):
            lst = []
            # iterate number of columns to be iterated
            for i in range(len(columnwidths)):
                str = ""
                # Generate the random characters based on the column widths specifed
                for j in range(int(columnwidths[i])):
                    str = str + generaterandomchar()
                lst.append(str)
            # Write each record in to the file by looping the result lst.
            for rec in lst:
                fxdlenfile.write(rec)
            fxdlenfile.write('\n')
        return True
    except Exception as e:
        print("Issue found ", e)
        return False
    finally:
        if fxdlenfile != None:
            fxdlenfile.close()


#Below fumction is used to generate the result string with Column Header with the required offsets
def getfixedcolumnoffsets(columnwidths, columnheadings):
    offsets = map(int, columnwidths)
    resultstr = ("".join("%*s" % i for i in zip(offsets, columnheadings)))
    return resultstr


# retun a random character of ascii letter
def generaterandomchar():
    return "" + random.choice(string.ascii_letters)


# The magic starts here
def startthemagic(spec_json):
    try:
        nooflines = int(input("Enter the number of lines to generate a fixed length file:"))
        if nooflines<0:
            raise  ValueError("Please enter the positive numbers")
        delimiter = input("Enter the delimiter whcih you want to use generate the file")
        if delimiter=="":
            raise  ValueError("Please enter the delimiter")
    except ValueError as e:
        print("Issue found ", e)
        return
    # Read the required specifications from JSON file
    specs_dict = readJSON(spec_json)
    if specs_dict != None:
        columnwidths = specs_dict['Offsets']
        columnheadings = specs_dict['ColumnNames']
        print("columnheadings:", columnheadings)
        print("columnwidths:", columnwidths)
        if generatefixedwidthfile(columnwidths, columnheadings, nooflines, encoding=specs_dict['FixedWidthEncoding']):
            if generatecsvfile(columnwidths,delimiter, encoding=specs_dict['DelimitedEncoding']):
                print("Please refer fixed file :: {} and csv file :: {}".format(os.path.abspath(FIXED),os.path.abspath(CSV)))
            else:
                print("Some issues with the CSV file generation!! Fix the issues and try again")
        else:
            print("Some issues with the Fixed file generation!! Fix the issues and try again")
    else:
        print("Something wrong with the specifications. Please validate the requred json : {}".format(os.path.abspath(spec_json)))


if (__name__ == "__main__"):
    startthemagic(JSON)
