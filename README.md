#### ENCRYPT CYTHON C++
Hii, bagaimana cara encrypt c++ menggunakan cython? kamu hanya perlu menginstall module cython:
<br>```pip install cython```</br>

setelah kalian install module cython kamu install script nya dulu dengan mengetik:
```python
$ pkg install python2 git
$ pip install cython
$ git clone https://github.com/XNSCODE/cpp
$ cd $HOME/cpp
```

setelah sudah kamu install script nya kamu ubah terlebih dahulu pada bagian file ```setup.py```
kalian ubah tulisan: <b>ambf</b> menjadi nama file kamu.

[![IMG-20211006-192256.jpg](https://i.ibb.co/60XNf6b/carbon.png)](https://ibb.co/v4XDK2m)

jika sudah kalian ubah menjadi nama file kalian, kalian run sc nya dengan mengetik: ```python setup.py build_ext --inplace```

#### CARA SIMPLE 
kamu cukup ketik: ```cython --cplus namafile.pyx```
