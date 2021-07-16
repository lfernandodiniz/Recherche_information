from __future__ import print_function

import mysql.connector
from models import Trouble_relation
from dao import TroubleDao

cnx = mysql.connector.connect(host="localhost",
                              user="root",
                              port=3306,
                              password="NEWPASSWORD",
                              auth_plugin='mysql_native_password', database='troubleshooting')


cursor = cnx.cursor()

# add_fault = ("INSERT INTO fault (description_fault) VALUES (%s)")
#
# add_cause = ("INSERT INTO cause (fault_no, description_cause) VALUES (%s, %s)")
# Insert new resolution_method
# add_resolution_method = ()
# data_resolution_method = {
#   'fault_no': fault_no,
#   'description_resolution': 'Check the head connection',
# }
# cursor.execute("INSERT INTO resolution_method (fault_no, description_resolution) VALUES ('{}', '{}')".format(5, 'Check the head connection'))
# fault_no = cursor.lastrowid
# data_fault = ('Module (head) is not detected on the HMI panel')
# Insert new fault
# cursor.execute(add_fault, (data_fault,))
# Insert new cause
# data_cause = (5, 'Incorrect connections of the head',)
# cursor.execute(add_cause, data_cause)
#
# Insert new reference
#cursor.execute("INSERT INTO reference (fault_no, description_reference) VALUES ({}, {}".format(5,"Figure 3.9"))
# fault_no = 5
#Insert new trouble_relation


trouble = Trouble_relation('primeiro', 'segundo', 'terceiro', 'quarto')


# def insert_data(trouble):


#add's
add_fault = ("INSERT INTO fault "
             "(description_fault) "
             "VALUES ( %(description_fault)s)")

add_cause = ("INSERT INTO cause "
             "(fault_no, description_cause) "
             "VALUES ( %(fault_no)s, %(description_cause)s)")

add_resolution = ("INSERT INTO resolution_method "
             "(fault_no, description_resolution) "
             "VALUES ( %(fault_no)s, %(description_resolution)s)")

add_reference = ("INSERT INTO reference "
                  "(fault_no, description_reference) "
                  "VALUES ( %(fault_no)s, %(description_reference)s)")

add_trouble_relation = ("INSERT INTO trouble_relation "
                        "(fault_no, description_fault, description_cause, description_resolution, description_reference) "
                        "VALUES ( %(fault_no)s, %(description_fault)s, %(description_cause)s, %(description_resolution)s, %(description_reference)s)")


# insert_fault
data_fault = {
    'description_fault': trouble.description_fault,
}
cursor.execute(add_fault, data_fault)
trouble.fault_no = cursor.lastrowid

print(trouble.fault_no)

# insert_cause
data_cause = {
    'fault_no': trouble.fault_no,
    'description_cause': trouble.description_cause,
}
cursor.execute(add_cause, data_cause)

#insert resolution_method
data_resolution = {
    'fault_no': trouble.fault_no,
    'description_resolution': trouble.description_resolution,
}
cursor.execute(add_resolution, data_resolution)

# insert reference
data_reference = {
    'fault_no': trouble.fault_no,
    'description_reference': trouble.description_reference,
}
cursor.execute(add_reference, data_reference)

# insert trouble_relation
data_trouble_relation = {
  'fault_no': trouble.fault_no,
  'description_fault': trouble.description_fault,
  'description_cause': trouble.description_cause,
  'description_resolution': trouble.description_resolution,
  'description_reference': trouble.description_reference,

}
cursor.execute(add_trouble_relation, data_trouble_relation)
trouble.trouble_no = cursor.lastrowid

# add_trouble_relation = ("INSERT INTO trouble_relation "
#               "(fault_no, description_fault, description_cause, description_resolution, description_reference) "
#               "VALUES ( %(fault_no)s, %(description_fault)s, %(description_cause)s, %(description_resolution)s, %(description_reference)s)")
#
#
#
#
# data_trouble_relation = {
#   'fault_no': fault_no,
#   'description_fault': 'Module (head) is not detected on the HMI panel',
#   'description_cause': 'Incorrect connections of the head',
#   'description_resolution': 'Check the head connection',
#   'description_reference': 'Figure 3.9',
#
# }
# cursor.execute(add_trouble_relation, data_trouble_relation)




# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
    # return trouble
