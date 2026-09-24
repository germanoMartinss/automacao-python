from openpyxl import load_workbook

# 1 - Lendo planilha Excel
arquivo = 'files/teste.xlsx'
wb = load_workbook(arquivo)
planilha1 = wb['Planilha 1']

# 2 - Acessando um determinado valor
# print(planilha1['C2'].value)

# 3 - Interando valores por meio de loop
for i in range(2, 5):
    ano = planilha1['A%s' %i].value
    lucro = planilha1['B%s' %i].value
    custo = planilha1['C%s' %i].value

    print("{0} teve {1} de lucro e {2} de custos".format(ano, lucro, custo))