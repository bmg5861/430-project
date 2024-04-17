import oracledb

def Connection():
    try:
        Username = None
        Password = None

        with open('secret.txt', 'r') as file:
            Data = file.readlines()

        Username = Data[0].rstrip()
        Password = Data[1].rstrip()

        dsn_tns = oracledb.makedsn('h3oracle.ad.psu.edu', '1521', 
                                    service_name = 'orclpdb.ad.psu.edu')
        connection = oracledb.connect(user = Username, 
                                    password = Password, dsn = dsn_tns)
        return connection
    except oracledb.Error as error:
        print(error)
