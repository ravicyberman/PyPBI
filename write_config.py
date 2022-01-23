
from configparser import ConfigParser

# init config file 

config = ConfigParser()

# Add a section in the config file 

config.add_section('power_bi_app')

config.set('power_bi_app','client_id','a73dd903-e963-4fa8-8e04-d9145da56f39')
config.set('power_bi_app','client_secret','_.z-VQ2x6_3as7z42_uKr_.r3JHL1EAVu6')


# Write to a configfile.ini 

with open(file='configs/configs.ini', mode='w+') as f:

    config.write(f)



