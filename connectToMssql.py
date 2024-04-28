import time
from colorama import Fore

import pyodbc


class database_:

    def __init__(self, server, database):

        self.cursor = None
        self.conn_str = None
        self.conn = None
        self.connect = True
        self.server = server
        self.database = database

    def connectToDatabase(self, count=None):

        try:
            self.conn_str = f"DRIVER={{SQL Server}} ;SERVER={self.server};" \
                            f"DATABASE={self.database}"
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()

            self.connect = True
            return True

        except:
            counter = 0
            while count > counter:
                counter += 1
                print(Fore.YELLOW + f"{counter}. try in progress...")
                time.sleep(1)
                print(Fore.RED + "::WARN:: Connection failed")

            self.connect = False
            print(Fore.RED + "::WARN:: Connect Error !")

            return False

    def createTable(self, name_table, columns):

        if self.connect:

            try:

                self.cursor.execute(
                    f"CREATE TABLE {name_table} ({', '.join(columns)})")
                self.conn.commit()
                print(Fore.GREEN + f"{name_table} table is created")

            except:

                print(Fore.RED + "An error occurred while creating the table.")
        else:
            self.connectToDatabase()
            print(Fore.RED + "::WARN:: Connection Error")

    def writeToTable(self, name_table, *args):
        if self.connect:
            self.cursor.execute(f"INSERT INTO {name_table} VALUES ({','.join(['?'] * len(args))})", args)
            self.conn.commit()
            print(Fore.BLUE + "Data is added. .")

        else:
            if self.cursor:
                print(Fore.RED + "::WARN:: Cursor Error")
                return False
            else:
                self.connectToDatabase()

    def readFromTable(self, name_table, mode, key=None, value=None, number=None, **kwargs):

        if self.connect:

            columns = list(kwargs.keys())

            if mode == "all":
                self.cursor.execute(f"SELECT * FROM {name_table}")

            elif mode == "rows":
                self.cursor.execute(f"SELECT TOP {number} * FROM {name_table}")

            elif mode == "range":
                self.cursor.execute(f"SELECT * FROM {name_table} WHERE {key}>={value}")

            elif mode == "date":
                self.cursor.execute(f"SELECT * FROM {name_table} WHERE {key}='{value}'")

            elif mode == "specific":
                condition = " AND ".join(f"{column}='{kwargs[column]}'" for column in columns)
                query = f"SELECT * FROM {name_table} WHERE {condition}"
                self.cursor.execute(query)

            else:
                print(Fore.GREEN + "Choose a mode")

            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.conn.commit()

        else:
            self.connectToDatabase()
            print(Fore.RED + "::WARN:: Connection Error")
            return False

    def deleteFromTable(self, name_table, mode, column=None, key=None, value=None):

        if self.connect:

            if mode == "all":
                self.cursor.execute(f"DELETE FROM {name_table}")
                print(Fore.GREEN + f"{name_table} table is deleted. .")

            elif mode == "one_col":
                self.cursor.execute(f"ALTER TABLE {name_table} DROP COLUMN {column}")
                print(Fore.GREEN + f"{column} column is deleted. .")

            elif mode == "some_rows":
                self.cursor.execute(f"DELETE FROM {name_table} WHERE {key}={value}")
                print(Fore.GREEN + f"Data with a value of {value} has been deleted from the table.")

            elif mode == "specific":
                condition = f"{key} = {value}"
                query = f"DELETE FROM {name_table} WHERE {condition} "
                self.cursor.execute(query)

            self.conn.commit()

        else:
            self.connectToDatabase()
            print(Fore.RED + "::WARN:: Connection Error")

    def deleteTable(self, name_table):
        if self.connect:
            self.cursor.execute(f"TRUNCATE TABLE {name_table}")
            self.conn.commit()
            print(Fore.GREEN + "Table is deleted")
        else:
            self.connectToDatabase()
            print(Fore.RED + "::WARN:: Connection Error")

    def closeCursor(self):
        self.cursor.close()
        self.conn.close()
