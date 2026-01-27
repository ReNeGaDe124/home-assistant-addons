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
  4. In sectiunea `Devices & services` din Home Assistant, apasa pe butonul `+ Add integration`.
  5. Cauta si alege din lista `Subs.ro Plex Subtitle Downloader`.

#### Manual
  1. Descarca fisierele din acest repository.
  2. Copiază folderul `custom_components/subsro` în directorul `custom_components` din Home Assistant.
  3. Restarteaza Home Assistant.
  4. In sectiunea `Devices & services` din Home Assistant, apasa pe butonul `+ Add integration`.
  5. Cauta si alege din lista `Subs.ro Plex Subtitle Downloader`.

## ⚙️ Configurare

### 🧩 Add-on

<p align="center">
  <img src="https://github.com/user-attachments/assets/5de500b1-58ed-45f2-bda0-eb24c51afb8e" width="250" />
</p>

| Optiune | Tip | Implicit | Descriere |
|--------|------|---------|-------------|
| <p align="center">`plex_url`</p> | <p align="center">str</p> | `http://localhost:32400` | Linkul catre serverul Plex Media Server. |
| <p align="center">`plex_token`</p> | <p align="center">str</p> | | Token de autentificare Plex Media Server - X-Plex-Token (vezi [aici](https://github.com/ReNeGaDe124/home-assistant-addons/tree/homeassistant?tab=readme-ov-file#-x-plex-token) cum sa il obtii). |
| <p align="center">`subsro_api_key`</p> | <p align="center">str</p> | | Token de autentificare API Subs.ro (vezi [aici](https://github.com/ReNeGaDe124/home-assistant-addons/tree/homeassistant?tab=readme-ov-file#-api-token-subsro) cum sa il obtii). |
| <p align="center">`webhook_secret`</p> | <p align="center">password?</p> | | Parola ce va fi folosita pentru interconectarea dintre Add-on si Integrare (daca nu se doreste folosirea Integrarii campul poate ramane gol). |
| <p align="center">`scheduled_download`</p> | <p align="center">bool</p> | <p align="center">`ON`</p> | Activare/Dezactivare a functiei de descarcare subtitrari pentru toate fisierele video ce nu au o subtitrare asociata. |
| <p align="center">`scheduled_cleanup`</p> | <p align="center">bool</p> | <p align="center">`ON`</p> | Activare/Dezactivare a functiei de curatare subtitrari orfane ce nu mai au un fisier video asociat. |
| <p align="center">`scan_time`</p> | <p align="center">str</p> | <p align="center">`03:00`</p> | Ora la care vor rula functiile `scheduled_download` si/sau `scheduled_cleanup`. |
| <p align="center">`debug_log`</p> | <p align="center">str</p> | <p align="center">`OFF`</p> | Activare/Dezactivare functie logare detaliata. |

Mentiune: Add-on-ul functioneaza pe portul **8999**. Acesta trebuie sa nu fie folosit de alt add-on sau aplicatie.

### 🔗 Integrare

<p align="center">
  <img src="https://github.com/user-attachments/assets/cba9f6d7-d273-46c2-a28a-a9178b6ed4c2" width="300" />
</p>

| Optiune | Tip | Implicit | Descriere |
|--------|------|---------|-------------|
| <p align="center">`url`</p> | <p align="center">str</p> | `http://localhost:8999` | Linkul catre Add-on-ul Subs.ro Plex Subtitle Downloader. (in mod normal nu trebuie schimbat) |
| <p align="center">`secret`</p> | <p align="center">str</p> | | Parola folosita in campul `webhook_secret` din Add-on. |

## ▶️ Utilizare Integrare

<p align="center">
  <img src="https://github.com/user-attachments/assets/b7277e41-2f55-439a-a331-c43bdc1bfb87" width="300" />
</p>

| Optiune | Metoda de activare | Descriere |
|--------|-------------|-------------|
| <p align="center">`Cleanup Orphaned Subtitles`</p> | <p align="center">Apasare pe buton</p> | Activare manuala a functiei de curatare subtitrari orfane ce nu mai au un fisier video asociat. |
| <p align="center">`Download for Latest Video`</p> | <p align="center">Apasare pe buton</p> | Activare manuala a functiei de descarcare subtitrare pentru cel mai recent fisier video importat in Plex Media Server. |
| <p align="center">`Download Missing Subtitles`</p> | <p align="center">Apasare pe buton</p> | Activare manuala a functiei de descarcare subtitrari pentru toate fisierele video ce nu au o subtitrare asociata. |
| <p align="center">`Search & Download Subtitles`</p> | <p align="center">Introducere text in campul de cautare</p> | Activare manuala a functiei de cautare si descarcare de subtitrari pentru fisierele video din libraria Plex Media Server pe baza cuvintelor cheie introduse in campul de cautare. |
| <p align="center">`Search & Delete Subtitles`</p> | <p align="center">Introducere text in campul de cautare</p> | Activare manuala a functiei de cautare si stergere de subtitrari pentru fisierele video din libraria Plex Media Server pe baza cuvintelor cheie introduse in campul de cautare. |
| <p align="center">`Status`</p> |  | Entitate de tip senzor ce permite vizualizarea statusului add-on-ului Subs.ro Plex Subtitle Downloader si acces facil la vizualizarea logului ultimei actiuni facuta de catre acesta. **(Stari posibile: Offline, Booting, Idle, Processing)** |

### 📋 Exemplu de card pentru Dashboard

```yaml
type: entities
entities:
  - entity: button.subs_ro_plex_subtitle_downloader_cleanup_orphaned_subtitles
    name: Cleanup Orphaned Subtitles
  - entity: button.subs_ro_plex_subtitle_downloader_download_for_latest_video
    name: Download for Latest Video
  - entity: button.subs_ro_plex_subtitle_downloader_download_missing_subtitles
    name: Download Missing Subtitles
  - entity: text.subs_ro_plex_subtitle_downloader_search_download_subtitles
    name: Search & Download Subtitles
  - entity: text.subs_ro_plex_subtitle_downloader_search_delete_subtitles
    name: Search & Delete Subtitles
  - entity: sensor.subs_ro_plex_subtitle_downloader_status
    name: Status
title: Subs.ro Plex Subtitle Downloader
```

### 🟢🟡🔴 Exemple de posibile rezultate in sectiunea `Attributes` a senzorului `Status`:

<p>
  <img src="https://github.com/user-attachments/assets/555599f3-0125-4de3-b7ef-84fd63a6d49e" width="240" />
  <img src="https://github.com/user-attachments/assets/1ed95ae3-2df2-4fb1-bbbd-1446cfa9f6d7" width="240" />
  <img src="https://github.com/user-attachments/assets/a99dfce8-80cc-41f5-8352-e230caff852d" width="240" />
  <img src="https://github.com/user-attachments/assets/8aaf0139-69b5-450f-a99b-acd4ddd8b4f2" width="240" />
</p>

## 📦 Dependente

### 🎬 X-Plex-Token

  1. Conecteaza-te pe serverul tau Plex Media Server.
  2. Apasa pe butonul `⋮` pe unul din obiectele din librarie si apoi pe optiunea `Get Info`.

<p align="center">
  <img width="338" alt="get-info" src="https://github.com/user-attachments/assets/4d70b189-c404-4439-8e20-14833bc6e6bb" />
</p>

  3. Apasa pe butonul `View XML`.

<p align="center">
<img width="500" alt="view-xml" src="https://github.com/user-attachments/assets/e5ee4523-5657-460d-bb61-c01a9cddd7ca" />
</p>

  4. Copiaza din bara de adresa a paginii care se deschide valoarea de la sfarsitul linkului, de dupa `X-Plex-Token=`.

<p align="center">
<img width="693" height="108" alt="x-plex-token" src="https://github.com/user-attachments/assets/79835b17-f494-4ee8-bdba-3bb3e36e3982" />
</p>

  5. Pune valoarea copiata in campul `plex_token` din Add-on.

### 💬 API Token Subs.ro

  1. Creaza-ti cont pe [Subs.ro](https://subs.ro/).
  2. Logheaza-te si acceseaza [pagina de profil](https://subs.ro/utilizator/profil).
  3. Mergi la sectiunea `Acces API` si apasa pe butonul `Genereaza o cheie API`.

<p align="center">
<img width="300" alt="subsro-generate-api-key" src="https://github.com/user-attachments/assets/7f744f0c-b054-4ff2-b4ed-c7ad71791dc7" />
</p>

  4. Copiaza valoarea din sectiunea `Cheia dumneavoastra API`.

<p align="center">
<img width="350" alt="subsro-copy-api-key" src="https://github.com/user-attachments/assets/9e8c7940-2c7a-4ce6-acb0-6cab32a63279" />
</p>

  5. Pune valoarea copiata in campul `subsro_api_key` din Add-on.

