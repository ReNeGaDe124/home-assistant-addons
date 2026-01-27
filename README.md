![logo](https://github.com/user-attachments/assets/85c9a86d-de41-48da-a4a1-e16a0c6e04ac)

# Subs.ro Plex Subtitle Downloader - Add-on si Integrare pentru Home Assistant

Descarcă automat subtitrări în limba română de pe Subs.ro pentru Plex Media Server. (Home Assistant)

## ✨ Functionalitati
  - Descarcare automata a subtitrarii pentru fisiere video nou importate in Plex Media Server (🧩)
  - Logica robusta de alegerea a subtitrarii pentru a selecta o versiune cat mai potrivita pentru fisierul video in cauza si pentru a minimiza cat mai mult posibil apelarea API-ului Subs.ro (🧩)
  - Convertire automata a subtitrarile in format "UTF8 with BOM" pentru o compatibilitate sporita (🧩)
  - Redenumirea subtitrarile pentru a include extensia ".ro.srt" si plasarea in folderul fisierului video pentru preluarea in mod automat si clar de catre Plex Media Server (🧩)
  - Rulare activitati la o ora programata:
      - Descarcare subtitrari pentru toate fisierele video ce nu au o subtitrare asociata (🧩)
      - Curatare subtitrari orfane ce nu mai au un fisier video asociat (🧩)
  - Rulare activitati in mod manual:
      - Descarcare subtitrari pentru toate fisierele video ce nu au o subtitrare asociata (🧩+🔗)
      - Curatare subtitrari orfane ce nu mai au un fisier video asociat (🧩+🔗)
      - Descarcare subtitrare pentru cel mai recent fisier video importat in Plex Media Server (🧩+🔗)
      - Cautare si descarcare de subtitrari pentru fisierele video din libraria Plex Media Server pe baza cuvintelor cheie introduse in campul de cautare (🧩+🔗)
      - Cautare si stergere de subtitrari pentru fisierele video din libraria Plex Media Server pe baza cuvintelor cheie introduse in campul de cautare (🧩+🔗)
  - Entitate de tip senzor ce permite vizualizarea statusului add-on-ului Subs.ro Plex Subtitle Downloader si acces facil la vizualizarea logului ultimei actiuni facuta de catre acesta (🧩+🔗)

(🧩) = functionalitate ce necesita doar instalarea add-on-ului<br>
(🧩+🔗) = functionalitate ce necesita atat instalarea add-on-ului cat si a integrarii

## 🛠️ Instalare

### 🧩 Add-on
  1. Adauga acest repository in instanta ta de Home Assistant: <br><br>[![https://github.com/ReNeGaDe124/Subs.ro-Plex-Subtitle-Downloader](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https://github.com/ReNeGaDe124/Subs.ro-Plex-Subtitle-Downloader)<br>
  2. Cauta add-on-ul `Subs.ro Plex Subtitle Downloader` si instaleaza-l.

### 🔗 Integrare

#### Automat prin HACS
  1. Adauga acest repository in instanta ta de Home Assistant: <br><br>[![https://github.com/ReNeGaDe124/Subs.ro-Plex-Subtitle-Downloader](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ReNeGaDe124&repository=Subs.ro-Plex-Subtitle-Downloader&category=Integration)
  2. Cauta integrarea `Subs.ro Plex Subtitle Downloader` si instaleaza-o.
  3. Restarteaza Home Assistant.

#### Manual
  1. Descarca fisierele din acest repository.
  2. Copiază folderul `custom_components/subsro` în directorul `custom_components` din Home Assistant.
  3. Restarteaza Home Assistant.

## ⚙️ Configurare

### 🧩 Add-on
<p align="left">
  <img src="https://github.com/user-attachments/assets/5de500b1-58ed-45f2-bda0-eb24c51afb8e" width="250" />
</p>

| Optiune | Tip | Implicit | Descriere |
|--------|------|---------|-------------|
| `plex_url` | str | `http://localhost:32400` | Linkul catre serverul Plex Media Server |
| `plex_token` | str | | Token de autentificare Plex Media Server - X-Plex-Token (vezi aici cum sa il obtii) |




## 📦 Dependente
### 🎬 X-Plex-Token
