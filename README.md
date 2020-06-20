To Run on a local PC first download and install postgres sql package. At the time of installation set a top level passwd.
See attached Excel for instructions

Setup a postgres db, in example below it is called test2
(1) start psql.exe from command line, e.g.

	c:\Program Files\PostgreSQL\12\bin\psql.exe -U postgres
	
(2) CREATE DATABASE test2;

(3)\q (to quit psql) the psql command line interface

All other steps are taken care of from app.py

