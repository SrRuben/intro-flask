from conexion.conexion import Conexion
class CiudadDao:

    def getCiudades(self):

        ciudadSQL = """
        SELECT id, descripcion 
        FROM ciudades
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        try:
            pass
        except:
            pass
        finally:
            pass
        
