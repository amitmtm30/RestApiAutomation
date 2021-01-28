from configparser import ConfigParser

obj = ConfigParser()

# Reading configuration file
obj.read("D://Rest Api Automation//Programm//Config.cfg")
usrnme = obj.get("section1","username")
print(usrnme)
passwrd = obj.get("sr=ection")