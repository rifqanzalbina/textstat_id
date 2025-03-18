import unittest
from textstat_id.counter import hitung_statistik, hitung_frekuensi

class TestCounter(unittest.TestCase):
    
    def test_hitung_statistik(self):
        teks = "Saya sedang belajar Python. Ini sangat menyenangkan!"
        hasil = hitung_statistik(teks)
        
        self.assertEqual(hasil["jumlah_kata"], 7)
        self.assertEqual(hasil["jumlah_kalimat"], 2)
        self.assertGreater(hasil["jumlah_karakter"], 0)
        self.assertGreater(hasil["rata_panjang_kata"], 0)
        self.assertEqual(hasil["rata_kata_per_kalimat"], 3.5)
    
    def test_hitung_frekuensi(self):
        teks = "satu dua tiga satu dua satu"
        hasil = hitung_frekuensi(teks)
        
        self.assertEqual(hasil["satu"], 3)
        self.assertEqual(hasil["dua"], 2)
        self.assertEqual(hasil["tiga"], 1)

if __name__ == '__main__':
    unittest.main()