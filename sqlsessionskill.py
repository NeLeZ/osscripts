import pyodbc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--server')
parser.add_argument('--database')
parser.add_argument('--user')
parser.add_argument('--password')

args = parser.parse_args()

connenction_string = (
"DRIVER=FreeTDS;"
f"SERVER={args.server};"
f"DATABASE={args.database};"
f"UID={args.user};"
f"PWD={args.password};"
)

try:
    with pyodbc.connect(connenction_string) as connection:
        connection.autocommit = True
        with connection.cursor() as cursor:
            query = f"select CONVERT(varchar, spid) as id from sys.sysprocesses where dbid=db_id('{args.database}') and program_name = '1CV83 Server'"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(f"kill {row.id}")
                //cursor.execute(f"kill {row.id}")
except pyodbc.Error as ex:
      print("An error occurred in SQL Server:", ex)