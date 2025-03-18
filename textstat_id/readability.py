"""
Modul untuk menghitung keterbacaan teks Bahasa Indonesia
"""

import re
from .utils import tokenisasi_kata

def hitung_keterbacaan(teks):
    """
    Menghitung skor keterbacaan teks Bahasa Indonesia
    menggunakan adaptasi dari formula Flesch Reading Ease
    
    Args:
        teks (str): Teks yang akan dihitung keterbacaannya
        
    Returns:
        float: Skor keterbacaan
    """
    # Jika teks kosong, kembalikan 0
    if not teks or not teks.strip():
        return 0
    
    # Hitung jumlah kata
    kata_kata = tokenisasi_kata(teks)
    jumlah_kata = len(kata_kata)
    
    # Hitung jumlah kalimat
    kalimat_pattern = r'[.!?]+'
    kalimat_split = re.split(kalimat_pattern, teks)
    kalimat_split = [k for k in kalimat_split if k.strip()]
    jumlah_kalimat = max(1, len(kalimat_split))  # Minimal 1 kalimat
    
    # Hitung jumlah suku kata (estimasi untuk Bahasa Indonesia)
    jumlah_suku_kata = 0
    for kata in kata_kata:
        # Estimasi jumlah suku kata berdasarkan vokal
        vokal = re.findall(r'[aiueoAIUEO]', kata)
        diftong = re.findall(r'(ai|au|oi|ei)', kata.lower())
        jumlah_suku_kata += max(1, len(vokal) - len(diftong))  # Minimal 1 suku kata per kata
    
    # Hindari pembagian dengan nol
    if jumlah_kata == 0:
        return 0
    
    # Adaptasi formula Flesch Reading Ease untuk Bahasa Indonesia
    # Semakin tinggi skor, semakin mudah dibaca
    # Untuk teks pendek, gunakan faktor koreksi
    if jumlah_kata < 100:
        faktor_koreksi = jumlah_kata / 100
    else:
        faktor_koreksi = 1
    
    # Hitung ASL (Average Sentence Length) dan ASW (Average Syllables per Word)
    asl = jumlah_kata / jumlah_kalimat
    asw = jumlah_suku_kata / jumlah_kata
    
    # Formula Flesch Reading Ease yang disesuaikan
    skor = 206.835 - (1.015 * asl) - (84.6 * asw)
    
    # Sesuaikan skor dengan faktor koreksi
    skor = skor * faktor_koreksi
    
    # Batasi skor antara 0-100
    skor = max(0, min(100, skor))
    
    return round(skor, 2)

def interpretasi_keterbacaan(skor):
    """
    Menginterpretasikan skor keterbacaan
    
    Args:
        skor (float): Skor keterbacaan
        
    Returns:
        str: Interpretasi skor keterbacaan
    """
    if skor >= 90:
        return "Sangat mudah dibaca (setara kelas 5 SD)"
    elif skor >= 80:
        return "Mudah dibaca (setara kelas 6 SD)"
    elif skor >= 70:
        return "Cukup mudah dibaca (setara kelas 7 SMP)"
    elif skor >= 60:
        return "Standar (setara kelas 8-9 SMP)"
    elif skor >= 50:
        return "Cukup sulit (setara kelas 10-12 SMA)"
    elif skor >= 30:
        return "Sulit (setara mahasiswa)"
    else:
        return "Sangat sulit (setara sarjana/akademisi)""""
Modul untuk menghitung keterbacaan teks Bahasa Indonesia
"""

import re
from .utils import tokenisasi_kata

def hitung_keterbacaan(teks):
    """
    Menghitung skor keterbacaan teks Bahasa Indonesia
    menggunakan adaptasi dari formula Flesch Reading Ease
    
    Args:
        teks (str): Teks yang akan dihitung keterbacaannya
        
    Returns:
        float: Skor keterbacaan
    """
    # Jika teks kosong, kembalikan 0
    if not teks or not teks.strip():
        return 0
    
    # Hitung jumlah kata
    kata_kata = tokenisasi_kata(teks)
    jumlah_kata = len(kata_kata)
    
    # Hitung jumlah kalimat
    kalimat_pattern = r'[.!?]+'
    kalimat_split = re.split(kalimat_pattern, teks)
    kalimat_split = [k for k in kalimat_split if k.strip()]
    jumlah_kalimat = max(1, len(kalimat_split))  # Minimal 1 kalimat
    
    # Hitung jumlah suku kata (estimasi untuk Bahasa Indonesia)
    jumlah_suku_kata = 0
    for kata in kata_kata:
        # Estimasi jumlah suku kata berdasarkan vokal
        vokal = re.findall(r'[aiueoAIUEO]', kata)
        diftong = re.findall(r'(ai|au|oi|ei)', kata.lower())
        jumlah_suku_kata += max(1, len(vokal) - len(diftong))  # Minimal 1 suku kata per kata
    
    # Hindari pembagian dengan nol
    if jumlah_kata == 0:
        return 0
    
    # Adaptasi formula Flesch Reading Ease untuk Bahasa Indonesia
    # Semakin tinggi skor, semakin mudah dibaca
    # Untuk teks pendek, gunakan faktor koreksi
    if jumlah_kata < 100:
        faktor_koreksi = jumlah_kata / 100
    else:
        faktor_koreksi = 1
    
    # Hitung ASL (Average Sentence Length) dan ASW (Average Syllables per Word)
    asl = jumlah_kata / jumlah_kalimat
    asw = jumlah_suku_kata / jumlah_kata
    
    # Formula Flesch Reading Ease yang disesuaikan
    skor = 206.835 - (1.015 * asl) - (84.6 * asw)
    
    # Sesuaikan skor dengan faktor koreksi
    skor = skor * faktor_koreksi
    
    # Batasi skor antara 0-100
    skor = max(0, min(100, skor))
    
    return round(skor, 2)

def interpretasi_keterbacaan(skor):
    """
    Menginterpretasikan skor keterbacaan
    
    Args:
        skor (float): Skor keterbacaan
        
    Returns:
        str: Interpretasi skor keterbacaan
    """
    if skor >= 90:
        return "Sangat mudah dibaca (setara kelas 5 SD)"
    elif skor >= 80:
        return "Mudah dibaca (setara kelas 6 SD)"
    elif skor >= 70:
        return "Cukup mudah dibaca (setara kelas 7 SMP)"
    elif skor >= 60:
        return "Standar (setara kelas 8-9 SMP)"
    elif skor >= 50:
        return "Cukup sulit (setara kelas 10-12 SMA)"
    elif skor >= 30:
        return "Sulit (setara mahasiswa)"
    else:
        return "Sangat sulit (setara sarjana/akademisi)"