import sqlite3 as lite
import time
import platform
import sys
import os

if sys.platform == 'win32':

    db_file = os.path.expanduser(os.path.join('~HOME', '.config', 'timebook', 'sheets.db'))
    connection = lite.connect(db_file)
else:
    db_file = os.path.expanduser(os.path.join('~', '.config', 'timebook', 'sheets.db'))
    connection = lite.connect(db_file)

if connection:
    cursor = connection.execute("SELECT id, sheet, start_time, end_time,\
        description FROM entry")
    database_list = []

    for row in cursor:
        database_list.append(row[0])        
        

    print """
    1 - List the database
    2 - Modify start_time
    3 - Modify end_time
    4 - Modify description"""

    while True:
        answ = raw_input('\t')

        if answ == '1':
            print "Your database has %s entries." % len(database_list)
            list_db = raw_input("\nTo list the entire database press A. \
To list a certain range, select anything else.")
                        
            if list_db == 'a'.upper():
                for row in cursor:
    
                    print "\tId= ", row[0]
                    print "start_time= ", time.asctime(time.localtime(row[2]))
                    print "end_time= ", time.asctime(time.localtime(row[3]))
                    print "description= ", row[4]
            else:
                start = int(raw_input('\nSelect start range.\t'))
                end = int(raw_input('Select end range\t'))
                cursor = connection.execute("SELECT id, sheet, start_time, end_time,\
        description FROM entry")
                for row in cursor:
                    if row[0] >= start and row[0] <= end:
                        print "\n\tId= ", row[0]
                        print "start_time= ", time.asctime(time.localtime(row[2]))
                        print "end_time= ", time.asctime(time.localtime(row[3]))
                        print "description= ", row[4]

        if answ == '2':          
            Id_ch = raw_input('\n\tId to make changes:')
            time_ch = raw_input('\n\tThe new start_time in format "year-month-day 00:00:00":')

            if Id_ch.isdigit():

                time_ch_unix = time.mktime(time.strptime(time_ch, '%Y-%m-%d %H:%M:%S'))
                cursor.execute('UPDATE entry SET start_time=? WHERE Id=?', (time_ch_unix, Id_ch)) 
                connection.commit()
                print "Number of rows updated: %d" %cursor.rowcount
            else:
                print "Id you entered is not a number!"

        if answ == '3':
            Id_ch = raw_input('\n\tId to make changes:')
            time_ch = raw_input('\n\tThe new end_time in format "year-month-day 00:00:00":')

            if Id_ch.isdigit():
                time_ch_unix = time.mktime(time.strptime(time_ch, '%Y-%m-%d %H:%M:%S'))
                cursor.execute('UPDATE entry SET end_time=? WHERE Id=?', (time_ch_unix, Id_ch)) 
                connection.commit()
                print "Number of rows updated: %d" %cursor.rowcount
            else:
                print "Id you entered is not a number!"

        if answ == '4':
            Id_ch = raw_input('\n\tId to make changes:')
            new_desc = raw_input('\nInsert the new description.\n')
            cursor.execute('UPDATE entry SET description=? WHERE Id=?', (new_desc, Id_ch))
            connection.commit()
            print "Number of rows updated: %d" %cursor.rowcount

        quit = raw_input('Press Q to exit or anything to repeat:')

        if quit.upper() == 'Q':
            break
        else:
            
            pass











    

        
       
