import unittest
from textstat_id.readability import hitung_keterbacaan, interpretasi_keterbacaan

class TestReadability(unittest.TestCase):
    
    def test_hitung_keterbacaan(self):
        # Teks yang sangat mudah dibaca
        teks_mudah = "Ini teks pendek. Kata-katanya juga pendek. Mudah dibaca. Semua kalimat singkat. Tidak ada kata sulit."
        
        # Teks yang lebih sulit dibaca
        teks_sulit = "Implementasi algoritma kompleks tersebut membutuhkan pemahaman mendalam mengenai struktur data abstrak dan paradigma pemrograman fungsional yang memungkinkan manipulasi data secara deklaratif dengan memanfaatkan konsep immutability dan higher-order functions."
        
        skor_mudah = hitung_keterbacaan(teks_mudah)
        skor_sulit = hitung_keterbacaan(teks_sulit)
        
        print(f"Skor teks mudah: {skor_mudah}")
        print(f"Skor teks sulit: {skor_sulit}")
        
        # Pastikan skor teks mudah lebih tinggi dari teks sulit
        self.assertGreater(skor_mudah, skor_sulit)
        
        # Pastikan skor dalam rentang yang valid
        self.assertGreaterEqual(skor_mudah, 0)
        self.assertLessEqual(skor_mudah, 100)
        self.assertGreaterEqual(skor_sulit, 0)
        self.assertLessEqual(skor_sulit, 100)
    
    def test_interpretasi_keterbacaan(self):
        interpretasi_90 = interpretasi_keterbacaan(90)
        interpretasi_70 = interpretasi_keterbacaan(70)
        interpretasi_50 = interpretasi_keterbacaan(50)
        interpretasi_20 = interpretasi_keterbacaan(20)
        
        self.assertIn("Sangat mudah", interpretasi_90)
        self.assertIn("Cukup mudah", interpretasi_70)
        self.assertIn("Cukup sulit", interpretasi_50)
        self.assertIn("Sangat sulit", interpretasi_20)

if __name__ == '__main__':
    unittest.main()