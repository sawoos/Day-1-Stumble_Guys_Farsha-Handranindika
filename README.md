# Day-1-Stumble-Guys_Farsha-Handranindika

- **Nama Lengkap:** Farsha Handranindika
- **Kelompok:** Stumble Guys

# Deskripsi
Repository ini dibuat untuk memenuhi penugasan Day-1 workshop dengan topik pengembangan perangkat lunak menggunakan bantuan AI dan manajemen versi menggunakan Git serta GitHub.

## Tujuan Repository
- Menyimpan dan mendokumentasikan seluruh hasil latihan, catatan, serta file proyek yang dikerjakan selama workshop.
- Mempraktikkan manajemen perubahan kode (*version control*) menggunakan Git dan GitHub.

## Informasi Kegiatan Workshop
- **Judul Kegiatan:** Building with AI, Managing Change with GitHub
- **Pembicara/Mentor:** Nugi Farhan
- **Ringkasan Singkat:** Workshop ini membahas cara merancang instruksi (*prompt engineering*) yang efektif untuk AI serta dasar-dasar pengelolaan repositori menggunakan Git dan GitHub.


## Dokumentasi Kegiatan Workshop

### 1. Materi atau Topik yang Disampaikan
Workshop hari pertama ini berjudul **"Building with AI, Managing Change with GitHub"** yang dibawakan oleh **Nugi Farhan**. Fokus materi terbagi menjadi dua bagian utama:
* **Prompt Engineering:** Cara merancang instruksi yang efektif agar AI memberikan jawaban yang tepat, relevan, dan terstruktur.
* **Git & GitHub:** Pengenalan sistem kontrol versi (*version control*) lokal menggunakan Git serta kolaborasi berbasis web menggunakan GitHub.

### 2. Catatan & Rangkuman Materi Workshop

#### A. Prompt Engineering
* **Definisi:** Prompt adalah instruksi atau masukan yang diberikan kepada model AI untuk mendapatkan hasil tertentu.
* **Context is Key:** Pemberian konteks yang jelas sangat memengaruhi hasil output AI. Perbandingan tanpa konteks vs dengan konteks sangat menentukan kualitas respons.
* **Struktur Prompt yang Baik:** Menggunakan elemen **Role** (peran AI), **Task** (tugas utama), **Context** (latar belakang/kebutuhan), dan **Format** (bentuk keluaran yang diinginkan).
* **Keuntungan:** Meningkatkan performa model AI, mengurangi bias, serta memberikan kontrol dan prediktabilitas yang lebih baik.

#### B. Git & GitHub
* **Git vs GitHub:**
  * **Git:** Sistem *version control* terdistribusi (DVCS) untuk melacak perubahan kode secara lokal.
  * **GitHub:** Platform berbasis web untuk menyimpan repositori Git secara online dan mendukung kolaborasi tim.
* **Git Workflow (Alur Kerja Git):**
  1. *Working Directory:* Salinan proyek yang sedang dikerjakan di komputer.
  2. *Staging Area:* Area sementara untuk menampung perubahan file sebelum di-*commit*.
  3. *Git Directory (Repository):* Tempat penyimpanan metadata dan basis data riwayat proyek.
* **Perintah Dasar Git (*Essential Commands*):**
  * `git init` : Memulai repositori baru.
  * `git add .` / `git add --all` : Memindahkan file ke *staging area*.
  * `git commit -m "pesan"` : Menyimpan perubahan ke repositori lokal.
  * `git remote add <name> <url>` : Menghubungkan repositori lokal ke remote.
  * `git push origin main` : Mengunggah perubahan dari lokal ke GitHub.
  * `git pull origin main` : Mengambil dan menggabungkan perubahan dari GitHub ke lokal.

---

### 3. Poin-Poin Penting & Pengetahuan Baru
* Menyusun *prompt* dengan struktur yang jelas (**Role, Task, Context, Format**) menghasilkan kode atau teks yang jauh lebih akurat dan minim revisi.
* Pentingnya memahami perbedaan fungsi antara Git (pengelolaan versi lokal) dan GitHub (penyimpanan cloud & kolaborasi).
* Praktik langsung membuat proyek sederhana (*Student Task Planner*) menggunakan bantuan AI, lalu menerapkannya ke dalam *version control* Git dan mengunggahnya ke GitHub.
