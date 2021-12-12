#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA = ['Sex', 'Embarked']

CATEGORICAL_VARS_WITH_NA_FREQ = ['Sex', 'Embarked']

#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['Age']

#Varibles para transformación logaritmia
NUMERICALS_LOG_VARS = ["Fare"]

#Variables para hacer mapeo categorico 
BINARY_VARS =  ['Sex']
MAR_VARS = ['Embarked']

#Mapeos de variables categoricas
BINARY_MAP = {'male': 0, 'female': 1}

MAR_MAP = {'C':1, 'Q':2, 'S': 3, 'nan': 0}

#Variables seleccionadas según análisis de Lasso
FEATURES = ['Pclass', 'Sex', 'Age', 'SibSp', 'Embarked']