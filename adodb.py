import adodbapi
import pandas as pd
import numpy as np
    
workspace = 'your published workspace'
report = 'report_name'
    
sec = 'Integrated Security=SSPI'
conn = adodbapi.connect(f"Provider=MSOLAP.8;Data Source='powerbi://api.powerbi.com/v1.0/myorg/Alchemy%20Datasets%20%5BTest%5D';Initial Catalog='Eagel Eye Model';10800;")
cur = conn.cursor()
     
def get_df(data):
    ar = np.array(data.ado_results) # turn ado results into a numpy array
    df = pd.DataFrame(ar).transpose() # create a dataframe from the array
    df.columns = data.columnNames.keys() # set column names
    return df
    
    your_table_name = "Data"
    your_column_name = "date_created"
    
    DAX_Query = f'''
    DEFINE
      VAR FilteredTable = 
        FILTER(
           '{your_table_name}',
            AND(
                '{your_table_name}'[{your_column_name}] >= DATE(2021, 1, 2),
                '{your_table_name}'[{your_column_name}] < DATE(2022, 4, 2)
              )
        )
    
    EVALUATE
      FilteredTable
    '''
     
    cur.execute(DAX_Query)
    data=cur.fetchall()
    demo_df = get_df(data)