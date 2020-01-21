# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:00:12 2020

@author: Daniel Santos
"""

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score

data = pd.read_csv('base_alunos.csv', sep=';',encoding='latin-1', error_bad_lines=False)
#data = data.loc[:, ~data.columns.str.match('Unnamed')]

#situation types
data.loc[data.Situacao_Matricula == 'Abandono','Situacao_Matricula']= 'Desistente'
data.loc[data.Situacao_Matricula == 'Trancado','Situacao_Matricula']= 'Desistente'
data.loc[data.Situacao_Matricula == 'Cancelado Voluntariamente','Situacao_Matricula']= 'Desistente'
data.loc[data.Situacao_Matricula == 'Cancelado Compulsoriamente','Situacao_Matricula']= 'Desistente'
data.loc[data.Situacao_Matricula == 'Formado','Situacao_Matricula'] = 'Concludente'
data.loc[data.Situacao_Matricula == 'Concluído','Situacao_Matricula'] = 'Concludente'


#Database of students who dropped out of college
Desistentes = data.loc[(data.Situacao_Matricula == 'Desistente')]
Concludentes = data.loc[(data.Situacao_Matricula == 'Concludente')]


dataset = pd.concat([Desistentes,Concludentes])


previsores = dataset.iloc[:,[2,3,13,16,19,20,24,25,41,47]].values

classe = dataset.iloc[:, 4].values

labelencoder_prev = LabelEncoder()
previsores[:,1] = labelencoder_prev.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder_prev.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder_prev.fit_transform(previsores[:,3])
previsores[:,5] = labelencoder_prev.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder_prev.fit_transform(previsores[:,6])
previsores[:,7] = labelencoder_prev.fit_transform(previsores[:,7])
previsores[:,8] = labelencoder_prev.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder_prev.fit_transform(previsores[:,9])





