"""
Класс ассемблера.

Задача:
"w = R1 + R2" -> func -> "0010 0001 0010 0011"
"""
from utils.instructions import BYTE
from Classes.config import config
class Decoder():
    def __init__(self):
        self.register_size = config.registers_size
        self.commands = {
        '+': '0010',
        # 'R1': '0001',
        # 'R2': '0010',
        'w': '1101',
        '1': '0001',
        '2': '0000',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',

    }
    
    def to_chunks(self, final_output: str) -> list[str]:
        final_output = BYTE(final_output)
        chank = ""
        output = []
        for i, byte in enumerate(final_output):
            chank += str(byte)
            if len(chank) == 4:
                output.append(chank)
                chank = ""
        final_output = output
        return final_output
    
    def decode(self, command:str) -> list[str]:
        final_output_str = ""
        if not set(command) - {'0', '1', ' '}:
            final_output_str = command 
        else: 
            #FIXME: .split()
            commands_list = []
            added = ""
            for char in command:
                if char != " ":
                    added += char
                else:
                    commands_list.append(added)
                    added = ""
            commands_list.append(added)
            commands_list.pop(1)
            copy = commands_list.copy()
            commands_list = [copy[2], copy[1], copy[3], copy[0]]
            output_str = ""
            for char in commands_list:
                output_str += f'{self.commands[char]} '
            final_output_str = output_str

        raw_chunks = final_output_str.strip().split(' ')
        padded_chunks = []
        for chunk in raw_chunks:
            if chunk:
                padded_chunk = chunk.zfill(self.register_size)
                padded_chunks.append(padded_chunk)
        return padded_chunks

    def get_command_repr(self, command: list) -> str:
        command_str = "".join(map(str, command))
        opcode = command_str[-4:]
        for key, variable in self.commands.items():
            if variable == opcode:
                return key
        return "?"


