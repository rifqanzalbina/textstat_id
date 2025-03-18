import unittest
from textstat_id.analyzer import analisis_dasar, deteksi_kata_tidak_baku, ekstrak_kata_kunci

class TestAnalyzer(unittest.TestCase):
    
    def test_analisis_dasar(self):
        teks = "Saya sedang belajar membuat library Python untuk analisis teks Bahasa Indonesia."
        hasil = analisis_dasar(teks)
        
        self.assertIn("statistik", hasil)
        self.assertIn("kata_frekuensi_tertinggi", hasil)
        self.assertIn("kata_tidak_baku", hasil)
        
        self.assertEqual(hasil["statistik"]["jumlah_kata"], 11)
        self.assertEqual(hasil["statistik"]["jumlah_kalimat"], 1)
    
    def test_deteksi_kata_tidak_baku(self):
        teks = "Gue udah gak mau pake bahasa yang gitu lagi."
        hasil = deteksi_kata_tidak_baku(teks)
        
        self.assertIn("gue", hasil)  # Ubah dari "Gue" menjadi "gue"
        self.assertIn("udah", hasil)
        self.assertIn("gak", hasil)
        self.assertIn("pake", hasil)
        self.assertIn("gitu", hasil)
        
        self.assertEqual(hasil["gue"], "saya")
        self.assertEqual(hasil["udah"], "sudah")
        self.assertEqual(hasil["gak"], "tidak")
    
    def test_ekstrak_kata_kunci(self):
        teks = "Python adalah bahasa pemrograman yang populer. Python sering digunakan untuk data science dan machine learning. Python juga mudah dipelajari."
        hasil = ekstrak_kata_kunci(teks, jumlah=3)
        
        self.assertIn("python", hasil)  # Ubah dari "Python" menjadi "python"
        self.assertEqual(len(hasil), 3)

if __name__ == '__main__':
    unittest.main()