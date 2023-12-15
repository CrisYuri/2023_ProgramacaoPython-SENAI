# Classe Data

class Data(object):
    # Dicionário com meses e dias em cada mês - usado na validação de mês e dia
    diasNoMes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # Método construtor
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.validarData()

    # Encapsulamento 
    def setDia(self, dia):
        self.dia = dia
    
    def getDia(self):
        return self.dia
   
    def setMes(self, mes):
        self.mes = mes
    
    def getMes(self):
        return self.mes
    
    def setAno(self, ano):
        self.ano = ano
    
    def getAno(self):
        return self.ano
    
    # Retorno de dados
    def __str__(self):
        return ('\n Dia: ' + str(self.getDia()) + 
                '\n Mês: ' + str(self.getMes()) + 
                '\n Ano: ' + str(self.getAno())
                )
    
    # Metodos de validação
    def validarAno(self):
        if self.ano < 0: #o ano tem que ser um valor positivo qualquer
            self.ano = 'Ano inválido'

    def validarMesDia(self):
        if self.mes == 2 and self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0): #se for ano bissexto, mês 2 tem 29 dias
            self.diasNoMes[2] = 29
        if self.mes in self.diasNoMes: #só vai entrar na validação do dia, se o mês for válido!
            if not (1<= self.dia <= self.diasNoMes[self.mes]): #o dia tem que estar entre 1 e o valor da chave do dicionário diasNoMes (=numero de dias de cada mês)
                self.dia = 'Dia inválido'
        else: #se o mês for inválido, retorna:
            self.mes = 'Mês inválido'
            self.dia = 'Mês inválido, não é possível validar o dia'

    def validarData(self):
        self.validarMesDia()
        self.validarAno()
