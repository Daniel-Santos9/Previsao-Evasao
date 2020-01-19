# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:00:12 2020

@author: Daniel Santos
"""

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score

data = pd.read_csv('data_sis.csv', sep=';',encoding='latin-1', error_bad_lines=False)
#data = data.loc[:, ~data.columns.str.match('Unnamed')]

#situation types
Abandono = data.loc[data.Situacao_Matricula == 'Abandono']
Trancamento = data.loc[data.Situacao_Matricula == 'Trancado']
Cancelado_vol = data.loc[data.Situacao_Matricula == 'Cancelado Voluntariamente']
Cancelado_comp = data.loc[data.Situacao_Matricula == 'Cancelado Compulsoriamente']
Formado = data.loc[data.Situacao_Matricula == 'Formado']
Matriculado = data.loc[data.Situacao_Matricula == 'Matriculado']
Transferido_ext = data.loc[data.Situacao_Matricula == 'Transferido Externo']


#Database of students who dropped out of college
Desistentes = data.loc[(data.Situacao_Matricula == 'Abandono') | (data.Situacao_Matricula == 'Trancado') | (data.Situacao_Matricula == 'Cancelado Voluntariamente') | (data.Situacao_Matricula == 'Cancelado Compulsoriamente')]
Form_matri = Formado = data.loc[(data.Situacao_Matricula == 'Formado')|(data.Situacao_Matricula == 'Matriculado')]
