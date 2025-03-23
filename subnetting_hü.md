# Subnetting Übungsprotokoll

---

## Übung 1: Erstellen von 4 Subnetzen aus 192.168.0.0 /24

### **Aufgabe:**  
Erstelle 4 Subnetze mit der Mindestanzahl an nutzbaren Hosts:  
- Netz A: mindestens 20 Hosts  
- Netz B: mindestens 15 Hosts  
- Netz C: mindestens 30 Hosts  
- Netz D: verbleibende Adressen

### **Lösung:**

| Netz  | Netzwerkadresse  | Subnetzmaske | Broadcastadresse | Hosts |
|-------|-----------------|--------------|------------------|-----------------------|
| A     | 192.168.0.0     | /27 (255.255.255.224) | 192.168.0.31  | 192.168.0.1 - 192.168.0.30 |
| B     | 192.168.0.32    | /28 (255.255.255.240) | 192.168.0.47  | 192.168.0.33 - 192.168.0.46 |
| C     | 192.168.0.48    | /27 (255.255.255.224) | 192.168.0.79  | 192.168.0.49 - 192.168.0.78 |
| D     | 192.168.0.80    | /26 (255.255.255.192) | 192.168.0.143 | 192.168.0.81 - 192.168.0.142 |

---

## Übung 2: Netz 193.170.20.0 /24 in 8 Subnetze aufteilen

### **Lösung:**
- Jedes Subnetz hat die Subnetzmaske **/27 (255.255.255.224)**.
- Subnetz-Adressen:

| Subnetz | Netzwerkadresse | Broadcastadresse  | Hosts |
|---------|----------------|------------------|----------------------|
| 1       | 193.170.20.0   | 193.170.20.31    | 193.170.20.1 - 193.170.20.30 |
| 2       | 193.170.20.32  | 193.170.20.63    | 193.170.20.33 - 193.170.20.62 |
| 3       | 193.170.20.64  | 193.170.20.95    | 193.170.20.65 - 193.170.20.94 |
| 4       | 193.170.20.96  | 193.170.20.127   | 193.170.20.97 - 193.170.20.126 |
| 5       | 193.170.20.128 | 193.170.20.159   | 193.170.20.129 - 193.170.20.158 |
| 6       | 193.170.20.160 | 193.170.20.191   | 193.170.20.161 - 193.170.20.190 |
| 7       | 193.170.20.192 | 193.170.20.223   | 193.170.20.193 - 193.170.20.222 |
| 8       | 193.170.20.224 | 193.170.20.255   | 193.170.20.225 - 193.170.20.254 |

---

## Übung 3: Netz 172.28.40.0 /26 in zwei Subnetze aufteilen

### **Lösung:**

| Subnetz | Netzwerkadresse | Subnetzmaske | Broadcastadresse | Hosts |
|---------|----------------|--------------|------------------|---------------|
| 1       | 172.28.40.0    | /27          | 172.28.40.31     | 172.28.40.1 - 172.28.40.30 |
| 2       | 172.28.40.32   | /27          | 172.28.40.63     | 172.28.40.33 - 172.28.40.62 |

---

## Übung 4: Subnetzmaske für 17.0.0.0 mit 10 Subnetzen und mindestens 12 Hosts

- Benötigte Adressen: mindestens **14 (12 nutzbare Hosts)**
- Ein **/28-Netz (255.255.255.240)** passt.
- Die Subnetzmaske für 10 Subnetze ist **255.255.255.240**.

---

## Übung 5: Subnetzmaske für 210.52.190.0 mit 5 Subnetzen und mindestens 10 Hosts

- Benötigte Adressen: mindestens **12 (inkl. Netzwerk- und Broadcastadresse)**
- **/28 (255.255.255.240)** bietet 16 Adressen pro Subnetz.
- Die Subnetzmaske ist **255.255.255.240**.

---

## Übung 6: Nutzen von /30-Netzen

- **Ein /30-Netz hat nur 4 Adressen**, davon **2 nutzbare Hosts**.
- Typischer Einsatz: **Point-to-Point-Verbindungen** zwischen Routern.

---

## Übung 7: Netzwerk- und Hostanteil der Klassen A, B und C

| Klasse | Netzwerkanteil | Hostanteil |
|--------|---------------|------------|
| A      | 8 Bit         | 24 Bit     |
| B      | 16 Bit        | 16 Bit     |
| C      | 24 Bit        | 8 Bit      |

---
