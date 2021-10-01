
import mysql.connector

def getsqltables(database):
    db = mysql.connector.connect(
            host="localhost",
            user="user",
            passwd="password",
            database=database,
            auth_plugin='mysql_native_password'
            )
    
    cursor = db.cursor()
    query = "USE "+database
    cursor.execute(query)
    query = "SHOW TABLES"
    cursor.execute(query)
    tables=[x for x in cursor]
    cursor.close()
    db.close()
    return tables
    
    
def put_csv2db(database,table):
    db = mysql.connector.connect(
            host="localhost",
            user="user",
            passwd="password",
            database=database,
            auth_plugin='mysql_native_password',
            allow_local_infile=True
            )
    
    cursor = db.cursor()
    query = "LOAD DATA LOCAL INFILE '"+file+"' INTO TABLE "+table+" FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS"
    cursor.execute(query)
    cursor.close()
    db.commit()
    db.close()
    return "OK"


def tables(database):
    lt=getsqltables(database)
    tables_lists=[item for t in lt for item in t]
    return tables_lists


database=input('Enter the database: ')
choice=input('Do you want to update the whole database?(Y/N)')

if choice=='N':
    table=input('Enter the name of the table: ')
    file='path/%s.csv'%table
    put_csv2db(database,table)
    print('%s successfully uploaded to %s'%(table,database))
else:
    tables=tables(database)
    for table in tables:
        file='path/%s.csv'%table
        put_csv2db(database,table)
        print('%s successfully uploaded to %s'%(table,database))



