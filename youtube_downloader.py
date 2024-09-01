from pytubefix import YouTube
from function import time

# Header Aplikasi
print('\n')
print('Youtube Downloader V.001')
print('--Code by whiter0se---\n')
url = input('Masukkan URL Youtube : ')

try:
    yt = YouTube(url)
    judul = yt.title
    penonton = yt.views
    durasi = yt.length
    waktu = time.convert_durasi(durasi)

    # Tampilan Informasi Video
    print('\n-- Informasi--')
    print("Judul           : %s" %judul)
    print("Jumlah Penonton : %s viewers" %penonton)
    print(f"Durasi          : {waktu} jam\n")

    #memilih stream untuk diunduh
    cek = yt.streams.filter(file_extension='mp4')
    for i in cek:
        print(i)

    # apakah akan mendownload video?
    data = input("Apakah kamu akan mendownload video (y/n)? ").lower()
    if data == 'y':
        tag = input("Masukkan itag : ")
        unduh = yt.streams.get_by_itag(tag)
        unduh.download()
    else :
        print("--Whiter0se--")

except Exception as e:
    print(f"Terjadi kesalahan : {e}")
