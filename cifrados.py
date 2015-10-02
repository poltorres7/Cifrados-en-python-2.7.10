"""Variable global que contendra el archivo a trabajar"""
archivo=""

def main():
	"""Menu de opciones de todo el programa"""
	opc=0;
	while opc!=10:
		print("\nMenu\n")
		print("1.- Ingresa un archivo .txt a descifrar o cifrar\n")
		print("2.- Cifrado Morse 	6.- Descifrar Morse\n")
		print("3.- Cifrado ASCII 	7.- Descifrar ASCII\n")
		print("4.- Cifrado Cesar 	8.- Descifrar Cesar\n")
		print("5.- Cifrado Escitala 	9.- Descifrar Escitala\n")
		print("10.- Salir\n")
		print("Opcion:")
		opc=input()
		if opc == 1:
			abrirArchivo()
		elif opc == 2:
			cifrarMorse()
		elif opc == 3:
			cifrarASCII()
		elif opc == 4:
			cifrarCesar()
		elif opc == 5:
			cifrarEscitala()
		elif opc == 6:
			descifrarMorse()
		elif opc == 7:
			descifrarASCII()
		elif opc == 8:
			descifrarCesar()
		elif opc == 9:
			descifrarEscitala()
		elif opc == 10:
			print("\n 		Adios!!!")
		else:
			opc=10;
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

	tam=len(text)
	
	"""hacemos el array que usaremos para guardar nuestro cifrado"""
	cifrado=[]
	for i in range(tam):
		cifrado.append(0)

	"""hacemos el cifrado"""
	cont=0
	for i in range (tam):
		x=(col*(i%row))+(i/row)		
		"""metodo de ordenamiento para el cifrado"""
		cifrado[cont]=text[x]
		cont=cont+1
	"""cifrado es tipo list, lo pasamos a string para poder llenar el txt"""
	cif=''.join(cifrado)
	print("\nCifrado: "+cif)
	archi=open('cifradoEscitala.txt','w')
	archi.write(cif)
	archi.close()

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

	"""se crea el arreglo donde se escribira el mensaje"""
	desCifrado=[]
	for i in range(tam):
		desCifrado.append(0)
	
	cont=0
	for i in range (tam):
		x=(row*(i%col))+(i/col)		
		"""metodo de ordenamiento para el descifrado"""
		desCifrado[cont]=texto[x]
		cont=cont+1
	mensaje=''.join(desCifrado)
	print("\n	Mensaje: "+mensaje)

	archi=open('mensajeEscitala.txt','w')
	archi.write(mensaje)
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

main()