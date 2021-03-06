import argparse
import ast
import sys

from datautils import datautils
from webutils import webutils

__version__ = 1.0

def main(argv=None):
    parser = argparse.ArgumentParser(description='This program will allow Federal Spending to be pulled and stored.')
    parser.add_argument('--version', action='version', version='%(prog)s {0}'.format(__version__)) #version number for this program, increment upon changes
    #TODO: Add code for arguments        

    try:
        
        args = parser.parse_args()
        #TODO: Add code for extracting arguments
        
        #TODO: Write logic to get data based on the accounts and fiscal years passed as parameters

    except SystemExit:
        parser.print_help()
        sys.exit(1)
    except Exception as err:
        print(err)

def dfToJSON(df):
    '''This will take a dataframe and return the data formated as JSON by records'''
    dfAsJSON = df.to_json(orient = 'records', double_precision=2) #if precision not there goes to more than 2 digits
    return json.loads(json.dumps(dfAsJSON, indent=4))  

#TODO: Added functions to pull answers to questions, they must live here in the base, but can be added to the datautils as the actual code
def getQuestion1Answer():
    answer = ""
    #TODO: code the way get the answer, but could be call to the datautils to have a set of functions there

    print("Question 1 Answer\n")
    print(answer)
    return answer

def getQuestion2Answer():
    answer = ""
    #TODO: code the way get the answer, but could be call to the datautils to have a set of functions there
    
    print("Question 2 Answer\n")
    print(answer)
    return answer

def getQuestion3Answer():
    answer = ""
    #TODO: code the way get the answer, but could be call to the datautils to have a set of functions there
    
    print("Question 3 Answer\n")
    print(answer)  

def getQuestion4Answer():
    answer = ""
    #TODO: code the way get the answer, but could be call to the datautils to have a set of functions there
    
    print("Question 4 Answer\n")
    print(answer)
    return answer

def getQuestion5Answer():
    answer = ""
    #TODO: code the way get the answer, but could be call to the datautils to have a set of functions there
    
    print("Question 5 Answer\n")
    print(answer)
    return answer

def getQuestion6Answer():
    answer = ""
    #TODO: code the way get the answer, but could be call to the datautils to have a set of functions there
    
    print("Question 6 Answer\n")
    print(dfToJSON(answer))
    return answer

def getQuestion7Answer():
    answer = ""
    #TODO: code the way get the answer, but could be call to the datautils to have a set of functions there
    
    print("Question 7 Answer\n")
    print(answer)
    return answer

def getQuestion8Answer():
    answer = ""
    #TODO: code the way get the answer, but could be call to the datautils to have a set of functions there
    
    print("Question 8 Answer\n")
    print(answer)
    return answer

main(sys.argv)
