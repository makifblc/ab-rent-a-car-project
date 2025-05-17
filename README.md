# ab-rent-a-car-project
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>AB RENT A CAR - Araç Kiralama Uygulaması</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #111;
      color: #eee;
      padding: 20px;
      max-width: 900px;
      margin: auto;
    }
    h1, h2 {
      color: #00aaff;
    }
    img {
      width: 100%;
      border-radius: 10px;
      margin-bottom: 20px;
      border: 1px solid #555;
    }
    pre {
      background: #222;
      padding: 10px;
      border-radius: 8px;
      overflow-x: auto;
      color: #0f0;
    }
    a {
      color: #00ccff;
    }
  </style>
</head>
<body>

<h1>🚗 AB RENT A CAR</h1>
<p><strong>Geliştirici:</strong> Mehmet Akif Balcı</p>
<p><strong>Sürüm:</strong> 1.0</p>

<h2>📌 Uygulama Hakkında</h2>
<p>
AB Rent A Car, Python programlama dili ve <strong>CustomTkinter</strong> arayüz bileşenleri kullanılarak geliştirilmiş bir araç kiralama otomasyon sistemidir.
</p>
<p>Kullanıcı dostu tasarımı ve veritabanı desteğiyle, müşterileri ve araçları yönetebilir, kiralama işlemlerini gerçekleştirebilir ve geçmişi görüntüleyebilirsiniz.</p>

<h2>🧰 Kullanılan Teknolojiler</h2>
<ul>
  <li>Python 3.x</li>
  <li>CustomTkinter (modern arayüz)</li>
  <li>MySQL (Veritabanı)</li>
  <li>Pillow (Görsel işleme)</li>
  <li>tkcalendar (Tarih seçici)</li>
</ul>

<h2>🖼️ Ekran Görüntüleri</h2>

<img src="screenshots/Screenshot_1.png" alt="Giriş Ekranı">
<img src="screenshots/Screenshot_2.png" alt="Ana Sayfa">
<img src="screenshots/Screenshot_3.png" alt="Müşteri Kayıt">
<img src="screenshots/Screenshot_4.png" alt="Araba Kayıt">
<img src="screenshots/Screenshot_5.png" alt="Araç Kiralama">
<img src="screenshots/Screenshot_6.png" alt="Aktif Kiralamalar">
<img src="screenshots/Screenshot_7.png" alt="Hakkında Ekranı">

<h2>⚙️ Özellikler</h2>
<ul>
  <li>🔐 Kullanıcı girişi ve kayıt işlemleri</li>
  <li>👤 Müşteri kayıt ve yönetimi</li>
  <li>🚘 Araç kayıt sistemi</li>
  <li>📅 Kiralama süresi ve fiyat hesaplama</li>
  <li>📊 Aktif kiralamaları ve geçmişi görüntüleme</li>
  <li>📁 Veritabanı işlemleri (MySQL)</li>
</ul>

<h2>📂 Proje Yapısı</h2>
<pre>
AB RENT A CAR/
│
├── abrent.py               # Ana uygulama
├── AB RENT A CAR.exe       # Derlenmiş uygulama (PyInstaller)
├── arabotomasyon.sql       # Veritabanı dump (isteğe bağlı)
├── icon_logo.ico           # Uygulama ikonu
├── screenshots/            # Görüntüler
├── icons/                  # Buton ikonları
└── README.html             # Bu dosya
</pre>

<h2>🚀 Kurulum</h2>
<pre>
1. pip install customtkinter pillow mysql-connector-python tkcalendar
2. python abrent.py
</pre>

<h2>🔐 Giriş Bilgisi</h2>
<p>Yeni kullanıcı oluşturmak için "Kayıt Ol" seçeneğini kullanın.</p>

<h2>📝 Lisans</h2>
<p>Bu proje açık kaynak değildir. Her hakkı geliştiricisine aittir.</p>

</body>
</html>
