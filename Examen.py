notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}
notasJuan = notas_estudiantes['Juan']
notasMaria =notas_estudiantes['Maria']
notasPedro =notas_estudiantes['Pedro']

sumaJuan = sum(notasJuan)
sumaPedro =sum(notasPedro)
sumaMaria =sum(notasMaria)


promedioJuan = sumaJuan / len(notasJuan)
promedioMaria = sumaMaria / len(notasMaria)
promedioPedro = sumaPedro /len(notasPedro)

print(promedioJuan)
print(promedioMaria)
print(promedioPedro)


