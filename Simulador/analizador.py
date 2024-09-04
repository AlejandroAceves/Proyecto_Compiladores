#Logica para el funcionamiento del analizador
#Leer archivo read.py
file = open("read.sh")

#Diccionarios Importantes para el analizador Lexico
identifiers = {'modify':'Modify Files', 'organize':'Organize files'}
identifiers_key = identifiers.keys()

keywords = {'date':'by date','Size':'by file size','text':'by file name', 'move':' move file to ', 
            'delete':'delete file','copy':' copy file', 'fileType':'by file type','on':'place'}
keywords_key = keywords.keys()

punctutators ={';':'end statement', '/':'Archive location','c://':'disk in use'}
punctutators_key = punctutators.keys()

#Programa lee el archivo read.py
readFile = file.read()

analize = readFile.split("\n")


#buscar los tokens en el archivo

for line in analize:
    #Leer los tokens en la linea
    tokens = line.split(';')

    #Encontrar los tokens
    for token in tokens:
        dir_pos =line.find("on;")
        # Verificar si el token es "on" (indicador del comienzo del directorio)
        if "on;" in line and token == "on":
            # Extraer el directorio después de "on;"
            dir_pos = line.find("on;")
            if dir_pos != -1:
                # Guardar la parte del directorio para mostrar al final
                directorio = line[dir_pos + len("on;"):].strip()
        if token in identifiers_key: 
            print("el identificador es: ", token, ":",identifiers[token])
        elif token in keywords_key: 
            print("el identificador es: ", token, ":", keywords[token])
        elif token in punctutators_key: 
            print("el identificador es: ", token, ":", punctutators[token])

if directorio:
    print("Directorio es:", directorio)
    
   
        