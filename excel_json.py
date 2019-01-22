# read contents from excel files
# cells may contains json
# change and save output



import xlrd
import json
# loading wb
loc = 'C:/Users/yanjingy/Documents/work/two_customers.xlsx'
wb = xlrd.open_workbook(loc)

# open sheet by index , 1 represent the most left one
sheet = wb.sheet_by_index(0)

# grab a cell's info
a_cell_info = sheet.cell_value(1,1)

# create an new worksheet


#  按 }，{ 分开
list_of_json=list(a_cell_info.split("},{"))
#print(list_of_json)
list_of_json[0] = list_of_json[0].replace("[","") + "}"
list_of_json[-1] = "{"+list_of_json[-1].replace("]","")

# 将每个item 转化为可以转为字典的sting 格式
for i in range(0,len(list_of_json)):
    if i != 0 and i != len(list_of_json)-1:
        list_of_json[i] = "{"+list_of_json[i]+"}"
        list_of_json[i] = json.loads(list_of_json[i])
        #print(i,type(list_of_json[i]),list_of_json[i])
    else:
        list_of_json[i] = json.loads(list_of_json[i])
        #print(i,type(list_of_json[i]), list_of_json[i])


for i in range(0,len(list_of_json)):
    list_of_json[i] = (list_of_json[i]["call_time_6m"],list_of_json[i])

from pythonds.graphs import PriorityQueue
class PriorityQueue(PriorityQueue):
    def delMin(self):
        retval = self.heapArray[1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return retval

def CompareJson(alist):
    stack_container = []
    list_container = []
    container = PriorityQueue()
    container.buildHeap(alist)
    while container.currentSize > 0:
        stack_container.append(container.delMin())
    while len(list_container)<10:
        list_container.append(stack_container.pop())
    return list_container

coms = CompareJson(list_of_json)
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
output_wb = Workbook()
dest_filename = 'output.xlsx'
ws1 = output_wb.active
ws1.title = "test_writing"

for row in range(1, len(coms)):
    ws1.append([sheet.cell_value(1,0 ), str(coms[row])])
output_wb.save(filename=dest_filename)









