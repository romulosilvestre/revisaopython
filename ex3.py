# programação orientada a objetos

"""
 POO
"""
class Aluno():
    def __init__(self,ch,faltas):
        self.ch = ch
        self.faltas = faltas

    def calcular_faltas(self):
        percent_ch = self.ch * (25/100)        
        return f" faltas permitidas: {percent_ch}"