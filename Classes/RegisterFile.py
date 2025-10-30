from utils.instructions import BYTE
from utils.formated import center_text_fill

from Classes.config import config

class RegisterFile():
    def __init__(self, 
                 registers_cnt: int = config.registers_cnt, 
                 registers_size: int = config.registers_size, 
                 pc: int = 0):
        self.size = registers_size
        self.registers_cnt = registers_cnt

        self.registers = [[0]*registers_size for _ in range(registers_cnt)]
        self.pc = pc
    
    def _format_register_data(self, register_data: list[int]) -> str:
        return " ".join(map(str, register_data))

    def __repr__(self):
        output = '\n'
        output += center_text_fill("(reg)")
        output += f' [PC] {self.pc.counter}'
        for i, register_data in enumerate(self.registers):
            prefix = ""
            if i == 0:
                prefix = f"[OP]"
            elif i == len(self.registers) - 1:
                prefix = f"[w] "
            else:
                prefix = f"[R{i}]"
            output += f'\n{prefix:<5} {self._format_register_data(register_data)}'
        return output

    def load_instruction(self, execute: list[str]) -> None:
        for i, chank in enumerate(execute):
            if i < len(self.registers):
                data = BYTE(chank)
                self.registers[i] = data

    def get_instruction(self) -> list:
        return self.registers[0]
    
    def get_arguments(self) -> list:
        return [self.registers[i] for i in range(1,self.registers_cnt - 1)]
    
    def write(self, data: tuple) -> None:
        result_bits = list(data)[1:]
        self.registers[len(self.registers) - 1] = result_bits