# Sistem Analisis Data Siswa

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.24-orange?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Deskripsi Proyek

Sistem Analisis Data Siswa adalah aplikasi berbasis **Python dan Streamlit** untuk memudahkan analisis data siswa sekolah.
Aplikasi ini memungkinkan pengguna untuk:

* Mengunggah file Excel data siswa.
* Menampilkan tabel data siswa.
* Menyediakan ringkasan statistik (total siswa, jumlah laki-laki dan perempuan).
* Analisis jumlah siswa per tahun ajaran.
* Grafik interaktif menggunakan Plotly (bar, line, dan pie chart).
* Kesimpulan otomatis berdasarkan data.
* Menyediakan download hasil analisis dalam format Excel.

Aplikasi ini cocok digunakan oleh guru, staf administrasi, atau pihak sekolah yang ingin menganalisis data siswa dengan cepat dan visual.

---

## 🎯 Fitur Utama

* Upload file Excel siswa (`.xlsx`)
* Ringkasan statistik jumlah siswa
* Analisis per tahun ajaran
* Analisis distribusi gender
* Visualisasi interaktif:

  * Bar chart (jumlah siswa per tahun)
  * Line chart (kenaikan jumlah siswa)
  * Pie chart (perbandingan laki-laki dan perempuan)
* Kesimpulan otomatis dengan tab
* Download hasil analisis (Excel)

---

## 💻 Instalasi & Konfigurasi

### 1. Clone Repository

```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

### 2. Buat Virtual Environment (Opsional tapi direkomendasikan)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / MacOS
source venv/bin/activate
```

### 3. Install Dependency

```bash
pip install -r requirements.txt
```

> Jika belum ada `requirements.txt`, buat file ini dengan isi:

```
streamlit
pandas
plotly
openpyxl
```

### 4. Jalankan Aplikasi

```bash
streamlit run app.py
```

Ganti `app.py` dengan nama file utama Python kamu jika berbeda.

---

## 📝 Cara Menggunakan

1. Buka aplikasi melalui browser setelah `streamlit run app.py`.
2. Upload file Excel data siswa.
3. Lihat ringkasan statistik dan tabel data.
4. Analisis grafik otomatis akan muncul.
5. Gunakan tab kesimpulan untuk melihat insight data.
6. Download hasil analisis dalam format Excel jika diperlukan.

---

## 📂 Struktur Proyek

```
├─ app.py                # File utama Streamlit
├─ requirements.txt      # Dependency Python
├─ data/                 # Opsional: Folder untuk menyimpan data Excel
└─ README.md
```

---

## 🛠 Kontribusi

Kontribusi sangat welcome! Silakan fork repository dan buat pull request.
Pastikan mengikuti format kode dan menambahkan penjelasan fitur baru jika ada.

---

## 📄 License

Proyek ini menggunakan lisensi **MIT License**.

---

## 📬 Kontak

* Email: [your.email@example.com](mailto:your.email@example.com)
* LinkedIn: [linkedin.com/in/username](https://linkedin.com/in/username)
* GitHub: [github.com/username](https://github.com/username)
