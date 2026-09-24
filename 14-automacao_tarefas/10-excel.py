from openpyxl import Workbook


# 1- Criar um arquivo Excel
wb = Workbook()
name = 'files/teste.xlsx'


# 2- Utilizando Worksheet do Excel
ws1 = wb.active
ws1.title = 'Planilha 1'

# 3- Adicionando dados
data = [
    ['Ano', 'Lucro', 'Custos'],
    [2023, '25%', '30%'],
    [2024, '30%', '40%'],
    [2025, '35%', '65%'] 
]

for line in data:
    ws1.append(line)

ws2 = wb.create_sheet(title='Pi')
ws2['D2'] = 3.15


wb.save(filename=name)