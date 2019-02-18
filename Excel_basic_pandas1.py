
import pandas as pd
import numpy as np
import openpyxl


location = '/Users/yanjingy/Documents/work/Todayswork/Auto Consolidated Tracker-1 v2.xlsx'
sheetname = 'Spec Level'

spec = pd.read_excel(location,sheetname,header = 0,
              index_col= None,usecols="A,B,D,H,I,L"
              )

print(spec.head())
print(spec['MFR Part'].head())

# select two columns
new_spec = spec[['Date','MFR Part']]
print(new_spec.head())


# for int indexing
# if dont know the column name, can using index in df.columns
asquare = spec.iloc[0:2,0:3]
print(asquare)
print("the columns is {}, \n"
      "the columns container type is {},\n"
      "the fourth column name is {},\n"
      "column name type is {}"
      .format(spec.columns,type(spec.columns),
       spec.columns[4],type(spec.columns[4])))

output_loc = '/Users/yanjingy/Documents/work/Todayswork/output.xlsx'
with pd.ExcelWriter(output_loc) as writer:
    asquare.to_excel(writer, sheet_name='Sheet1', index=False,
                     startrow=0, startcol=0, freeze_panes=(1, 1)
                     )

    new_spec.to_excel(writer, startrow=writer.sheets['Sheet1'].max_row,
                      startcol=1,index=False)
    writer.save()

 ## reference from https://stackoverflow.com/questions/47737220/append-dataframe-to-excel-with-pandas
 ## undate multiple worksheets

writer.sheets = {ws.title: ws for ws in book.worksheets}

for sheetname in writer.sheets:
    df1.to_excel(writer,sheet_name=sheetname, startrow=writer.sheets[sheetname].max_row, index = False,header= False)

writer.save()