import re

class Calc(object):

    
    def cloc_action(self, line_list, singleline, multiline1, multiline2):
        #Checking contents of line list array
        #print line_list
        
        is_multiline = False
        sig_line = 0
        blank_line = 0
        for line in line_list:
            line = line.strip(" ")
            #print line
            if line.startswith(singleline) and is_multiline == False:
                continue
            elif line.startswith(multiline1) and is_multiline == False:
                is_multiline = True
                continue
            elif line.startswith(multiline2) and is_multiline == True:
                is_multiline = False
                continue
            elif is_multiline == False and (not line.startswith("\n")):
                sig_line += 1
                continue
            elif line.startswith("\n"):
                #testing to check blank line
                #print "blank line"
                blank_line += 1
                continue



        
        #print "Significant lines are %d " % len(line_list)
        return sig_line, blank_line

 
