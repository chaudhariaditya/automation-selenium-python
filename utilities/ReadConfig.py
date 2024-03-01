import configparser

config = configparser.RawConfigParser()
configfile = "D:\\class\\orangeHRM\\configuration\\config.ini"

config.read(configfile)
class Readconfig:
    @staticmethod
    def getusername():
        username= config.get('common data','username')
        return username

    @staticmethod
    def getpassword():
        password= config.get('common data','password')
        return password
    @staticmethod
    def GetFNAME():
        First=config.get('employee data','Firstname')
        return First

    @staticmethod
    def GetMNAME():
        Middle = config.get('employee data', 'Middelname')
        return Middle

    @staticmethod
    def GetLNAME():
        Last = config.get('employee data', 'Lastname')
        return Last

    @staticmethod
    def GetImage():
       Image= config.get('employee data', 'Imagee')
       return Image


