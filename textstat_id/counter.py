"""
Modul untuk menghitung statistik teks Bahasa Indonesia
"""

import re
from collections import Counter

from .utils import bersihkan_teks, tokenisasi_kata

def hitung_statistik(teks):
    """
    Menghitung statistik dasar dari teks
    
    Args:
        teks (str): Teks yang akan dihitung statistiknya
        
    Returns:
        dict: Statistik teks
    """
    # Hitung jumlah karakter
    jumlah_karakter = len(teks)
    jumlah_karakter_tanpa_spasi = len(teks.replace(" ", ""))
    
    # Hitung jumlah kata
    kata_kata = tokenisasi_kata(teks)
    jumlah_kata = len(kata_kata)
    
    # Hitung jumlah kalimat
    kalimat_pattern = r'[.!?]+'
    kalimat_split = re.split(kalimat_pattern, teks)
    kalimat_split = [k for k in kalimat_split if k.strip()]
    jumlah_kalimat = len(kalimat_split)
    
    # Hitung rata-rata panjang kata
    if jumlah_kata > 0:
        rata_panjang_kata = sum(len(kata) for kata in kata_kata) / jumlah_kata
    else:
        rata_panjang_kata = 0
    
    # Hitung rata-rata kata per kalimat
    if jumlah_kalimat > 0:
        rata_kata_per_kalimat = jumlah_kata / jumlah_kalimat
    else:
        rata_kata_per_kalimat = 0
    
    return {
        "jumlah_karakter": jumlah_karakter,
        "jumlah_karakter_tanpa_spasi": jumlah_karakter_tanpa_spasi,
        "jumlah_kata": jumlah_kata,
        "jumlah_kalimat": jumlah_kalimat,
        "rata_panjang_kata": round(rata_panjang_kata, 2),
        "rata_kata_per_kalimat": round(rata_kata_per_kalimat, 2)
    }

def hitung_frekuensi(teks):
    """
    Menghitung frekuensi kata dalam teks
    
    Args:
        teks (str): Teks yang akan dihitung frekuensi katanya
        
    Returns:
        dict: Frekuensi kata
    """
    teks_bersih = bersihkan_teks(teks)
    kata_kata = tokenisasi_kata(teks_bersih)
    
    # Hitung frekuensi
    frekuensi = Counter(kata_kata)
    
    return dict(frekuensi)