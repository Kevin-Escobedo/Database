import sqlite3

class Database:
    def __init__(self, name:str):
        '''Creates the connection to a database'''
        self.connection = sqlite3.connect("{}.db".format(name))
        self.c = self.connection.cursor()

    def create_table(self, table_name:str, column_name:str, data_type:str) -> None:
        '''Creates a table with this connection'''
        self.c.execute("CREATE TABLE {tn} ({cn} {ft})".format(tn=table_name, cn=column_name, ft = data_type))

    def add_column_to_table(self, table_name:str, column_name:str, data_type:str) -> None:
        '''Adds a column to the table'''
        self.c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name, cn=column_name, ct = data_type))
        
    def close(self) -> None:
        '''Closes the database connection'''
        self.connection.commit()
        self.connection.close()

if __name__ == "__main__":
    database = Database("practice")
    database.create_table("first_table", "first_column", "INTEGER")
    database.close()
