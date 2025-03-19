"""
texstat_id - Library untuk analisis statistik teks Bahasa Indonesia
"""

# Import fungsi-fungsi langsung ke namespace package
from .analyzer import analisis_dasar, deteksi_kata_tidak_baku, ekstrak_kata_kunci
from .counter import hitung_frekuensi, hitung_statistik
from .readability import hitung_keterbacaan
from .sentiment import analisis_sentimen, SentimentAnalyzer
from .url_exctract import ekstrak_url, analisis_url

__version__ = '0.1.1'
__all__ = [
    'analisis_dasar',
    'deteksi_kata_tidak_baku',
    'ekstrak_kata_kunci',
    'hitung_frekuensi',
    'hitung_statistik',
    'hitung_keterbacaan', 
    'analisis_sentimen',
    'SentimentAnalyzer',
    'ekstrak_url',
    'analisis_url',
]