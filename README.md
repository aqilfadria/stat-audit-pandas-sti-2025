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
| 05_simulation.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aqilfadria/stat-audit-pandas-sti-2026/blob/main/notebooks/05_simulation.ipynb) |

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
1. Probabilitas Pull Request Berhasil Di-merge
Berdasarkan Bernoulli Maximum Likelihood Estimation (MLE), probabilitas sebuah pull request berhasil di-merge pada repository pandas-dev/pandas diperkirakan sebesar 65,86%. Dari 5.000 pull request yang dianalisis, sebanyak 3.293 berhasil di-merge dan 1.707 tidak di-merge. Hasil ini menunjukkan bahwa mayoritas kontribusi yang diajukan memiliki peluang yang cukup tinggi untuk diterima oleh maintainer repository.

2. Confidence Interval Probabilitas Merge
Analisis confidence interval menunjukkan bahwa probabilitas merge pull request berada pada rentang 64,53% hingga 67,16% dengan tingkat kepercayaan 95%. Rentang yang relatif sempit ini menunjukkan bahwa estimasi probabilitas merge cukup stabil dan memiliki tingkat ketidakpastian yang rendah.

3. Aktivitas Diskusi pada Issue
Analisis menggunakan distribusi Poisson menghasilkan estimasi rata-rata 2,38 komentar per issue. Temuan ini menunjukkan bahwa issue pada repository pandas-dev/pandas umumnya melibatkan diskusi aktif antara kontributor dan maintainer sebelum diselesaikan.

4. Waktu Penyelesaian Issue Mengalami Perubahan Signifikan
Hasil uji Mann-Whitney U menghasilkan U = 2.763.969,50 dengan p-value < 0,05, sehingga hipotesis nol ditolak. Hasil ini menunjukkan bahwa terdapat perbedaan yang signifikan pada waktu penyelesaian issue antara tahun 2025 dan 2026. Hasil tersebut juga dikonfirmasi oleh Welch's t-test dengan t = 14,97 dan p-value < 0,05.

5. Peningkatan Responsivitas Pengelolaan Issue
Rata-rata waktu penyelesaian issue menurun dari 27,6 hari pada tahun 2025 menjadi 8,3 hari pada tahun 2026, atau berkurang sekitar 19,3 hari. Nilai Cohen's d = 0,4257 menunjukkan bahwa perbedaan ini memiliki dampak praktis yang tergolong sedang (medium effect size). Temuan ini mengindikasikan peningkatan responsivitas tim pemelihara repository dalam menangani issue.

6. Probabilitas Issue Membutuhkan Lebih dari 30 Hari
Melalui simulasi Monte Carlo sebanyak 50.000 percobaan, diperoleh estimasi probabilitas sebesar 16,42% bahwa sebuah issue membutuhkan waktu lebih dari 30 hari untuk ditutup. Dengan kata lain, sebagian besar issue dapat diselesaikan dalam waktu kurang dari 30 hari, namun masih terdapat sebagian issue yang memerlukan waktu penanganan lebih lama karena tingkat kompleksitas yang lebih tinggi.

7. Kondisi Repository Secara Keseluruhan
Secara keseluruhan, repository pandas-dev/pandas menunjukkan kondisi yang sehat dan aktif. Tingkat keberhasilan merge pull request yang cukup tinggi, aktivitas diskusi issue yang konsisten, penurunan signifikan waktu penyelesaian issue, serta probabilitas rendah terhadap issue yang berlarut-larut menunjukkan bahwa proses pengelolaan kontribusi dan pemeliharaan proyek berjalan dengan baik.

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
