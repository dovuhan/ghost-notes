# 👻 GhostNotes v2.1

GhostNotes, şık ve fonksiyonel bir not alma uygulamasıdır. Notlarınızı kolayca yönetin, arayın, kategorize edin ve güvende tutun.

## ✨ Özellikler

- **Şık Arayüz**: Koyu "hacker" teması ve `Consolas` fontu ile göz yormayan, modern bir tasarım.
- **Gelişmiş Not Yönetimi**: Notlar; başlık, içerik, oluşturulma tarihi, kategori ve favori durumu gibi bilgilerle saklanır.
- **Anlık Arama**: Not başlıkları ve içeriklerinde anında arama yapın.
- **Filtreleme ve Sıralama**: Notları kategoriye göre filtreleyin; tarihe, başlığa veya favori durumuna göre sıralayın.
- **Kategoriler**: Notlarınızı "İş", "Kişisel", "Proje" gibi özel kategorilere ayırın.
- **Favoriler**: Önemli notlarınızı favorilere ekleyerek kolayca erişin.
- **Otomatik Kaydetme**: Yazarken notlarınız periyodik olarak otomatik kaydedilir.
- **Güvenli Veri Saklama**: Notlarınız, programın yanında değil, işletim sisteminizin kullanıcı klasörü içinde güvenli bir yerde (`~/.config/ghostnotes/` veya benzeri) saklanır.
- **Dışa Aktarma**: Notlarınızı `.txt` dosyası olarak dışa aktarın.
- **Terminal Komutu**: Sisteme kurulduktan sonra terminalden `doguhan` komutu ile çalıştırılabilir.

## 🚀 Kurulum

Uygulamayı sisteminize kurmak ve `doguhan` komutu ile çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
- Python 3.6 veya üstü
- `git` (projeyi klonlamak için)

### Adımlar

1.  **Projeyi Klonlayın**:
    Terminali veya komut istemcisini açın ve aşağıdaki komutla projeyi bilgisayarınıza indirin:
    ```sh
    git clone [https://github.com/dovuhan/ghost-notes.git](https://github.com/dovuhan/ghost-notes.git)
    ```

2.  **Proje Dizinine Girin**:
    ```sh
    cd ghostnotes
    ```

3.  **Uygulamayı Kurun**:
    Aşağıdaki komut, uygulamanın bağımlılıklarını kuracak ve `doguhan` komutunu sisteminize ekleyecektir.
    ```sh
    pip install .
    ```
    Eğer yönetici izni gerektiren bir hata alırsanız (özellikle Linux ve macOS'ta), komutu `sudo` ile çalıştırabilirsiniz: `sudo pip install .`. Alternatif olarak, sadece kendi kullanıcınız için kurmak isterseniz `--user` bayrağını kullanabilirsiniz: `pip install --user .`.

## 💻 Kullanım

Kurulum tamamlandıktan sonra, herhangi bir terminal veya komut istemcisini açıp aşağıdaki komutu yazarak uygulamayı başlatabilirsiniz:

```sh
doguhan

📂 Proje Yapısı

Proje, standart bir Python paketi yapısına sahiptir:

ghostnotes/
├── ghostnotes/
│   ├── __init__.py      # Bu dizinin bir Python paketi olduğunu belirtir.
│   └── main.py          # Ana uygulama kodunu içerir.
├── setup.py             # Kurulum ve paketleme ayarlarını içerir.
└── README.md            # Bu dosya.

