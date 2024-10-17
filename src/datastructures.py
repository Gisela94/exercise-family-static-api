
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1

        # example list of members
        self._members = []
    

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member['id'] = self._generateId() #Para generarle un ID al nuevo miembro
        self._members.append(member) #La función append integra ese miembro a la familia

    def delete_member(self, id):
        # fill this method and update the return
        for index, member in enumerate(self._members): # Recorremos la lista de miembros
            if member['id'] == id: # Si encontramos un miembro con el id dado, lo eliminamos
                self._members.pop(index)  # Eliminamos el miembro
            return True  # Retornamos True indicando que se eliminó correctamente
        return False # Si no se encontró un miembro con el id dado, retornamos False

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members: # Recorremos la lista de miembros
            if member['id'] == id: # Si encontramos un miembro con el id dado, lo retornamos
                return member
            return None # Si no encontramos ningún miembro con ese id, retornamos None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
