import json, urllib.request, pathlib, datetime, concurrent.futures
BASE='https://whatsupindonesia.id/data/live/'
FILES={'gempa':'gempa.geojson','hotspot':'titik_panas.geojson','banjir':'banjir_bnpb.geojson','gunung':'gunung_api.geojson','laporan':'laporan.geojson','cuaca':'peringatan.geojson'}
def get(pair):
 k,f=pair
 with urllib.request.urlopen(BASE+f,timeout=45) as r: d=json.load(r)
 assert d.get('type')=='FeatureCollection'
 return k,d
out=dict(concurrent.futures.ThreadPoolExecutor(6).map(get,FILES.items()))
with urllib.request.urlopen(BASE+'meta.json',timeout=45) as r: out['meta']=json.load(r)
out['disalin']=datetime.datetime.now(datetime.timezone.utc).isoformat()
pathlib.Path('data').mkdir(exist_ok=True)
pathlib.Path('live.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':')))
