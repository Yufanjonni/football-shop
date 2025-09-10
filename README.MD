1.  -membuat direktori tempat file project django disimpan dan buka command promp
    -membuat dan menyalakan virtual environment yang berguna untuk package dan dependency agar tidak bertabrakan dengan versi lain
    -menginstal dependencies yang digunakan
    -membuat proyek dengan command 'django-admin startproject <nama_project> .'
    -konfigurasi environment dan proyek
    -menambahkan host yang dapat mengakses server
    -membuat aplikasi baru dengan menggunakan command python manage.py startapp <nama_aplikasi>
    -menambahkan aplikasi kedalam 'INSTALLED_APPS' didalam settings.py direktori project untuk medaftarkan aplikasi
    -membuka models.py dalam direktori aplikasi main untuk mendefinisikan mode dalam hal ini membuat class product beserta dengan atribut dan functionnya
    -migrasikan model ke database lokal
    -membuat fungsi didalam views.py yeng berisi nama aplikasi, nama, npm, dan kelas 
    -membuat direktori templates didalam direktori main dan membuat file html didalam templates tersebut
    -mengisi file html dengan apa yang ingin ditampilkan
    -membuat berkas urls.py didalam direktori main
    -membuat routing url pada aplikasi main
    -mengonfigurasi url projek
    -menambahkan url main kedalam url project
    -membuat test case untuk tes models.py
    -membuat projek pada pws dan push ke pws


2.  ![Alt Text](bagan.png)
    urls.py = memetakan URL path ke fungsi kelas view
    views.py = menerima request, berinteraksi dengan modls.py, dan mengembalikan respon
    models.py = definisi kelas model yang disimpan di database
    html = menampilkan context dari views.py dan menampilkannya ke browser client

3.  setting.py adalah pusat kontrol Django yang mengatur keamanan, aplikasi yang terinstal, Middleware, Host, database, dan zona waktu

4.  cara kerja migrasi
    - gunakan command 'python manage.py makemigrations'
    maka django akan membandingkan model dengan history migrasi dan membuat file migrasi
    -lanjutkan dengan command 'python manage.py migrate'
    Django akan menjalankan migrasi dan memasukkan model kedalam database

5.  -framework django menggunakan bahasa python yang merupakan high level language programing yang mendekati bahasa manusia sehingga lebih mudah dipahami
    -framework django memiliki struktur yang teratur membantu programmer pemula dalam memahami framework
    -framework django juga memiliki keamanan tinggi dan cepat
    -framework django dapat di projek kecil dan besar sehingga lebih fleksibel
    -framework django gratis dan open source