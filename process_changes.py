#### Name: Eilish Murphy
#### Number: 10190433
#### CA3 - Analyse a Dataset

from collections import Counter 

# read in file and count number of lines in file  
file = 'changes_python.txt'
data = [line.strip() for line in open(file, 'r')]
line_count = len(data) #there should be 5255 lines 

# count number of commits, there should be 422 , each commit is separated by a line of 72 '-'
# line 1 of each commit is a header line
# sample header line: r1551925 | viacheslav.vdovenko | 2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015) | 1 line
# header line is followed by list of changes made - no of changes varies per commit
# changes are followed by the user comment

# Create Commit Class
class Commit:
    
    def __init__(self, revision = None, author = None, time_stamp = None, date = None, time = None, lines_in_comment = None, paths_changed = None, comment = None):
        self.revision = revision 
        self.author = author
        self.time_stamp = time_stamp
        self.date = date
        self.time = time
        self.lines_in_comment = lines_in_comment
        self.paths_changed = paths_changed
        self.comment = comment
    
       
    
if __name__ == '__main__': ## Only run if program called from command line
    
    # define separator and starting index. create lists to hold different elements
    sep = '-'*72 
    index = 0 
    commits = []
    revisions = []
    authors = []
    dates = []
    times = []
    lines_in_comments = []
    path_changes = []
    comments = []
           
    # read through file and pull out required info and then move to next header line until end of file reached
    while True:
        try:
            wip_commit = Commit()
            
            # identify header liners and split on | and append to commits list
            header = data[index + 1].split(' | ') 
            commits.append(header)
            
            # divide header items into individual elements and append to list
            revision, author, time_stamp, lines_in_comment = header
            date, time, zone, day, day_no, month, year = time_stamp.split()
            lines_in_comment, line = lines_in_comment.split()
            paths_changed = data[index +2 : data.index('', index+1)]
                            
            wip_commit.revision = revision.strip()
            revisions.append(revision)
            wip_commit.author = author.strip()
            authors.append(author)
            wip_commit.date = date.strip()
            dates.append(date)
            wip_commit.time = time.strip()
            times.append(time)
            wip_commit.lines_in_comment = int(lines_in_comment.strip())
            lines_in_comments.append(lines_in_comment)
            wip_commit.paths_changed = paths_changed
            path_changes.append(paths_changed)
                    
            # move to next index and append current comment to list (last line in current comment)
            index = data.index(sep, index + 1)
            comment = data[index-wip_commit.lines_in_comment:index]
            wip_commit.comment = comment
            comments.append(comment)

        except IndexError:
            break

    dates.sort()
    mode_dates = Counter(dates)
    times.sort()
        
    # split changes made into type of change and apend to individual lists
    add = []
    modify = []
    delete = []
    
    [add.append(item)for element in path_changes for item in element if item.startswith('A')]
    [modify.append(item)for element in path_changes for item in element if item.startswith('M')]
    [delete.append(item)for element in path_changes for item in element if item.startswith('D')]
    
    # calculate total changes commited
    total_changes = len(add) + len(modify) + len(delete)
    
    # output details about file
    print '\nFile Details:' 
    print 'There are %d lines in the %s file' % (line_count, file)
    print 'There were %s commits made to the file' % len(commits)
    print '\nAuthor Details:'
    print 'There were ' + str(len(Counter(authors))) + ' authors who made changes.'
    print 'The mean number of commits per author was ' + str((float(len(revisions)))/len(Counter(authors)))
    print 'The number of commits made by each author is:\n' , Counter(authors)
    print '\nDates & Times Details:'
    print 'Commits were made to the file between %s and %s' % (dates[0], dates[-1])
    print 'The earliest commit was made at %s and the latest commit made at %s' %(times[0], times[-1])
    print 'The most commits were made on: '+ str(mode_dates.most_common(1))
    print '\nChanges Details:'
    print 'There were %d changes made to the file' % total_changes
    print 'There were ' + str(len(add)) + ' additions made to the file'
    print 'There were ' + str(len(modify)) + ' modifications made to the file'
    print 'There were ' + str(len(delete)) + ' deletions made to the file'
    print 'The mean changes per commit is: ' + str(total_changes/float(len(commits)))











