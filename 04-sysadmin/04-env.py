import os
import pprint

env_var = os.environ


def get_env(env):
    return env_var.get(env, 'No existe')


# Imprime las variables de entorno VIRTUAL_ENV y JAVA_HOME.
pprint.pprint(f'1. VIRTUAL_ENV: {get_env("VIRTUAL_ENV")}')
pprint.pprint(f'2. JAVA_HOME: {get_env("JAVA_HOME")}')

# Crea la variable de entorno EOI-CURRENT-MODULE con el valor sysadmin
# y comprueba que se ha creado correctamente.
os.environ['EOI-CURRENT-MODULE'] = 'sysadmin'
pprint.pprint(f'3. EOI-CURRENT-MODULE: {get_env("EOI-CURRENT-MODULE")}')

# Muestra el directorio actual de trabajo.
pprint.pprint(f'4. Directorio actual de trabajo: {os.getcwd()}')

# Cambia el directorio de trabajo a /tmp
# y comprueba que se ha cambiado correctamente.
tmp = '/tmp'
os.chdir(tmp)
pprint.pprint(f'5. Nuevo directorio de trabajo: {os.getcwd()}')

# Crea el directorio eoi-files en /tmp
# y cambia el directorio de trabajo a este directorio.
if not os.path.exists('eoi-files'):
    os.mkdir('eoi-files')
os.chdir('eoi-files')
pprint.pprint(f'6. Nuevo directorio de trabajo: {os.getcwd()}')

# Crea el directorio mydir_l1/mydir_l2/mydir_l3 en /tmp/eoi-files
# y muevete a este directorio.
path = 'mydir_l1/mydir_l2/mydir_l3'
if not os.path.exists(path):
    os.makedirs(path)

os.chdir(path)
pprint.pprint(f'7. Nuevo directorio de trabajo: {os.getcwd()}')

# Crear fichero prueba.txt con texto "Hola mundo {username}"
with open('prueba.txt', 'w') as f:
    f.write(f'hola mundo, soy {os.environ.get("USER")}')

pprint.pprint(f'8. Archivo creado: {os.getcwd()}/prueba.txt')

# Eliminar prueba.txt
os.remove('prueba.txt')

# Volver al directorio tmp/eoi-files/mydir_l1/mydir_l2/
# y elimina el directorio mydir_l3
os.chdir('./..')
os.rmdir('mydir_l3')

# Vuelve a la carpeta /tmp y muestra todas las carpetas
# y ficheros de forma recursiva.
# * /tmp/pyright-2806-Rsp6P11I5K35
# dirs:  []
# filenames:  0
os.chdir(tmp)
pprint.pprint(f'9. Directorio actual de trabajo: {os.getcwd()}')
for root, dirs, files in os.walk(tmp):
    pprint.pprint(f'root: {root}')
    pprint.pprint(f'dirs: {len(dirs)}')
    pprint.pprint(f'filenames: {len(files)}')

# Muestra los directorios y ficheros que no sean ocultos(.)
pprint.pprint(f'10. Directorio sin ocultos: {os.getcwd()}')
for root, dirs, files in os.walk(tmp):
    path_components = root.split('/')
    if any(component.startswith('.') for component in path_components):
        continue
    pprint.pprint(f'root: {root}')
    pprint.pprint(f'dirs: {len(dirs)}')
    pprint.pprint(f'filenames: {len(files)}')


# Muevete al directorio eoi-files, crea un fichero de texto
# y guarda la ruta en una variable
os.chdir(f'{tmp}/eoi-files')
with open('name.txt', 'w') as f:
    f.write(f'hola mundo, soy {os.environ.get("USER")}')
name = os.path.abspath('name.txt')

