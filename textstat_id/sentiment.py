"""
Modul untuk analisis sentimen teks Bahasa Indonesia
"""

import re
from collections import defaultdict

def analisis_sentimen(teks):
    """
    Menganalisis sentimen teks Bahasa Indonesia
    
    Args:
        teks (str): Teks yang akan dianalisis
        
    Returns:
        dict: Hasil analisis sentimen
    """
    # Kata-kata positif dalam Bahasa Indonesia
    kata_positif = {
        'baik', 'bagus', 'hebat', 'luar biasa', 'senang', 'gembira', 'suka',
        'cinta', 'indah', 'cantik', 'tampan', 'pintar', 'cerdas', 'berhasil',
        'sukses', 'menang', 'beruntung', 'sempurna', 'menyenangkan', 'ramah',
        'bersahabat', 'membantu', 'membanggakan', 'memuaskan', 'menarik'
    }
    
    # Kata-kata negatif dalam Bahasa Indonesia
    kata_negatif = {
        'buruk', 'jelek', 'gagal', 'sedih', 'kecewa', 'marah', 'benci',
        'kesal', 'jengkel', 'takut', 'khawatir', 'cemas', 'menyesal',
        'menyedihkan', 'mengerikan', 'menakutkan', 'menjijikkan', 'membosankan',
        'melelahkan', 'menyebalkan', 'mengecewakan', 'menyakitkan'
    }
    
    # Kata-kata penguat
    penguat_positif = {
        'sangat', 'amat', 'sekali', 'sungguh', 'benar-benar', 'luar biasa'
    }
    
    penguat_negatif = {
        'sangat', 'amat', 'sekali', 'sungguh', 'benar-benar', 'sama sekali'
    }
    
    # Kata-kata pembalik
    pembalik = {
        'tidak', 'bukan', 'tak', 'tanpa', 'jangan'
    }
    
    # Bersihkan teks
    teks = teks.lower()
    
    # Tokenisasi kalimat
    kalimat_list = re.split(r'[.!?]+', teks)
    kalimat_list = [k.strip() for k in kalimat_list if k.strip()]
    
    # Inisialisasi hasil
    hasil = {
        'skor_sentimen': 0,
        'sentimen': 'netral',
        'detail_kalimat': [],
        'kata_positif': [],
        'kata_negatif': []
    }
    
    total_skor = 0
    
    for kalimat in kalimat_list:
        skor_kalimat = _analisis_kalimat(kalimat, kata_positif, kata_negatif, penguat_positif, penguat_negatif, pembalik)
        total_skor += skor_kalimat['skor']
        
        hasil['detail_kalimat'].append({
            'kalimat': kalimat,
            'skor': skor_kalimat['skor'],
            'sentimen': skor_kalimat['sentimen']
        })
        
        hasil['kata_positif'].extend(skor_kalimat['kata_positif'])
        hasil['kata_negatif'].extend(skor_kalimat['kata_negatif'])
    
    # Hitung skor rata-rata
    if kalimat_list:
        hasil['skor_sentimen'] = round(total_skor / len(kalimat_list), 2)
    
    # Tentukan sentimen keseluruhan
    if hasil['skor_sentimen'] > 0.1:
        hasil['sentimen'] = 'positif'
    elif hasil['skor_sentimen'] < -0.1:
        hasil['sentimen'] = 'negatif'
    else:
        hasil['sentimen'] = 'netral'
    
    # Hapus duplikat
    hasil['kata_positif'] = list(set(hasil['kata_positif']))
    hasil['kata_negatif'] = list(set(hasil['kata_negatif']))
    
    return hasil

def _analisis_kalimat(kalimat, kata_positif, kata_negatif, penguat_positif, penguat_negatif, pembalik):
    """
    Menganalisis sentimen satu kalimat
    
    Args:
        kalimat (str): Kalimat yang akan dianalisis
        kata_positif (set): Set kata-kata positif
        kata_negatif (set): Set kata-kata negatif
        penguat_positif (set): Set kata-kata penguat positif
        penguat_negatif (set): Set kata-kata penguat negatif
        pembalik (set): Set kata-kata pembalik
        
    Returns:
        dict: Hasil analisis sentimen kalimat
    """
    kata_kata = kalimat.split()
    skor = 0
    kata_positif_terdeteksi = []
    kata_negatif_terdeteksi = []
    
    # Deteksi pembalik, penguat, dan kata sentimen
    i = 0
    while i < len(kata_kata):
        kata = kata_kata[i]
        
        # Cek apakah ada frasa (2-3 kata) yang cocok dengan daftar
        frasa_2 = ' '.join(kata_kata[i:i+2]) if i+1 < len(kata_kata) else ''
        frasa_3 = ' '.join(kata_kata[i:i+3]) if i+2 < len(kata_kata) else ''
        
        # Cek frasa dalam daftar kata positif/negatif
        if frasa_3 in kata_positif:
            skor += 1
            kata_positif_terdeteksi.append(frasa_3)
            i += 3
            continue
        elif frasa_3 in kata_negatif:
            skor -= 1
            kata_negatif_terdeteksi.append(frasa_3)
            i += 3
            continue
        elif frasa_2 in kata_positif:
            skor += 1
            kata_positif_terdeteksi.append(frasa_2)
            i += 2
            continue
        elif frasa_2 in kata_negatif:
            skor -= 1
            kata_negatif_terdeteksi.append(frasa_2)
            i += 2
            continue
        
        # Cek kata tunggal
        if kata in kata_positif:
            # Cek apakah ada pembalik sebelumnya
            if i > 0 and kata_kata[i-1] in pembalik:
                skor -= 1
                kata_negatif_terdeteksi.append(f"{kata_kata[i-1]} {kata}")
            else:
                # Cek apakah ada penguat sebelumnya
                if i > 0 and kata_kata[i-1] in penguat_positif:
                    skor += 2
                    kata_positif_terdeteksi.append(f"{kata_kata[i-1]} {kata}")
                else:
                    skor += 1
                    kata_positif_terdeteksi.append(kata)
        
        elif kata in kata_negatif:
            # Cek apakah ada pembalik sebelumnya
            if i > 0 and kata_kata[i-1] in pembalik:
                skor += 1
                kata_positif_terdeteksi.append(f"{kata_kata[i-1]} {kata}")
            else:
                # Cek apakah ada penguat sebelumnya
                if i > 0 and kata_kata[i-1] in penguat_negatif:
                    skor -= 2
                    kata_negatif_terdeteksi.append(f"{kata_kata[i-1]} {kata}")
                else:
                    skor -= 1
                    kata_negatif_terdeteksi.append(kata)
        
        i += 1
    
    # Normalisasi skor antara -1 dan 1
    if kata_kata:
        skor = max(-1, min(1, skor / (len(kata_kata) / 2)))
    
    # Tentukan sentimen
    sentimen = 'netral'
    if skor > 0.1:
        sentimen = 'positif'
    elif skor < -0.1:
        sentimen = 'negatif'
    
    return {
        'skor': skor,
        'sentimen': sentimen,
        'kata_positif': kata_positif_terdeteksi,
        'kata_negatif': kata_negatif_terdeteksi
    }

# Kelas SentimentAnalyzer untuk kompatibilitas dengan kode yang sudah ada
class SentimentAnalyzer:
    def __init__(self):
        pass
    
    def analisis(self, teks):
        return analisis_sentimen(teks)