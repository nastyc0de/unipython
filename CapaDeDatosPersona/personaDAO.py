from conexion import Conexion
from persona import Persona
from logger_base import log

class PersonaDAO:
    """
        DAO .- Data Access Object
        CRUD .- Create Read Update Delete
    """
    _CREATE = 'INSERT INTO persona(name, lastName, email) VALUES (%s, %s, %s)'
    _READ = 'SELECT * FROM persona ORDER BY id'
    _UPDATE = 'UPDATE persona SET name=%s, lastName=%s, email=%s WHERE id=%s'
    _DELETE = 'DELETE FROM persona WHERE id=%s'

    @classmethod
    def select(cls):
        with Conexion.getCursor() as cursor:
            cursor.execute(cls._READ)
            registers = cursor.fetchall()
            personas = []
            for register in registers:
                persona = Persona(register[0], register[1], register[2], register[3])
                personas.append(persona)
            return personas

if __name__ == '__main__':
    personas = PersonaDAO.select()
    for persona in personas:
        log.debug(persona)