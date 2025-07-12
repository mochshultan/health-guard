<div align="center">

# 🩺 Health Guardian: Prediksi Diabetes dengan Random Forest

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6.1-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

> **Aplikasi prediksi kadar gula darah berbasis AI yang dibangun dengan model Random Forest**

[🚀 Demo](#-demo) • [📋 Fitur](#-fitur-utama) • [🛠️ Instalasi](#️-instalasi) • [📊 Parameter](#-parameter-yang-digunakan) • [🔬 Model](#-detail-model)

---

</div>

## 📖 Tentang Proyek

Aplikasi ini memungkinkan pengguna untuk memprediksi kemungkinan seseorang terkena diabetes berdasarkan parameter kesehatan tertentu. Dikembangkan untuk keperluan latihan implementasi algoritma Machine Learning dengan fokus pada **Random Forest Classifier** yang telah dioptimasi.

### 🎯 Tujuan
- Memberikan prediksi diabetes yang akurat berdasarkan data klinis
- Menyediakan interface yang user-friendly untuk input parameter kesehatan
- Mendemonstrasikan implementasi Machine Learning dalam aplikasi web

---

## 🎨 Fitur Utama

### 🖥️ **Antarmuka Interaktif**
- ✨ Desain modern dan responsif dengan **TailwindCSS**
- 🎛️ Input parameter kesehatan dengan slider yang mudah digunakan
- ⚡ Tampilan real-time saat mengatur nilai
- 🧭 Navigasi yang smooth dan user-friendly
- 📱 Interface yang adaptif untuk semua perangkat

### 🤖 **Kemampuan AI**
- 🌳 Model **Random Forest** yang telah dilatih dan dioptimasi
- 📊 Prediksi dengan tingkat kepercayaan yang akurat
- ⚙️ Pemrosesan data yang efisien dengan preprocessing **SMOTE**
- 🎯 Model yang telah di-tune dengan parameter optimal
- 🔄 Real-time prediction dengan response cepat

### 📱 **Responsif & Modern**
- 📱 Dapat diakses di berbagai perangkat
- 🖥️ Tampilan optimal untuk desktop dan mobile
- 🎨 Interface yang adaptif dan modern
- ⚡ Performa yang cepat dan efisien

---

## 🛠️ Teknologi yang Digunakan

### 🔧 **Backend Stack**
| Teknologi | Versi | Keterangan |
|-----------|-------|------------|
| ![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python) | 3.9+ | Bahasa pemrograman utama |
| ![Flask](https://img.shields.io/badge/Flask-3.1.1-green?style=flat&logo=flask) | 3.1.1 | Web framework ringan |
| ![Flask-CORS](https://img.shields.io/badge/Flask--CORS-6.0.1-lightgrey?style=flat) | 6.0.1 | Cross-origin resource sharing |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6.1-orange?style=flat&logo=scikit-learn) | 1.6.1 | Machine Learning library |
| ![Pandas](https://img.shields.io/badge/Pandas-2.3.0-darkblue?style=flat&logo=pandas) | 2.3.0 | Pengolahan data |
| ![NumPy](https://img.shields.io/badge/NumPy-2.3.1-blue?style=flat&logo=numpy) | 2.3.1 | Komputasi numerik |
| ![Joblib](https://img.shields.io/badge/Joblib-1.5.1-orange?style=flat) | 1.5.1 | Penyimpanan model |
| ![Imbalanced-learn](https://img.shields.io/badge/Imbalanced--learn-0.8+-green?style=flat) | 0.8+ | Penanganan data tidak seimbang |
| ![KaggleHub](https://img.shields.io/badge/KaggleHub-0.3.12-purple?style=flat) | 0.3.12 | Dataset download |

### 🎨 **Frontend Stack**
| Teknologi | Keterangan |
|-----------|------------|
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) | Struktur dan markup |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) | Styling dan layout |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) | Interaktivitas |
| ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white) | CSS framework |
| ![FontAwesome](https://img.shields.io/badge/Font_Awesome-339AF0?style=flat&logo=fontawesome&logoColor=white) | Icon library |
| ![Poppins](https://img.shields.io/badge/Poppins-Google_Fonts-4285F4?style=flat&logo=google-fonts&logoColor=white) | Typography |

### 🛠️ **Development Tools**
| Tool | Keterangan |
|------|------------|
| ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) | Version control |
| ![Pip](https://img.shields.io/badge/Pip-3776AB?style=flat&logo=python&logoColor=white) | Package manager |
| ![Virtual Environment](https://img.shields.io/badge/Virtual_Environment-3776AB?style=flat&logo=python&logoColor=white) | Dependency isolation |

---

## 🚀 Instalasi

### 📋 **Prerequisites**
- Python 3.9 atau lebih tinggi
- Git
- Web browser modern

### 🔧 **Langkah Instalasi**

#### 1️⃣ **Clone Repository**
```bash
git clone [URL_REPOSITORI_ANDA]
cd PROJECT-AI-RF
```

#### 2️⃣ **Setup Virtual Environment**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

#### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

#### 4️⃣ **Run Application**
```bash
python backend.py
```

> 🌐 **Aplikasi akan otomatis terbuka di browser default Anda di `http://localhost:5000`**

---

## 🎮 Cara Menggunakan

### 📝 **Langkah-langkah Prediksi**

1. **📋 Input Parameter Kesehatan**
   - 👤 Pilih gender (Female/Male)
   - 🎂 Masukkan usia dalam tahun
   - 🩺 Input nilai-nilai parameter klinis lainnya
   
2. **🔮 Klik Tombol Prediksi**
   - Klik tombol "Prediksi" untuk melihat hasil
   
3. **📊 Lihat Hasil**
   - Status (Positif/Negatif Diabetes)
   - Tingkat kepercayaan prediksi
   - Rekomendasi berdasarkan hasil

### ⚠️ **Catatan Penting**
- Pastikan semua nilai parameter diisi dengan benar
- Nilai harus dalam rentang yang wajar untuk hasil yang akurat
- Hasil prediksi hanya sebagai referensi, bukan diagnosis medis

---

## 📊 Parameter yang Digunakan

Model ini menggunakan **10 parameter klinis** berikut untuk melakukan prediksi risiko diabetes:

| No | Parameter | Keterangan | Satuan | Rentang Normal |
|----|-----------|------------|--------|----------------|
| 1️⃣ | **Gender** | Jenis kelamin | - | 0: Wanita, 1: Pria |
| 2️⃣ | **AGE** | Usia | Tahun | 18-80 |
| 3️⃣ | **Urea** | Kadar urea dalam darah | mg/dL | 7-20 |
| 4️⃣ | **Cr** | Kadar kreatinin dalam darah | mg/dL | 0.6-1.2 |
| 5️⃣ | **HbA1c** | Rata-rata kadar glukosa darah | % | <5.7 |
| 6️⃣ | **Chol** | Kadar kolesterol total | mg/dL | <200 |
| 7️⃣ | **TG** | Kadar trigliserida | mg/dL | <150 |
| 8️⃣ | **LDL** | Low-Density Lipoprotein | mg/dL | <100 |
| 9️⃣ | **VLDL** | Very Low-Density Lipoprotein | mg/dL | <30 |
| 🔟 | **BMI** | Body Mass Index | kg/m² | 18.5-24.9 |

---

## 📂 Struktur Proyek

```
PROJECT-AI-RF/
├── 📁 asets/                    # Aset visualisasi dan dokumentasi
│   ├── 📊 class_dis_balanced.png
│   ├── 📊 class_dis_with_no-noise.png
│   ├── 📊 class_dis_with_noise.png
│   ├── 📄 clear_dataset_tabel.pdf
│   ├── 📊 confuss_matrix_after_smote_after_optimiz.png
│   ├── 📊 confuss_matrix_after_smote.png
│   ├── 📊 confuss_matrix_before_smote.png
│   ├── 📊 corr_matrix.png
│   ├── 📊 feature_importance.png
│   ├── 🌳 tree_sample_number99.png
│   └── 📋 workflow.jpg
├── 📁 models/                   # Model dan dataset
│   ├── 📊 Dataset of Diabetes (ASLI).csv
│   ├── 🔧 get_model.py         # Script training model
│   ├── 📈 min_max.csv          # Nilai min-max untuk normalisasi
│   ├── 🤖 random_forest_model_tuned_params.joblib
│   └── 📊 resampled_data.csv
├── 📁 templates/                # Template HTML
│   └── 🌐 index.html           # Halaman antarmuka pengguna (frontend)
├── 🐍 backend.py               # Aplikasi Flask sebagai backend
├── 📋 requirements.txt         # Daftar dependensi Python
└── 📖 README.md                # Dokumentasi proyek
```

---

## 🔬 Detail Model

### 🔄 **Preprocessing Data**
- **🔄 SMOTE (Synthetic Minority Over-sampling Technique)** - Menangani data tidak seimbang
- **🏷️ Label Encoding** - Konversi variabel kategorikal
- **🧹 Data Cleaning** - Menghilangkan duplikat dan data tidak valid
- **📊 Feature Scaling** - Normalisasi data untuk performa optimal

### ⚙️ **Parameter Model Random Forest**
| Parameter | Nilai | Keterangan |
|-----------|-------|------------|
| **n_estimators** | 100 | Jumlah pohon dalam forest |
| **criterion** | 'gini' | Fungsi untuk mengukur kualitas split |
| **max_depth** | 9 | Kedalaman maksimum pohon |
| **max_features** | 10 | Jumlah fitur maksimum untuk split |
| **min_samples_split** | 4 | Minimum sampel untuk split node |
| **min_samples_leaf** | 2 | Minimum sampel di leaf node |
| **random_state** | 42 | Seed untuk reproducibility |

### 📈 **Performa Model**
- ✅ **Akurasi Tinggi** - Model telah dioptimasi untuk performa maksimal
- ⚡ **Prediksi Cepat** - Response time yang minimal
- 🎯 **Konsistensi** - Hasil yang stabil dan dapat diandalkan
- 📊 **Validasi** - Telah divalidasi dengan berbagai metrik

---

## 📝 Catatan Penting

### ⚠️ **Peringatan**
- Pastikan semua dependensi terinstall dengan benar
- Aplikasi ini menggunakan model yang sudah dilatih sebelumnya dari dataset diabetes
- **Hasil prediksi hanya sebagai referensi, bukan diagnosis medis yang definitif**
- Konsultasikan dengan tenaga medis profesional untuk diagnosis yang akurat

### 📋 **Informasi Teknis**
- Dataset asli disimpan sebagai "Dataset of Diabetes (ASLI).csv"
- Model dapat dilatih ulang menggunakan script `get_model.py` jika diperlukan
- Aplikasi berjalan di port 5000 secara default
- Semua visualisasi dan analisis tersimpan di folder `asets/`

### 🔧 **Pengembangan Lanjutan**
- Model dapat ditingkatkan dengan dataset yang lebih besar
- Implementasi model lain (SVM, Neural Network, dll.)
- Penambahan fitur export hasil prediksi
- Integrasi dengan sistem kesehatan yang ada

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

## 🧑‍💻 Pengembang

<div align="center">

### **Moch. Shultan Ali Saifuddin**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mochshultan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/mochshultan)

**Dikembangkan dengan ❤️ untuk mata kuliah Kecerdasan Buatan**

---

### 🌟 **Star History**

[![Star History Chart](https://api.star-history.com/svg?repos=mochshultan/PROJECT-AI-RF&type=Date)](https://star-history.com/#mochshultan/PROJECT-AI-RF&Date)

---

<div align="center">

**Jika proyek ini membantu Anda, berikan ⭐ star di repository ini!**

[![GitHub stars](https://img.shields.io/github/stars/mochshultan/PROJECT-AI-RF?style=social)](https://github.com/mochshultan/PROJECT-AI-RF)
[![GitHub forks](https://img.shields.io/github/forks/mochshultan/PROJECT-AI-RF?style=social)](https://github.com/mochshultan/PROJECT-AI-RF)
[![GitHub issues](https://img.shields.io/github/issues/mochshultan/PROJECT-AI-RF)](https://github.com/mochshultan/PROJECT-AI-RF/issues)

</div>
