# Statistical Audit of pandas-dev/pandas
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)

## Notebooks

| Notebook | Open in Colab |
|----------|--------------|
| 01_eda.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aqilfadria/stat-audit-pandas-sti-2025/blob/main/notebooks/01_eda.ipynb) |
| 02_estimation.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aqilfadria/stat-audit-pandas-sti-2025/blob/main/notebooks/02_estimation.ipynb) |
| 03_inference.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aqilfadria/stat-audit-pandas-sti-2025/blob/main/notebooks/03_inference.ipynb) |
| 04_hypothesis_testing.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aqilfadria/stat-audit-pandas-sti-2025/blob/main/notebooks/04_hypothesis_testing.ipynb) |

## Project Description

Project ini bertujuan untuk melakukan statistical audit pada repository open-source `pandas-dev/pandas` menggunakan data dari GitHub REST API.

Analisis dilakukan terhadap issue dan pull request untuk mempelajari aktivitas repository menggunakan metode statistik seperti estimation, hypothesis testing, dan simulation.

Project ini menggunakan Python, Jupyter Notebook, pandas, matplotlib, dan seaborn untuk proses data collection, cleaning, dan exploratory data analysis (EDA).


## Repository Analyzed

Repository yang digunakan dalam project ini adalah repository open-source `pandas-dev/pandas` di GitHub.

Repository URL:
https://github.com/pandas-dev/pandas

Repository ini dipilih karena memenuhi persyaratan project, yaitu memiliki:

* lebih dari 1.000 closed issues
* lebih dari 500 merged pull requests
* data aktivitas repository yang lengkap dan timestamped
* aktivitas kontribusi yang tinggi


## Team Members
| Member | Name                              | NIM        | Role                   |
|--------|-----------------------------------|------------|------------------------|
| A      | Ahmad Aqil Fadria                 | 1519625006 | Data Engineer          |
| B      | Nasya Putri Salsabila             | 1519625007 | Estimation Analyst     |
| C      | Muhammad Hanief Inayatur Rahman   | 1519625026 | Inference Analyst      |
| D      | Muhammad Rizqi Hazami             | 1519625064 | Hypothesis Analyst     |
| E      | Krishna Dhikha Pratama            | 1519625070 | Computation Analyst    |

## Research Questions

1. Berapa estimasi probabilitas sebuah pull request dapat di-merge pada repository pandas-dev/pandas?

2. Apakah rata-rata tingkat penyelesaian issue pada repository pandas-dev/pandas berubah secara signifikan dalam periode tertentu?

3. Berapa probabilitas sebuah issue membutuhkan waktu lebih dari 30 hari untuk ditutup berdasarkan pendekatan simulasi statistik?

## Struktur Repository


```
stat-audit-pandas-sti-2026/
│
├── data/
│   │
│   ├── raw/
│   │   ├── issues_raw.csv
│   │   └── pull_requests_raw.csv
│   │
│   └── clean/
│       ├── dataset.csv
│       └── pr_dataset.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_estimation.ipynb
│   ├── 03_inference.ipynb
│   ├── 04_hypothesis_testing.ipynb
│   └── 05_simulation.ipynb
│
├── src/
│   └── estimator.py
│
├── reports/
│   ├── final_report.pdf
│   └── presentation.pptx
│
├── README.md
├── AI_USAGE_LOG.md
├── requirements.txt
└── .gitignore
```
## Temuan Utama
diisi setalah selesai menganalisis semua

## Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/aqilfadria/stat-audit-pandas-sti-2025
cd stat-audit-pandas-sti-2026
```

### 2. Install Library yang Dibutuhkan

```bash
pip install -r requirements.txt
```

### 3. Jalankan Jupyter Notebook

```bash
jupyter notebook
```

### 4. Jalankan Notebook Secara Berurutan

Buka folder `notebooks/` kemudian jalankan notebook berikut secara berurutan:

1. `01_eda.ipynb`
2. `02_estimation.ipynb`
3. `03_inference.ipynb`
4. `04_hypothesis_testing.ipynb`
5. `05_simulation.ipynb`

Notebook harus dijalankan dari atas ke bawah agar proses analisis berjalan dengan benar.


## Sumber Data

### Repository

Data diambil dari repository open-source `pandas-dev/pandas` pada GitHub.

Repository URL:
https://github.com/pandas-dev/pandas

### Tanggal Pengambilan Data

Data dikumpulkan menggunakan GitHub REST API pada 25 Mei 2026.

### Endpoint API

Endpoint API yang digunakan dalam project ini:

* Issues API
  `https://api.github.com/repos/pandas-dev/pandas/issues`

* Pull Requests API
  `https://api.github.com/repos/pandas-dev/pandas/pulls`

### Keterbatasan Data

Beberapa keterbatasan pada dataset yang digunakan:

* GitHub API memiliki rate limit untuk jumlah request
* Endpoint issues juga mengandung data pull request sehingga perlu filtering
* Tidak semua aktivitas repository tersedia pada dataset
* Data dapat berubah seiring aktivitas repository yang terus berjalan
