# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Machine Learning and NLP techniques.  
This system recommends similar movies based on user selection.

---

## 🚀 Features

- Recommend top 5 similar movies
- Based on genres, keywords, cast, and overview
- Uses cosine similarity
- Interactive UI using Streamlit

---

## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## 📊 How It Works

- Data preprocessing on movie dataset  
- Feature extraction (genres, keywords, cast, crew, overview)  
- Combine features into a single column (tags)  
- Convert text into vectors using CountVectorizer  
- Calculate similarity using cosine similarity  
- Recommend similar movies  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py


## 📥 Dataset

Datasets are not uploaded due to GitHub size limitations.

Download from Kaggle:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

After downloading:

- Create a folder named `data` in the project directory
- Place the following files inside the `data` folder:
  - tmdb_5000_movies.csv
  - tmdb_5000_credits.csv


## ⚠️ Model Files

Model files are not uploaded due to size limits.

To generate them, run:
python model_builder.py



## 📁 Project Structure
movie-recommendation-system/
│
├── app.py
├── model_builder.ipynb
├── requirements.txt
├── README.md
└── data/



## 👨‍💻 Author
Pankaj Kumar Rajak
git add .
git commit -m "added dataset instructions"
git push
