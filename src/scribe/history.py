import datetime as dt
import pandas as pd
from sqlalchemy import create_engine
import os

dbh=os.environ['DBHOST']
dbn=os.environ['DBNAME']
dbu=os.environ['DBUSER']
dbp=os.environ['DBPASS']

dburl = f"mysql+mysqlconnector://{dbu}:{dbp}@{dbh}/{dbn}"

def pull_records(uid):
    db = create_engine(dburl)
    df = pd.read_sql(f"SELECT * FROM u_{uid}", con=db)
    print('PULL')
    print(df)
    return df

def push_records(uid, df):
    print(f"PUSH {uid}")
    print(df)
    db = create_engine(dburl)
    df.to_sql(name=f"u_{uid}", con=db, if_exists='append', index=False)

def append_record(track, df):
    print('APPEND')
    print(track)
    print(df)
    g = dict(track)
    g['datetime'] = dt.datetime.now()
    ser = pd.Series(g)
    print(ser.to_frame().T)
    df1 = pd.concat([df, ser.to_frame().T])
    df1.reset_index(inplace=True, drop=True)
    return df1

def create_df(track):
    print('CREATE')
    print(track)
    g = dict(track)
    g['datetime'] = dt.datetime.now()
    ser = pd.Series(g)
    print(ser.to_frame().T)
    df = ser.to_frame().T
    df.reset_index(inplace=True, drop=True) 
    return df  