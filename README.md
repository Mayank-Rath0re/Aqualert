# GDSC

GDSC Project Topic: Life Below Water.

# IDEA

Create an application to alert users about the dangerous aquatic life near them.
\n Beneficial in protecting both human and aquatic life.

# APPROACH

1. Receive Client Location via Google Maps.
2. Host our application as a python file on a cloud VM taking user's latitude and longitude as parameters.
3. Programs takes user's coordinates and uses it to filter on database created by us.
4. If any dangerous species are found near him/her, An E-mail is generated via G-mail.
5. Mail contains description of species along with a link to their images making recognition easier.

# PRE-REQUISITES

1. Python
	Go to the link provided below and download the latest version
	https://www.python.org/downloads/

2. MySQL
	Go to the link provided below to download MySQL setup on your local environment.
	https://dev.mysql.com/downloads/installer/

3. Python-MySQL Connectivity
	After Downloading and installing both Python and MySQL on your local environment,
	Run the command provided below on your respective command prompt/Terminal.
	pip install mysql-connector-python

4. Download Our Database
	After Meeting all the previous 3 pre-requisites, run the upload_db.py file using
	Python.

5. geocoder module- Python
	To install geocoder module for Python, run either of the following commands:
	
		pip install geocoder
		
		pip3 install geocoder

# How to Run

After meeting all the pre-requisites, run only the aqualert.py file in your environment.
alert-generate.py is a module used in aqualert.py for the scenario where a client's location
trigger the need of generating and alert.

# DATA STRUCTURE
	species:
		SNo: integer, primary key
		Name: varchar(40)
		Region: varchar(25)
		duration: varchar(10)
		RNo: integer
	
	coordinates:
		RNo: integer, primary key
		Region: varchar(25)
		Latitude1: decimal(10,6)
		Latitude2: decimal(10,6)
		Longitude1: decimal(10,6)
		Longitude2: decimal(10,6)
