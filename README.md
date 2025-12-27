# 📟 TERMINUS MANAGER

![Python](https://img.shields.io/badge/python-3.x-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-linux-black?style=for-the-badge&logo=linux&logoColor=white)
![Type](https://img.shields.io/badge/tool-CLI%2FUtility-orange?style=for-the-badge)

**A Végső Rendszergazda Parancssori Felület (TUI) Linux Szerverekhez.**

A Terminus egy Python-alapú CLI keretrendszer, amelyet arra terveztünk, hogy a mindennapi rendszergazdai feladatokat egyetlen, hatékony és interaktív felületen egyesítse. Megszünteti a bonyolult `systemctl`, `docker` vagy hálózati parancsok és flagek észben tartásának kényszerét, helyette egy strukturált vezérlőközpontot kínál.

## ⚡ MIÉRT HASZNÁLD A TERMINUST?

* **Hatékonyság:** A gyakori feladatok (Szolgáltatások újraindítása, Docker logok olvasása, Rendszerállapot ellenőrzése) 3x gyorsabban végezhetők el, mint nyers parancsokkal.
* **Egységes Vezérlés:** A Systemd, a Docker és a Hálózat kezelése egyetlen képernyőről.
* **Vizuális Visszajelzés:** Színkódolt kimenetek és formázott ASCII fejlécek teszik a terminálélményt szervezetté és átláthatóvá.
* **Nincsenek Függőségek:** Tiszta Python 3-ban íródott, csak a standard könyvtárakat használja. Bármilyen szerverre ledobod, és azonnal működik.

## 🛠️ FUNKCIÓK

### 1. Szolgáltatás Kezelő (Service Manager)
Interaktív `systemctl` vezérlő.
* Állapot ellenőrzése, Indítás, Leállítás és Újraindítás bármely szolgáltatáson azonnal.
* Valós idejű visszajelzés.

### 2. Docker Parancsnok (Docker Commander)
Konténerek kezelése a szoftver elhagyása nélkül.
* Futó/Összes konténer listázása.
* **Élő Log Stream:** Csatlakozás a konténer naplóihoz egyetlen gombnyomással.
* Rendszer Tisztítás (Prune): Nem használt kötetek és lemezképek gyors törlése.

### 3. Rendszer és Hálózat Egészség
* **Health Dashboard:** Azonnali áttekintés a CPU terhelésről, Lemezhasználatról és RAM-ról.
* **Hálózati Eszközök:** Nyitott portok (LISTEN), aktív kapcsolatok és a publikus IP cím lekérdezése.

### 4. Auto-Updater
* Érzékeli a csomagkezelőt (`apt` vagy `yum`), és elvégzi a teljes rendszerfrissítést.

## 📥 TELEPÍTÉS ÉS HASZNÁLAT

A Terminus egyetlen fájlból álló segédprogram.

```bash
# 1. Letöltés
wget [https://raw.githubusercontent.com/aaron-devop/terminus-manager/main/terminus.py](https://raw.githubusercontent.com/aaron-devop/terminus-manager/main/terminus.py)

# 2. Futtathatóvá tétel
chmod +x terminus.py

# 3. Futtatás (Root jog szükséges a rendszerkezeléshez)
sudo ./terminus.py
```

## 🖥️ ELŐNÉZET

```text
  _______ ______ _____  __  __ _____ _   _ _    _  _____ 
 |__   __|  ____|  __ \|  \/  |_   _| \ | | |  | |/ ____|
    | |  | |__  | |__) | \  / | | | |  \| | |  | | (___  
    | |  | |____| | \ \| |  | |_| |_| |\  | |__| |____) |
    |_|  |______|_|  \_\_|  |_|_____|_| \_|\____/|_____/ 
                                       v1.0.0 | @aaron-devop

SYSTEM MANAGEMENT INTERFACE for production-server-01
------------------------------------------------------------
1. Service Manager (Systemd)
2. Docker Commander
3. System Health
4. Network Utilities
5. System Updates (Apt/Yum)
99. Exit
------------------------------------------------------------
root@terminus:~# 
```

## 📜 LICENC
MIT License
