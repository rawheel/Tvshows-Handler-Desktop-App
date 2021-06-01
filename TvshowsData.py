class TvshowsData:
    def __init__(self):
        self.NetflixData=[]
        self.HBOData = []
        self.DisneyData = []
    
    def add_NetflixData(self,data):
        self.NetflixData.append(data)
    
    def get_NetflixData(self):
        return self.NetflixData

    def add_HBOData(self,data):
        self.HBOData.append(data)
    
    def get_HBOData(self):
        return self.HBOData

    def add_DisneyData(self,data):
        self.DisneyData.append(data)
    
    def get_DisneyData(self):
        return self.DisneyData

class Action_and_Adventure(TvshowsData):
    def addData(self,Id,Name,Seasons,Episodes,IMDB_Ratings,Network):
        data = {
            'Id':Id,
            'Name':Name,
            'Seasons':Seasons,
            'Episodes':Episodes,
            'IMDB_Ratings':IMDB_Ratings,
            'Network':Network
        }

        if Network.lower() == 'netflix':
            self.add_NetflixData(data)
        elif Network.lower() == 'hbo':
            self.add_HBOData(data)
            
        elif Network.lower() == 'disney+':
            self.add_DisneyData(data)


class Scifi(TvshowsData):
    def addData(self,Id,Name,Seasons,Episodes,IMDB_Ratings,Network):
        data = {
            'Id':Id,
            'Name':Name,
            'Seasons':Seasons,
            'Episodes':Episodes,
            'IMDB_Ratings':IMDB_Ratings,
            'Network':Network
        }

        if Network.lower() == 'netflix':
            self.add_NetflixData(data)
        elif Network.lower() == 'hbo':
            self.add_HBOData(data)
            
        elif Network.lower() == 'disney+':
            self.add_DisneyData(data)
            

class Sitcom(TvshowsData):
    def addData(self,Id,Name,Seasons,Episodes,IMDB_Ratings,Network):
        data = {
            'Id':Id,
            'Name':Name,
            'Seasons':Seasons,
            'Episodes':Episodes,
            'IMDB_Ratings':IMDB_Ratings,
            'Network':Network
        }

        if Network.lower() == 'netflix':
            self.add_NetflixData(data)
        elif Network.lower() == 'hbo':
            self.add_HBOData(data)
            
        elif Network.lower() == 'disney+':
            self.add_DisneyData(data)

#Driver Code

ob_action = Action_and_Adventure()
ob_scifi = Scifi()
ob_sitcom = Sitcom()

# NETFLIX
def add_action_data():
    ob_action.addData('N_01','The 100',1,9,8.1,'Netflix')
    ob_action.addData('N_02','The Witcher',1,8,8.2,'Netflix')
    ob_action.addData('N_03','The Umbrella Academy',2,20,8,'Netflix')

    ob_action.addData('H_01','The Legacies',3,45,7.4,'HBO')
    ob_action.addData('H_02','The DoomPetrol',1,8,8.2,'HBO')
    ob_action.addData('H_03','Genration',2,20,8,'HBO')

    ob_action.addData('D_01','Falcon and the Winter Soldier',1,10,8.4,'Disney+')
    ob_action.addData('D_02','The DoomPetrol',1,8,8.2,'Disney+')
    ob_action.addData('D_03','Genration',2,20,8,'Disney+')
add_action_data()

def add_scifi_data():
    ob_scifi.addData('N_01','Stranger Things',3,25,8.1,'Netflix')
    ob_scifi.addData('N_02','Altered Carbon',2,16,7.6,'Netflix')
    ob_scifi.addData('N_03','Black Mirror',5,50,9,'Netflix')

    ob_scifi.addData('H_01','Titans',2,24,7.7,'HBO')
    ob_scifi.addData('H_02','His Dark Materials',2,16,7.9,'HBO')
    ob_scifi.addData('H_03','Raised by Wolves',5,50,9,'HBO')

    ob_scifi.addData('D_01','Loki',1,8,9,'Disney+')
add_scifi_data()

def add_sitcom_data():
    ob_sitcom.addData('N_01','Friends',1,8,8.1,'Netflix')
    ob_sitcom.addData('H_01','Silicon Valley',5,90,10,'HBO')
    ob_sitcom.addData('D_01','WandaVision',1,8,8.9,'Disney+')
add_sitcom_data()

def get_Netflix_action_data():
    return ob_action.get_NetflixData()
def get_HBO_action_data():
    return ob_action.get_HBOData()
def get_Disney_action_data():
    return ob_action.get_DisneyData()

def get_Netflix_scifi_data():
    return ob_scifi.get_NetflixData()
def get_HBO_scifi_data():
    return ob_scifi.get_HBOData()
def get_Disney_scifi_data():
    return ob_scifi.get_DisneyData()

def get_Netflix_sitcom_data():
    return ob_sitcom.get_NetflixData()
def get_HBO_sitcom_data():
    return ob_sitcom.get_HBOData()
def get_Disney_sitcom_data():
    return ob_sitcom.get_DisneyData() 
#print(get_HBO_action_data())
