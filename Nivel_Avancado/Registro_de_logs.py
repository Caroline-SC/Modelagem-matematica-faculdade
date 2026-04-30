import logging
from datetime import datetime
import os

caminho = r'C:\Users\202402860399\Documents\Modelagem_Matematica\Modelagem-matematica-faculdade\Nivel_Avancado\Arquivos\meu_log.log'

logging.basicConfig(
    filename = caminho,
    level=logging.INFO,
    encoding='utf-8',
    filemode='a',
    format= '%(levelname)s | %(message)s'
)

agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

logging.info(f'[{agora}] - O programa rodou com sucesso!')