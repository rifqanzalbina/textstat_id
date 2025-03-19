import re

def ekstrak_hashtag(teks : str) -> list:
    """
        Mengekstrak kata yang diawali tanda pagar (#) dari teks.

        Args :
            teks (str) : Teks yang akan diekstrak hashtag-nya.

        Returns : 
            list : Daftar hashtag yang ditemukan dalam teks.
    """
    pattern = r'#\w+'
    hashtags = re.findall(pattern, teks)
    return hashtags

