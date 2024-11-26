# importamos los modelos
import orm.modelos as modelos

# importamos el objeto sesión
from sqlalquemy.orm import Session

# Esta función es llamada por api.py
# para atender GET '/usuarios/{id}'
# SELECT * FROM app.usuarios WHERE id=2 
def usuario_por_ID(sesion:Session, id_usuario:int):
    print("select * from app.usuarios where id= ", id_usuario)
    # Con first() devuelve el primer elemento de la lista encontrado coincidente
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

# SELECT * FROM app.compras WHERE id=2
def compra_por_ID(sesion:Session, id_compra:int):
    print("select * from app.compras where id= ", id_compra)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_compra).first()

# SELECT * FROM app.compras WHERE id=1
def foto_por_ID(sesion:Session, id_foto:int):
    print("select * from app.fotos where id= ", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.foto.id==id_foto).first()
