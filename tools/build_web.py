"""Build the public web page (index.html) from the Claude artifact source (app/house-cost.html).

Usage: python3 tools/build_web.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = (root / "app" / "house-cost.html").read_text(encoding="utf-8")

head = """<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0E0F10">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="ต้นทุนบ้าน">
<meta name="description" content="คิดต้นทุนบ้าน ที่ดิน ตัวบ้าน ระยะร่น และแบ่งห้อง บันทึกในเครื่อง แชร์ให้คนอื่นได้">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230E0F10'/%3E%3Cpath d='M14 30L32 14l18 16v20H14z' fill='%23C9A27A'/%3E%3Crect x='27' y='36' width='10' height='14' fill='%230E0F10'/%3E%3C/svg%3E">
"""
body = src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
end_style = body.index("</style>") + len("</style>")
out = head + body[:end_style] + "\n</head>\n<body>\n" + body[end_style:] + "\n</body>\n</html>\n"
(root / "index.html").write_text(out, encoding="utf-8")
print("built index.html", len(out), "bytes")
