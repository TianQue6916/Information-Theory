import os, hashlib, re, json, base64

def walk(root, ext):
    out=[]
    for r,d,fs in os.walk(root):
        for f in fs:
            if f.endswith(ext):
                out.append(os.path.join(r,f).replace(chr(92),'/'))
    return out

htmls = walk('_superseded','.html')
print("html count", len(htmls))

formal = {}
for p in walk('02-讲义','.html'):
    formal.setdefault(os.path.basename(p),[]).append(p)

def norm_md5(p):
    b = open(p,'rb').read().replace(b'\r\n', b'\n')
    return hashlib.md5(b).hexdigest()

okA=[]; skipA=[]
for p in sorted(htmls):
    base = os.path.basename(p)
    cands = formal.get(base, [])
    m = re.search(r'/fig/(l\d+)/' + re.escape(base) + r'$', p)
    hit = None
    if m:
        ln = m.group(1)
        for c in cands:
            if '02-讲义/' + ln + '/' in c:
                hit = c
    if hit is None and len(cands) == 1:
        hit = cands[0]
    if hit is None:
        skipA.append({"file":p,"why":"找不到正式侧对应文件","cands":cands}); continue
    h1 = norm_md5(p); h2 = norm_md5(hit)
    if h1 == h2:
        okA.append({"file":p,"bytes":os.path.getsize(p),"formal":hit})
    else:
        skipA.append({"file":p,"why":"归一后 md5 不一致 %s vs %s (formal=%s)" % (h1[:8],h2[:8],hit)})
print("A ok", len(okA), "skip", len(skipA))
for s in skipA: print("  SKIP-A", s)

pngs = walk('_superseded','.png')
print("png count", len(pngs))
corpus = {}
for f in os.listdir('02-讲义'):
    if f.endswith('.md'):
        corpus[f] = open(os.path.join('02-讲义',f), encoding='utf-8', errors='replace').read()

okB=[]; skipB=[]
for p in sorted(pngs):
    b64 = base64.b64encode(open(p,'rb').read()).decode()
    hits = [f for f,t in corpus.items() if b64 in t]
    if hits: okB.append({"file":p,"bytes":os.path.getsize(p),"md":hits})
    else: skipB.append(p)
print("B ok", len(okB), "skip", len(skipB))
print("  skipB sample:", skipB[:5])

json.dump({"A":okA,"B":okB,"skipA":skipA,"skipB":skipB}, open(__import__('tempfile').gettempdir()+'/_deletelist.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print("bytesA", sum(x["bytes"] for x in okA))
print("bytesB", sum(x["bytes"] for x in okB))
print("bytesB_skip", sum(os.path.getsize(p) for p in skipB))
