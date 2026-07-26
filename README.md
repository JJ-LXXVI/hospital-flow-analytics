# 🏥 Previsão de Demanda e Monitoramento de Gargalos Hospitalares

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

## 📌 Visão Geral
Este dashboard foi desenvolvido para otimizar o acompanhamento preditivo de demanda de exames e a identificação precoce de gargalos operacionais em setores críticos (Ambulatório, Internação e Pronto-Socorro).

A solução consolida métricas operacionais chave (KPIs), prevê oscilações temporais de volume e categoriza o risco por modalidade de exame (ECG, Ressonância, Tomografia e Ultrassom).

---

## 📸 Interface do Painel

> *Adicione aqui uma imagem/print do seu dashboard finalizado*  
> `![Dashboard Overview](caminho/para/imagem.png)`

---

## 📊 Estrutura e Indicadores

### 1. KPIs Principais (Cabeçalho)
* **% Média Probabilidade Gargalo:** Probabilidade percentual consolidada de ocorrência de gargalos operacionais.
* **Demanda Prevista Total:** Volume absoluto de exames projetados para o período selecionado.
* **Taxa de Gargalo:** Índice de severidade de sobrecarga nos setores operacionais.

### 2. Análise Temporal (Gráfico de Linhas)
* **Previsão de Demanda Temporal:** Acompanhamento fluido da oscilação de exames ao longo dos dias/horas.
* **Comportamento Preditivo:** Leitura contínua de picos operacionais para apoio ao dimensionamento de equipe e salas de exame.

### 3. Matriz de Gargalos Reais vs. Probabilidade
* **Cruzamento por Origem e Exame:** Detalhamento da probabilidade e contagem real de gargalos segmentado por:
  * **Ambulatório**
  * **Internação (Leito)**
  * **Pronto-Socorro**
* **Tipos de Exame:** ECG, Ressonância, Tomografia e Ultrassom.

---

## 🎛️ Filtros Interativos (Slicers)
* **Tipo de Exame (`tipo_exame`):** Filtro dinâmico por modalidade diagnóstica.
* **Final de Semana (`is_final_semana`):** Segmentação de comportamento operacional para dias úteis vs. fins de semana/plantões.

---

## 🛠️ Tecnologias Utilizadas
* **Microsoft Power BI Desktop:** Construção do modelo de dados, layout de UI/UX e visualizações.
* **DAX (Data Analysis Expressions):** Criação de medidas agregadoras, cálculo de probabilidade e métricas de demanda.
* **Modelagem de Dados:** Estruturação de dados relacionais para performance preditiva.

---

## 🚀 Como Executar o Projeto

1. Faça o clone ou download deste repositório.
2. Certifique-se de ter o **Power BI Desktop** instalado em sua máquina.
3. Abra o arquivo `.pbix` localizado na pasta principal do projeto.