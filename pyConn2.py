

from sys import path
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\150')
from pyadomd import Pyadomd

from azure.identity import ClientSecretCredential

scope = 'powerbi://api.powerbi.com/v1.0/myorg/Alchemy%20Datasets%20%5BTest%5D'

tenant_id = input('Tenant id: cef04b19-7776-4a94-b89b-375c77a8f936 ')
client_id = input('Client id: a73dd903-e963-4fa8-8e04-d9145da56f39 ')
client_secret = input('Client secret: _.z-VQ2x6_3as7z42_uKr_.r3JHL1EAVu6 ')
authority = f'https://login.microsoftonline.com/'

credential = ClientSecretCredential(tenant_id, client_id, client_secret, authority=authority)
token = credential.get_token(scope)
serverName = 'powerbi://api.powerbi.com/v1.0/myorg/Alchemy%20Datasets%20%5BTest%5D'

connectionString = f'Provider=MSOLAP;Data Source={serverName};Initial Catalog=Test;User ID=;Password={token.token};Persist Security Info=True;Impersonation Level=Impersonate;'

query = "EVALUATE SUMMARIZECOLUMNS('Sample Data'[Value1])"

with Pyadomd(connectionString) as conn:
    with conn.cursor().execute(query) as cur:
        print(cur.fetchall())