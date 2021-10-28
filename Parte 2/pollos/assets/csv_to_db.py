import pandas as pd
from sqlalchemy import create_engine

datos = pd.read_csv('ETL.csv')
datos['fecha'] = pd.to_datetime(datos['fecha'])

creds = {
    'host': 'localhost',
    'user': 'root',
    'passw': '12345',
    'database': 'asimetrix',
    'port': '3306'
}

mydb = create_engine('mysql+pymysql://' + creds['user'] + ':' +
                     creds['passw'] + '@' + creds['host'] + ':' + creds['port'] + '/' + creds['database'], echo=False)

datos.to_sql(name='pollos_pollo', con=mydb,
             if_exists='append', index=False)

print("Listo")