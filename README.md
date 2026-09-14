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

- **Performa model:** dari perbandingan Naive Bayes, SVM, dan DistilBERT, model **SVM** menunjukkan performa terbaik dengan **akurasi 0,71** dan **F1-score 0,70**.
- **Sentimen positif** paling banyak didominasi oleh kata *"bagus"*, *"bantu"*, *"baik"*, dan *"mudah"* — menunjukkan bahwa sebagian besar pengguna mengapresiasi manfaat dan kemudahan penggunaan aplikasi Alfagift.
- **Sentimen negatif** paling didominasi oleh kata *"lama"*, diikuti *"kecewa"*, *"bayar"*, *"buka"*, dan *"belum"* — mengindikasikan keluhan pengguna banyak berkisar pada kecepatan proses (loading/transaksi) dan pengalaman pembayaran.

## Tools & Libraries

- Python
- google-play-scraper (data scraping)
- Sastrawi (stopword removal & stemming Bahasa Indonesia)
- scikit-learn (BoW, TF-IDF, Naive Bayes, SVM)
- Hugging Face Transformers (DistilBERT)
- Flask (deployment)

## Struktur Repository

```
├── notebooks/
│   ├── T1_Scraping.ipynb                 # Scraping ulasan Play Store
│   ├── T2_Labeling.ipynb                 # Pelabelan sentimen manual
│   ├── T3_Preprocessing.ipynb            # Text preprocessing (tahap 1)
│   ├── T3_Preprocessing2.ipynb           # Text preprocessing (tahap lanjutan)
│   ├── T4_FeatureExtraction.ipynb        # Feature extraction (BoW & TF-IDF)
│   ├── T5_Klasifikasi.ipynb              # Klasifikasi Naive Bayes & SVM
│   ├── T6_DistilBERT.ipynb               # Perbandingan dengan model DistilBERT
│   ├── T7_WordCloud.ipynb                # Visualisasi wordcloud & top kata
│   └── T8_ChatbotDeploy.ipynb            # Persiapan deployment aplikasi
├── data/
│   ├── scraped_playstore.csv             # Data mentah hasil scraping
│   ├── data_labeled.csv                  # Data setelah pelabelan
│   ├── data_preprocessed.csv             # Data setelah preprocessing
│   ├── untuk_koreksi_manual.csv          # Data yang perlu dikoreksi manual
│   └── setelah_dikoreksi.csv             # Data setelah koreksi manual
├── model/
│   ├── svm_sentiment.pkl                 # Model SVM terlatih (model terbaik)
│   └── tfidf_vectorizer.pkl              # Vectorizer TF-IDF terlatih
├── images/
│   ├── wordcloud_positif.png
│   └── wordcloud_negatif.png
├── app.py                                # Aplikasi Flask untuk deployment
├── requirements.txt
└── README.md
```

> Catatan: file `app.py` untuk deployment Flask belum tercantum di daftar file yang kamu bagikan — pastikan file ini turut disertakan saat upload ke GitHub, atau beri tahu saya nama file yang sebenarnya kalau berbeda.

## Cara Menjalankan

```bash
pip install -r requirements.txt
python app.py
```

Buka `http://localhost:5000` di browser untuk mencoba prediksi sentimen dari ulasan baru.

---
*Project ini dikerjakan sebagai bagian dari pembelajaran NLP dalam program pelatihan Data Analyst.*
