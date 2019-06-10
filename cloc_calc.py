import re

class Calc(object):

    
    def cloc_action(self, line_list, singleline, multiline1, multiline2):
        multi_index_array = []
        singe_index_array = []
        index = 0

        for line in line_list:
            if line.startswith(singleline):
                # debugging to check the comment line.
                singe_index_array.append(index)
                continue
            elif line.startswith(multiline1) or line.startswith(multiline2):
                #Calling another function from another module for muliline comment
                # print 'Multiline comment and need to branch to the multiline method.'
                multi_index_array.append(index)
                continue
            else:
                continue
            
            index += 1

        
        #remove singleline comments from line_array
        for ind in singe_index_array:
            line_list.pop(ind)

        #remove multiline comments from line_array
        



        
        #print "Significant lines are %d " % len(line_list)
        return len(line_list)

 
