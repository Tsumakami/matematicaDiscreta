#!/usr/bin/python
# coding: utf-8
print("##########################################")
print("#    Trabalho de Matemática Discreta", "   ","#")
print("##########################################\n\n")

print("Digite a quantidade de vagas: ", end='')
qt_vagas = int(input())
print("Digite a quantidade de candidatos: ", end='')
qt_candidatos = int(input())

print("A ordem importa? ")
print("Digite 'S' para SIM ou 'N' para NÃO: ", end='')
ordem = input().upper()

resultado = 1

if(ordem == 'S'):
	for i in range(1, qt_vagas + 1):
		resultado = resultado * qt_candidatos
		qt_candidatos = qt_candidatos - 1

	print("Resultado:", resultado)
else:
	for i in range(qt_vagas, 0, -1):
		resultado = resultado * (qt_candidatos / i)
		qt_candidatos = qt_candidatos - 1
	print("Resultado:", int(resultado))
