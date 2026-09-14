# Analisis Sentimen Ulasan Aplikasi Alfagift (Play Store)

Project Natural Language Processing (NLP) untuk menganalisis sentimen pengguna terhadap aplikasi Alfagift, mulai dari data scraping, pemrosesan teks, klasifikasi model machine learning hingga transformer, sampai deployment aplikasi.

## Latar Belakang

Alfagift merupakan aplikasi belanja online yang memiliki banyak ulasan pengguna di Play Store. Analisis sentimen terhadap ulasan ini penting untuk memahami persepsi pengguna secara sistematis dan cepat — tanpa harus membaca ribuan ulasan satu per satu — sehingga insight-nya dapat digunakan untuk perbaikan layanan aplikasi.

## Dataset

- **Sumber:** hasil scraping ulasan aplikasi Alfagift di Google Play Store menggunakan library `google-play-scraper`
- **Jumlah data:** 5.000 ulasan pengguna

## Alur & Metodologi

1. **Data Scraping** — mengambil 5.000 data ulasan aplikasi Alfagift dari Play Store menggunakan `google-play-scraper`.
2. **Labeling** — memberi label sentimen (positif/negatif) secara manual berdasarkan kata kunci pada tiap ulasan.
3. **Text Preprocessing** — membersihkan teks ulasan melalui proses **stopword removal** dan **stemming** untuk menyederhanakan variasi kata menjadi bentuk dasarnya.
4. **Feature Extraction** — mengekstraksi fitur teks menjadi representasi numerik menggunakan dua pendekatan: **Bag of Words (BoW)** dan **TF-IDF**.
5. **Modeling & Classification** — melatih model klasifikasi sentimen menggunakan **Naive Bayes** dan **Support Vector Machine (SVM)**, kemudian menguji model untuk memprediksi sentimen dari ulasan baru yang belum pernah dilihat model.
6. **Perbandingan dengan DistilBERT** — membandingkan performa model klasik (Naive Bayes, SVM) dengan model transformer **DistilBERT** untuk melihat sejauh mana pendekatan deep learning meningkatkan akurasi klasifikasi sentimen.
7. **Visualisasi** — membuat **wordcloud** untuk sentimen positif dan negatif, serta grafik **top 10 kata** yang paling sering muncul pada masing-masing sentimen.
8. **Deployment** — men-deploy model ke dalam aplikasi web sederhana menggunakan **Flask**, dijalankan secara localhost, untuk memprediksi sentimen dari input ulasan baru secara langsung.

## Insight Utama

*(Tambahkan di sini, misalnya: model mana yang performanya paling baik — Naive Bayes, SVM, atau DistilBERT — beserta angka accuracy/F1-score-nya, dan kata-kata apa yang paling dominan muncul di ulasan positif vs negatif.)*

## Tools & Libraries

- Python
- google-play-scraper (data scraping)
- Sastrawi/NLTK (stopword removal & stemming) — *sesuaikan bila library yang dipakai berbeda*
- scikit-learn (BoW, TF-IDF, Naive Bayes, SVM)
- Hugging Face Transformers (DistilBERT)
- Flask (deployment)

## Struktur Repository

```
├── notebook/
│   └── ...                      # Notebook: scraping, preprocessing, modeling, evaluasi
├── app.py                       # Aplikasi Flask untuk deployment
├── templates/
│   └── ...                      # File HTML untuk tampilan web Flask
├── images/
│   └── ...                      # Wordcloud & grafik top kata positif/negatif
├── requirements.txt
└── README.md
```

## Cara Menjalankan

```bash
pip install -r requirements.txt
python app.py
```

Buka `http://localhost:5000` di browser untuk mencoba prediksi sentimen dari ulasan baru.

---
*Project ini dikerjakan sebagai bagian dari pembelajaran NLP dalam program pelatihan Data Analyst.*
