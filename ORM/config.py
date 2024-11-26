# El engine permite configurar la conexión a la BD
from sqlalquemy import create_engine
# El session maker permite crear sesiones para hacer consultas
from sqlalquemy.orm import sessionmaker

from sqlalquemy.ext.declarative import declarative_base


# 1) Configurar la conexión a la base de datos
# servidor/BD://usuario:password@url:puerto/nombreBD
URL_BASE_DATOS = "postgresql://usuario-ejemplo:12345@localhost:5432/base-ejemplo"
# Conectarnos mediante el esquema app
engine =create_engine(URL_BASE_DATOS,
                        connect_args={
                                "options":"-csearch_path=app"
                            })

# 2) Obtener la clase que nos permite crear objetos tipo session
SessionClass = sessionmaker(engine) 

# crear una función para obtener objetos de la clase SessionClass
def obtener_sesion():
    sesion = SessionClass()
    try:
        # equivalente a return pero de manera segura
        yield sesion
    finally:
        sesion.close()


# 3) Obtener la clase base para mapear tablas
BaseClass = declarative_base
