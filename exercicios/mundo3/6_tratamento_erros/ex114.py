import urllib.request
from urllib.error import HTTPError

def verificar_pudim():
    try:
        with urllib.request.urlopen(urllib.request.Request("https://pudim.com.br", headers = 
            {
            # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0'
            }
            )) as response:
            if response.getcode() == 200:
                return "\033[1;33mO site Pudim é acessível\033[m"
    except HTTPError as erro:
            return f"\033[1;31mO site Pudim está inacessível/fora do ar: {erro.code}\033[m"

print(verificar_pudim())