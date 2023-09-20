

=======================================================================================================================================================================

# Tugas 3


[x] Membuat input form untuk menambahkan objek model pada app sebelumnya.

[x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

[x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

[x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.

 ## Apa perbedaan antara form POST dan form GET dalam Django?
      - GET biasanya digunakan untuk pengiriman data yang tidak sensitif, seperti query pencarian. 
      Sedangkan POST, biasanya digunakan untuk data yang membutuhkan keamanan tingkat tinggi, seperti username dan password.
      - GET mengirimkan data melalui URL lalu disimpan ke action, 
      sedangkan POST langsung mengirimkan data ke action untuk ditampung tanpa melalui URL
      - GET tidak boleh melebihi 2047 karakter, 
      sedangkan POST tidak tebatas
      - GET dapat meningkatkan efisiensi karena dapat dicache oleh server, 
      sedangkan POST memerlukan request baru


## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
      Dalam proses pengiriman data, JSON memiliki objek yang terdiri dari pasangan key-value di mana masing-masing objek memiliki key unik untuk mengakses value. 
      Sedangkan untuk HTML dan XML menggunakan konsep hierarki struktur pohon di mana elemen lain dapat membentuk elemen bersarang di dalam suatu elemen. 
      Antara HTML dan XML banyak menggunakan penandaan tag. Namun, perbedaan yang mencolok dari HTML dan XML terletak pada fungsionalitasnya. 
      HTML menampilkan data ke dalam bentuk konten (mengatur kerangka struktur web) dengan tujuan berbeda-beda, seperti img untuk menampilkan data dan tag a untuk mengalirkan ke suatu tautan. 
      Sedangkan XML, tag digunakan sebagai penandaan / identitas suatu nilai yang memiliki fungsi serupa dengan XML. 
      Walaupun HTML berfokus dalam pembuatan skeleton website, di HTML juga terdapat form yang dapat berperan sebagai pertukaran data.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
      JSON memiliki sintaks yang mudah dipahami dan sajian datanya memiliki kemiripan dengan bahasa yang serupa seperti Python, Java, dan Java Script. Salah satu hal yang serupa dilakukan di JSON adalah bisa melakukan penyimpanan struktur data yang kompleks menggunakan array. Dalam melakukan parsing, JSON tidak memiliki cara khusus karena hanya tinggal mengimplementasikan dari javascript. Efisiensi tinggi yang dimiliki JSON juga menajdi keunggulan. Dalam hal ini, JSON mengurangi beban jaringan saat transfer data dan klien karena tidak memerlukan ukuran file yang besar.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Migrate Ulang
   Saya melakukan migrasi ulang karena terdapat kesalahan no amount in list dengan menggunakan command di mana saat melakukan itu saya set angka 1 pada base value.
   ```bash
   py manage.py makemigrations
   py manage.py migrate
   ```
### Mengubah routing ke `/`
Di file `urls.py`, saya melakukan pengubahan routing dari `main/` menjadi `/`.

### Membuat folder base untuk kerangka HTML dan mengatur `settings.py`
Saya melakukan penambahan berkas `base.html` ke dalam direktori templates untuk membuat formatting kerangka HTML. Lalu, setelah itu saya mencoba mengatur berkas main.html mana saja yang perlu dihapus dari file tugas2 sebelumnya. Agar berkas base.html terdeteksi, saya menambahkan
```bash
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
       
    }
]
```
ke dalam file `settings.py`.

### Membuat Form Data Produk
Di file sebelumnya, saya melakukan input manual untuk data produk. Pada tugas ini, saya membuat berkas `forms.py` untuk menginisiasi data models yang ada di Product. Setelah itu saya menambahkan beberapa import di dalam `view.py`.
```bash
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```

### Terima request form
Agar form bisa diakses, perlu suatu parameter yang menerima submit dari form. Saya menginisiasi fungsi `create_product` agar bisa memvalidasi isi input dan menyimpannya.

### Ubah show_main
Karena produk-produk diinisiasi secara otomatis, saya mencoba menghapus key dari dict context. Lalu, untuk data produk yang diisi manual saya inisiasi kembali dengan membuat suatu objek yang dapat mengambil object Produk.

### Membuat akses add produk
Agar produk bisa ditambahkan secara iteratif, saya membuat file `create_product.html` dan mengedit `urls.py` untuk menambahkan import serta path.

### XML
Untuk menampilkan data dalam format XML, saya membuat sebuah fungsi di dalam file `views.py` yang terletak di dalam folder `main`. Fungsi ini diberi nama `show_xml` sesuai dengan tugas yang diberikan. Fungsi `show_xml` ini akan menerima parameter request dan akan mengambil semua data dari objek Product dan menyimpannya dalam sebuah variabel. Data ini akan diubah menjadi format XML menggunakan `serializers` dan akan dikirim kembali kepada pengguna dalam bentuk respons `HttpResponse`. Agar fungsi ini dapat berjalan dengan baik, kita perlu menambahkan impor `serializers` dan `HttpResponse` dari modul Django. Selanjutnya, untuk menampilkan data berdasarkan ID, kita akan membuat sebuah fungsi baru yang diberi nama `show_xml_by_id`. Fungsi ini akan memiliki fungsionalitas yang serupa dengan fungsi sebelumnya, tetapi dengan penambahan parameter id.

Setelah selesai membuat kedua fungsi tersebut, saya perlu mengimpor keduanya ke dalam file `urls.py` yang terletak di dalam folder `main`. Selanjutnya, tambahkan dua path yaitu `path('xml/', show_xml``, name='show_xml')` dan `path('xml/<int:id>/'``, show_xml_by_id, name='show_xml_by_id')` ke dalam daftar `urlpatterns`. Dengan demikian, kita akan dapat melihat data dalam bentuk XML melalui tautan `http://localhost:8000/xml` dan `http://localhost:8000/xml/[id]` untuk melihat hasilnya.

### JSON
   Dalam hal ini, saya menginginkan projek bisa diakses dalam format JSON. Oleh karena itu, hal yang saya lakukan adalah membuat fungsi yang menerima parameter `show_json_id`. Kemudian, di dalam file `urls.py` saya menambahkan path `path('json/', show_json, name='show_json'),` dan `path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),` ke dalam list `urlpatterns`. Kemudian, saya mengecek hasil melalui `http://localhost:8000/json` ataupun `http://localhost:8000/json/1`

[x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

![menu](menu.png)
![create-product](create-product.png)
![xml](xml.png)
![xml-1](xml-1.png)
![json](json.png)
![json-1](json-1.png)

[x] Melakukan add-commit-push ke GitHub.
   Sebelum push, saya mendapatkan masalah file bentrok di file head dan hal yang saya lakukan melakukan 
   ```bash
   git checkout main
   ```
   Lalu, melakukan merge dengan branch selain main.
   ```bash
   git merge task3
   ```
   Di terminal, saya melakukan tahap akhir yaitu mem-push semua perubahan.
   ```bash
   git add .
   git commit -m "pesan"
   git push -u origin main
   ```








=======================================================================================================================================================================

Tugas 2

https://task2inventory.adaptable.app

1. Langkah membuat proyek Inventori Alat dan Produk untuk Kucing:

A. Menuju ke terminal / cmd:
   - Melihat posisi direktori saat ini dengan command: `pwd`
   - Menuju tempat penyimpanan folder yang diinginkan berdasarkan posisi direktori dengan command: `cd`
   - Membuat direktori baru di dalam direktori tujuan dengan command: `mkdir task2_inventori`

B. Membuat/mengaktivasi virtual environment:
   - Aktivasi dilakukan untuk mengisolasi dependensi spesifik dengan versi paket Python yang sesuai.
   - Membuat VE dengan command: `python -m venv env` dan mengaktivasi dengan command: `env\Scripts\activate.bat`

C. Instalasi Django:
   - Melakukan instalasi dependencies dengan perintah `pip install -r requirements.txt`

D. Membuat proyek Django:
   - Proyek Django dibuat dengan perintah `django-admin startproject task2_inventori`

E. Menjalankan server pengembangan lokal:
   - Menambahkan perizinan akses ke semua dengan menginput `*` pada `ALLOWED_HOST` di `settings.py` dalam direktori proyek `task2_inventori`.
   - Perintah `python manage.py runserver` digunakan dalam kerangka kerja Django untuk menjalankan server pengembangan lokal.

F. Membuat aplikasi "main":
   - Perintah `python manage.py startapp main` dalam kerangka kerja Django digunakan untuk membuat sebuah "app" baru dalam proyek Django.

G. Merouting URL ke app "main":
   - Di direktori `task2_inventori`, dilakukan penambahan routing ke file `urls.py` sehingga proses yang direquest dari URL utama akan diteruskan ke "main".

H. Membuat model "Item":
   - Model "Item" didefinisikan dalam file `models.py` di aplikasi "main". Model ini mendefinisikan atribut seperti name, amount, description, dan price.

I. Mengatur logika aplikasi dengan membuat `views.py`:
   - Untuk mengatur logika aplikasi, dibuat fungsi "items" dalam file `views.py` di aplikasi "main". Fungsi ini akan mengambil data dari model "Item" dan merendernya ke dalam template HTML.

J. Membuat routing untuk fungsi:
   - Routing untuk fungsi yang telah dibuat di file `views.py` dalam `urls.py` dilakukan untuk mengatur cara HTTP mencapai fungsi yang sesuai di aplikasi "main" saat mengakses URL tertentu.

K. Membuat template implementasi HTML:
   - Dalam tahap implementasi HTML template, menciptakan template HTML di dalam direktori baru dalam aplikasi "main". Template ini berfungsi untuk mengelola tampilan halaman web yang akan ditampilkan kepada pengguna. Data yang diperoleh dari `views.py` akan dimasukkan ke dalam template ini.

L. Uji proyek Django dengan test:
   - Untuk menguji proyek Django, melakukan pengujian dengan membuat unit test dan `TestCase` menggunakan model-model dari proyek `task2_inventori`. Langkah ini bertujuan untuk menguji atribut-atribut yang ada dalam proyek.

M. Add, commit, hingga push ke repository:
   - Setelah berhasil melakukan pengujian, langkah selanjutnya adalah meng-add, meng-commit, dan meng-push proyek ke repositori GitHub "Library-Inventory". Sebelum melakukan pengunggahan, juga membuat file `.gitignore` untuk menentukan berkas dan direktori yang tidak perlu disertakan dalam repositori Git. Setelah itu, dilakukan tahap menambahkan (add), meng-commit, dan meng-push ke repositori GitHub.

N. Deploy ke Adaptable:
   - Selanjutnya, proyek di-deploy ke Adaptable setelah selesai dikembangkan secara lokal. Hal ini memungkinkan aplikasi dapat diakses secara online oleh orang lain melalui internet.

O. Menjawab pertanyaan dan mengumpulkan berkas pengumpulan:
   - Setelah seluruh tahap selesai, membuat file README.md yang berisi tautan ke aplikasi di Adaptable dan menjawab pertanyaan yang terkait dengan proyek aplikasi ini. Kemudian, kembali melakukan tahap menambahkan (add), meng-commit, dan meng-push file README.md ke repositori GitHub.

P. Menutup virtual environment:
   - Terakhir, setelah semua tahap selesai, melakukan perintah "deactivate" pada virtual environment karena sudah tidak lagi diperlukan.


2. Bagan request client yang berkaitan dengan urls.py, views.py, models.py, dan berkas lain.

        **Client's Web Browser**
                    |
                    v
        **Django Web Application**
                    |
                    v
    **urls.py** <-------->  **views.py**
        |                 |
        v                 v
    **models.py**   **items.html**

Penjelasan:
* Client's Web Browser: Sebuah permintaan dimulai dari web browser pengguna atau client saat mereka memasukkan URL atau mengklik tautan.
* Django Web Application: Permintaan tersebut kemudian diterima oleh aplikasi web berbasis Django, yang akan memprosesnya dan mengirimkan respons kembali ke client.
* urls.py: File urls.py bertanggung jawab untuk menentukan bagaimana permintaan URL akan diarahkan dan menghubungkan URL yang diterima dari client dengan fungsi tindakan yang sesuai di dalam views.py.
* views.py: Ketika permintaan URL diteruskan oleh urls.py, views.py mengambil alih untuk memproses permintaan tersebut. views.py dapat mengakses model untuk memproses data dan merender items.html atau mengembalikan respons JSON, tergantung pada kasus penggunaan.
* models.py: File models.py menggambarkan struktur data dalam aplikasi dan memberikan definisi model yang digunakan untuk berinteraksi dengan database atau data lainnya. models.py dapat digunakan oleh views.py untuk mengambil atau menyimpan data.
* items.html: items.html digunakan untuk mengatur tampilan yang akan diberikan kepada pengguna atau client. views.py dapat merender items.html dengan data yang diambil dari model dan kemudian mengirimkannya kembali ke client sebagai respons HTML yang siap ditampilkan.


3. Mengapa virtual environment penting dalam pengembangan python
Virtual environment (lingkungan virtual) adalah alat yang krusial dalam pengembangan Python yang diciptakan untuk mengisolasi dan mengelola dependensi serta paket Python untuk setiap proyek. Hal ini menyebabkan proyek tidak mengalami tumpang tindih / konflik dengan penggunaan package dan dependensi yang spesifik. Tanpa adanya virtual environment, pengelolaan terhadap versi versi python yang ada menjadi sulit serta pengisolasian dependensi proyek yang berbeda lebih rumit. 


4. MVVM, MVT, dan MVC

A. MVVM dan Kerangka Kerja JavaScript:
* MVVM adalah pola arsitektur yang umumnya digunakan dalam pengembangan aplikasi berbasis kerangka kerja JavaScript, seperti Angular, Vue.js, dan Knockout.js.
* MVVM sangat cocok untuk mengembangkan aplikasi berbasis klien (client-side) di mana tampilan (View) sering berinteraksi secara dinamis dengan data yang berubah (Model).
* Dalam MVVM, ViewModel berperan sebagai perantara antara Model (data) dan tampilan (UI). Ini memungkinkan tampilan untuk berinteraksi dengan data melalui ViewModel tanpa perlu tahu secara langsung tentang Model.
B. MVC/MVT dan Pengembangan Server-Side:
* MVC (Model-View-Controller) dan MVT (Model-View-Template) adalah pola arsitektur yang umumnya digunakan dalam pengembangan server-side, seperti dalam kerangka kerja web seperti Django (Python) dan Ruby on Rails (Ruby).
* MVC/MVT adalah pendekatan yang baik untuk mengatur kode server dan mengelola permintaan HTTP serta respons yang diberikan oleh server.
* Model digunakan untuk mengelola data dan interaksi dengan database, View atau Template digunakan untuk menghasilkan tampilan HTML, dan Controller digunakan untuk mengatur logika aplikasi.
C. Pemisahan Logika Tampilan:
* MVVM cenderung lebih memisahkan logika tampilan dari Model dibandingkan dengan MVC/MVT. Ini karena ViewModel mengambil tanggung jawab untuk mengelola logika presentasi, sehingga tampilan (View) hanya bertanggung jawab untuk menampilkan data yang diberikan oleh ViewModel.
* Dalam MVC/MVT, logika tampilan biasanya lebih dekat terkait dengan Model dan Controller/View yang bertindak sebagai perantara untuk mengambil data dari Model dan mengirimkannya ke tampilan (View/Template).
D. Tampilan Data-Binding:
* MVVM sering menggunakan teknik data-binding yang kuat, yang memungkinkan perubahan dalam Model secara otomatis diteruskan ke tampilan (View) tanpa perlu memperbarui tampilan secara manual.
* Dalam MVC/MVT, perubahan dalam Model biasanya memerlukan upaya tambahan untuk mengirim ulang data ke tampilan.
Kesimpulannya, MVVM adalah pola arsitektur yang lebih umumnya digunakan dalam pengembangan aplikasi berbasis kerangka kerja JavaScript dan memiliki pemisahan logika tampilan yang lebih ketat dari Model. Sementara itu, MVC/MVT adalah pendekatan yang umumnya digunakan dalam pengembangan server-side seperti Django, di mana tampilan, model, dan controller/templating berperan dalam mengelola komponen aplikasi secara terpusat. Pilihan antara keduanya akan bergantung pada konteks pengembangan dan teknologi yang digunakan.
https://docs.djangoproject.com/en/3.2/intro/tutorial01/#creating-the-poll-app
