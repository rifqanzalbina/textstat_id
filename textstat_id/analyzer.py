"""
Modul untuk analisis teks Bahasa Indonesia
"""

import json
import os
import re
from collections import Counter

from .counter import hitung_statistik, hitung_frekuensi
from .utils import bersihkan_teks, tokenisasi_kata

# Load kata baku data
def _load_kata_baku():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'kata_baku.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Fallback to a small default dictionary if file not found
        return {
            "gak": "tidak",
            "nggak": "tidak",
            "gua": "saya",
            "gue": "saya",
            "udah": "sudah",
            "aja": "saja",
            "doang": "saja",
            "gitu": "begitu",
            "gini": "begini",
            "gimana": "bagaimana",
            "kayak": "seperti",
            "kaya": "seperti",
            "banget": "sangat"
        }

# Dictionary kata baku
KATA_BAKU = _load_kata_baku()

def analisis_dasar(teks):
    """
    Melakukan analisis dasar pada teks Bahasa Indonesia
    
    Args:
        teks (str): Teks yang akan dianalisis
        
    Returns:
        dict: Hasil analisis dasar
    """
    if not teks:
        return {
            "status": "error",
            "message": "Teks tidak boleh kosong"
        }
    
    # Hitung statistik dasar
    statistik = hitung_statistik(teks)
    
    # Hitung frekuensi kata (top 10)
    frekuensi = hitung_frekuensi(teks)
    top_kata = dict(sorted(frekuensi.items(), key=lambda x: x[1], reverse=True)[:10])
    
    # Deteksi kata tidak baku
    kata_tidak_baku = deteksi_kata_tidak_baku(teks)
    
    return {
        "statistik": statistik,
        "kata_frekuensi_tertinggi": top_kata,
        "kata_tidak_baku": kata_tidak_baku
    }

def deteksi_kata_tidak_baku(teks):
    """
    Mendeteksi kata tidak baku dalam teks
    
    Args:
        teks (str): Teks yang akan dianalisis
        
    Returns:
        dict: Kata tidak baku dan sarannya
    """
    kata_tidak_baku = {}
    teks_bersih = bersihkan_teks(teks)
    kata_kata = tokenisasi_kata(teks_bersih)
    
    for kata in kata_kata:
        kata_lower = kata.lower()
        if kata_lower in KATA_BAKU:
            kata_tidak_baku[kata] = KATA_BAKU[kata_lower]  # Gunakan kata asli sebagai key
    
    return kata_tidak_baku

def ekstrak_kata_kunci(teks, jumlah=5):
    """
    Mengekstrak kata kunci dari teks
    
    Args:
        teks (str): Teks yang akan dianalisis
        jumlah (int): Jumlah kata kunci yang akan diambil
        
    Returns:
        list: Daftar kata kunci
    """
    teks_bersih = bersihkan_teks(teks)
    kata_kata_original = tokenisasi_kata(teks_bersih)
    
    # Buat versi lowercase untuk perbandingan
    kata_kata_lower = [kata.lower() for kata in kata_kata_original]
    
    # Filter kata-kata umum (stopwords sederhana)
    stopwords = {"yang", "dan", "di", "dengan", "untuk", "pada", "adalah", "ini", "itu", "atau", "juga"}
    
    # Buat dictionary untuk memetakan kata lowercase ke kata asli
    kata_map = {}
    for i, kata in enumerate(kata_kata_lower):
        if kata not in stopwords and len(kata) > 2:
            kata_map[kata] = kata_kata_original[i]
    
    # Hitung frekuensi
    frekuensi = Counter(kata_kata_lower)
    
    # Filter stopwords dari frekuensi
    for stopword in stopwords:
        if stopword in frekuensi:
            del frekuensi[stopword]
    
    # Filter kata pendek
    for kata in list(frekuensi.keys()):
        if len(kata) <= 2:
            del frekuensi[kata]
    
    # Ambil kata kunci berdasarkan frekuensi tertinggi
    kata_kunci_lower = [kata for kata, _ in frekuensi.most_common(jumlah)]
    
    # Konversi kembali ke kata asli
    kata_kunci = [kata_map.get(kata, kata) for kata in kata_kunci_lower]
    
    return kata_kunci