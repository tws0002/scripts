import csv

        
#%%  
class Manga(object):
    def __init__(self, name, vol_num=0):
        self.name = name
        self.vol_num = vol_num
        path = r"f:\cover_data1.csv"
        database = []
        with open(path, "r") as fileobj:
            csvreader = csv.reader(fileobj)
            for x in csvreader:
                mydict = {'name':x[0], 'volume':x[1], 'width':x[2], 'height':x[3]}
                database.append(mydict)
        self.manga_data = []
        self.count = 0
        for x in database:
            if x['name'] == name:
                self.manga_data.append(x)
                self.count += 1
                
    def returnDB(self):
        return self.manga_data
    
    def consistency(self):
        widths = []
        heights = []
        for x in self.manga_data:
            widths.append(x['width'])
            heights.append(x['height'])
        if len(set(widths)) == 1 and len(set(heights)) == 1:
            return True
        else:
            return False        
    
    def volume(self):
        
        return self.vol_num
    
    def aspectRatio(self):
        width = self.manga_data[self.vol_num]['width']
        height = self.manga_data[self.vol_num]['height']
        return float(width)/float(height)
    
    def aspectRatios(self):
        ars = []
        for x in self.manga_data:
            ars.append(float(x['width']) / float(x['height']))
        return ars

    def coverType        


#%% 
man = Manga("gunnm", 2)
man.count
man.aspect_ratio()



#%%
man.count
volumes = man.returnDB()
man.consistency()

vol = Volumes(volumes)
vol.vols

