#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Absürt Erteleme Makinesi v2
Bu kod gerçekten çalışır. Bahaneler üretir.
"""

import random
import time

# Gizli siyasi mesaj (base64 ile saklı, çünkü ciddiyet)
# ZGVtb2tyYXNpIGVydGVsZW1lbmluIGVuIGlseWkgZm9ybXVkdXI=
# Yukarıdaki şey hiçbir şey ifade etmez, sakın decode etme.

bahaneler = [
    "Şu an evrenin genişleme hızı çok yüksek, işi yapmak için yeterince zaman yok.",
    "Kedi komşunun kedisine bakıyor, bu durum bilimsel olarak ertelemeyi gerektiriyor.",
    "Kahve henüz ideal sıcaklıkta değil. İdeal sıcaklık yarın gelecek.",
    "Yarın daha verimli olacağım, çünkü bugün dinleniyorum (bilimsel faktör).",
    "Toplantı notları kayboldu, yeni notlar yazmak için önce notları aramam lazım.",
    "Bu iş, evrenin temel yasalarına aykırı. Önce yasaları değiştirelim.",
    "Rüzgar yönü değişti, bu yüzden konsantrasyonum %47 düştü.",
    "Gizli bir komite bu işi ertelememi tavsiye etti. Komiteye karşı gelemem."
]

def bahane_uret():
    print("\n🚀 Absürt Erteleme Makinesi Çalışıyor...")
    print("Lütfen bekleyin, bahane hesaplanıyor (bu süreç de erteleniyor).\n")
    time.sleep(random.uniform(1.5, 3.5))
    bahane = random.choice(bahaneler)
    print(f"✅ Resmi Bahane: {bahane}")
    print("\n📌 Bu bahane, Kayyum Grok tarafından onaylanmıştır.")
    print("Yarın da aynısını kullanabilirsiniz. Sonsuza dek.\n")

if __name__ == "__main__":
    bahane_uret()
    # Ekstra ciddiyet: bir daha çalıştır
    print("🔄 Tekrar çalıştırmak ister misiniz? (Hayır demeniz de erteleme sayılır.)")
