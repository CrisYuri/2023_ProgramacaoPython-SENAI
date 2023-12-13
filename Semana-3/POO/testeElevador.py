# Teste Elevador
import random
from Elevador import Elevador

# Criação e instância de um objeto de classe elevador
e1 = Elevador(andarAtual=0, portaAberta=True, peso=random.random()*1000)

# Exibindo o elevador parado
print('\n\t\t\t -- Elevador Parado --')
print(e1)

# Subindo...
print('\n\t\t\t -- Subir --')
e1.subir(5)

# Exibindo o elevador no 5º andar
print('\n\t\t\t -- Elevador no 5º andar --')
print(e1)

# Descendo...
print('\n\t\t\t -- Descer -- ')
e1.descer(0)

# Exibindo o elevador no 5º andar
print('\n\t\t\t -- Elevador no Térreo --')
print(e1)