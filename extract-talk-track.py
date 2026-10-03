"""Pull each slide's on-screen text and speaker notes out of a deck into a talk-track markdown file.

Usage: python3 extract-talk-track.py new-week1-fundamentals.html week1-talk-track.md "Week 1"
"""
import html
import os
import re
import sys

src, dst, label = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src).read()
secs = re.findall(r'(?:<!-- =+ ([^=]+?) =+ -->\s*)?<section class="slide[^"]*"[^>]*>(.*?)</section>', s, re.S)


def strip(t):
    t = re.sub(r'<br\s*/?>', ' ', t)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', t))).strip()


out = [f"# {label} — Talk Track", "",
       f"Speaker notes for `{src}`, in slide order. **On screen** is the slide's text (kept even after it's stripped from the slide); **Say** is the talk track. `[Click]` means press → to reveal the next step.", ""]
for i, (hdr, body) in enumerate(secs, 1):
    m = re.search(r'<h2[^>]*>(.*?)</h2>', body, re.S) or re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S)
    title = hdr.split('. ', 1)[-1].title() if hdr else ''
    heading = f"## {i}. {title}" + (f" — {strip(m.group(1))}" if m else "")
    screen = re.search(r'<aside class="onscreen">(.*?)</aside>', body, re.S)
    screen = [html.unescape(l.strip()) for l in screen.group(1).splitlines() if l.strip()] if screen else []
    notes = [strip(n) for n in re.findall(r'<aside class="notes">(.*?)</aside>', body, re.S)]
    out += [heading, ""]
    if screen:
        out += ["**On screen**", ""] + [f"- {l}" for l in screen] + [""]
    out += ["**Say**", ""] + ([n + "\n" for n in notes] if notes else ["_(no notes)_", ""])
# talk track for slides that were removed from the deck lives in <dst stem>-removed.md and is kept at the end
removed = dst[:-3] + "-removed.md"
if os.path.exists(removed):
    out += ["", "---", "", "## Removed slides", "", "_Kept for reference; these slides are no longer in the deck._", "",
            re.sub(r'<!--.*?-->\s*', '', open(removed).read(), flags=re.S)]
open(dst, "w").write("\n".join(out))
print(f"{len(secs)} slides -> {dst}")
