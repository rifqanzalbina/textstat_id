import unittest
from textstat_id.url_exctract import ekstrak_url, analisis_url

class TestUrlExtractor(unittest.TestCase):

    def test_ekstrak_url_empty_text(self):
        """Menguji ekstrak_url dengan teks kosong."""
        result = ekstrak_url("")
        self.assertEqual(result, [], "Seharusnya mengembalikan list kosong untuk teks kosong")

    def test_ekstrak_url_single_url(self):
        """Menguji ekstrak_url dengan satu URL sederhana."""
        teks = "Cek website ini: www.example.com"
        result = ekstrak_url(teks)
        self.assertEqual(len(result), 1, "Seharusnya menemukan 1 URL")
        self.assertIn("www.example.com", result, "URL 'www.example.com' harusnya terdeteksi")

    def test_ekstrak_url_multiple_urls(self):
        """Menguji ekstrak_url dengan banyak URL."""
        teks = "Kunjungi https://example.com atau http://testsite.org untuk info, serta www.testid.co.id sekalian."
        result = ekstrak_url(teks)
        self.assertEqual(len(result), 3, "Seharusnya menemukan 3 URL dalam teks")

    def test_analisis_url_basic(self):
        """Menguji analisis_url untuk menghitung domain dan daftar URL."""
        teks = "Lihat www.example.com info, lalu buka https://www.example.com/about, dan cek http://test.org"
        analysis = analisis_url(teks)

        # Cek apakah key 'daftar_url' benar
        self.assertIn('daftar_url', analysis, "dictionary hasil harus punya key 'daftar_url'")
        self.assertTrue(len(analysis['daftar_url']) >= 2, "Minimal harus ada beberapa URL terdeteksi")

        # Cek apakah domain_frekuensi terdeteksi
        self.assertIn('domain_frekuensi', analysis, "dictionary hasil harus punya key 'domain_frekuensi'")
        self.assertGreaterEqual(len(analysis['domain_frekuensi']), 1, "Harus terdeteksi minimal satu domain")

        # Cek apakah jumlah_url sudah muncul
        self.assertIn('jumlah_url', analysis, "dictionary hasil harus punya key 'jumlah_url'")

if __name__ == "__main__":
    unittest.main()