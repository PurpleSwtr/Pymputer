from utils.instructions import BYTE
from utils.formated import center_text_fill

class RegisterFile():
    def __init__(self, size: int = 4, registers_cnt: int = 4, pc: int = 0):
        self.size = size
        self.registers_cnt = registers_cnt

        self.registers = [[0]*size for _ in range(registers_cnt)]
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
        data = list(data)
        data.remove(0)
        self.registers[len(self.registers) - 1] = data