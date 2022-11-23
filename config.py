import os
import ProxyCloud

BOT_TOKEN = '5762258841:AAF_T2lW812AVyqqdFeYoMh96-qA5kn0Wzo' #Aqui va el token del bot
API_ID =  9520699 #Tu api id de telegram
API_HASH = '353e5b6ef2c174d0e8d7fb62e277840d' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','bladimirlorenzo').split(';')

static_proxy = '' #agrega si kieres tener un proxy statico Con @bladimirlorenzo si kieres comprar un proxy
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['bladimirlorenzo'] = 0
