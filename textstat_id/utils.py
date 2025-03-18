"""
Modul utilitas untuk texstat_id
"""

import re

def bersihkan_teks(teks):
    if teks is None:
        return ""
    teks = teks.lower()
    teks = re.sub(r'[^\w\s.,!?;:-]', '', teks)
    return teks

def tokenisasi_kata(teks):
    """
    Memecah teks menjadi token kata
    
    Args:
        teks (str): Teks yang akan ditokenisasi
        
    Returns:
        list: Daftar token kata
    """
    # Hapus tanda baca
    teks = re.sub(r'[^\w\s]', '', teks)
    
    # Tokenisasi berdasarkan spasi
    kata_kata = teks.split()
    
    return kata_kata

def deteksi_bahasa(teks):
    """
    Mendeteksi apakah teks kemungkinan besar berbahasa Indonesia
    
    Args:
        teks (str): Teks yang akan dideteksi bahasanya
        
    Returns:
        bool: True jika kemungkinan besar berbahasa Indonesia
    """
    # Kata-kata umum dalam Bahasa Indonesia
    kata_umum_id = {
        'yang', 'dan', 'di', 'ke', 'dari', 'untuk', 'dengan', 'adalah', 'ini', 'itu',
        'pada', 'tidak', 'akan', 'saya', 'kamu', 'anda', 'mereka', 'kami', 'kita'
    }
    
    # Bersihkan dan tokenisasi teks
    teks_bersih = bersihkan_teks(teks)
    kata_kata = tokenisasi_kata(teks_bersih)
    
    # Hitung kata umum Bahasa Indonesia
    kata_id = sum(1 for kata in kata_kata if kata.lower() in kata_umum_id)
    
    # Jika lebih dari 10% kata adalah kata umum Bahasa Indonesia, kemungkinan besar berbahasa Indonesia
    if len(kata_kata) > 0 and (kata_id / len(kata_kata)) > 0.1:
        return True
    
    return False