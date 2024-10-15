import psycopg2

class PostgreSQLConnect:
    def __init__(self,dbname,user,passw,host,port):
        self.dbname = dbname
        self.user = user
        self.passw = passw
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname = self.dbname,
                user = self.user,
                password = self.passw,
                host = self.host,
                port = self.port
            )
            print("Connect To PostgreSQL")
        except psycopg2.Error as er:
            print(f"Error connect to PG: {er}")

    def disconect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from PG")

