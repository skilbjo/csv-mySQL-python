#CSV Import Tool
## Using Python Scripting
### Also includes a CSV Output tool (from mySQL)!

This CSV Import tool is an easy way to update mySQL tables quickly. 

### Installation
####Dependencies

	
1. mySQL installed with root privledges. 
	- to install a local LAMP server on your machine, see the helpful guide here for installing [macports](http://muddledramblings.com/rumblings-from-the-secret-labs/lamp-server-from-scratch-with-macports/).

2. The mySQLdb library for Python
	
	- to install mySQLdb, download it from [Source Forge](http://sourceforge.net/projects/mysql-python/) first, then run the following commands in your terminal: 
`
	
		$ gunzip MySQL-python-1.2.2.tar.gz
		$ tar -xvf MySQL-python-1.2.2.tar
		$ cd MySQL-python-1.2.2
		$ python setup.py build
		$ python setup.py install
		
3. Log in to mySQL using the command prompt and create a database called `forjar` and a table called `csvtable`

		$ mysql -u root
		mysql> create database forjar;
		mysql> create table csvtable (id MEDIUMINT 			PRIMARY KEY AUTO_INCREMENT NOT NULL, sname 			VARCHAR(40), sclass VARCHAR(40));

###Documentation
