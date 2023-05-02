import sqlite3

# create connection to database
conn = sqlite3.connect('courses.db')

# create courses table
conn.execute('''CREATE TABLE courses
             (pid TEXT PRIMARY KEY NOT NULL,
             title TEXT NOT NULL,
             catalog_course_id TEXT NOT NULL,
             description TEXT NOT NULL,
             academic_level TEXT NOT NULL,
             credits INTEGER NOT NULL,
             date_start TEXT NOT NULL,
             online_offering INTEGER NOT NULL,
             campus_offering INTEGER NOT NULL,
             subject_code TEXT NOT NULL);''')

# create prerequisites table
conn.execute('''CREATE TABLE prerequisites
             (prerequisite_id TEXT PRIMARY KEY NOT NULL,
             course_id TEXT NOT NULL,
             course_title TEXT NOT NULL,
             course_credits TEXT NOT NULL,
             FOREIGN KEY (course_id) REFERENCES courses(pid));''')

# close connection
conn.close()
