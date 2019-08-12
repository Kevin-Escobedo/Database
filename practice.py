import sqlite3

if __name__ == "__main__":
    sqlite_file = "info.db"
    table_name1 = "my_table_1"
    table_name2 = "my_table_2"
    new_field = "my_1st_column"
    field_type = "INTEGER"

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute("CREATE TABLE {} ({} {})".format(table_name1, new_field, field_type))

    c.execute("CREATE TABLE {} ({} {} PRIMARY KEY)".format(table_name2, new_field, field_type))

    conn.commit()
    conn.close()
