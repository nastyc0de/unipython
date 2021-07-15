try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agrega\n')
    archivo.write('Adiós')
except Exception as e:
    print(e)
finally:
    archivo.close()