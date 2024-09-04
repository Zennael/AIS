
## I - CONFIGURATION DE LA CARTE RESEAU (A CHAUD)

```
ip link set dev eth0 promisc on
```
Configuration de l'offload
```
ip ink show eth0
apt install ethtool ethtool -k rth0 |grep receive-offload
ethtool -K eth0 gro off lro off
ethtool -k eth0 | grep receive-offload
```

## II - CONFIGURATION DU PARAMETRAGE AUTO DE LA NIC EN TANT QUE SERVICE
Création du fichier de service
```
nano /etc/systemd/system/snort3-nic.service
```
Contenu du fichier
```
[Unit] Description=Set Snort 3 NIC in promiscuous mode and Disable GRO, LRO on boot
After=network.target

[Service] Type=oneshot
ExecStart=/usr/sbin/ip link set dev ens18 promisc on
ExecStart=/usr/sbin/ethtool -K ens18 gro off lro off
TimeoutStartSec=0
RemainAfterExit=yes

[Install]
WantedBy=default.target
```
Activation et redémarrage du service
```
systemctl daemon-reload
systemctl start snort3-nic.service systemctl
enable --now snort3-nic.service
```


## III - CREATION D'UN FICHIER DE REGLES PERSONNALISEES
Création du fichier de règles
```
nano /etc/snort/rules/test.rules
```
Contenu du fichier
```
alert icmp any any -> any any (msg:"!!! ICMP Alert !!!";sid:1000001;rev:1;)
```


## III - CONFIGURATION DES LOGS
Création du répertoire
```
mkdir /var/log/snort
chmod 777 /var/log/snort
```
Modification du fichier de configuration de Snort
```
nano /etc/snort/snort.lua
```
Modifier le fichier

>Se rendre tout en bas du fichier, dans la catégorie "7. configure outputs"
```
alert_full =
{
    file = true,
    limit = 100000
}
```


## IV - TEST
Lancer un ping à destination de votre machine

Lancer la capture Snort
```
sudo snort -c /etc/snort/snort.lua -R /etc/snort/rules/test.rules -i eth0 -A alert_fast -l /var/log/snort
```

![alt tag](https://github.com/Zennael/AIS/blob/main/Rendu/Screenshot/snort-Sniffe.png)