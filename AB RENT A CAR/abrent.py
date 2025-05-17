import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as mysql
from dataclasses import dataclass
from typing import List
import customtkinter as ctk
from PIL import Image, ImageTk
import uuid

try:
    import tkcalendar as tkc
except ImportError:
    tkc = None

# Görsel dosyalarının yolları (örnek, yerel dosyalara göre güncelleyin)
background_images = {
    "main": "rent-a-car-with-python-main/bg.png",
}

# Arka plan görseli ekleme fonksiyonu
def set_background(window, image_key, width, height):
    try:
        image_path = background_images.get(image_key, "bg.png")
        image = Image.open(image_path)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = tk.Label(window, image=photo)
        background_label.image = photo  # Referansı tut
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.lower()
    except Exception as e:
        print(f"Arka plan görseli yüklenemedi ({image_key}): {e}")
# İkon dosyalarının yolları (örnek, yerel dosyalara göre güncelleyin)
icon_images = {
    "save": "icons/save_icon.png",
    "rent": "icons/rent_icon.png",
    "user": "icons/user_icon.png",
    "car": "icons/car_icon.png",
    "history": "icons/history_icon.png",
    "active": "icons/active_icon.png",
}

# Arka plan görseli ekleme fonksiyonu
def set_background(window, image_key, width, height):
    try:
        image_path = background_images.get(image_key, "bg.png")
        image = Image.open(image_path)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        background_label = tk.Label(window, image=photo)
        background_label.image = photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.lower()
    except Exception as e:
        print(f"Arka plan görseli yüklenemedi ({image_key}): {e}")

# Customtkinter ayarları
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

@dataclass
class DBConfig:
    host: str = "localhost"
    user: str = "root"
    password: str = "1234"
    database: str = "arabaotomasyonu"

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def load_icon(icon_key, size=(20, 20)):
    try:
        image_path = icon_images.get(icon_key, "default_icon.png")
        image = Image.open(image_path)
        image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"İkon yüklenemedi ({icon_key}): {e}")
        return None

class LoginScreen:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Giriş Yap")
        center_window(self.root, 400, 350)
        self.root.resizable(False, False)
        self.root.iconbitmap('rent-a-car-with-python-main/icon_logo.ico')

        ctk.CTkLabel(self.root, text="Kullanıcı Adı:", font=("Arial", 12)).pack(pady=10)
        self.entry_username = ctk.CTkEntry(self.root, width=200)
        self.entry_username.pack(pady=5)

        ctk.CTkLabel(self.root, text="Şifre:", font=("Arial", 12)).pack(pady=10)
        self.entry_password = ctk.CTkEntry(self.root, show="*", width=200)
        self.entry_password.pack(pady=5)

        ctk.CTkButton(
            self.root,
            text="Giriş Yap",
            command=self.login,
            image=load_icon("user"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        ctk.CTkButton(
            self.root,
            text="Kayıt Ol",
            command=self.open_register,
            image=load_icon("user"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        self.root.mainloop()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        try:
            connection = mysql.connect(
                host=DBConfig.host,
                user=DBConfig.user,
                password=DBConfig.password,
                database=DBConfig.database
            )
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM kullanicilar WHERE kullanici_adi=%s AND sifre=%s",
                (username, password)
            )
            result = cursor.fetchone()
            cursor.close()
            connection.close()

            if result:
                self.root.destroy()
                AracOtomasyonu()
            else:
                messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış.")
        except mysql.Error as err:
            messagebox.showerror("Hata", f"Veritabanı hatası: {err}")

    def open_register(self):
        self.register_window = ctk.CTkToplevel(self.root)
        self.register_window.title("Kayıt Ol")
        center_window(self.register_window, 300, 250)
        self.register_window.resizable(False, False)
        self.register_window.attributes('-topmost', True)

        ctk.CTkLabel(self.register_window, text="Kullanıcı Adı:", font=("Arial", 12)).pack(pady=10)
        self.reg_entry_username = ctk.CTkEntry(self.register_window, width=200)
        self.reg_entry_username.pack(pady=5)

        ctk.CTkLabel(self.register_window, text="Şifre:", font=("Arial", 12)).pack(pady=10)
        self.reg_entry_password = ctk.CTkEntry(self.register_window, show="*", width=200)
        self.reg_entry_password.pack(pady=5)

        ctk.CTkButton(
            self.register_window,
            text="Kayıt Ol",
            command=self.register,
            image=load_icon("save"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold")
        ).pack(pady=10)

    def register(self):
        username = self.reg_entry_username.get()
        password = self.reg_entry_password.get()

        if not username or not password:
            messagebox.showerror("Hata", "Kullanıcı adı ve şifre boş olamaz!")
            return

        try:
            connection = mysql.connect(
                host=DBConfig.host,
                user=DBConfig.user,
                password=DBConfig.password,
                database=DBConfig.database
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO kullanicilar (kullanici_adi, sifre) VALUES (%s, %s)",
                (username, password)
            )
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Başarılı", "Kayıt tamamlandı!")
            self.register_window.destroy()
        except mysql.Error as err:
            messagebox.showerror("Hata", f"Kayıt başarısız: {err}")

class AracOtomasyonu:
    def __init__(self):
        self.setup_database()
        self.setup_ui()
        self.pencere.mainloop()

    def __del__(self):
        if hasattr(self, 'db') and self.db.is_connected():
            self.cursor.close()
            self.db.close()

    def setup_database(self):
        try:
            self.db = mysql.connect(
                host=DBConfig.host,
                user=DBConfig.user,
                password=DBConfig.password
            )
            self.cursor = self.db.cursor()
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DBConfig.database}")
            self.cursor.execute(f"USE {DBConfig.database}")
            self.create_tables()
        except mysql.Error as err:
            messagebox.showerror("Hata", f"MySQL bağlantısı kurulamadı: {err}")
            exit(1)

    def create_tables(self):
        tables = {
            "musteribilgileri": """
                CREATE TABLE IF NOT EXISTS musteribilgileri (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ad VARCHAR(255),
                    soyad VARCHAR(255),
                    tcNo VARCHAR(11),
                    dogumTarihi DATE,
                    adres VARCHAR(255),
                    telefonNo VARCHAR(15),
                    meslek VARCHAR(255),
                    ehliyet VARCHAR(10),
                    medeniHal VARCHAR(20),
                    egitim VARCHAR(50)
                )
            """,
            "arababilgileri": """
                CREATE TABLE IF NOT EXISTS arababilgileri (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    marka VARCHAR(255),
                    model VARCHAR(255),
                    uretimYili INT,
                    yakitTuru VARCHAR(50),
                    vites VARCHAR(20),
                    motorGucu INT,
                    kasaTipi VARCHAR(50),
                    motorHacmi INT,
                    cekisTuru VARCHAR(50),
                    kapiSayisi INT,
                    renk VARCHAR(50),
                    motorNo VARCHAR(50),
                    sasiNo VARCHAR(50),
                    gunlukKiralamaUcreti DECIMAL(10,2) DEFAULT 100,
                    kiradaMi BOOLEAN DEFAULT FALSE,
                    kullanimDisi BOOLEAN DEFAULT FALSE
                )
            """,
            "kiralamabilgileri": """
                CREATE TABLE IF NOT EXISTS kiralamabilgileri (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    musteri_id INT,
                    araba_id INT,
                    kiralamaSuresi INT,
                    nereyeGidecek VARCHAR(255),
                    ucret DECIMAL(10,2),
                    kiralamaTarihi DATETIME DEFAULT CURRENT_TIMESTAMP,
                    aktif BOOLEAN DEFAULT TRUE,
                    FOREIGN KEY (musteri_id) REFERENCES musteribilgileri(id),
                    FOREIGN KEY (araba_id) REFERENCES arababilgileri(id)
                )
            """,
            "kullanicilar": """
                CREATE TABLE IF NOT EXISTS kullanicilar (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    kullanici_adi VARCHAR(255) UNIQUE,
                    sifre VARCHAR(255)
                )
            """
        }
        for table_sql in tables.values():
            try:
                self.cursor.execute(table_sql)
            except mysql.Error as err:
                print(f"Tablo oluşturma hatası: {err}")
        self.db.commit()

    def setup_ui(self):
        self.pencere = ctk.CTk()
        self.pencere.title("AB RENT A CAR")
        center_window(self.pencere, 950, 600)
        self.pencere.resizable(False, False)
        set_background(self.pencere, "main", 950, 600)
        try:
            self.pencere.iconbitmap('rent-a-car-with-python-main/icon_logo.ico')
        except:
            print("İkon yüklenemedi")

        self.create_menu()

        ctk.CTkLabel(
            self.pencere,
            text="",
            font=("Arial", 24, "bold")
        ).grid(row=0, column=0, columnspan=5, pady=40)
        self.create_main_buttons()

    def create_menu(self):
        menu_frame = ctk.CTkFrame(self.pencere, fg_color="transparent")
        menu_frame.grid(row=0, column=0, sticky="nw", columnspan=5, padx=10)

        self.yardim_var = tk.StringVar(value="Yardım")
        yardim_menu = ctk.CTkOptionMenu(
            menu_frame,
            values=["Nasıl çalışır", "Hakkında", "Çıkış"],
            variable=self.yardim_var,
            command=self.yardim_menu_command,
            width=120,
            font=("Arial", 12)
        )
        yardim_menu.grid(row=0, column=0, padx=5)

        self.veritabani_var = tk.StringVar(value="Veri Tabanları")
        veritabani_menu = ctk.CTkOptionMenu(
            menu_frame,
            values=["Müşteri Veritabanı", "Araba Veritabanı", "Kiralama Geçmişi"],
            variable=self.veritabani_var,
            command=self.veritabani_menu_command,
            width=120,
            font=("Arial", 12)
        )
        veritabani_menu.grid(row=0, column=1, padx=5)

    def yardim_menu_command(self, choice):
        if choice == "Nasıl çalışır":
            self.help_page()
        elif choice == "Hakkında":
            self.about_page()
        elif choice == "Çıkış":
            self.pencere.quit()
        self.yardim_var.set("Yardım")

    def veritabani_menu_command(self, choice):
        if choice == "Müşteri Veritabanı":
            self.kayitli_musterileri_goruntule()
        elif choice == "Araba Veritabanı":
            self.kayitli_arabalari_goruntule()
        elif choice == "Kiralama Geçmişi":
            self.kiralama_gecmisi_ekrani()
        self.veritabani_var.set("Veri Tabanları")

    def create_main_buttons(self):
        btn_info = [
            ("Müşteri Kayıt", self.musteri_bilgileri_ekrani, "user"),
            ("Araba Kayıt", self.araba_bilgileri_ekrani, "car"),
            ("Araç Kiralama", self.arac_kiralama_ekrani, "rent"),
            ("Aktif Kiralamalar", self.kirada_olan_araclar_ekrani, "active"),
            ("Kiralama Geçmişi", self.kiralama_gecmisi_ekrani, "history")
        ]
        for idx, (text, command, icon) in enumerate(btn_info):
            ctk.CTkButton(
                self.pencere,
                text=text,
                command=command,
                image=load_icon(icon),
                compound="left",
                font=("Arial", 12, "bold"),
                width=160,
                height=100,
                corner_radius=10
            ).grid(row=10, column=idx, pady=120, padx=15)

    def musteri_bilgileri_ekrani(self):
        self.musteri_kayit = ctk.CTkToplevel(self.pencere)
        self.musteri_kayit.title("Müşteri Kayıt")
        self.musteri_kayit.resizable(False, False)
        center_window(self.musteri_kayit, 500, 600)
        self.musteri_kayit.attributes('-topmost', True)

        labels = [
            "Müşteri Adı", "Müşteri Soyadı", "Müşteri TC",
            "Doğum Tarihi", "Adres", "Telefon No",
            "Meslek", "Ehliyet Sınıfı", "Medeni Hali", "Eğitim Durumu"
        ]
        self.musteri_entries = {}
        for idx, label in enumerate(labels):
            ctk.CTkLabel(
                self.musteri_kayit,
                text=f"{label}:",
                font=("Arial", 12, "bold")
            ).grid(row=idx+1, column=0, padx=20, pady=8, sticky="e")
            if label == "Doğum Tarihi" and tkc:
                entry = tkc.DateEntry(self.musteri_kayit, date_pattern='yyyy-mm-dd')
            else:
                entry = ctk.CTkEntry(self.musteri_kayit, width=200)
            entry.grid(row=idx+1, column=1, pady=8)
            self.musteri_entries[label] = entry

        ctk.CTkButton(
            self.musteri_kayit,
            text="Müşteri Kaydı Tamamla",
            command=self.musteri_verilerini_taboya_gonder,
            image=load_icon("save"),
            compound="left",
            font=("Arial", 12, "bold"),
            width=300,
            corner_radius=10
        ).grid(row=12, column=0, columnspan=2, pady=20)

    def musteri_verilerini_taboya_gonder(self):
        data = {k: v.get() for k, v in self.musteri_entries.items()}
        try:
            sql = """
                INSERT INTO musteribilgileri
                (ad, soyad, tcNo, dogumTarihi, adres, telefonNo, meslek, ehliyet, medeniHal, egitim)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = tuple(data.values())
            self.cursor.execute(sql, values)
            self.db.commit()
            messagebox.showinfo("Başarılı", "Müşteri kaydı tamamlandı.")
            self.musteri_kayit.destroy()
        except mysql.Error as err:
            messagebox.showerror("Hata", f"Kayıt başarısız: {err}")

    def araba_bilgileri_ekrani(self):
        self.araba_kayit = ctk.CTkToplevel(self.pencere)
        self.araba_kayit.title("Araba Kayıt")
        self.araba_kayit.resizable(False, False)
        center_window(self.araba_kayit, 500, 700)
        self.araba_kayit.attributes('-topmost', True)

        labels = [
            "Marka", "Model", "Üretim Yılı", "Yakıt Türü", "Vites",
            "Motor Gücü", "Kasa Tipi", "Motor Hacmi", "Çekiş Türü",
            "Kapı Sayısı", "Renk", "Motor No", "Şasi No",
            "Günlük Kiralama Ücreti"
        ]
        self.araba_entries = {}
        for idx, label in enumerate(labels):
            ctk.CTkLabel(
                self.araba_kayit,
                text=f"{label}:",
                font=("Arial", 12, "bold")
            ).grid(row=idx+1, column=0, padx=20, pady=8, sticky="e")
            entry = ctk.CTkEntry(self.araba_kayit, width=200)
            entry.grid(row=idx+1, column=1, pady=8)
            self.araba_entries[label] = entry

        ctk.CTkButton(
            self.araba_kayit,
            text="Araba Kaydı Tamamla",
            command=self.araba_verilerini_taboya_gonder,
            image=load_icon("save"),
            compound="left",
            font=("Arial", 12, "bold"),
            width=300,
            corner_radius=10
        ).grid(row=16, column=0, columnspan=2, pady=20)

    def araba_verilerini_taboya_gonder(self):
        data = {k: v.get() for k, v in self.araba_entries.items()}
        try:
            sql = """
                INSERT INTO arababilgileri
                (marka, model, uretimYili, yakitTuru, vites, motorGucu, kasaTipi, 
                motorHacmi, cekisTuru, kapiSayisi, renk, motorNo, sasiNo, gunlukKiralamaUcreti)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                data["Marka"], data["Model"], int(data["Üretim Yılı"]),
                data["Yakıt Türü"], data["Vites"], int(data["Motor Gücü"]),
                data["Kasa Tipi"], int(data["Motor Hacmi"]), data["Çekiş Türü"],
                int(data["Kapı Sayısı"]), data["Renk"], data["Motor No"],
                data["Şasi No"], float(data["Günlük Kiralama Ücreti"])
            )
            self.cursor.execute(sql, values)
            self.db.commit()
            messagebox.showinfo("Başarılı", "Araba kaydı tamamlandı.")
            self.araba_kayit.destroy()
        except (mysql.Error, ValueError) as err:
            messagebox.showerror("Hata", f"Kayıt başarısız: {err}")

    def arac_kiralama_ekrani(self):
        self.kiralama_ekrani = ctk.CTkToplevel(self.pencere)
        self.kiralama_ekrani.title("Araç Kiralama")
        self.kiralama_ekrani.resizable(False, False)
        center_window(self.kiralama_ekrani, 400, 400)
        self.kiralama_ekrani.attributes('-topmost', True)

        ctk.CTkLabel(
            self.kiralama_ekrani,
            text="Müşteri Seçin:",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=0, padx=20, pady=10)
        self.musteri_secim = ctk.CTkComboBox(self.kiralama_ekrani, values=self.get_musteri_listesi(), width=200)
        self.musteri_secim.grid(row=0, column=1, pady=10)

        ctk.CTkLabel(
            self.kiralama_ekrani,
            text="Araba Seçin:",
            font=("Arial", 12, "bold")
        ).grid(row=1, column=0, padx=20, pady=10)
        self.araba_secim = ctk.CTkComboBox(self.kiralama_ekrani, values=self.get_araba_listesi(), width=200)
        self.araba_secim.grid(row=1, column=1, pady=10)

        ctk.CTkLabel(
            self.kiralama_ekrani,
            text="Kiralama Süresi (gün):",
            font=("Arial", 12, "bold")
        ).grid(row=2, column=0, padx=20, pady=10)
        self.kiralama_suresi = ctk.CTkEntry(self.kiralama_ekrani, width=200)
        self.kiralama_suresi.grid(row=2, column=1, pady=10)

        ctk.CTkLabel(
            self.kiralama_ekrani,
            text="Nereye Gidecek:",
            font=("Arial", 12, "bold")
        ).grid(row=3, column=0, padx=20, pady=10)
        self.nereye_gidecek = ctk.CTkEntry(self.kiralama_ekrani, width=200)
        self.nereye_gidecek.grid(row=3, column=1, pady=10)

        ctk.CTkButton(
            self.kiralama_ekrani,
            text="Kiralamayı Tamamla",
            command=self.kiralama_islemi,
            image=load_icon("rent"),
            compound="left",
            font=("Arial", 12, "bold"),
            width=200,
            corner_radius=10
        ).grid(row=4, column=0, columnspan=2, pady=20)

    def kiralama_islemi(self):
        try:
            musteri_id = self.get_musteri_id(self.musteri_secim.get())
            araba_id = self.get_araba_id(self.araba_secim.get())
            sure = int(self.kiralama_suresi.get())
            nereye_gidecek = self.nereye_gidecek.get()
            ucret = self.get_araba_ucreti(araba_id) * sure

            sql = """
                INSERT INTO kiralamabilgileri 
                (musteri_id, araba_id, kiralamaSuresi, nereyeGidecek, ucret, aktif)
                VALUES (%s, %s, %s, %s, %s, TRUE)
            """
            self.cursor.execute(sql, (musteri_id, araba_id, sure, nereye_gidecek, ucret))

            self.cursor.execute(
                "UPDATE arababilgileri SET kiradaMi = TRUE WHERE id = %s",
                (araba_id,)
            )
            self.db.commit()
            messagebox.showinfo("Başarılı", "Araç kiralama tamamlandı.")
            self.kiralama_ekrani.destroy()
        except (mysql.Error, ValueError) as err:
            messagebox.showerror("Hata", f"İşlem başarısız: {err}")

    def get_musteri_listesi(self) -> List[str]:
        try:
            self.cursor.execute("SELECT id, CONCAT(ad, ' ', soyad) FROM musteribilgileri")
            return [f"{row[0]} - {row[1]}" for row in self.cursor.fetchall()]
        except mysql.Error:
            return []

    def get_araba_listesi(self) -> List[str]:
        try:
            self.cursor.execute("SELECT id, marka FROM arababilgileri WHERE kiradaMi=0 AND kullanimDisi=0")
            return [f"{row[0]} - {row[1]}" for row in self.cursor.fetchall()]
        except mysql.Error:
            return []

    def get_musteri_id(self, selection: str) -> int:
        try:
            return int(selection.split(" - ")[0])
        except:
            return 0

    def get_araba_id(self, selection: str) -> int:
        try:
            return int(selection.split(" - ")[0])
        except:
            return 0

    def get_araba_ucreti(self, araba_id: int) -> float:
        try:
            self.cursor.execute("SELECT gunlukKiralamaUcreti FROM arababilgileri WHERE id=%s", (araba_id,))
            result = self.cursor.fetchone()
            return result[0] if result else 0.0
        except mysql.Error:
            return 0.0

    def kirada_olan_araclar_ekrani(self):
        pencere = ctk.CTkToplevel(self.pencere)
        pencere.title("Aktif Kiralamalar")
        pencere.resizable(False, False)
        center_window(pencere, 900, 400)
        pencere.attributes('-topmost', True)

        columns = ("ID", "Marka", "Model", "Kiralama Süresi", "Müşteri", "Ücret", "Kiralama Tarihi")
        tree = ttk.Treeview(pencere, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        tree.pack(fill=tk.BOTH, expand=True)

        try:
            sql = """
                SELECT ar.id, ar.marka, ar.model, kir.kiralamaSuresi, 
                       CONCAT(m.ad, ' ', m.soyad), kir.ucret, kir.kiralamaTarihi
                FROM arababilgileri ar
                JOIN kiralamabilgileri kir ON ar.id = kir.araba_id
                JOIN musteribilgileri m ON kir.musteri_id = m.id
                WHERE kir.aktif = TRUE
            """
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)
        except mysql.Error as err:
            messagebox.showerror("Hata", f"Veri alınamadı: {err}")

    def kiralama_gecmisi_ekrani(self):
        pencere = ctk.CTkToplevel(self.pencere)
        pencere.title("Kiralama Geçmişi")
        pencere.resizable(False, False)
        center_window(pencere, 900, 400)
        pencere.attributes('-topmost', True)

        columns = ("ID", "Marka", "Model", "Kiralama Süresi", "Müşteri", "Ücret", "Kiralama Tarihi", "Durum")
        tree = ttk.Treeview(pencere, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=110)
        tree.pack(fill=tk.BOTH, expand=True)

        try:
            sql = """
                SELECT kir.id, ar.marka, ar.model, kir.kiralamaSuresi, 
                    CONCAT(m.ad, ' ', m.soyad), kir.ucret, kir.kiralamaTarihi, 
                        CASE WHEN kir.aktif = TRUE THEN 'Aktif' ELSE 'Tamamlandı' END
                FROM arababilgileri ar
                JOIN kiralamabilgileri kir ON ar.id = kir.araba_id
                JOIN musteribilgileri m ON kir.musteri_id = m.id
            """
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)
        except mysql.Error as err:
            messagebox.showerror("Hata", f"Veri alınamadı: {err}")

    def kayitli_musterileri_goruntule(self):
        pencere = ctk.CTkToplevel(self.pencere)
        pencere.title("Kayıtlı Müşteriler")
        pencere.resizable(True, True)
        center_window(pencere, 900, 600)
        pencere.attributes('-topmost', True)

        columns = ("ID", "Ad", "Soyad", "Telefon No", "Adres", "TC No")
        tree = ttk.Treeview(pencere, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=140)
        tree.pack(fill=tk.BOTH, expand=True)

        try:
            self.cursor.execute("SELECT id, ad, soyad, telefonNo, adres, tcNo FROM musteribilgileri")
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)
        except mysql.Error as err:
            messagebox.showerror("Hata", f"Veri alınamadı: {err}")

    def kayitli_arabalari_goruntule(self):
        pencere = ctk.CTkToplevel(self.pencere)
        pencere.title("Kayıtlı Arabalar")
        pencere.resizable(True, True)
        center_window(pencere, 900, 600)
        pencere.attributes('-topmost', True)

        columns = ("ID", "Marka", "Model", "Üretim Yılı", "Durum", "Günlük Ücret")
        tree = ttk.Treeview(pencere, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=140)
        tree.pack(fill=tk.BOTH, expand=True)

        try:
            self.cursor.execute("SELECT id, marka, model, uretimYili, kiradaMi, gunlukKiralamaUcreti FROM arababilgileri")
            for row in self.cursor.fetchall():
                durum = "Kirada" if row[4] else "Müsait"
                tree.insert("", "end", values=(row[0], row[1], row[2], row[3], durum, row[5]))
        except mysql.Error as err:
            messagebox.showerror("Hata", f"Veri alınamadı: {err}")

    def help_page(self):
        mesaj = ("Bu araç kiralama otomasyon programı sayesinde, müşterilerinizi ve araçlarınızı kolayca kaydedebilir, "
                "araç kiralama işlemlerini hızlı bir şekilde gerçekleştirebilir, aktif kiralamaları ve kiralama geçmişini "
                "görüntüleyebilirsiniz.")
        messagebox.showinfo("Nasıl Çalışır", mesaj)

    def about_page(self):
        mesaj = "Geliştirici: Mehmet Akif Balcı\nVersiyon: 1.0"
        messagebox.showinfo("Hakkında", mesaj)

if __name__ == "__main__":
    LoginScreen()
    
#pyinstaller --onefile --icon=icon_logo.ico abrent.py