# 🧠 GPU Shortage Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Model](https://img.shields.io/badge/Model-DistilBERT-yellow?logo=huggingface&logoColor=black)

Analisi del sentiment su tweet riguardanti le principali aziende produttrici di GPU (NVIDIA, AMD, Intel) durante il periodo di **shortage globale di schede video** (2020–2021), con tecniche di NLP e modelli preaddestrati di Hugging Face.

---

## 🧰 Tech Stack

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" width="40" />
  <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="40" />
</p>

---

## 📁 Contenuto del progetto

- `main.ipynb` — Notebook principale con tutte le fasi:
  - Caricamento e pulizia dati
  - Preprocessing del testo
  - Sentiment analysis (DistilBERT via HuggingFace)
  - Analisi esplorativa (visualizzazioni, WordCloud)
  - Analisi per brand (NVIDIA, AMD, Intel)
- `utils/` — Funzioni riutilizzabili
- `data/` — Dataset dei tweet (non incluso)
- `output/` — File CSV con i risultati (facoltativo)
- `requirements.txt` — Librerie richieste

---

## 🤗 Sentiment Analysis

Il modello utilizzato è:

> `distilbert-base-uncased-finetuned-sst-2-english`

Via HuggingFace `pipeline`, il sentiment è assegnato come:
- `positive`
- `negative`

---

## 📊 Analisi effettuate

- Distribuzione dei tweet per sentiment
- Andamento del sentiment nel tempo
- Boxplot dello score
- WordCloud per tipo di sentiment
- Retweet medi per sentimento
- Analisi per brand (NVIDIA, AMD, Intel, altro)

---

## 📷 Esempi di output

| Distribuzione sentiment | WordCloud Positivi |
|-------------------------|--------------------|
| ![](img/sentiment_distribution.png) | ![](img/wordcloud_positive.png) |

---

## ⚙️ Esecuzione

1. Clona la repository
2. Installa i requisiti:
   ```bash
   pip install -r requirements.txt
3. Avvia il notebook:
   ```bash
   jupyter notebook main.ipynb

## Requirements

Per far funzionare correttamente questo progetto, assicurati di avere installate le seguenti librerie Python:

- pandas  
- numpy  
- matplotlib  
- seaborn  
- nltk  
- transformers  
- scikit-learn  
- wordcloud

## 📄 Licenza

Questo progetto è rilasciato sotto licenza **Apache 2.0**.  
I dati originali dei tweet non sono redistribuiti per motivi di licenza.

---

## 👤 Autore

Salvatore Zizzi — Studente di Statistica, appassionato di NLP e AI.  
📫 [LinkedIn](https://www.linkedin.com/in/salvatore-zizzi-242151107/)

