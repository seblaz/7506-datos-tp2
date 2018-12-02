"""
La idea de esta notebbok es loguear los mejores hiperparámetros encontrados hasta ahora.
Se debe ejecutar desde la notebook de la siguiente forma:

%run -i write_hyperparameters.py

Además en la notebook debe existir una variable de tipo diccionario llamada 
hyperparameter_data que tenga los siguientes atributos:

    'algorithm': string
        Nombre del csv que va a guardar los hiperparámetros. 
    
    'hyperparameters': dict
        Diccionario con los hiperparámetros en el formato {hiperparámetro: valor}.
    
    'cv_splits': int
        Cantidad de splits utilizados para el cross validation.
    
    'auc': float
        Valor del auc obtenido.

    'features': list
        Lista de los features que se tenían al momento que se obtuvo el valor de auc.
"""

from os.path import join
import pandas as pd

# leo los hiperparámetros actuales
csv = join('hiperparametros', hyperparameter_data['algorithm']+'.csv')
mejores_resultados = pd.read_csv(csv, index_col='fecha')

# creo un dataframe con el nuevo resultado
nuevo_resultado = pd.DataFrame(data=hyperparameter_data['hyperparameters'], index=[pd.datetime.now().strftime("%Y-%m-%d %H:%M")])
nuevo_resultado['cv_splits'] = hyperparameter_data['cv_splits']
nuevo_resultado['features'] = ','.join(hyperparameter_data['features'])
nuevo_resultado['auc'] = hyperparameter_data['auc']
nuevo_resultado.index.name = 'fecha'

# lo agrego a los resultados anteriores y lo guardo
mejores_resultados = mejores_resultados.append(nuevo_resultado, sort=False)
mejores_resultados.to_csv(csv)