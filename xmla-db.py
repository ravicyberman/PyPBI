import adodbapi
#from click import command

#import command

conn = adodbapi.connect(
    
  Provider = 'MSOLAP.8',  
 client_id = 'a73dd903-e963-4fa8-8e04-d9145da56f39',
 client_secret = '_.z-VQ2x6_3as7z42_uKr_.r3JHL1EAVu6',
 Data Source = 'powerbi://api.powerbi.com/v1.0/myorg/Alchemy%20Datasets%20%5BTest%5D',
    initial catalog='HERO UDM w/ partitions' ")


print('The tables in your database are:')
for name in conn.get_table_names():
    print(name)

#