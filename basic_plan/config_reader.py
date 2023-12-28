from configparser import ConfigParser

def readconfig_file(section,key):
    config = ConfigParser()
    config.read("..\\configuration_data\\config.ini", encoding='utf-8')
    return config.get(section,key)


print(readconfig_file('Links','Login_Url'))