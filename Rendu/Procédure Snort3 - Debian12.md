# Installation de Snort3 sur debian 12

## Mettre à jour le système

Assurez-vous que votre système est à jour :
```bash
sudo apt-get update && upgrade -y
```
## Installer les dépendances requises

Installez les outils de développement, les bibliothèques et autres utilitaires nécessaires :

```bash
sudo apt-get install -y build-essential autotools-dev libdumbnet-dev libluajit-5.1-dev libpcap-dev \
zlib1g-dev pkg-config libhwloc-dev cmake liblzma-dev openssl libssl-dev cpputest libsqlite3-dev \
libtool uuid-dev git autoconf bison flex libcmocka-dev libnetfilter-queue-dev libunwind-dev \
libmnl-dev ethtool libjemalloc-dev
```
## Étape 3 : Installation de DAQ

```
mkdir snort
cd /snort
```

Installer DAQ :

```bash
sudo git clone https://github.com/snort3/libdaq.git
cd libdaq
```

```bash
sudo ./bootstrap
```

Exécutez autoreconf si bootstrap échoue :

```bash
autoreconf -fvi
```

Configurer et installer DAQ :

```bash
./configure
make -j$(nproc)
sudo make install
```


## Télécharger et installer Snort3

Cloner le dépôt Snort3 :

```bash
cd ..
git clone https://github.com/snort3/snort3.git
cd snort3
```

Générer les fichiers de configuration :

```bash
./configure_cmake.sh
```

Construire et installer Snort3 :

```bash
cd build
make -j$(nproc)
sudo make install
```

## Vérifier l'installation
Pour vérifier que Snort3 est installé correctement, utilisez la commande suivante :

```bash
cd /usr/local/snort/bin
./snort -V
```

![alt tag](https://github.com/Zennael/AIS/blob/main/Rendu/Screenshot/snort-version.png)

