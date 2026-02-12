#creamos diccionarios de configuración para diferentes entornos
#config_base tiene la configuración común para todos los entornos, mientras que config_desarrollo y config_produccion tienen las configuraciones específicas para cada entorno
config_base = {
    "host": "localhost",
    "port": 3306,
    "debug": False
}
#config_desarrollo tiene debug activado y log_level en verbose, mientras que config_produccion tiene un host diferente y log_level en error
config_desarrollo = {
    "debug": True,
    "log_level": "verbose"
}
#config_produccion tiene un host diferente y log_level en error
config_produccion = {
    "host": "192.168.1.10",
    "log_level": "error"
}

#diccionarios
#usamos unpacking para combinar la configuración base con la específica de cada entorno, creando así config_final_dev y config_final_prod que contienen toda la configuración necesaria para cada entorno
config_final_dev = {**config_base, **config_desarrollo}
#config_final_prod combina la configuración base con la configuración de producción, sobrescribiendo el host y log_level según lo definido en config_produccion
config_final_prod = {**config_base, **config_produccion}


# versión con parámetros normales
# def conectar(host, port, debug, log_level):
#     print(f"Conectando a {host}:{port} | debug={debug} | log={log_level}")
def conectar(host, port, debug, log_level="info"):
    #imprimimos la configuración de conexión usando unpacking
    print(f"Conectando a {host}:{port} | debug={debug} | log={log_level}")


# llamada con unpacking
#usamos unpacking para pasar la configuración completa a la función conectar, lo que hace que el código sea más limpio y fácil de mantener, ya que no tenemos que especificar cada parámetro individualmente
conectar(**config_final_dev)
#usamos unpacking para pasar la configuración completa a la función conectar, lo que hace que el código sea más limpio y fácil de mantener, ya que no tenemos que especificar cada parámetro individualmente
conectar(**config_final_prod)


# kwargs
#creamos una función conectar_flexible que acepta cualquier cantidad de parámetros usando **kwargs, lo que permite una mayor flexibilidad al pasar configuraciones, ya que no estamos limitados a un conjunto específico de parámetros
def conectar_flexible(**kwargs):
    print(f"\nConfiguración recibida:")
    #usamos unpacking para iterar sobre los parámetros recibidos en kwargs e imprimir cada clave y valor, lo que permite ver fácilmente la configuración que se está utilizando sin importar qué parámetros se hayan pasado
    for clave, valor in kwargs.items():
        #imprimimos cada clave y valor usando unpacking, lo que hace que el código sea más dinámico y adaptable a diferentes configuraciones sin necesidad de modificar la función
        print(f"{clave}: {valor}")


# kwargs
conectar_flexible(**config_final_dev)
