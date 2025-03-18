
## Langkah 4: Implementasi Kode Library

### 1. File `__init__.py`

"""
textstat_id - Library untuk analisis statistik teks Bahasa Indonesia
"""

from .analyzer import analisis_dasar, deteksi_kata_tidak_baku, ekstrak_kata_kunci
from .counter import hitung_frekuensi, hitung_statistik
from .readability import hitung_keterbacaan

__version__ = '0.1.0'
__all__ = [
    'analisis_dasar',
    'deteksi_kata_tidak_baku',
    'ekstrak_kata_kunci',
    'hitung_frekuensi',
    'hitung_statistik',
    'hitung_keterbacaan',
]