class Ruby(object):

    def __init__(self):
        self.singleline = "#"
        self.multiline1 = "=begin"
        self.multiline2 = "=end"
    
    def getting(self):
        return self.singleline, self.multiline1, self.multiline2