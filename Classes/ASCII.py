"""
Начиная с этого момента я думаю нужно пойти в сторону некоторых упрощений всё-таки...

Это конечно круто, что у меня весь core проекта написан буквально в стиле C,
без использования возможностей python, но если я всё-таки решу пойти в сторону добавление это в API,
то тут уже действительно будет стоять вопрос производительности, и мутить тут какой-то мега-словарь со всеми символами, где мы будем к нему обращаться звучит как перегруз. Всё-таки не на C пишу! 
"""
class ASCIManager():
    def __init__(self, encoding: str) -> None:
        self.encoding: str = encoding

    def decode(self, bin_num: str) -> str:
        bin_num = bin_num.replace(" ", "")
        integer = int(bin_num, 2)
        return chr(integer)

    def encode(self, text: str):
        encoded = [] 
        for char in text:
            encoded.append(bin(ord(char))[2:])   
        return encoded