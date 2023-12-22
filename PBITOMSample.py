global System, DataTable, AMO, ADOMD

import sys

import ssas_api as powerbi
import pandas as pd

print("Hit Enter to connect and say 'Hi TOM!'")
input()

print('Power BI Desktop Connection')
print(str(sys.argv[1]))
print(str(sys.argv[2]))

conn = "Provider=MSOLAP;Data Source=" + str(sys.argv[1]) + ";Initial Catalog='';"
print(conn)
print()

dax_string = 'EVALUATE ROW("Loading .NET assemblies",1)'
df = powerbi.get_DAX(connection_string=conn, dax_string=dax_string)

print("Crossing the streams...")
global System, DataTable, AMO, ADOMD

import System
from System.Data import DataTable
import Microsoft.AnalysisServices.Tabular as TOM
import Microsoft.AnalysisServices.AdomdClient as ADOMD

print("Reticulating splines...")
print()

TOMServer = TOM.Server()
TOMServer.Connect(conn)

print("Hi TOM...")
print()

# Database info
for item in TOMServer.Databases:
    print("Database: ", item.Name)
    print("Compatibility Level: ", item.CompatibilityLevel) 
    print("Created: ", item.CreatedTimestamp)

DatabaseId = str(sys.argv[2])
PowerBIDatabase = TOMServer.Databases[DatabaseId]

print()

# Define measure dataframe
dfMeasures = pd.DataFrame(
    columns=['Table',
             'Name', 
             'Description', 
             'DataType', 
             'DataCategory',
             'Expression',
             'FormatString',
             'DisplayFolder',
             'Implicit',
             'Hidden',
             'ModifiedTime',
             'State'])

# Define column dataframe
dfColumns = pd.DataFrame(
    columns=['Table',
             'Name'])

# Tables
print("Listing tables...")
for table in PowerBIDatabase.Model.Tables:
    print(table.Name)

    # Assign current table by name
    CurrentTable = PowerBIDatabase.Model.Tables.Find(table.Name)

    print(type(CurrentTable))
    print(type(CurrentTable.Measures))

    # Measures
    for measure in CurrentTable.Measures:
        new_row = {'Table':table.Name,
                'Name':measure.Name, 
                'Description':measure.Description, 
                'DataType':measure.DataType,
                'DataCategory':measure.DataCategory,
                'Expression':measure.Expression,
                'FormatString':measure.FormatString,
                'DisplayFolder':measure.DisplayFolder,
                'Implicit':measure.IsSimpleMeasure,
                'Hidden':measure.IsHidden,
                'ModifiedTime':measure.ModifiedTime,
                'State':measure.State}
        #print(new_row)
        dfMeasures = dfMeasures.append(new_row, ignore_index=True)

    # Columns
    for column in CurrentTable.Columns:
        new_row = {'Table':table.Name,
                'Name':column.Name}
        #print(column.Name)
        dfColumns = dfColumns.append(new_row, ignore_index=True)

print(dfMeasures)
print(dfColumns)

input()