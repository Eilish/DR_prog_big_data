#### Name: Eilish Murphy
#### Number: 10190433
#### CA3 - Analytics on Dataset

# open and read in file
file = "changes_python.txt"
data = [line.strip() for line in open(file, 'r')]

# count number of lines in file, there should be 5255 lines
line_count = len(data)

# count number of commits, there should be 422 , each commit is separated by a line of 72 '-'
# line 1 of each commit is a headder line
# sample header line: r1551925 | viacheslav.vdovenko | 2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015) | 1 line
# header line is followed by list of changes made - no of changes varies per commit
# changes are followed by the user comment

sep = '-'*72 
index = 0 

commits = []
authors = {}
dates = {}
hours = {}

# read through file and pull out required info and then move to next header line until end of file reached
while True:
    try:
        # identify header liners and split on | and append to commits list
        header = data[index + 1].split(' | ') 
        commits.append(header)
        
        # split header into separate elements
        revision, author, date_time, comment_lines = header
        
        # sub-divide date/time into separate elements
        date_time = date_time.split()
        full_date, time, zone, day, day_no, month, year = date_time
        # split time to identify hour
        time = time.split(':')
        hour = time[0]
                
        # add authors and number of their commits to authors dictionary
        authors[author] = authors.get(author, 0) +1
        
        # add dates and number of commits per day to date dictionary
        dates[full_date] = dates.get(full_date, 0) +1
        
        # add hours and number of commits per hour to hours dictionary
        hours[hour] = hours.get(hour, 0) +1        
        
        
        index = data.index(sep, index + 1)
    except IndexError:
        break

# process authors dictionary to find author with most and least commits
author_commits = []
for key, value in authors.items():
    author_commits.append((value, key))
author_commits.sort(reverse = True)
most, busy_author = author_commits[0]
least, lazy_author = author_commits[-1] 

# process dates dictionary to find first and last date and day with most commits
date_commits = []
for key, value in dates.items():
    date_commits.append((key, value))
date_commits.sort()
first, no1 = date_commits[0]
last, no2 = date_commits[-1]

busiest_day = []
for key, value in dates.items():
    busiest_day.append((value, key))
busiest_day.sort(reverse = True)
count, busy_day = busiest_day[0]
    
 
print 'There are %d lines in the %s file' % (line_count, file)
print 'There were %s commits made to the file' % len(commits)
print 'There were ' + str(len(authors)) + ' authors who made changes.'
print 'The author who made the most commits was %s with %d commits' % (busy_author, most)
print 'The author who made the least commits was %s with %d commits' % (lazy_author, least)

print 'Commits were made to the file between %s and %s' % (first, last)
print 'The most commits were made on %s with %d commits' % (busy_day, count)

# print 'The earliest commit was made at %s and the latest commit at %s' %(time[0], time[-1])














