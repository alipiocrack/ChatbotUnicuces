import sys
sys.path.append("./src/database")
sys.path.append("./src/interfaces")
sys.path.append("./src/views")

from TipoUsuario import TipoUsuario

tipoUsuario = TipoUsuario()
tipoUsuario.init()