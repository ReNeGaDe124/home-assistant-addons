import os, threading
from plexapi.server import PlexServer
from subsro.api import SubsAPI
from subsro.plex import get_media_file, get_ids, subtitle_path
from subsro.matcher import pick_best
from subsro.webhook import start_webhook

plex = PlexServer(os.getenv("PLEX_URL"), os.getenv("PLEX_TOKEN"))
subs = SubsAPI(os.getenv("SUBSRO_API_KEY"))

def process(item):
    f = get_media_file(item)
    if not f: return
    srt = subtitle_path(f)
    if os.path.exists(srt): return
    field,val = get_ids(item)
    if not field: return
    best = pick_best(subs.search(field,val), os.path.basename(f))
    if not best: return
    if os.getenv("DRY_RUN")=="true":
        print("DRY RUN", srt); return
    from subsro.extract import extract_srt
    
	archive = subs.download(best["id"])
	ok = extract_srt(archive, srt)

	if ok:
    	print(f"Extracted subtitle: {srt}")
	else:
    	print(f"No SRT found in archive for {item.title}")

def scan():
    for m in plex.library.section("Movies").all(): process(m)
    for s in plex.library.section("TV Shows").all():
        for e in s.episodes(): process(e)

if __name__ == "__main__":
    threading.Thread(target=start_webhook,args=(scan,),daemon=True).start()
    scan()
