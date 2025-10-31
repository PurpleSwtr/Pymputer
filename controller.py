import time
from Classes.ASCII import ASCIManager
from Classes.Computer import Computer

# По факту вот так минимально можно это реализовать

if __name__ == "__main__":
    computer = Computer()
    while True:
        # Тут куча всего можно будет переносить в классы компьютера,
        # computer.comp_repr()
        choice = input("\n>>> ")
        if choice:
            computer.command(choice)