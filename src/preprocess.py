import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)


def load_and_clean_data(file_path: str) -> pd.DataFrame:
  logging.info(f'Carregando dados de: {file_path}')

  # Adicionado encoding='latin1' para evitar erros de acentuação no Windows/Pandas
  df = pd.read_csv(file_path, sep=';', encoding='latin1')

  # Parse explicito de data no formato DD/MM/YYYY HH:MM
  df['data_entrada'] = pd.to_datetime(
      df['data_entrada'], format='%d/%m/%Y %H:%M'
  )

  # Feature Engineering de Tempo
  df['hora_do_dia'] = df['data_entrada'].dt.hour
  df['dia_da_semana'] = df['data_entrada'].dt.dayofweek
  df['is_final_semana'] = df['dia_da_semana'].apply(
      lambda x: 1 if x >= 5 else 0
  )

  return df


def aggregate_hourly_volume(df: pd.DataFrame) -> pd.DataFrame:
  """Agrupa o histórico por hora para gerar a série temporal de demanda."""
  df_hourly = (
      df.set_index('data_entrada').resample('h').size().reset_index(name='volume')
  )
  return df_hourly