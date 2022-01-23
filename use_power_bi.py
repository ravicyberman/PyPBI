from pprint import pprint
from configparser import ConfigParser
from use_power_bi import PowerBiClient
#from powerbi.client import PowerBiClient 

     
config = ConfigParser()

config.read('Configs/configs.ini')

client_id = config.get('power_bi_app','client_id')
client_secrect = config.get('power_bi_app','client_secret')

# Init the PowerBi client 

power_bi_client = PowerBiClient(

client_id = client_id,
client_secrect = client_secrect,
credentials='Config/power_bi_state.jsonc'

)
