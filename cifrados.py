"""Variable global que contendra el archivo a trabajar"""
archivo=""

def main():
	"""Menu de opciones de todo el programa"""
	opc=0;
	while opc!=9:
		print("\nMenu\n")
		print("1.- Cifrado Morse 	2.- Descifrar Morse\n")
		print("3.- Cifrado ASCII 	4.- Descifrar ASCII\n")
		print("5.- Cifrado Cesar 	6.- Descifrar Cesar\n")
		print("7.- Cifrado Escitala 	8.- Descifrar Escitala\n")
		print("9.- Salir\n")
		print("Opcion:")
		opc=input()
		if opc == 1:
			cifrarMorse()
		elif opc == 2:
			descifrarMorse()
		elif opc == 3:
			cifrarASCII()
		elif opc == 4:
			descifrarASCII()
		elif opc == 5:
			cifrarCesar()
		elif opc == 6:
			descifrarCesar()
		elif opc == 7:
			cifrarEscitala()
		elif opc == 8:
			descifrarEscitala()
		elif opc == 9:
			print("\n 		Adios!!!")
		else:
			opc=9;
			print("\n 		Adios!!!")

def abrirArchivo():
	global archivo
	archivo=raw_input("\n 	Ingresa la ruta del archivo: ")

def cifrarASCII():
	"""Se lee el archivo caracter a caracter y se va grabando con el metodo grabartxt"""
	archi=open (archivo,'r')
	linea=archi.read(1)
	while linea!="":
		"""la funcion ord() convierte a valores acssi"""
		a = ord(linea)
		grabartxt(a)
		linea=archi.read(1)
	archi.close()
	print("\n 	Se ha terminado de cifrar, revisa el arhivo cifradoASCII.txt")

def grabartxt(a):
	"""Aqui se va escribiendo en el archivo txt creado"""
	archi=open ('cifradoASCII.txt','a') 
	"""convertimos a string con str() porque write solo escribe strings"""
	b = str(a)
	archi.write(b+" ")
	archi.close()

def descifrarASCII():
	""" Aqui se descifra ascii"""
	global archivo
	archivo=raw_input("\n 	Ingresa la ruta del archivo a descifrar: ")
	archi=open (archivo,'r')
	linea=archi.read()
	archi.close()
	linea=linea.split(" ")
	grabar2(linea)

def grabar2(linea):	
	""" Aqui se graba el mensaje traducido"""
	tam=len(linea)-1	
	archi=open ('mensajeASCII.txt','w')
	for i in range(tam):
		"""se convierte a int porque viene de un string"""
		a=int(linea[i])
		"""y de int convertimos a el valor letra, simobolo o numero"""
		s=chr(a)		
		archi.write(s)
	archi.close()
	print("\n 	Se ha terminado de descifrar, revisa el arhivo mensajeASCII.txt");

def cifrarEscitala():
	"""Se solicitan los valores al usuario"""
	print("	Escriba el numero de largo:")
	col=input()
	print("	Escriba el numero de diametro:")
	row=input()
	"""leemos el archivo"""
	archi=open(archivo,'r')
	text=archi.read()
	"""se guarda en una variable string"""
	archi.close()
	"""se muestra el mensaje a cifrar"""
	print("\n	Mensaje a cifrar: "+text)	

	m=[]
	for i in range(row):
		m.append([0]*col)

	con=0
	tam=len(text)
	for i in range(0,row):
		for j in range(0,col):
			if con<tam:
				m[i][j]=text[con]			
			else:
				m[i][j]=" "
			con=con+1

	tam=row*col
	cifrado=[]
	for i in range(tam):
		cifrado.append(" ")

	con=0
	for i in range(0,col):
		for j in range(0,row):
			cifrado[con]=m[j][i]		
			con=con+1
	
	"""cifrado es tipo list, lo pasamos a string para poder llenar el txt"""
	archi=open('cifradoEscitala.txt','w')
	msg=''.join(cifrado)
	print(msg)
	for i in range(tam):
		#print(cifrado[i])
		archi.write(cifrado[i])
	
	archi.close()
	print("\n 	Se ha terminado de cifrar, revisa el arhivo cifradoEscitala.txt");

def descifrarEscitala():
	global archivo
	archivo=raw_input("\n 	Ingresa la ruta del archivo a descifrar: ")
	archi=open(archivo,'r')
	text=archi.read()
	print("\n	Cifrado "+text)
	texto=list(text)
	print("\n 	Indique las columnas para descifrar:")
	col=input()
	print("\n 	Indique las filas para descifrar:")
	row=input()
	tam=col*row

	m=[]
	for i in range(row):
		m.append([0]*col)

	con=0
	tam=len(text)
	for i in range(0,col):
		for j in range(0,row):
			m[j][i]=text[con]			
			con=con+1

	msgOr=[]
	for i in range(tam):
		msgOr.append(" ")

	con=0
	for i in range(0,row):
		for j in range(0,col):
			msgOr[con]=m[i][j]		
			con=con+1

	archi=open('mensajeEscitala.txt','w')
	for i in range(tam):
		archi.write(msgOr[i])
	archi.close()

def cifrarMorse():
    infile = open(archivo,'r')
    msg = infile.read(200)
    verify(msg)
    print ('El fichero dice:'+ '\n' + msg + '\n')
    print "_________________________________________________"
    print "encriptando informacion del fichero..."
    print "_________________________________________________"
    archi=open('cifradoMorse.txt','w')
    
    for char in msg:
        if char == ' ':
            print ' '*2,
        else:
            archi.write(CODE[char.upper()]+" ")
    
    archi.close()
    print("\n 	Se ha terminado de cifrar, revisa el arhivo cifradoMorse.txt");

def verify(string):
    keys = CODE.keys()
    for char in string:
        if char.upper() not in keys and char != ' ':
            sys.exit('OJO con el caracter ' + char + ' no puede ser traducido a clave morse en su lugar use espacio.')
            raise BaseException(format(char))

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

def descifrarMorse():
	global archivo
	archivo=raw_input("\n 	Ingresa la ruta del archivo a descifrar: ")
	infile = open(archivo,'r')
	msg = infile.read()
	morse=msg.split(" ")
	print ('El fichero dice:')
	print(morse)
	print "_________________________________________________"
	print "encriptando informacion del fichero..."
	print "_________________________________________________"
	tam=len(morse)-1
	archi=open('mensajeMorse.txt','w')
	for i in range(tam):
		archi.write(CODE2[morse[i]])
	archi.close()
	print("\n 	Se ha terminado de descifrar, revisa el arhivo mensajeMorse.txt");

CODE2 = {'.-': 'A',     '-...': 'B',   '-.-.': 'C', 
        '-..': 'D',    '.': 'E',      '..-.': 'F',
        '--.': 'G',    '....': 'H',   '..': 'I',
        '.---': 'J',   '-.-': 'K',    '.-..': 'L',
        '--': 'M',     '-.': 'N',     '---': 'O',
        '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
        '...': 'S',    '-': 'T',      '..-': 'U',
        '...-': 'V',   '.--': 'W',    '-..-': 'X',
        '-.--': 'Y',   '--..': 'Z',
        '-----': '0',  '.----': '1',  '..---': '2',
        '...--': '3',  '....-': '4',  '.....': '5',
        '-....': '6',  '--...': '7',  '---..': '8',
        '----.': '9'
        }

abc = 'abcdefghijklmnopqrstuvwxyz'
    #datos para el cifrado cesar

def cifrarCesar():
	archi=open(archivo,'r')
	msg=archi.read()
	c = msg.lower() 
	n = int(raw_input('Ingresa la clave numerica: '))
	
	text_cifrado = ''
	archi=open('cifradoCesar.txt','w')
	for letra in c:
		suma = abc.find(letra) + n
		modulo = int(suma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])
	archi.write(text_cifrado)
	archi.close()
	print("\n 	Se ha terminado de cifrar, revisa el arhivo cifradoCesar.txt");

def descifrarCesar():
	global archivo
	archivo=raw_input("\n 	Ingresa la ruta del archivo a descifrar: ")
	cn = int(raw_input('Ingresa la clave numerica: '))
	text_cifrado = ''
	archi=open(archivo,'r')
	msg=archi.read()
	archi.close()
	arch=open('mensajeCesar.txt','w')
	for letra in msg:
		suma = abc.find(letra) - cn
		modulo = int(suma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])
	arch.write(text_cifrado)
	arch.close()
	print("\n 	Se ha terminado de descifrar, revisa el arhivo mensajeCesar.txt");

abrirArchivo()
main()