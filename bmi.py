class bmi(object):
    count = 0
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = float(weight)
        self.height = float(height)
        bmitotal = 0
        bmi.count += 1
    def display_count(self):
        print  bmi.count
    
    def calc_bmi(self):
        return (self.weight) / (self.height ** 2)
        


