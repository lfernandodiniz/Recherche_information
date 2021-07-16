from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode



DB_NAME = 'troubleshooting'

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="NEWPASSWORD",
    auth_plugin='mysql_native_password'
                              )
cursor = cnx.cursor()

TABLES = {}
TABLES['fault'] = (
    "CREATE TABLE `fault` ("
    "  `fault_no` int(11) NOT NULL AUTO_INCREMENT,"   
    "  `description_fault` varchar(500) NOT NULL,"    
    "  PRIMARY KEY (`fault_no`), UNIQUE KEY `description_fault` (`description_fault`)"
    ") ENGINE=InnoDB")

TABLES['cause'] = (
    "CREATE TABLE `cause` ("
    "  `cause_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `description_cause` varchar(500) NOT NULL,"
    "  PRIMARY KEY (`cause_no`), UNIQUE KEY `description_cause` (`description_cause`)"  
    ") ENGINE=InnoDB")

TABLES['resolution_method'] = (
    "CREATE TABLE `resolution_method` ("
    "  `resolution_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `description_resolution` varchar(500) NOT NULL,"
    "  PRIMARY KEY (`resolution_no`), UNIQUE KEY `description_resolution` (`description_resolution`)" 
    ") ENGINE=InnoDB")

TABLES['reference'] = (
    "CREATE TABLE `reference` ("
    "  `reference_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `description_reference` varchar(200) NOT NULL,"
    "  PRIMARY KEY (`reference_no`), UNIQUE KEY `description_reference` (`description_reference`)"
    ") ENGINE=InnoDB")

TABLES['trouble_relation'] = (
    "  CREATE TABLE `trouble_relation` ("
    "  `trouble_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `description_fault` varchar(500) NOT NULL,"  
    "  `description_cause` varchar(500) NOT NULL,"
    "  `description_resolution` varchar(500) NOT NULL,"
    "  `description_reference` varchar(200) NOT NULL,"
    "  PRIMARY KEY (`trouble_no`),"
    "  CONSTRAINT `trouble_relation_ibfk_1` FOREIGN KEY (`description_fault`) "
    "     REFERENCES `fault` (`description_fault`) ON DELETE CASCADE ON UPDATE CASCADE,"
    "  CONSTRAINT `trouble_relation_ibfk_2` FOREIGN KEY (`description_cause`) "
    "     REFERENCES `cause` (`description_cause`) ON DELETE CASCADE ON UPDATE CASCADE,"
    "  CONSTRAINT `trouble_relation_ibfk_3` FOREIGN KEY (`description_resolution`) "
    "     REFERENCES `resolution_method` (`description_resolution`) ON DELETE CASCADE ON UPDATE CASCADE,"
    "  CONSTRAINT `trouble_relation_ibfk_4` FOREIGN KEY (`description_reference`) "
    "     REFERENCES `reference` (`description_reference`) ON DELETE CASCADE ON UPDATE CASCADE "    
    ") ENGINE=InnoDB")


TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `id_user` varchar(8) NOT NULL,"   
    "  `name` varchar(20) NOT NULL,"
    "  `pwd` varchar(8) NOT NULL,"
    "  PRIMARY KEY (`id_user`)"
    ") ENGINE=InnoDB")


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
