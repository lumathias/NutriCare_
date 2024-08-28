import pandas as pd
from sqlalchemy import create_engine

# 1. Establish a Connection
engine = create_engine('mysql+pymysql://root:root@localhost/db')

# 2. Read the CSV file
df = pd.read_csv('AlimentosBrasileiros.csv') 

# 3. Load the data into the MySQL table
df.to_sql('Alimentos', con=engine, if_exists='append', index=False)