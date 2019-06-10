import sys
from javajs import JavaJS
from python import Python
from ruby import Ruby
from cloc_calc import Calc

if __name__ == "__main__":
    
    #open the file from the second argument
    file_to_test = str(sys.argv[1])
    
    # testing to check the file type
    #print file_to_test
    
    sig_line = 0
    blank_line = 0
    total_line = 0
    #create the file type.
    f = open(file_to_test, "r")
    
    #store the lines of the file in an array
    line_list = f.readlines()
    
    #testing the line list array
    #print line_list
    total_line = len(line_list)

    #initialize singleline and mutliline comments
    singleline = ""
    multiline1 = ""
    multiline2 = ""

    #initiliaze the calculator class
    calc = Calc()

    if file_to_test.endswith('.py'):
        pyt = Python()
        singleline, multiline1, multiline2 = pyt.getting()
        #call the calculator function
        # print "File is a python file"
  
    elif file_to_test.endswith('.java') or file_to_test.endswith('.js'):
        javajs = JavaJS()
        singleline, multiline1, multiline2 = javajs.getting()
    
    elif file_to_test.endswith('.rb'):
        rub = Ruby()
        singleline, multiline1, multiline2 = rub.getting()
    
    print "Total number of lines are " + str(total_line)

    #call the calculator function
    sig_line, blank_line = calc.cloc_action(line_list, singleline, multiline1, multiline2)
    print "Number of significant lines are " + str(sig_line)
    print "Number of blank lines are " + str(blank_line)
    print "Number of commented lines are " + str(total_line - sig_line - blank_line)
    

    
    #close the file
    f.close()

    

