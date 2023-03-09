"""
lab4 task5
"""

class Room:
    """
    class representation game room
    """

    def __init__(self, room_name: str) -> None:
        self.room_name = room_name
        self.__room_desc = ''
        self.__conected_rooms = {}

    def set_description(self, description: str):
        """
        setter game description
        """
        self.__room_desc = description

    def link_room(self, __o: object, direction: str):
        """
        connect room to another room
        """
        if isinstance(__o, Room):
            self.__conected_rooms[direction] = __o 
            return
        print('BAD ROOM')

    def set_character(self, character: object):
        """
        setter of character
        """
        self.__character = character

    def set_item(self, item: object):
        """
        setter of item in room
        """
        self.__item = item

class Enemy:
    """
    class representation enemy
    """

    def __init__(self, enemy_name: str, enemy_desc: str) -> None:
        """
        func init
        """
        self.enemy_name = enemy_name
        self.__enemy_desc = enemy_desc
        self.__conversation = ''
        self.__weakness = ''

    def set_conversation(self, conversation: str):
        """
        setter for conversation
        """
        self.__conversation = conversation

    def set_weakness(self, weakness: str):
        """
        setter for weakness
        """
        self.__weakness = weakness

class Item:
    