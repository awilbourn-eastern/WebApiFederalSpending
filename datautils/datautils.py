import sqlite3
import os

def getSQLDBConnection():
   '''Open connection and return  for SQLite database.'''
    #check for log folder to exist, if not create it
   if not os.path.exists("./data"):
      os.makedirs("./data")

   return sqlite3.connect("./data/federalspending.db")

def runSQLInsertStatement(sqlInsert):
    '''The given SQL INSERT script will be run against the database.'''
    cn = getSQLDBConnection()

    try:
        cn.execute(sqlInsert)
        cn.commit()
    except:
        cn.rollback()
        raise
    finally:
        cn.close()

def setupSQLiteTables(deleteExistingDatabase = False):
    '''Create a new SQLite database and create the base tables.
    '''
    # TODO: Add code for deleteing an existing data based on the parameter passed.

    cn = getSQLDBConnection()
    cur = cn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS "Accounts" (
            "toptier_code"	TEXT NOT NULL,
            "baseDataURL" 	TEXT,
            PRIMARY KEY("toptier_code")
        );
        CREATE TABLE IF NOT EXISTS "Departments" (
            "dept_code"	TEXT,
            "toptier_code"	TEXT,
            "dept_name"	TEXT NOT NULL,
            PRIMARY KEY("dept_code"),
            CONSTRAINT "FK_Accounts" FOREIGN KEY("toptier_code") REFERENCES Accounts(toptier_code)
        );
        CREATE TABLE IF NOT EXISTS "SubDepartments" (
            "sub_dept_code"	TEXT NOT NULL,
            "fiscal_year"	INTEGER NOT NULL,
            "dept_code"	TEXT NOT NULL,
            "sub_dept_name"	TEXT NOT NULL,
            "sub_obligated_amount"	REAL NOT NULL DEFAULT 0,
            "sub_gross_outlay_amount"	REAL NOT NULL DEFAULT 0,
            CONSTRAINT "FK_Departments" FOREIGN KEY("dept_code") REFERENCES Departments(dept_code),
            PRIMARY KEY("sub_dept_code","fiscal_year")
        );
    """)
    cn.close()

