import logging
from src.preprocess import load_and_clean_data, aggregate_hourly_volume
from src.model_classification import train_classifier
from src.model_forecasting import train_forecasting

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_pipeline():
    logging.info("--- INICIANDO PIPELINE HOSPITAL FLOW ANALYTICS ---")
    
    # 1. Pré-processamento
    df = load_and_clean_data("data/raw_hospital_data.csv")
    df_hourly = aggregate_hourly_volume(df)
    
    # 2. Classificação de Gargalo
    _, df_class_results = train_classifier(df)
    
    # 3. Previsão de Demanda Horária
    df_forecast = train_forecasting(df_hourly, steps_ahead=168)
    
    # 4. Exportação consolidada para uso no Power BI
    df_forecast.to_csv("data/processed_predictions.csv", index=False, sep=";")
    df_class_results.to_csv("data/risk_predictions.csv", index=False, sep=";")
    
    logging.info("--- PIPELINE CONCLUÍDA COM SUCESSO ---")

if __name__ == "__main__":
    run_pipeline()