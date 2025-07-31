# 🧠 GPU Shortage Sentiment Analysis (GPU market analysis V1.0)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)  
![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  
![Model](https://img.shields.io/badge/Model-DistilBERT-yellow?logo=huggingface&logoColor=black)

Sentiment analysis on tweets related to the main GPU manufacturers (NVIDIA, AMD, Intel) during the **global graphics card shortage** (2020–2021), using NLP techniques and pretrained models from Hugging Face.

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

## 📁 Project Structure

- `main.ipynb` — Main notebook covering all steps:
  - Data loading and cleaning  
  - Text preprocessing  
  - Sentiment analysis (DistilBERT via Hugging Face)  
  - Exploratory data analysis (visuals, WordCloud)  
  - Brand-specific analysis (NVIDIA, AMD, Intel)  
- `utils/` — Reusable utility functions  
- `data/` — Tweet dataset (not included)  
- `output/` — CSV output files (optional)  
- `requirements.txt` — Required libraries  

---

## 🤗 Sentiment Analysis

The model used:

> `distilbert-base-uncased-finetuned-sst-2-english`

Using Hugging Face's `pipeline`, sentiment is classified as:
- `positive`
- `negative`

---

## 📊 Analysis Performed

- Sentiment distribution of tweets  
- Sentiment trends over time  
- Score boxplots  
- WordClouds by sentiment  
- Average retweets per sentiment  
- Brand-wise analysis (NVIDIA, AMD, Intel, others)  

---

## 📷 Sample Outputs

| Sentiment Distribution | Positive WordCloud |
|------------------------|--------------------|
| ![](images/Evolution_Sentiment.png) | ![](images/WordCloud_Positive.png) |

---

## ⚙️ How to Run

1. Clone the repository  
2. Install the required packages:
   ```bash
   pip install -r requirements.txt


## Requirements

To run this project, make sure you have the following Python libraries installed:

- pandas  
- numpy  
- matplotlib  
- seaborn  
- nltk  
- transformers  
- scikit-learn  
- wordcloud

## 📄 Licenza

This project is released under the Apache 2.0 license.
The original tweet data is not redistributed due to licensing restrictions.

---

## 👤 Author

Salvatore Zizzi — Statistics graduate, passionate about NLP and AI. 
📫 [LinkedIn](https://www.linkedin.com/in/salvatore-zizzi-242151107/)

