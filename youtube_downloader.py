from pytubefix import YouTube

url = 'https://www.youtube.com/watch?v=3UOyky9sEQY&list=PL7yh-TELLS1FwBSNR_tH7qVbNpYHL4IQs'

try:
    yt = YouTube(url)
    judul = yt.title
    penonton = yt.views
    durasi = yt.length
    deskripsi = yt.description

    # menampilkan informasi video
    print("Judul : %s" %judul)
    print("Jumlah Penonton : %s" %penonton)
    print("Durasi : %s\n" %durasi)

    #memilih stream terbaik untuk diunduh
    cek = yt.streams.filter(file_extension='mp4')
    for i in cek:
        print(i)

    # apakah akan mendownload video?
    data = input("Apakah kamu akan mendownload video (Y/n)? ")
    if data == 'Y' or 'y':
        tag = input("Masukkan itag : ")
        unduh = yt.streams.get_by_itag(tag)
        unduh.download()
    else :
        print("--Whiter0se--")

except Exception as e:
    print(f"Terjadi kesalahan : {e}")
