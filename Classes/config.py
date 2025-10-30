from dataclasses import dataclass

@dataclass
class Config():
    registers_cnt: int = 8
    registers_size: int = 8

config = Config()