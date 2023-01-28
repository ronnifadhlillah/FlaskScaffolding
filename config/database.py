[Database]
# Select your main driver as a main database.
# Driver / Database available : SQLite, MySQL, MSSQL, PostgreSQL(Soon).
  Driver=MariaDB
  Prefix=_dbp
  PoolSize=10
  MaxOverflow=20
  AutoCommit=False,
  AutoFlush=False

[SQLite]
# SQLite OS available: unix, windows, raw.
# SQLite connect to file based database. define the path / folder of database.
  Driver=SQLite
  OS=windows
  Name=flask_scaffolding
  CheckSameThread=False,
  PathDirectory=database

[MariaDB]
# This dialect+driver is full compatible with MySQL.
# Change Dialect & Driver if you're using MySQL as main database.
# MySQL Dialect / DBAPI available: default, pymysql, mysqldb.
# MySQL guide refer to this URL : https://docs.sqlalchemy.org/en/14/dialects/mysql.html.
# MariaDB guide refer to this URL : https://mariadb.com/resources/blog/using-sqlalchemy-with-mariadb-connector-python-part-1/.
  Dialect=mariadb
  Adaptor=mariadbconnector
  Host=127.0.0.1
  port=3306
  Name=test
  Username=root
  Password=
  Charset=utf8
  Strict=True
  Engine=Null


[MSSQL]
# provided by Microsoft.
# Link for connector / adapter : https://docs.microsoft.com/en-us/connectors/sql/.
# MSSQL Dialect / DBAPI available: pyodbc, pymssql.
  Dialect=pyodbc
  Driver=MSSQL
  Host=localhost
  Port=1433
  Name=homestead
  Username=homestead
  Password=homestead
  Charset=utf8
  Prefix=

# for in memory database
