import os
def get_media_file(item):
    try: return item.media[0].parts[0].file
    except: return None
def get_ids(item):
    for g in item.guids:
        if g.id.startswith("imdb://"): return ("imdbid", g.id.replace("imdb://","").replace("tt",""))
        if g.id.startswith("tmdb://"): return ("tmdbid", g.id.replace("tmdb://",""))
    return (None,None)
def subtitle_path(media_file):
    return os.path.splitext(media_file)[0] + ".ro.srt"
