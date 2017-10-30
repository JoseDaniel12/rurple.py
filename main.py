import tools
import time
print("_____________________________________Rurple_____________________________________")
archivoMapa=open(input("Ingres el nombre del archivo con el mapa: "))
archivoInstrucciones=open(input("Ingres el nombre del archivo con las instrucciones: "))

tablero=tools.tablero_conversion(archivoMapa)
mi_mapa=tools.Mapa(tablero)
print(mi_mapa.imprimir())

for instruccion in archivoInstrucciones:
	mi_mapa.ejecutar_instruccion(instruccion.strip("\n"))
	print(mi_mapa.imprimir())
	time.sleep(0.35)

print("  ¡¡¡FIN DE LA EJECUCIÓN!!!")
