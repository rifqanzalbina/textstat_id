"""
Modul untuk ektraksi URL dari teks
"""

import re
from typing import List, Dict, Union
from .utils import bersihkan_teks

def ekstrak_url(teks: str) -> List[str]:
    """
    Mengekstrak URL dari teks
    
    Args:
        teks (str): Teks yang akan diekstrak URL-nya
        
    Returns:
        list: Daftar URL yang ditemukan dalam teks
    """
    if not teks:
        return []
    
    # Pattern untuk mendeteksi URL dengan berbagai format
    pattern = r'(https?://[^\s]+|www\.[^\s]+\.[^\s]+)'
    
    # Temukan semua URL dalam teks
    urls = re.findall(pattern, teks)
    
    # Bersihkan URL dari tanda baca yang mungkin terbawa di akhir
    cleaned_urls = []
    for url in urls:
        # Hapus tanda baca di akhir URL jika ada
        url = re.sub(r'[.,;:!?)]$', '', url)
        cleaned_urls.append(url)
    
    return cleaned_urls

def analisis_url(teks : str) -> Dict[str, Union[int, List]]:
    """
        Menganalisis URL dalam teks

        Args : 
            teks (str) : Teks yang akan dianalisis URL-nya

        Returns :
            dict : Hasil analisis URL yang berisi jumlah URL dan daftar URRL
    """
    urls = ekstrak_url(teks)

    # Kategorikan URL berdasarkan domain
    domains = {}
    for url in urls:
        # Ekstrak domain dari URL
        domain_match = re.search(r'https?://(?:www\.)?([^/]+)', url)
        if domain_match:
            domain = domain_match.group(1)
            if domain in domains:
                domains[domain] += 1
            else:
                domains[domain] = 1

    return {
        "jumlah_url" : len(url),
        "daftar_url" : urls,
        "domain_frekuensi" : domains
    }
    
