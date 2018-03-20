from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']


def getvalue(x): return x.value


years = list(map(getvalue, sheet['A'][1:]))
t_sun = list(map(getvalue, sheet['C'][1:]))
act_sun = list(map(getvalue, sheet['D'][1:]))


pyplot.plot(years, t_sun, label='1')
pyplot.plot(years, act_sun, label='2')
pyplot.show()
