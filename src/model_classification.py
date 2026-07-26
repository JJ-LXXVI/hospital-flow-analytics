import logging
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def train_classifier(df: pd.DataFrame):
  logging.info('Treinando Modelo de Classificação de Gargalos...')

  # Incluindo as novas colunas de tempo no conjunto de atributos (X)
  X = df[[
      'tipo_exame',
      'prioridade',
      'origem_paciente',
      'hora_do_dia',
      'dia_da_semana',
      'is_final_semana',
      'tempo_espera_sala_min',
      'tempo_realizacao_min',
      'tempo_espera_laudo_min',
  ]]
  y = df['gargalo_identificado']

  categorical_cols = ['tipo_exame', 'prioridade', 'origem_paciente']
  numerical_cols = [
      'hora_do_dia',
      'dia_da_semana',
      'is_final_semana',
      'tempo_espera_sala_min',
      'tempo_realizacao_min',
      'tempo_espera_laudo_min',
  ]

  preprocessor = ColumnTransformer(
      transformers=[
          ('num', StandardScaler(), numerical_cols),
          ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
      ]
  )

  model_pipeline = Pipeline(
      steps=[
          ('preprocessor', preprocessor),
          (
              'classifier',
              RandomForestClassifier(n_estimators=100, random_state=42),
          ),
      ]
  )

  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42, stratify=y
  )

  model_pipeline.fit(X_train, y_train)

  preds = model_pipeline.predict(X_test)
  auc = roc_auc_score(y_test, model_pipeline.predict_proba(X_test)[:, 1])

  logging.info(f'Modelo Treinado. AUC-ROC: {auc:.4f}')

  joblib.dump(model_pipeline, 'models/gargalo_classifier.pkl')

  X_test_copy = X_test.copy()
  X_test_copy['gargalo_real'] = y_test
  X_test_copy['probabilidade_gargalo'] = model_pipeline.predict_proba(X_test)[
      :, 1
  ]

  return model_pipeline, X_test_copy