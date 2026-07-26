import logging
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def train_forecasting(df_hourly: pd.DataFrame, steps_ahead: int = 168) -> pd.DataFrame:
    logging.info("Treinando modelo de séries temporais (Holt-Winters)...")
    
    df_hourly = df_hourly.sort_values('data_entrada')
    series = df_hourly.set_index('data_entrada')['volume']
    
    # Modelo com Sazonalidade Diária (24 horas)
    model = ExponentialSmoothing(
        series, 
        trend='add', 
        seasonal='add', 
        seasonal_periods=24
    ).fit()
    
    forecast_values = model.forecast(steps=steps_ahead)
    
    # Criar DataFrame com as datas futuras previstas
    last_date = series.index[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(hours=1), periods=steps_ahead, freq='h')
    
    df_forecast = pd.DataFrame({
        'data_hora': future_dates,
        'demanda_prevista_exames': forecast_values.values.round()
    })
    
    return df_forecast