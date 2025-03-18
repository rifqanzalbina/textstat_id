# textstat id

Analisis statistik teks Bahasa Indonesia.

## Instalasi

```bash
pip install textstat_id

```

## Usage Example

```python
import textstat_id

# Analisis teks
teks = "Saya sedang belajar membuat library Python untuk analisis teks Bahasa Indonesia."
hasil = textstat_id.analisis_dasar(teks)
print(hasil)

# Menghitung frekuensi kata
frekuensi = textstat_id.hitung_frekuensi(teks)
print(frekuensi)

# Menghitung readability score
score = textstat_id.hitung_keterbacaan(teks)
print(f"Skor keterbacaan: {score}")
```

## Fitur
- Menghitung frekuensi kata dalam teks Bahasa Indonesia
- Menghitung jumlah kalimat, kata, dan karakter
- Mendeteksi kata tidak baku dalam bahasa Indonesia
- Mengekstrak kata kunci dari teks
- Menghitung readability score untuk teks Bahasa Indonesia
