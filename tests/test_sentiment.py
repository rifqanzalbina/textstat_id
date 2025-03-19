import pytest
from textstat_id.sentiment import SentimentAnalyzer

def test_positif():
    analyzer = SentimentAnalyzer()
    hasil = analyzer.analisis("Saya merasa sangat senang dan luar biasa")
    assert hasil["sentimen"] == "positif"
    assert hasil["skor_sentimen"] > 0

def test_negatif():
    analyzer = SentimentAnalyzer()
    hasil = analyzer.analisis("Saya kecewa dan marah dengan pelayanan ini")
    assert hasil["sentimen"] == "negatif"
    assert hasil["skor_sentimen"] < 0

def test_netral():
    analyzer = SentimentAnalyzer()
    hasil = analyzer.analisis("Hari ini biasa saja")
    assert hasil["sentimen"] == "netral"
    assert hasil["skor_sentimen"] == 0

def test_pembalik():
    analyzer = SentimentAnalyzer()
    # "tidak bagus" harus terdeteksi sebagai negatif
    hasil = analyzer.analisis("Ini tidak bagus")
    assert hasil["sentimen"] == "negatif"

def test_penguat_positif():
    analyzer = SentimentAnalyzer()
    # "sangat hebat" seharusnya menambah skor positif
    hasil = analyzer.analisis("Tim bermain sangat hebat")
    assert hasil["sentimen"] == "positif"
    # Pastikan skor di atas threshold tertentu
    assert hasil["skor_sentimen"] > 0.5

def test_multiple_sentences():
    analyzer = SentimentAnalyzer()
    teks = "Saya suka sekali makanan ini. Tapi teman saya merasa kecewa."
    hasil = analyzer.analisis(teks)
    # Memastikan overall sentimen netral atau mendekati
    assert "positif" in hasil["kata_positif"] or "kecewa" in hasil["kata_negatif"]
    # Skor kemungkinan kecil atau netral
    assert -0.5 < hasil["skor_sentimen"] < 0.5