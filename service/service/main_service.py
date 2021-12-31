import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd


class MorseCodeService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):
        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)
        start_time = time.time()

        texto=" ".join(texts['textoMensagem'])
        response_codes = self.traduzir_code(texto)

        logger.debug(mensagens.FIM_SERVICO)
        logger.debug(f"Fim de todas as conversoes em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['textoMensagem'])
        df_response['conversao'] = response_codes

        df_response = df_response.drop(columns=['textoMensagem'])

        response = {
                     "listaFrases": json.loads(df_response.to_json(
                                                                            orient='records', force_ascii=False))}

        return response

    def traduzir_code(self, texts):
        logger.debug('Iniciando a codificacao...')
        code = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....',
            'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-',
            'U': '..-', 'V': '...-',
            'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----',
            '2': '..---', '3': '...--',
            '4': '....-', '5': '.....',
            '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', ' ': ' '
        }
        response = [] 
        
        for text in texts:
            response += code[text.upper()]
              
        codemorse="".join(response)

        return codemorse
