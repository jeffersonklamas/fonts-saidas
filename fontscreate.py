#----------------------------------------------------------------------
# Biblioteca para criar saidas com fontes externas personalizáveis.
#
# Pacote instalado
# pip install pyfiglet
#
#
#----------------------------------------------------------------------
import pyfiglet
from pyfiglet import Figlet

# Para verificar as fontes disponíveis ver site http://www.figlet.org/fontdb.cgi

fonteEscolhida = Figlet(font='bell')

print (fonteEscolhida.renderText('Jefferson'))
