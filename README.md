# 💪 MUSCLELOGIC

## 🧠 Sistem Pakar Rekomendasi Latihan *Muscle Building* Pemula

> 🏆 **Academic Final Project — Informatics Engineering**
>
> MuscleLogic adalah aplikasi sistem pakar berbasis web yang memberikan rekomendasi program latihan *muscle building* bagi pengguna pemula berdasarkan karakteristik dan kondisi pengguna.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge\&logo=django\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge\&logo=bootstrap\&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)
![Forward Chaining](https://img.shields.io/badge/Forward%20Chaining-FF9800?style=for-the-badge)

---

# 🌟 OVERVIEW

**MuscleLogic** dikembangkan sebagai project **Tugas Akhir Program Studi Teknik Informatika** untuk menerapkan konsep **Sistem Pakar berbasis aturan** dalam memberikan rekomendasi latihan bagi pengguna pemula.

Sistem menggunakan metode **Forward Chaining** untuk memproses fakta awal pengguna dan mencocokkannya dengan aturan pada basis pengetahuan hingga menghasilkan rekomendasi program latihan.

### 🎯 Karakteristik yang Dipertimbangkan

| 🧩 Karakteristik    | 📌 Keterangan                                    |
| ------------------- | ------------------------------------------------ |
| ⚖️ **BMI**          | Kondisi tubuh berdasarkan tinggi dan berat badan |
| 🏋️ **Pengalaman**  | Pengalaman latihan pengguna                      |
| 📚 **Teknik Dasar** | Pemahaman teknik dasar latihan                   |
| 🎯 **Tujuan**       | Tujuan latihan pengguna                          |
| 💪 **Prioritas**    | Fokus latihan pengguna                           |
| 🏢 **Tempat**       | Gym atau latihan di rumah                        |
| 🧰 **Peralatan**    | Peralatan yang tersedia                          |
| 📅 **Frekuensi**    | Jumlah hari latihan                              |
| ⏱️ **Durasi**       | Durasi latihan                                   |
| 🩹 **Cedera**       | Riwayat cedera                                   |
| 📍 **Area Cedera**  | Lokasi cedera pengguna                           |

---

# ✨ FEATURES

### 👤 Konsultasi Pengguna

📝 Input karakteristik pengguna
⚖️ Perhitungan BMI
📊 Klasifikasi kondisi tubuh
🌱 Penentuan level pemula
🎯 Penentuan tujuan latihan
💪 Penentuan prioritas latihan
🏢 Penentuan tempat latihan
🧰 Penyesuaian berdasarkan peralatan
📅 Penentuan frekuensi latihan
⏱️ Penyesuaian berdasarkan durasi
🩹 Identifikasi kondisi cedera

### 🧠 Sistem Pakar

🔹 Pembentukan fakta awal
🔹 Pencocokan fakta dengan rule
🔹 Penerapan Forward Chaining
🔹 Pembentukan fakta turunan
🔹 Penentuan batasan gerakan
🔹 Penentuan intensitas awal
🔹 Penyesuaian program
🔹 Penyesuaian peralatan
🔹 Penentuan rekomendasi akhir

### 🏋️ Program Latihan

📦 Paket latihan
📅 Jadwal latihan berdasarkan hari
🏋️ Daftar gerakan
🔢 Set dan repetisi
⏱️ Waktu istirahat
⚠️ Batasan latihan
📝 Catatan latihan

---

# 🧠 FORWARD CHAINING

MuscleLogic menggunakan **Forward Chaining** sebagai metode inferensi.

Proses dimulai dari **fakta awal** yang diperoleh melalui konsultasi pengguna. Fakta tersebut kemudian dicocokkan dengan kondisi aturan yang terdapat dalam basis pengetahuan.

Jika kondisi suatu aturan terpenuhi, aturan dijalankan dan menghasilkan **fakta turunan**. Fakta tersebut kemudian digunakan kembali dalam proses pencocokan aturan berikutnya hingga diperoleh rekomendasi akhir.

### 🔄 Alur Inferensi

```text
             👤 PENGGUNA
                  │
                  ▼
          📝 DATA KONSULTASI
                  │
                  ▼
             📌 FAKTA AWAL
                  │
                  ▼
          🔍 PENCocokan RULE
                  │
                  ▼
          ❓ RULE TERPENUHI?
             │          │
            ❌          ✅
             │          │
             │          ▼
             │     ⚙️ JALANKAN RULE
             │          │
             │          ▼
             │     📌 FAKTA TURUNAN
             │          │
             └──────────┤
                        ▼
                🔄 RULE BERIKUTNYA
                        │
                        ▼
                 🎯 REKOMENDASI
                        │
                        ▼
                  📦 PAKET LATIHAN
```

---

# 📚 KNOWLEDGE BASE

Basis pengetahuan MuscleLogic terdiri dari beberapa kelompok aturan:

| 🔢 Rule       | 📖 Dataset            | 🎯 Fungsi                         |
| ------------- | --------------------- | --------------------------------- |
| 🩹 **RS15**   | `RS15_Safety`         | Aturan cedera dan batasan gerakan |
| ⚖️ **RS5**    | `RS5_KondisiTubuh`    | Kondisi tubuh berdasarkan BMI     |
| 🌱 **RS6**    | `RS6_Level`           | Penentuan level pemula            |
| 🔥 **RS3**    | `RS3_IntensitasAwal`  | Penentuan intensitas awal         |
| ⚙️ **RS4**    | `RS4_Penyesuaian`     | Penyesuaian program latihan       |
| 🧰 **RS7**    | `RS7_PenyesuaianAlat` | Penyesuaian berdasarkan peralatan |
| 🎯 **RS1**    | `RS1_Rekomendasi`     | Penentuan rekomendasi akhir       |
| 📦 **OUTPUT** | `Paket_Latihan`       | Data paket latihan sebagai output |

---

# 🏆 RECOMMENDATION OUTPUT

Setelah proses inferensi selesai, sistem menghasilkan **paket latihan** yang disesuaikan dengan karakteristik pengguna.

Contoh struktur hasil:

```text
╔══════════════════════════════════════╗
║          🏋️ PAKET LATIHAN            ║
╠══════════════════════════════════════╣
║ 🎯 Tujuan    : Muscle Building       ║
║ 🌱 Level     : Pemula                ║
║ 📅 Frekuensi : 2x / Minggu           ║
║ ⏱️ Durasi    : < 30 Menit            ║
╠══════════════════════════════════════╣
║ 📅 HARI 1                             ║
║                                      ║
║ 🏋️ Leg Press                         ║
║ 🏋️ Chest Press                       ║
║ 🏋️ Lat Pulldown                      ║
║ 🏋️ Dead Bug                          ║
║                                      ║
║ 📅 HARI 2                             ║
║                                      ║
║ 🏋️ Leg Press                         ║
║ 🏋️ Glute Bridge                      ║
║ 🏋️ Seated Row                        ║
║ 🏃 Treadmill Ringan                  ║
╚══════════════════════════════════════╝
```

---

# 🛠️ TECHNOLOGY STACK

![Python](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Django](https://img.shields.io/badge/DJANGO-092E20?style=for-the-badge\&logo=django\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLITE-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![Bootstrap](https://img.shields.io/badge/BOOTSTRAP-7952B3?style=for-the-badge\&logo=bootstrap\&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)

---

# 📁 PROJECT STRUCTURE

```text
musclelogic-sistem-pakar/
│
├── 📂 project/
│   │
│   ├── 📂 apps/
│   │
│   ├── 📂 data/
│   │
│   ├── 📂 project/
│   │
│   ├── 🗄️ db.sqlite3
│   │
│   ├── 📄 requirements.txt
│   │
│   ├── ⚙️ manage.py
│   │
│   └── 📜 import_ruleset.py
│
└── 📄 README.md
```

### 📌 Folder & File

| 📂 File / Folder    | 💡 Keterangan              |
| ------------------- | -------------------------- |
| `apps/`             | Aplikasi Django            |
| `data/`             | Data dan ruleset sistem    |
| `project/`          | Konfigurasi utama Django   |
| `db.sqlite3`        | Database SQLite            |
| `requirements.txt`  | Dependency Python          |
| `manage.py`         | Pengelolaan project Django |
| `import_ruleset.py` | Script import ruleset      |

---

# 🚀 INSTALLATION

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Aldaka/musclelogic-sistem-pakar.git
```

## 2️⃣ Masuk ke Folder Project

```bash
cd musclelogic-sistem-pakar/project
```

## 3️⃣ Buat Virtual Environment

```bash
python -m venv env
```

## 4️⃣ Aktifkan Virtual Environment

### 🪟 Windows CMD

```bash
env\Scripts\activate
```

### 🪟 Windows PowerShell

```powershell
.\env\Scripts\Activate.ps1
```

Jika berhasil, terminal akan menampilkan:

```text
(env) C:\...\musclelogic-sistem-pakar\project>
```

## 5️⃣ Install Dependency

```bash
pip install -r requirements.txt
```

## 6️⃣ Jalankan Server

```bash
python manage.py runserver
```

## 7️⃣ Buka Aplikasi

🌐 **http://127.0.0.1:8000/**

---

# 🔄 CONSULTATION FLOW

```text
👤 Pengguna
     │
     ▼
📝 Input Konsultasi
     │
     ▼
⚖️ BMI & Kondisi Tubuh
     │
     ▼
🧠 Fakta Awal
     │
     ▼
🔍 Forward Chaining
     │
     ├── 🩹 RS15 → Safety
     ├── ⚖️ RS5  → Kondisi Tubuh
     ├── 🌱 RS6  → Level Pemula
     ├── 🔥 RS3  → Intensitas Awal
     ├── ⚙️ RS4  → Penyesuaian
     ├── 🧰 RS7  → Penyesuaian Alat
     └── 🎯 RS1  → Rekomendasi
              │
              ▼
       📦 Paket Latihan
              │
              ▼
       🏋️ Program Latihan
```

---

# 📊 CONSULTATION RESULT

Sistem menampilkan hasil konsultasi berupa:

| 🖥️ Output          | 📌 Informasi                      |
| ------------------- | --------------------------------- |
| ⚖️ BMI              | Nilai dan kategori BMI            |
| 🧠 Inference        | Proses inferensi Forward Chaining |
| 🎯 Recommendation   | Paket latihan yang sesuai         |
| 📅 Schedule         | Jadwal berdasarkan hari           |
| 🏋️ Exercise        | Gerakan latihan                   |
| 🔢 Set & Repetition | Set dan repetisi                  |
| ⏱️ Rest             | Waktu istirahat                   |
| ⚠️ Safety           | Batasan latihan                   |
| 📝 Notes            | Catatan latihan                   |

---

# 🎓 ACADEMIC PROJECT

🎓 **Tugas Akhir**
🏫 **Program Studi Teknik Informatika**

Project ini dikembangkan untuk menerapkan konsep **Sistem Pakar berbasis aturan** dengan metode **Forward Chaining** dalam memberikan rekomendasi latihan *muscle building* bagi pengguna pemula.

---

# 👨‍💻 DEVELOPER

## Pasadena Saka

🎓 Program Studi Teknik Informatika

---

# ⚠️ DISCLAIMER

> MuscleLogic dikembangkan untuk kebutuhan akademik dan demonstrasi implementasi sistem pakar berbasis web.
>
> Rekomendasi latihan yang diberikan sistem merupakan panduan umum dan bukan pengganti konsultasi langsung dengan pelatih kebugaran atau tenaga profesional.

---

# ⭐ MUSCLELOGIC

### 💪 Smart Recommendation for Beginner Muscle Building

**Built with Python • Django • SQLite • Forward Chaining**

⭐ **If you find this project interesting, consider giving the repository a Star!**
