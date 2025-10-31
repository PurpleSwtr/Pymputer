import time
from Classes.ASCII import ASCIManager
from Classes.Computer import Computer

# TODO: реализовать взаимодействие например через консоль пока что, а всё логику вынести в отдельный файл.
# Чтобы можно было в реальном времени что0то отправлять в регистры

# Экземпляр основного класса ассемблера
computer = Computer()

# Отображение регистров памяти (16 бит)
computer.comp_repr()

"""
Ассемблер спроектирован так, чтобы иметь возможность выполнять программы как в машинных кодах,
так и на упрощенном ассемблерном языке.
"""

# Варианты передачи машинного кода:
computer.command("0010 0100 0010 0101")
computer.command("0010 1110 0010 0101")

# Пример выполнения ассемблерной команды. 
computer.command("w = 12 + 12")

# Первый прототип эмулятора декодера ASCI символов 

decoder = ASCIManager(encoding="")

# 128 64 32 16   8 4 2 1 
# 0   0  0  0    0 0 0 0

asm_dir = "Classes/asm.txt"
asm_file = []

just_text = "Это кажется просто обычный текст\nНо что происходит на самом деле в регистрах памяти, и как команды видит процессор?\nПолучается что вот так...\nА вроде бы обычный print"

with open(asm_dir, "w") as file:
    lines = decoder.encode(just_text)
    for line in lines:
        file.write(line + "\n")

with open(asm_dir, "r") as file:
    for line in file:
        asm_file.append(line.strip())
        print(decoder.decode(line.strip()), end="")
        time.sleep(0.01)
print()