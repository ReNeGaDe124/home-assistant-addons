import re

def pick_best(results, video_filename):
    if not results:
        return None

    return results[0]