# open and read in file
file = "changes_python.txt"
# fhand = open(file)
# data = fhand.readlines()
data = [line.strip() for line in open(file, 'r')]


# count number of lines in file, there should be 5255 lines
line_count = len(data)

# count number of commits, there should be 422 , each commit is separated by a line of 72 '-'
# sample header line: r1551925 | viacheslav.vdovenko | 2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015) | 1 line

sep = '-'*72
index = 0 
commits = []
authors = []
commits_per_author = {}
time = []

while True:
    try:
        header = data[index + 1].split('|') 
        commits.append(header)
        
        author = header[1].strip()
        
        time_stamp = header[2].split()
        time_stamp = time_stamp[1]
        
        if author not in authors:
            authors.append(author)
        
        if time_stamp not in time:
            time.append(time_stamp)
        time.sort()
        
        
        index = data.index(sep, index + 1)
    except IndexError:
        break
   
    
print 'There are %d lines in the %s file' % (line_count, file)
print 'There were %s commits made to %s file' %(len(commits), file)
print 'There were ' + str(len(authors)) + ' authors who made changes.'
# print authors
# print time
print 'The earliest commit was made at %s and the latest commit at %s' %(time[1], time[-1])














