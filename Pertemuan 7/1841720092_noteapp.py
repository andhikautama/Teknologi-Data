# -*- coding: utf-8 -*-
"""1841720092_NoteApp

from google.colab import drive

drive.mount('/content/drive')

# file main.py

def main():
  app = App()
  selesai = False
  while selesai is not True:
      selesai = app.jalankan()

main()

# file app.py

class App:
  def __init__(self):
    self.kegiatan = Keuangan()

  def jalankan(self):
    print('-------------------------------')
    print('Welcome to NoteApp!')
    print('-------------------------------')
    print('Menu:')
    print('(1) Input a New Note')
    print('(2) Look at Existing Notes')
    print('(3) Pandas Demos')
    print('(0) Quit')
    pilihan = input('What is your choice? ')
    print('Your choice is ', pilihan)
    selesai = False
    if pilihan == '0':
      selesai = True
    else:
      if pilihan == '1':
        #print('choice (1)')
        self.kegiatan.tampilkan_form()
        self.kegiatan.simpan()
      elif pilihan == '2':
        #print('choice (2)')
        self.kegiatan.tampilkan_tersimpan()
      elif pilihan == '3':
        #print('choice (3)')
        print('Membuka program latihan Pandas')
        pd = PandasDemos()
        lanjut = True
        while lanjut:
          lanjut = pd.tampilkan_pilihan()
      else:
        print('[ERROR] Your choice is not valid')
        selesai = False
    return selesai

# file keuangan.py

class Keuangan(Kegiatan):
  def __init__(self):
    super().__init__()
    self.jenis = 'kredit'
    self.nominal = 0
  
  def tampilkan_form(self):
    super().tampilkan_form()
    str_jenis = input('Masukkan Jenis: ')
    str_nominal = input('Masukkan Nominal: ')
    self.jenis = str_jenis
    self.nominal = float(str_nominal)

  def simpan(self):
    data = {
        'tanggal': self.tanggal,
        'nama': self.nama,
        'jenis': self.jenis,
        'nominal': self.nominal,
    }
    self.tersimpan.append(data)
  
  def tampilkan_tersimpan(self):
    i = 0
    while i < len(self.tersimpan):
      baris = self.tersimpan[i]
      print('{}. [{}] {} | {} | Rp{}'.format(
          (i + 1),
          baris['tanggal'],
          baris['nama'],
          baris['jenis'],
          baris['nominal']
      ))
      i = (i + 1)

# file kegiatan.py

from datetime import datetime

class Kegiatan:
  def __init__(self):
    self.tanggal = datetime.now()
    self.nama = ''
    self.tersimpan = []

  def tampilkan_form(self):
    str_tanggal = input('Masukkan tanggal: ')
    str_nama = input('Masukkan nama: ')
    self.tanggal = datetime.strptime(str_tanggal, '%Y-%m-%d')
    self.nama = str_nama

  def simpan(self):
    data = {'tanggal': self.tanggal, 'nama': self.nama}
    self.tersimpan.append(data)

  def tampilkan_tersimpan(self):
    i = 0
    while i < len(self.tersimpan):
      baris = self.tersimpan[i]
      print('{}. [{}] {}'.format(
          (i + 1),
          baris['tanggal'],
          baris['nama']
      ))
      i = (i + 1)

# file pandasdemos.py

import pandas as pd

class PandasDemos:
  def __init__(self):
    self.data = None

  def tampilkan_pilihan(self):
    print('Pandas Demos')
    print('-------------------------------')
    print('Menu:')
    print('(1) Load dataset')
    print('(2) Preview the top and bottom 5 data rows')
    print('(3) Show the data of intelligence system group research')
    print('(4) Show authors and their proposal titles')
    print('(0) Quit')
    pilihan = input('What is your choice? ')
    print('Your choice is ', pilihan)
    if pilihan == '1':
        self.load_dataset()
        return True
    elif pilihan == '2':
        self.tampilkan_5_baris_awal_akhir()
        return True
    elif pilihan == '3':
        self.tampilkan_data_sistem_cerdas()
        return True
    elif pilihan == '4':
        self.tampilkan_pengusul_dan_judul()
        return True
    else:
        return False

  def load_dataset(self):
    print('Load dataset..')
    self.data = pd.read_csv(
         '/content/drive/MyDrive/rekap_proposal.csv',
        sep = ';',                # Separator
        error_bad_lines = False,  # Skip baris yang error
        engine = 'python'         # Mengganti Parser engine dari C ke Python
    )
    # Set kolom 'id' sebagai index
    self.data.set_index('id')
    # Cetak di console
    print(self.data.to_string())

  def tampilkan_5_baris_awal_akhir(self):
    print('Menyeleksi beberapa baris di awal dan akhir..')
    # Mengambil N=baris teratas
    awal5 = self.data.head(5)
    print(awal5.to_string())
    # Mengambil N-baris terakhir
    akhir5 = self.data.tail(5)
    print(akhir5.to_string())
  
  def tampilkan_data_sistem_cerdas(self):
    print('Seleksi baris dengan WHERE..')
    # Membuat filter untuk WHERE
    filter = self.data['grup_riset'] == 'SISTEM CERDAS'
    # Seleksi data
    data_sc = self.data.where(filter)
    print(data_sc)

  def tampilkan_pengusul_dan_judul(self):
    print('Memilih kolom tertentu..')
    # Mengambil berdasarkan nama kolom
    nama = self.data['nama_pengusul']
    # Bisa juga dengan cara seperti ini
    judul = self.data.judul_proposal
    # Menggabungkan 2 DataFrame
    # A. Digabungkan barisnya (Ditumpuk)
    gabung_baris = pd.concat([nama, judul], axis = 0)
    print(gabung_baris.to_string())
    # B. Digabungkan kolomnya (Digandeng)
    gabung_kolom = pd.concat([nama, judul], axis = 1)
    print(gabung_kolom.to_string())