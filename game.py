"""
lab4 task5
"""
import random
class Room:
    """
    class representation game room
    """

    def __init__(self, room_name: str) -> None:
        self.room_name = room_name
        self.__room_desc = ''
        self.__conected_rooms = {}
        self.__character = None
        self.__item = None
        self.__link_rooms_info = ''


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
            self.__link_rooms_info = '\n'.join(\
                [f'The {self.__conected_rooms[key].room_name} is {key}'\
                for key in self.__conected_rooms])
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

    def get_details(self):
        """
        getter of rooms details
        """
        print(f'{self.room_name}\n'+ '-'*20 + f'\
\n{self.__room_desc}\
\n{self.__link_rooms_info}')

    def get_character(self):
        """
        getter of character in room
        """

        if self.__character:
            return self.__character

    def get_item(self):
        """
        getter of character in room
        """

        if self.__item:
            return self.__item

    def move(self, direction: str):
        """
        getter for room
        """
        if direction in self.__conected_rooms:
            return self.__conected_rooms[direction]
        return

class Enemy:
    """
    class representation enemy
    """

    __defeated = 0

    def __init__(self, enemy_name: str, enemy_desc: str) -> None:
        """
        func init
        """
        self.enemy_name = enemy_name
        self.__enemy_desc = enemy_desc
        self.__conversation = ''
        self.weakness = ''

    def set_conversation(self, conversation: str):
        """
        setter for conversation
        """
        self.__conversation = conversation

    def set_weakness(self, weakness: str):
        """
        setter for weakness
        """
        self.weakness = weakness

    def describe(self):
        """
        output info about enemy in room
        """
        print(f'{self.enemy_name} is here')
        print(self.__enemy_desc)

    def talk(self):
        """
        func to talk with enemy
        """
        return f'[{self.enemy_name} says]: {self.__conversation}'

    def fight(self, fight_with: object):
        """
        func generate a fight between two characters
        """
        win = random.choice([0, 0, 1, 1, 1])
        if win == 1:
            print(f'You fend {self.enemy_name} off with the {fight_with}')
            return True
        else:
            print(f'{self.enemy_name} crushes you, puny adventurer!')
            return False

    def get_defeated(self):
        """
        getter for defeated enemies
        """
        Enemy.__defeated =+ 1
        return Enemy.__defeated
class Item:
    """
    class representation item
    """
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__description = ''

    def set_description(self, desc: str):
        """
        setter for description of item
        """
        self.__description = desc

    def describe(self):
        """
        output info about item in room
        """
        print(f'The [{self.__name}] is here', end=' - ')
        print(self.__description)

    def get_name(self):
        """
        getter for name
        """
        if self.__name:
            return self.__name
