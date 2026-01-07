#!/usr/bin/env bash
export PLEX_URL=$(jq -r .plex_url /data/options.json)
export PLEX_TOKEN=$(jq -r .plex_token /data/options.json)
export SUBSRO_API_KEY=$(jq -r .subsro_api_key /data/options.json)
export SCAN_MOVIES=$(jq -r .scan_movies /data/options.json)
export SCAN_TV=$(jq -r .scan_tv /data/options.json)
export DRY_RUN=$(jq -r .dry_run /data/options.json)
python3 -u /app/subsro/main.py
