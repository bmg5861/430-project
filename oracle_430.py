import cx_Oracle

connection = None

try:
    dsn_tns = cx_Oracle.makedsn('h3oracle.ad.psu.edu', '1521', 
                                service_name = 'orclpdb.ad.psu.edu')
    connection = cx_Oracle.connect(user = "<username>", 
                                   password = "<password>", dsn = dsn_tns)

    # show the version of the Oracle Database
    print(connection.version)
    
except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()

