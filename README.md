# Predicting user conversions

Desarrollo de algoritmos de Machine Learning para la competencia de Kaggle
[www.kaggle.com/c/trocafone](https://www.kaggle.com/c/trocafone) en la que obtuvimos el segundo puesto.

## Competencia

La competencia consistía en determinar, para cada usuario presentado, la probabilidad de que dicho usuario realice una compra en la plataforma [Trocafone](trocafone.com) en un periodo determinado.

## Herramientas utilizadas

 - [Python 3](https://www.python.org/)
 - [Jupyter](https://jupyter.org/)
 - [Pandas](https://pandas.pydata.org/)
 - [Numpy](https://numpy.org/)
 - [scikit-learn](https://scikit-learn.org/)

## Algoritmos de Machine Learning

Algunos de los algoritmos de Machine Learning utilizados fueron:

 - [AdaBoost](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)
 - [Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html)
 - [RandomForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
 - [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)
 - [XGBoost](https://xgboost.readthedocs.io/en/latest/)
 
## Ensambles

A su vez los resultados de los algoritmos de machine learning fueron combinados para obtener un mejor resultado en los siguientes ensambles:

 - [Blending]()
 - [Stacking]()
 
## Prerequisitos
 - [Python 3](https://www.python.org/)

## Instalación
Se recomienda utilizar un [virtual environment](https://virtualenv.pypa.io/en/latest/) para realizar la instalación. Luego ejecutar:

    $ pip install -r requirements.txt

## Ejecución
Para lanzar la notebook ejecutar:
    
    $ jupyter notebook

Si se desa se puede leer el [informe](https://github.com/seblaz/Predicting-user-conversions/blob/master/Informe.pdf) con más detalles.
