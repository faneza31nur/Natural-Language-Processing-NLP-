from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

app = Flask(__name__)
CORS(app)

# Load model
svm = joblib.load('svm_sentiment.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

# Sastrawi
stemmer = StemmerFactory().create_stemmer()
stopword = StopWordRemoverFactory().create_stop_word_remover()


def preprocess(text):
    if not isinstance(text, str):
        return ''

    text = text.lower()

    # Hapus URL
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # Hapus mention dan hashtag
    text = re.sub(r'@\w+|#\w+', '', text)

    # Hapus angka
    text = re.sub(r'\d+', '', text)

    # Hapus tanda baca
    text = re.sub(r'[^\w\s]', '', text)

    # Rapikan spasi
    text = re.sub(r'\s+', ' ', text).strip()

    # Stopword
    text = stopword.remove(text)

    # Stemming
    text = stemmer.stem(text)

    return text


@app.route('/predict', methods=['POST'])
def predict():

    try:
        data = request.get_json(force=True)

        teks = data.get('teks', '').strip()

        if not teks:
            return jsonify({
                'status': 'error',
                'message': 'Teks tidak boleh kosong'
            }), 400

        clean = preprocess(teks)

        vector = tfidf.transform([clean])

        label = svm.predict(vector)[0]

        return jsonify({
            'status': 'success',
            'teks': teks,
            'teks_processed': clean,
            'sentimen': str(label)
        })

    except Exception as e:

        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
