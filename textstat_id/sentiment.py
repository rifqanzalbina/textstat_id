import os
import re
import json
from collections import defaultdict

# ! load data kata positif
def _load_kata_positif():
    """
    Memuat daftar kata positif dari file JSON 
    """
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'kata_positif.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data.get("kata_positif", []))
    except FileNotFoundError:
        return set()

# ! load data kata negatif
def _load_kata_negatif():
    """
    Memuat daftar kata negatif dari file JSON 
    """
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'kata_negatif.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data.get("kata_negatif", []))
    except FileNotFoundError:
        return set()
    
# ! load data kata penguat positiff
def _load_kata_penguat_positif():
    """
        Memuat daftar kata negatif dari file JSON
    """
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'kata_penguat_positif.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data.get("kata_penguat_positiff", []))
    except FileNotFoundError:
        return set()

# ! load data kata penguat negatif
def _load_kata_penguat_negatif():
    """
        Memuat daftar kata negatif dari file JSON
    """
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'kata_penguat_negatif.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data.get("kata_penguat_negatif", []))
    except FileNotFoundError:
        return set()

# Global sets (berasal dari file JSON)
KATA_POSITIF = _load_kata_positif()
KATA_NEGATIF = _load_kata_negatif()
KATA_PENGUAT_POSITIF = _load_kata_penguat_positif()
KATA_PENGUAT_NEGATIF = _load_kata_penguat_negatif()

def analisis_sentimen(teks):
    """
    Menganalisis sentimen teks Bahasa Indonesia
    
    Args:
        teks (str): Teks yang akan dianalisis
        
    Returns:
        dict: Hasil analisis sentimen
    """
    # Kata positif
    kata_positif = KATA_POSITIF

    # Kata negatif
    kata_negatif = KATA_NEGATIF
    
    # Kata-kata penguat
    penguat_positif = KATA_PENGUAT_POSITIF

    penguat_negatif = KATA_PENGUAT_NEGATIF
    
    # Kata-kata pembalik
    pembalik = {
        'tidak', 'bukan', 'tak', 'tanpa', 'jangan'
    }
    
    # Bersihkan teks
    teks = teks.lower()
    
    # Tokenisasi kalimat (pisah berdasarkan titik, tanda seru, atau tanya)
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
        skor_kalimat = _analisis_kalimat(kalimat, kata_positif, kata_negatif,
                                         penguat_positif, penguat_negatif, pembalik)
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
    """
    kata_kata = kalimat.split()
    skor = 0
    kata_positif_terdeteksi = []
    kata_negatif_terdeteksi = []
    
    i = 0
    while i < len(kata_kata):
        kata = kata_kata[i]
        
        # Cek frasa 2-3 kata (opsional)
        frasa_2 = ' '.join(kata_kata[i:i+2]) if i+1 < len(kata_kata) else ''
        frasa_3 = ' '.join(kata_kata[i:i+3]) if i+2 < len(kata_kata) else ''
        
        # Cek frasa positif
        if frasa_3 in kata_positif:
            skor += 1
            kata_positif_terdeteksi.append(frasa_3)
            i += 3
            continue
        elif frasa_2 in kata_positif:
            skor += 1
            kata_positif_terdeteksi.append(frasa_2)
            i += 2
            continue
        
        # Cek frasa negatif
        if frasa_3 in kata_negatif:
            skor -= 1
            kata_negatif_terdeteksi.append(frasa_3)
            i += 3
            continue
        elif frasa_2 in kata_negatif:
            skor -= 1
            kata_negatif_terdeteksi.append(frasa_2)
            i += 2
            continue
        
        # Cek kata positif
        if kata in kata_positif:
            # Jika ada pembalik sebelumnya
            if i > 0 and kata_kata[i-1] in pembalik:
                skor -= 1
                kata_negatif_terdeteksi.append(f"{kata_kata[i-1]} {kata}")
            else:
                # Jika ada penguat sebelumnya
                if i > 0 and kata_kata[i-1] in penguat_positif:
                    skor += 2
                    kata_positif_terdeteksi.append(f"{kata_kata[i-1]} {kata}")
                else:
                    skor += 1
                    kata_positif_terdeteksi.append(kata)
        
        # Cek kata negatif
        elif kata in kata_negatif:
            # Jika ada pembalik sebelumnya
            if i > 0 and kata_kata[i-1] in pembalik:
                skor += 1
                kata_positif_terdeteksi.append(f"{kata_kata[i-1]} {kata}")
            else:
                # Jika ada penguat negatif sebelumnya
                if i > 0 and kata_kata[i-1] in penguat_negatif:
                    skor -= 2
                    kata_negatif_terdeteksi.append(f"{kata_kata[i-1]} {kata}")
                else:
                    skor -= 1
                    kata_negatif_terdeteksi.append(kata)
        
        i += 1
    
    # Normalisasi skor antara -1 dan 1
    if kata_kata:
        # Bagi dengan (len(kata_kata) / 2) agar kalimat panjang tidak
        # terlalu besar skornya
        normal_score = skor / (len(kata_kata) / 2)
        skor = max(-1, min(1, normal_score))
    
    # Tentukan sentimen kalimat
    if skor > 0.1:
        sentimen = 'positif'
    elif skor < -0.1:
        sentimen = 'negatif'
    else:
        sentimen = 'netral'
    
    return {
        'skor': skor,
        'sentimen': sentimen,
        'kata_positif': kata_positif_terdeteksi,
        'kata_negatif': kata_negatif_terdeteksi
    }

class SentimentAnalyzer:
    def __init__(self):
        pass
    
    def analisis(self, teks):
        """
        Mempertahankan kompatibilitas API lama.
        """
        return analisis_sentimen(teks)