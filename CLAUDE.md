# House cost app — how updates work

- `app/house-cost.html` is the source. It is also published as the Claude artifact
  https://claude.ai/artifact/YSpi2Wf6vk2oRG39tao4m4 (capabilities: sample images, db, user, downloads — keep them).
- `index.html` is the public web build served by GitHub Pages at https://suparerkar24-ux.github.io/house-cost/ .
  Never edit it by hand: run `python3 tools/build_web.py` after changing the source.

To ship a change:
1. Edit `app/house-cost.html`.
2. Publish it to the artifact URL above (Artifact tool, `url` = the artifact link, same file).
3. `python3 tools/build_web.py`, bump `APP_VER` in the source if present, commit, push to `root` (the default branch).
   Pages redeploys in about a minute.

Notes: outside Claude, `window.claude` is missing, so AI deed reading is off (user taps corners) and
projects save to localStorage only. Sharing works by `#h=` link (no deed photo) or `.house.json` file.
The user and UI text are Thai.
