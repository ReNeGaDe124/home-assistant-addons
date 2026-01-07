def pick_best(subs, release=""):
    if not subs: return None
    return sorted(subs, key=lambda s: s.get("rating",0), reverse=True)[0]
