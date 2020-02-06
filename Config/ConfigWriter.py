import configparser

config = configparser.ConfigParser()
config['User'] = {
    'Username': 'jp20170315@gmail.com',
    'Password': '12345'
}
config['Website'] = {}
config['Website']['URL']="http://automationpractice.com/index.php"


config['Testrail'] = {
    'URL': 'https://matthewlee2019369.testrail.com',
    'User': 'matthewlee0904@gmail.com',
    'Password': 'C8n4iTjwEnkK1Upva2bZ'
}
with open('Config.ini','w') as configfile:
    config.write(configfile)
