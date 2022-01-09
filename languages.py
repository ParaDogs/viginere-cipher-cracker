# languages info

class Language:
    def __init__(self, alphabet, IC_min, IC_max, MIC_min, MIC_max):
        self.alphabet = alphabet
        self.IC_min = IC_min
        self.IC_max = IC_max
        self.MIC_min = MIC_min
        self.MIC_max = MIC_max

RU = Language("абвгдеёжзийклмнопрстуфхцчшщъыьэюя_", 0.03, 0.0529, 0, 0)

EN = Language("abcdefghijklmnopqrstuvwxyz_", 0.038, 0.0662, 0, 0)