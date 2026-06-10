# AI USAGE LOG - pandas-dev/pandas Statistical Audit

## Ringkasan

| Member                          | Peran               | Tools   | ~% Kode AI-assisted | Interpretation AI-assisted? |
| ------------------------------- | ------------------- | -----   | ------------------- | --------------------------- |
| Ahmad Aqil Fadria               | Data Engineer       | ChatGPT |          55%        |              No             |
| Nasya Putri Salsabila           | Estimation Analyst  | Claude  |          50%        |              No             |
| Muhammad Hanief Inayatur Rahman | Inference Analyst   |         |                     |                             |
| Muhammad Rizqi Hazami           | Hypothesis Analyst  | ChatGPT |          55%        |              No             |
| Krishna Dhikha Pratama          | Computation Analyst |Perplexity         |          75%           |              No               |


## Member A - Ahmad Aqil Fadria - Data Engineer

| No | Tugas                          | Alat AI | Prompt Singkat                                                | Cara Output Digunakan                                      |
| -- | ------------------------------ | ------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| 1  | Setup repository GitHub        | ChatGPT | Cara membuat struktur repository proyek statistical audit     | Digunakan sebagai panduan membuat struktur folder dan file |
| 2  | Data cleaning issue dataset    | ChatGPT | Membuat proses cleaning issue dataset dan feature engineering | Digunakan sebagai dasar preprocessing data                 |
| 3  | Debugging error Git dan Python | ChatGPT | Mengatasi error Git, pip, dan notebook                        | Digunakan sebagai panduan troubleshooting                  |

## Member B - Nasya Putri Salsabila - Estimation Analyst

| No | Tugas | Alat AI | Prompt Singkat | Cara Output Digunakan |
|----|-------|---------|----------------|----------------------|
| 1 | Scaffold estimator.py dan struktur notebook | Claude | Scaffold MLE functions per Tsun 2020 for pandas-dev/pandas audit | Digunakan sebagai kerangka awal, diverifikasi dan disesuaikan dengan kolom output Role A |
| 2 | Penyesuaian fungsi MLE dengan dataset | Claude | Sesuaikan fungsi mle_bernoulli dengan kolom merged di pr_dataset.csv | Digunakan sebagai referensi, dimodifikasi sesuai kebutuhan analisis |
| 3 | Debugging import error src.estimator | Claude | Cara mengatasi ModuleNotFoundError src.estimator di Jupyter notebook | Digunakan sebagai panduan troubleshooting path Python |

---

## Member C - Muhammad Hanief Inayatur Rahman - Inference Analyst

| No | Tugas | Alat AI | Prompt Singkat | Cara Output Digunakan |
| -- | ----- | ------- | -------------- | --------------------- |
| 1  | Struktur & implementasi notebook 03_inference (CI Wald, Wilson, Poisson, Credible Interval)| Claude  |Bantu saya jelaskan apa itutugas Inference Analyst dan cara implementasi kode cell ke VSCode|Digunakan sebagai dasar notebook, lalu dipahami & disesuaikan dengan struktur project|
| 2  |Penjelasan konsep & rumus CI Frequentist vs Bayesian Credible Interval| Claude  |elaskan line per line untuk kodeserta rumus - rumusnya|Digunakan untuk memahami teori, ditulis ulang dengan pemahaman sendiri|
| 3  |Debugging error import src/inference.py & path di VSCode | Claude  |requirements tidak ketemu / error import                | Diterapkan untuk memperbaiki environment di laptop|

---

## Member D - Muhammad Rizqi Hazami - Hypothesis Analyst

| No | Tugas | Alat AI | Prompt Singkat | Cara Output Digunakan |
| -- | ----- | ------- | -------------- | --------------------- |
| 1  |Menentukan metode inferensi statistik yang sesuai untuk data proyek|ChatGPT|Metode inferensi statistik apa yang cocok untuk membandingkan dua kelompok data?|digunakan sebagai referensi untuk memilih uji statistik|
| 2  |Menjelaskan interpretasi hasil uji hipotesi|ChatGPT| Jelasin cara baca p value dan keputusan H0 pada uji hipotesis|digunakan untuk menyusun interpretasi hasil pada laporan dan presentasi|
| 3  |Membantu menyusun narasi kesimpulan analisis inferensi|ChatGPT| contoh kesimpulan analisis inferensi statistik | referensi penulisan bagian kesimpulan, kemudian disesuaikan dengan hasil analisis proyek|

---

## Member E - Krishna Dhikha Pratama - Computation Analyst

| No | Tugas | Alat AI | Prompt Singkat | Cara Output Digunakan |
| -- | ----- | ------- | -------------- | --------------------- |
| 1  |Memberikan overview materi tentang Monte Carlo simulation, Bloom Filter dan MCMC       |Perplexity         |Boleh tolong jabarkan materi tentang....                |Digunakan untuk memahami materi tugas yang dikerjakan secara teori                       |
| 2  |Struktur Module dan Notebook Simulation       |Perplexity         |Dari hasil yang sudah dikerjakan teman kelompok saya, bantu untuk jelaskan serta step by step...                |Digunakan untuk menyusun isi dan interpretasi di folder src dan notebook                       |
| 3  |Membuat grafik berdasarkan hasil yang sudah dibuat di notebook       |Perplexity         |Apakah dari hasil kode dan interpretasinya diatas ada yang bisa ditampilkan dalam bentuk grafik?                |Output digunakan untuk menampilkan grafik sebagai penunjang visual dari isi notebook                       |


# Group Reflection
Proyek Statistical Audit terhadap repository pandas-dev/pandas memberikan pengalaman dalam menerapkan konsep statistik pada data nyata GitHub, mulai dari parameter estimation, confidence interval, hypothesis testing, hingga Monte Carlo simulation. Selain meningkatkan pemahaman tentang analisis data dan penggunaan Python, proyek ini juga mengajarkan pentingnya kolaborasi tim, pengelolaan repository dengan Git/GitHub, serta bagaimana data issue dan pull request dapat digunakan untuk mengevaluasi kesehatan dan aktivitas sebuah proyek open-source.
