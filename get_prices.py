import pandas as pd
import requests, json, re

model_result = pd.read_csv('modelos_resultado.csv', sep=';', index_col='model')
precios = pd.read_csv('precios_a_buscar.csv', index_col='sku')

for url in model_result['url']:
    r = requests.get(url)
    if r.status_code != 200:
        raise ValueError('Request invalido')
    json_string = re.search('(?<=var trocables = )(.*)(?=;\n)', r.text).group()
    products = json.loads(json_string)
    for product in products:
        sku = product['trocable_id'] # trocable_id = sku
        if sku in precios.index:
            for key, value in product.items():
                if (key == 'installments_info') or (key == 'images'):
                    value = json.dumps(value)
                precios.loc[sku, key] = value

precios.to_csv('precios_resultado.csv')
assert(precios[precios['model'].isna()].shape[0] == 0)