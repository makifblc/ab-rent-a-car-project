# 🚗 AB Rent A Car – Python OOP GUI Araç Kiralama Uygulaması

AB Rent A Car, Python programlama dili ve grafik kullanıcı arayüzü (GUI) teknolojileri kullanılarak geliştirilmiş modern ve kapsamlı bir araç kiralama otomasyon sistemidir. Uygulama, nesne yönelimli programlama (OOP) prensiplerine sıkı sıkıya bağlı kalınarak geliştirilmiş olup, sağlam bir MySQL veritabanı altyapısıyla desteklenmektedir. Bu sayede hem ölçeklenebilir hem de sürdürülebilir bir çözüm sunar.

## 🧱 Kullanılan Teknolojiler

* **Python 3.x:** Uygulamanın temelini oluşturan, okunabilir ve güçlü bir programlama dili.
* **MySQL:** Güvenilir ve yaygın olarak kullanılan açık kaynaklı veritabanı yönetim sistemi.
* **Tkinter & CustomTkinter:** Modern ve özelleştirilebilir kullanıcı arayüzleri oluşturmak için kullanılan GUI kütüphaneleri. CustomTkinter, Tkinter'in görünümünü iyileştirerek daha çağdaş bir deneyim sunar.
* **Pillow (PIL):** Görüntü işleme yetenekleri sağlayan, ikonlar ve arka plan görselleri gibi görsel öğelerin yönetimi için kullanılan kütüphane.
* **tkcalendar:** Kullanıcıların tarihleri kolayca seçmelerini sağlayan takvim bileşeni (isteğe bağlı olarak kullanılabilir).

## 🧠 Nesne Yönelimli Programlama (OOP) Yapısı

Uygulama, OOP'nin temel prensiplerini benimseyerek modüler, esnek ve bakımı kolay bir mimari sunar:

* **🔒 Encapsulation (Kapsülleme):**

    Her modül, kendi verisi ve bu veriye erişim sağlayan metotlarla birlikte kapsüllenmiştir. Bu, veri güvenliğini artırır ve istenmeyen değişiklikleri önler. Örneğin, müşteri bilgileri veya araç detayları, ilgili sınıflar içinde yönetilir ve doğrudan erişime kapalıdır.

* **📜 Inheritance (Kalıtım):**

    Sistem, ortak özellikleri ve davranışları paylaşan sınıflar arasında kalıtım ilişkileri kurarak kod tekrarını en aza indirir. Örneğin, farklı pencere türleri (müşteri kayıt, araç kayıt vb.) ortak bir temel sınıftan türetilerek, temel GUI özelliklerini devralır. Bu, geliştirme sürecini hızlandırır ve tutarlılığı sağlar.

* **✨ Polymorphism (Çok Biçimlilik):**

    Farklı nesnelerin aynı metot çağrısına farklı şekillerde yanıt verebilmesi prensibidir. Uygulamada, örneğin, farklı veri giriş ekranları (müşteri kayıt, araç kayıt, kiralama) benzer "kaydet" veya "görüntüle" gibi işlemleri farklı biçimlerde uygulayarak çok biçimliliğe örnek teşkil eder.

* **🧩 Abstraction (Soyutlama):**

    Karmaşık sistem detaylarının kullanıcıdan gizlenerek, sadece gerekli işlevselliğin sunulmasıdır. Veritabanı işlemleri, GUI bileşenlerinin detaylı yapılandırması ve kullanıcı etkileşimlerinin yönetimi gibi arka plandaki süreçler, soyut sınıflar ve metotlar aracılığıyla basitleştirilmiştir. Bu, uygulamanın kullanımını kolaylaştırır ve geliştirme sürecini hızlandırır.

## ⚙️ Özellikler

* **👤 Kullanıcı Girişi & Kayıt Olma:**

    Güvenli kullanıcı yönetimi ile sisteme erişimi kontrol altına alır. Kullanıcılar, kendi hesaplarını oluşturabilir ve geçerli kimlik bilgileriyle sisteme giriş yapabilir.

    ![Giriş Ekranı](Uygulama Resimleri\Screenshot_1.png)

* **📄 Müşteri Kayıt ve Yönetimi:**

    Müşteri bilgilerinin (ad, soyad, TC kimlik numarası, iletişim bilgileri vb.) kaydedilmesi, güncellenmesi ve yönetilmesi.

    ![Müşteri Kayıt Ekranı](Screenshot_3.png)

* **🚘 Araç Ekleme, Listeleme ve Güncelleme:**

    Araç bilgilerinin (marka, model, üretim yılı, teknik özellikler vb.) sisteme eklenmesi, mevcut araçların listelenmesi ve bilgilerinin güncellenmesi.

    ![Araç Kayıt Ekranı](Screenshot_4.jpg)

* **📆 Araç Kiralama, Ücret Hesaplama ve Süre Takibi:**

    Müşteri ve araç seçimi yapılarak kiralama işlemlerinin gerçekleştirilmesi, kiralama süresinin belirlenmesi ve otomatik ücret hesaplaması.

    ![Kiralama Ekranı](Screenshot_5.png)

* **📜 Kiralama Geçmişi ve Aktif Kiralamalar:**

    Geçmiş kiralama kayıtlarının görüntülenmesi ve şu anda devam eden aktif kiralama işlemlerinin takibi.

    ![Ana Sayfa](Screenshot_2.png)

* **💾 MySQL Veritabanı Entegrasyonu:**

    Verilerin güvenli ve kalıcı olarak saklanmasını sağlayan MySQL veritabanı ile sorunsuz entegrasyon.

* **📤 CSV Dışa Aktarım (Genişletilebilir):**

    İstenilen verilerin CSV formatında dışa aktarılabilmesi (gelecekte farklı formatlara genişletilebilir).

* **🌙 Dark Mode Desteği:**

    Kullanıcı tercihine göre ayarlanabilen, göz yorgunluğunu azaltan modern karanlık tema desteği.

## 🗃️ Veritabanı Yapısı

Uygulama, verileri düzenli ve verimli bir şekilde saklamak için aşağıdaki tabloları kullanır. Tablolar, uygulama ilk kez çalıştırıldığında otomatik olarak oluşturulur:

| Tablo Adı          | Açıklama
