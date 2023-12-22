import sys

print('powerbi://api.powerbi.com/v1.0/myorg/Alchemy%20Datasets%20%5BTest%5D')
server='powerbi://api.powerbi.com/v1.0/myorg/Hero%20Analytics%20%5BDev%5D'
db=''
print('')
conn = "Provider=MSOLAP;Data Source=" + str(sys.argv[1]) + ";Initial Catalog='';"
print(conn)

input() 