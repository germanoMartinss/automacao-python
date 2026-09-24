from openpyxl import Workbook

# 1 - Criar um arquivo Excel
file_txt = open('files/gastos.txt', 'r', encoding='utf-8')
file = file_txt.read()
# print(file)
list_data = file.splitlines()
# print(list_data)

# 2 - Iterando os valores da lista
for i in range(0, len(list_data)):
    list_data[i] = list_data[i].split(',')
print(list_data)


# 3 - Criação da planilha
wb = Workbook()
planilha1 = wb.active

for row in list_data:
    planilha1.append(row)

wb.save(filename='files/gastos.xlsx')