
from tabula import read_pdf
location = '/Users/yanjingy/Desktop/D018183/20180731/1591497'
file_names = ['0154334909a 001.pdf']
test1 = location+'/'+file_names[0]
print(type(test1))
df = read_pdf(test1)
print(df)
