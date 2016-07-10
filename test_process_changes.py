#### Name: Eilish Murphy
#### Number: 10190433
#### CA3 - Analyse a Dataset

#### Test Suite for process_changes.py 

import unittest
from process_changes import *

class TestProcessChanges(unittest.TestCase):
   
    def setUp(self):
        self.process = Commit()
        self.process.commits = []
        self.process.revisions = []
        self.process.authors = []
        self.process.dates = []
        self.process.times = []
        self.process.lines_in_comments = []
        self.process.path_changes = []
        self.process.comments = []
        index = 0
        self.process.header = data[index + 1].split(' | ')
        self.process.revision, self.process.author, self.process.time_stamp, self.process.lines_in_comment = self.process.header
        self.process.date, self.process.time, self.process.zone, self.process.day, self.process.day_no, self.process.month, self.process.year = self.process.time_stamp.split()
        self.process.add = []
        self.process.modify = []
        self.process.delete = []
        
    def test_header_elements(self):
        # test if header is dividing into correct elements and time_stamp is sub-dividing correctly
        # first header line: r1551925 | viacheslav.vdovenko | 2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015) | 1 line
        self.assertEqual('r1551925', self.process.revision)
        self.assertEqual('viacheslav.vdovenko', self.process.author)
        self.assertEqual('2015-11-27', self.process.date)
        self.assertEqual('16:57:44', self.process.time)
        self.assertEqual('1 line', self.process.lines_in_comment)
        
    def test_all_elements_are_counted(self):    
        result = 422
        sep =  '-'*72
        index = 0
        while True:
            try:
                self.process.header = data[index + 1].split(' | ')
                self.process.revision, self.process.author, self.process.time_stamp, self.process.lines_in_comment = self.process.header
                self.process.date, self.process.time, self.process.zone, self.process.day, self.process.day_no, self.process.month, self.process.year = self.process.time_stamp.split()
                self.process.revisions.append(self.process.revision)
                self.process.authors.append(self.process.author)
                self.process.dates.append(self.process.date)
                self.process.times.append(self.process.time)
                self.process.lines_in_comments.append(self.process.lines_in_comment)
                index = data.index(sep, index + 1)
            except IndexError:
                break
        self.assertEqual(result, len(self.process.revisions))
        self.assertEqual(result, len(self.process.authors))
        self.assertEqual(result, len(self.process.dates))
        self.assertEqual(result, len(self.process.times))
        self.assertEqual(result, len(self.process.lines_in_comments))
    
    def test_path_changes_and_types(self):
        sep =  '-'*72
        index = 0
        while True:
            try:
                self.process.header = data[index + 1].split(' | ')
                self.process.paths_changed = data[index +2 : data.index('', index+1)]
                self.process.path_changes.append(self.process.paths_changed)
                index = data.index(sep, index + 1)
            except IndexError:
                break
        [self.process.add.append(item)for element in self.process.path_changes for item in element if item.startswith('A')]
        [self.process.modify.append(item)for element in self.process.path_changes for item in element if item.startswith('M')]
        [self.process.delete.append(item)for element in self.process.path_changes for item in element if item.startswith('D')]
        self.assertEqual(1056, len(self.process.add))
        self.assertEqual(1186, len(self.process.modify))
        self.assertEqual(767, len(self.process.delete))
        
if __name__ == '__main__':
    unittest.main()