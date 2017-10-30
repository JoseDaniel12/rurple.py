class Mapa(object):
	def __init__(self, tablero):
		self.tablero=tablero
		self.paredes=[]
		self.pilas_monedas=[]
		self.robot=Robot(0,0,">")
		self.ancho=len(self.tablero[0])
		self.alto=len(self.tablero)

		y=0
		for fila in self.tablero:
			x=0
			for celda in fila:
				if celda==">" or celda=="v" or celda=="<" or celda=="ᴧ":
					self.robot= Robot(x,y,celda)
				else:
					if celda=="x":
						self.paredes.append(Pared(x,y))
					elif celda!="0":
						self.pilas_monedas.append(Pila_monedas(x,y,int(celda)))

				x+=1
			y+=1

	def ejecutar_instruccion(self, instruccion):

		if instruccion=="move":
			robotp=Robot(self.robot.x, self.robot.y, self.robot.direccion)
			robotp.move()
			permiso_move=True
			if robotp.x<self.ancho and robotp.x>=0 and robotp.y<self.alto and robotp.y>=0:
				for i in self.paredes:
					if i.x==robotp.x and i.y==robotp.y:
						permiso_move=False
			else:
				permiso_move=False

			if permiso_move:
				self.robot.move()

		elif instruccion=="rotate":
			self.robot.rotate()


		elif instruccion=="pick":
			for i in self.pilas_monedas:
				if i.x==self.robot.x and i.y==self.robot.y:
					self.robot.pick()
					i.restar()

	def imprimir(self):
		impresion=""
		impresion+="  "+"─"*self.ancho+"\n"
		for y in range(self.alto):
			impresion+=" | "
			for x in range(self.ancho):
				pared=False
				pila=False

				if self.robot.x==x and self.robot.y==y:
					impresion+=self.robot.direccion
				else:
					for i in self.paredes:
						if i.x==x and i.y==y:
							impresion+="x"
							pared=True
						
					for i in self.pilas_monedas:
						if i.x==x and i.y==y:
							impresion+=str(i.cantidad)
							pila=True
								
					if pared==False and pila==False:
						impresion+=" "

			impresion+="|"+"\n"
		impresion+="  "+"─"*self.ancho+"\n"
		impresion+="  Fichas recogidas: "+str(self.robot.cantidad_monedas)+"\n"
		return impresion

#------------------------------------------------------------------------------------------------------------------------------------------------------

class Robot(object):                            
	def __init__(self, x, y, direccion):
		self.x=x
		self.y=y
		self.direccion=direccion
		self.cantidad_monedas=0

	def move(self):
		if self.direccion==">":
			self.x+=1	
		elif self.direccion=="<":
			self.x-=1
		elif self.direccion=="v":
			self.y+=1
		elif self.direccion=="ᴧ":
			self.y-=1

	def pick(self):
		self.cantidad_monedas+=1

	def rotate(self):
		formas=[">","v","<","ᴧ"]
		self.direccion=formas[(formas.index(self.direccion)+1)%4]

#-----------------------------------------------------------------------------------------------------------------------------------------------------

class Pila_monedas(object):
	def __init__(self, x ,y, cantidad):
		self.x = x
		self.y = y
		self.cantidad = cantidad

	def restar(self):
		self.cantidad=self.cantidad-1

#-----------------------------------------------------------------------------------------------------------------------------------------------------

class Pared(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def tablero_conversion(archivoMapa):
	lista_listas=[]
	for fila in archivoMapa:
		linea=[]
		for celda in fila:
			if celda!="\n":
				linea.append(celda)
		lista_listas.append(linea)
	return lista_listas
