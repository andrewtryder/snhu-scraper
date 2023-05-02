# snhu-scraper
SNHU Scraper for Course Data

SNHU uses Kauli.co for managing their courses and degrees. 
It looks to be a popular provider for doing so and they thankfully have an API that's easy to reverse engineer and understand.

For a project, we're trying to make a tool to make it easier to figure out a degree plan, so we needed the data.

Files:
classes.py - This creates the initial course data based on a dump from the catalog. It is used as a starting point for classes2.py
classes2.py - This queries the DB that classes.py created and then hits, one by one, each class for all the data. Its output is a course DB and prerequisites DB. 
snhu_courses.db - This is the output of everything. You want course_data and prerequisites here. 
snhu_courses.sql - Text dump of this DB.