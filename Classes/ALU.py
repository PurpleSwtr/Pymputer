from typing import Callable
from utils.formated import center_text_fill
from utils.check import check
from utils.instructions import TO_DEC, list_to_tuple, tuple_to_int

# TODO:
# - [x] AND
# - [x] XOR
# - [x] AND + XOR = HALF ADDER!!!
# - [x] HALF ADDER + HALF ADDER + OR = FULL ADDER!!!!!!!

def command_print(instruction: str, num_1: int, num_2: int, res: int) -> None:
    # return print(f'{TO_DEC(num_1)}({num_1}) {instruction} {TO_DEC(num_2)}({num_2}) = {TO_DEC(res)} ({res})')
    return print(f'{TO_DEC(num_1)} {instruction} {TO_DEC(num_2)} = {TO_DEC(res)}')

"""
Арифметико-логическое устройство.

Требуется также реализовать помимо сложения и остальные методы.
"""

class ALU():
    
    def __init__(self):
        self.counter: int = 0
        self.instruction: Callable
        self.arguments: tuple

        self.access_instuctions: dict = {
            '0010': self.ADD_4
        }

        self.command_print: str

    def __repr__(self):
        return f" [ALU_PC] {self.counter}"
    
    @check()
    def AND(self, a: int, b: int) -> int:
        if a == 1 and b == 1:
            return 1
        else:
            return 0
    @check()
    def OR(self, a: int, b: int) -> int:
        if a == 1 or b == 1:
            return 1
        else:
            return 0
    
    @check()
    def XOR(self, a: int, b: int) -> int:
        first_step = self.AND(a, b)
        second_step = self.NOT(first_step)

        semi_step = self.OR(a, b)
        
        final_step = self.AND(second_step,semi_step)
        return final_step
    
    @check(num_inputs=1) 
    def NOT(self, a: int) -> int:
        if a == 1:
            return 0
        else:
            return 1

    @check(output_labels=('CARRY', 'SUM'))
    def HALF_ADDER(self, a: int, b: int) -> tuple:
        output_sum = self.XOR(a, b)
        output_carry = self.AND(a, b)
        #  CARRY, SUM
        return (output_carry, output_sum)
    
    @check(num_inputs=3, output_labels=('CARRY', 'SUM'))
    def FULL_ADDER (self, a: int, b:int, c:int) -> tuple:
        half_adder_1_c, half_adder_1_s = self.HALF_ADDER(a, b)
        half_adder_2_c, half_adder_2_s = self.HALF_ADDER(half_adder_1_s, c)
        
        output_carry = self.OR(half_adder_1_c, half_adder_2_c) 
        output_sum = half_adder_2_s
        
        return (output_carry, output_sum)
    
    @check(num_inputs=8, output_labels=('CARRY', 'S3', 'S2', 'S1', 'S0'))
    def ADD_4(self, *args: int) -> tuple:
        if len(args) != 8:
            raise ValueError("функция ожидает 8 бит")
            
        a_bits_msb = args[0:4]  # Первые 4 бита
        b_bits_msb = args[4:8]  # Следующие 4 бита

        a_bits_lsb = list(reversed(a_bits_msb))
        b_bits_lsb = list(reversed(b_bits_msb))

        carry_in = 0 
        result_sum_bits_lsb = [] 
        
        for i in range(4):
            carry_out, sum_bit = self.FULL_ADDER(a_bits_lsb[i], b_bits_lsb[i], carry_in)
            result_sum_bits_lsb.append(sum_bit)
            carry_in = carry_out
            
        final_sum_msb = tuple(reversed(result_sum_bits_lsb))
        output = (carry_in, *final_sum_msb)
        self.CHECK_OWERFLOW(output)
        return output
    
    @check(cnt_comands=False)
    def CHECK_OWERFLOW(self, bits: tuple) -> None:
        list_bits = list(bits)
        if list_bits[0] == 0:
            return
        else:
            print("\n[WARNING] - stack overflow!")

    @check()
    def LOAD_INSTRUCTION(self, instruction: list) -> None:
        # inspect.stack()
        instruction = tuple(instruction)
        self.instruction = self.access_instuctions[str(tuple_to_int(instruction))]
    
    @check()
    def LOAD_ARGUMENTS(self, arguments: list) -> None:
        self.arguments = list_to_tuple(arguments)
    
    # FIXME: Он единственный возвращает кортеж в компьютер, нехорошо...
    @check()
    def RUN(self,) -> tuple:
        # FIXME: Возможно это станет большой блять проблемой...
        arguments = self.arguments
        return self.instruction(*arguments)
    
    @check()
    def command_print(self, instruction: str, arguments: list, result: tuple) -> None:
        print("|---=====---|")
        print(center_text_fill('(alu)'), end="")
        print(self)
        # FIXME: ХАРДКОД
        # for i, arg in enumerate(arguments):
        #     print(arguments[i])
        #     ...

        num_1_integer = tuple_to_int(arguments[0])
        num_2_integer = tuple_to_int(arguments[1])
        result_integer = tuple_to_int(result)

        command_print(instruction=instruction, 
                      num_1=num_1_integer, 
                      num_2=num_2_integer, 
                      res=result_integer)



