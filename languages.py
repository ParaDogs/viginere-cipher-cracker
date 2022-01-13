# languages info

class Language:
    def __init__(self, alphabet, IC, MIC_min, MIC_max):
        self.alphabet = alphabet
        self.IC = IC
        self.MIC_min = MIC_min
        self.MIC_max = MIC_max

RU = Language("абвгдежзийклмнопрстуфхцчшщъыьэюя_", 0.0529, 0.053, 0.07)

EN = Language("abcdefghijklmnopqrstuvwxyz_", 0.0662, 0.053, 0.07)