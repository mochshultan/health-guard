# Kadar : Kalkulasi Akurat Diabetes dengan Random Forest

Aplikasi prediksi kadar gula darah berbasis AI yang dibangun dengan model Random Forest. Aplikasi ini memungkinkan pengguna untuk memprediksi kemungkinan seseorang terkena diabetes berdasarkan parameter kesehatan tertentu. Dikembangkan untuk keperluan latihan implementasi algoritma Machine Learning.

## 🎯 Fitur Utama

- 🎨 **Antarmuka Interaktif**
  - Desain modern dan responsif
  - Input parameter kesehatan dengan slider yang mudah digunakan
  - Tampilan real-time saat mengatur nilai

- 🤖 **Kemampuan AI**
  - Model Random Forest yang telah dilatih
  - Prediksi dengan tingkat kepercayaan
  - Pemrosesan data yang efisien

- 📱 **Responsif**
  - Dapat diakses di berbagai perangkat
  - Tampilan optimal untuk desktop dan mobile

## 🛠️ Teknologi yang Digunakan

### Backend
- **Python 3.9+** - Bahasa pemrograman utama
- **Flask** - Web framework ringan
- **Scikit-learn** - Untuk model Machine Learning
- **Pandas** - Pengolahan data
- **Joblib** - Penyimpanan model

### Frontend
- **HTML5 & CSS3** - Struktur dan gaya
- **JavaScript Vanilla** - Interaktivitas
- **TailwindCSS** - Kerangka kerja CSS
- **FontAwesome** - Pustaka ikon

### Pengembangan
- **Git** - Version control
- **Pip** - Manajemen package Python
- **Virtual Environment** - Isolasi dependensi

## 🛠️ Instalasi

1. Clone repositori ini:
   ```bash
   git clone [github.com/mochshultan/health-guardian.git]
   cd <health-guard>
   ```

2. Buat dan aktifkan virtual environment (disarankan):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # MacOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r code/requirements.txt
   ```

4. Jalankan aplikasi:
   ```bash
   python backend.py
   ```
   Aplikasi akan otomatis terbuka di browser default Anda.

## 🎮 Cara Menggunakan

1. Masukkan parameter kesehatan yang diminta:
   - Arrow up/down untuk mengatur nilai
   - Atau ketik langsung nilai yang diinginkan
   
2. Klik tombol "Prediksi" untuk melihat hasil

3. Hasil prediksi akan menampilkan:
   - Status (Positif/Negatif Diabetes)
   - Tingkat kepercayaan prediksi
   - Rekomendasi

## 📊 Parameter yang Digunakan

Model ini menggunakan 10 parameter klinis berikut untuk melakukan prediksi risiko diabetes:

1.  **Gender**: Jenis kelamin (0: Wanita, 1: Pria)
2.  **AGE**: Usia dalam tahun
3.  **Urea**: Kadar urea dalam darah (mg/dL)
4.  **Cr**: Kadar kreatinin dalam darah (mg/dL)
5.  **HbA1c**: Rata-rata kadar glukosa darah (%)
6.  **Chol**: Kadar kolesterol total (mg/dL)
7.  **TG**: Kadar trigliserida (mg/dL)
8.  **LDL**: Kadar *Low-Density Lipoprotein* (kolesterol jahat) (mg/dL)
9.  **VLDL**: Kadar *Very Low-Density Lipoprotein* (mg/dL)
10. **BMI**: *Body Mass Index* (Indeks Massa Tubuh) (kg/m²)

## 📂 Struktur Proyek

```
nama-proyek/
├── models/           # Berisi model, dataset, dan script training
│   ├── random_forest_model_tuned_params.joblib
│   └── get_model.py
├── backend.py        # Aplikasi Flask sebagai backend
├── index.html        # Halaman antarmuka pengguna (frontend)
├── requirements.txt  # Daftar dependensi Python
└── README.md         # Dokumentasi proyek
```

## 📝 Catatan

- Pastikan semua dependensi terinstall dengan benar.
- Aplikasi ini menggunakan model yang sudah dilatih sebelumnya dari dataset Kaggle.
- Untuk pengembangan lebih lanjut, model bisa dilatih ulang dengan dataset yang lebih besar.

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

## 🧑‍💻 Pengembang

- **Moch. Shultan Ali Saifuddin** - [github.com/mochshultan](https://github.com/mochshultan)

---
Dikembangkan dengan ❤️ untuk mata kuliah Kecerdasan Buatan