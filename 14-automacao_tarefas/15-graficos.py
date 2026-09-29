from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference, Series

wb = Workbook()
ws = wb.active

data = [
    ['Ano', 'Lucro', 'Custos'],
    [2019, 2, 5],
    [2020, 8, 10],
    [2021, 14, 15],
    [2022, 26, 25],
    [2023, 33, 30],
    [2024, 45, 40],
    [2025, 90, 65]
]

for d in data:
    ws.append(d)

# Criação do Gráfico
chart = AreaChart()
chart.title = 'Lucro x Custos'
chart.style = 13
chart.x_axis.title = 'Ano'
chart.y_axis.title = 'Porcentagem'

categorias = Reference(
    ws,
    min_col=1,
    min_row=2,
    max_row=8
)

dados = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_col=3,
    max_row=8
)

chart.add_data(dados, titles_from_data=False)
chart.set_categories(categorias)

ws.add_chart(chart, 'A10')

wb.save('files/chart.xlsx')