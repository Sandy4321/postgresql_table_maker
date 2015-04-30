'''
psycog2 wrapper to easily make new tables from csv files
'''

import sys
import psycopg2
import csv


def file_reader(filename, type='csv'):
    data_file = []
    if type == 'csv':
        with open(filename, "rb") as f:
            reader = csv.reader(f, delimiter=' ', quotechar='|', quoting = csv.QUOTE_NONNUMERIC)
            headers = reader.next()
            for row in reader:
                data_file.append(row)
    else:
        except "unknown file type"
    return data_file, headers

print file_reader("")

# def connectdb(dbname, user):
#     conn = psycopg2.connect("dbname="+dbname+" user="+user)
#     cur = conn.cursor()
#     return conn, cur

# def commit_and_closedb(cursor, connection):
#     conn.commit()
#     cursor.close()
#     connection.close()

# def create_table(cursor, data, table_name, headers, convert_numeric=True, convert_dates=False):
#     column_type_list = []
#     for item in data_file[0]:
#         if type(item) is float:
#             column_list.append("double precision")
#         elif type(item) is str:
#             column_list.append("varchar")
#         else:
#             except "unknown item type"
#     sql_statement = ", ".join( [str(j)+" "str(k) for j,k in zip(headers, column_list)] )
#     cur.execute("CREATE TABLE {0} ({1});".format(table_name, sql_statement))

# def fill_table(data, table_name):
#     pass

# def main():
#     try:
#         dbname = sys.argv[1]
#     except:
#         dbname = raw_input("Database name: ")
#     try:
#         user = sys.argv[2]
#     except:
#         user = raw_input("User name: ")
#     try:
#         filename = sys.argv[3]
#     except:
#         filename = raw_input("File name: ")
#     try:
#         table_name = sys.argv[4]
#     except:
#         table_name = raw_input("New table name: ")

#     data, headers = file_reader(filename)
#     cursore, connection = connectdb(dbname, user)
#     create_table(cursor, data, table_name, headers)
#     fill_table(data, table_name)
#     commit_and_closedb(cursor, connection)

# if __name__ == "__main__":
#     main()
