import unittest
from textstat_id.sentiment import analisis_sentimen, SentimentAnalyzer

class TestSentiment(unittest.TestCase):

    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_positif(self):
        hasil = self.analyzer.analisis("Saya merasa sangat bahagia hari ini")
        self.assertEqual(hasil["sentimen"], "positif")
        self.assertGreater(hasil["skor_sentimen"], 0)

    def test_negatif(self):
        hasil = self.analyzer.analisis("Saya kecewa dan marah")
        self.assertEqual(hasil["sentimen"], "negatif")
        self.assertLess(hasil["skor_sentimen"], 0)
        

    def test_netral(self):
        hasil = self.analyzer.analisis("Hari ini cukup biasa saja")
        self.assertEqual(hasil["sentimen"], "netral")
        self.assertEqual(hasil["skor_sentimen"], 0)

    def test_pembalik(self):
        # Kata "tidak bagus" seharusnya memunculkan sentimen negatif
        hasil = self.analyzer.analisis("Ini tidak bagus sama sekali")
        self.assertEqual(hasil["sentimen"], "negatif")

    def test_lima_kalimat(self):
        teks = "Saya senang. Saya kecewa. Ini hari biasa. Saya sangat bahagia. Semua berjalan lancar."
        hasil = analisis_sentimen(teks)
        # Memastikan hasil general, minimal tidak kosong
        self.assertIn("detail_kalimat", hasil)
        self.assertTrue(len(hasil["detail_kalimat"]) == 5)

if __name__ == "__main__":
    unittest.main()