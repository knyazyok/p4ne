from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x):
    return x.value

wb=load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']
x = list(map(getvalue,sheet['A'][1:]))
y1 = list(map(getvalue,sheet['C'][1:]))
y2 = list(map(getvalue,sheet['D'][1:]))

pyplot.plot(x,y1,label="Temperature")
pyplot.plot(x,y2,label="Sun Activity")
pyplot.legend(loc="upper left")
pyplot.xlabel('Years')
pyplot.ylabel('Values')
pyplot.show()