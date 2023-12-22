from sys import path
import clr

path.append('c:\\Program Files\\Microsoft.NET\\ADOMD.NET\\150')
#clr.AddReference(r"C:\Program Files\MicrosoftOffice\root\vfs\ProgramFiles\Microsoft.NET\ADOMD.NET\150\Microsoft.AnalysisServices.AdomdClient.dll")
#clr.AddReference('Microsoft.AnalysisServices.AdomdClient')
#from Microsoft.AnalysisServices.AdomdClient import AdomdConnection , AdomdDataAdapter

from pyadomd import pyadomd

model_name=''
port_number=''

