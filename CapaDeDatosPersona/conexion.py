import re
from logger_base import log
import psycopg2 as db
import sys
class Conexion:
    _DATABASE = 'test'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def getConection(cls):
        if cls._conexion is None:
            try:
                cls._conexion = db.connect(host=cls._HOST,
                                            user=cls._USERNAME,
                                            password=cls._PASSWORD,
                                            port=cls._DB_PORT,
                                            database=cls._DATABASE)
                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio una excepcion {e}')
                sys.exit()
        else:
            return cls._conexion
    @classmethod
    def getCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.getConection().cursor()
                log.debug(f'se abrio el cursor:{cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor
if __name__ == '__main__':
    Conexion.getConection()
    Conexion.getCursor()