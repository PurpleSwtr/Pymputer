from Classes.RegisterFile import RegisterFile
from Classes.ProgrammCounter import PC
from Classes.Decoder import Decoder
from Classes.ALU import ALU

"""
Главный класс компьютера, который на самом деле пока что даже процессор не реализует..
Но в дальнейшем предполагается, что тут будет отдельный класс процессора, который соберёт
в себе кучу ещё не реализованных компонентов, а уже этот компонент войдёт в следующий уровень абстракции компьютера.
"""

class Computer():

    def __init__(self, reg: RegisterFile = None, pc: PC = None, decoder: Decoder = None, alu: ALU = None):
        self.pc = pc or PC()
        self.reg = reg or RegisterFile(pc=self.pc)
        self.decoder = decoder or Decoder()
        self.alu = alu or ALU()
    
    def comp_repr(self,) -> None:
        print(self.reg)

    def command(self, exec: str):
        self.pc.add()
        exec = self.decoder.decode(exec)
        self.reg.load_instruction(execute=exec)
        instruction = self.reg.get_instruction()
        arguments = self.reg.get_arguments()
        self.alu.LOAD_INSTRUCTION(instruction=instruction)
        self.alu.LOAD_ARGUMENTS(arguments=arguments)
        result = self.alu.RUN()
        self.reg.write(data=result)

        self.comp_repr()
    
        operate = self.decoder.get_command_repr(instruction)
        self.alu.command_print(instruction=operate, arguments=arguments, result=result)
