from configparser import ConfigParser
import os

class ConfigReader:
    __reader = None
    def __init__(self):
        if ConfigReader.__reader is not None:
            pass
        else:
            ConfigReader.__reader = ConfigParser()
            Base_Dir = os.path.dirname(os.path.abspath(__file__))
            File_path = os.path.abspath(os.path.join(Base_Dir, 'Config.ini'))
            ConfigReader.__reader.read(File_path)

    @staticmethod
    def getInstance():
        if ConfigReader.__reader is None:
            ConfigReader()
        return ConfigReader.__reader


    @staticmethod
    def get_name():
        if ConfigReader.__reader is None:
            ConfigReader()
        return ConfigReader.__reader['User']['Username']

    @staticmethod
    def get_password():
        if ConfigReader.__reader is None:
            ConfigReader()
        return ConfigReader.__reader['User']['Password']

    @staticmethod
    def get_url():
        if ConfigReader.__reader is None:
            ConfigReader()
        return ConfigReader.__reader['Website']['url']

    @staticmethod
    def get_testratil_url():
        if ConfigReader.__reader is None:
            ConfigReader()
        return ConfigReader.__reader['Testrail']['url']

    @staticmethod
    def get_testratil_name():
        if ConfigReader.__reader is None:
            ConfigReader()
        return ConfigReader.__reader['Testrail']['user']

    @staticmethod
    def get_testratil_password():
        if ConfigReader.__reader is None:
            ConfigReader()
        return ConfigReader.__reader['Testrail']['password']