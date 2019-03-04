<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import pandas as pd
import re

# this location is for testing

class Pget:
    def __init__(self ,file):
        self.f = open(file,'r')
        self.lines = self.f.readlines()
        self.info = []
        self.week = 0
        self.start_date = None
        self.end_date = None

    def get_lines(self):
        for line in self.lines:
            self.info.append(line)
        return self.info

    def get_week(self):
        self.week = int(re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", self.info[0])[0])
        return self.week

    def set_date(self,index):
        match = re.search(r'\d{4}-\d{2}-\d{2}', self.info[index])
        date = time.strptime(match.group(), '%Y-%m-%d')
        date = "{}-{}-{}".format(date[0],date[1],date[2])
        return pd.to_datetime(date)

    def get_start(self):
        self.start_date = self.set_date(1)
        return self.start_date

    def get_end(self):
        self.end_date = self.set_date(2)
        return self.end_date

    def close(self):
        self.f.close()


=======
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import pandas as pd
import re

# this location is for testing

class Pget:
    def __init__(self ,file):
        self.f = open(file,'r')
        self.lines = self.f.readlines()
        self.info = []
        self.week = 0
        self.start_date = None
        self.end_date = None

    def get_lines(self):
        for line in self.lines:
            self.info.append(line)
        return self.info

    def get_week(self):
        self.week = int(re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", self.info[0])[0])
        return self.week

    def set_date(self,index):
        match = re.search(r'\d{4}-\d{2}-\d{2}', self.info[index])
        date = time.strptime(match.group(), '%Y-%m-%d')
        date = "{}-{}-{}".format(date[0],date[1],date[2])
        return pd.to_datetime(date)

    def get_start(self):
        self.start_date = self.set_date(1)
        return self.start_date

    def get_end(self):
        self.end_date = self.set_date(2)
        return self.end_date

    def close(self):
        self.f.close()


>>>>>>> adddbee2a85b4786c4c9a1c91ecccc5eb68a0bbf
