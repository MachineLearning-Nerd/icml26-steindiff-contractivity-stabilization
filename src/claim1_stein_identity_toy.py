"""Exact CPU toy for source gamma formula; not an end-to-end diffusion reproduction."""
import argparse
import csv
import json
import random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs/claim1_attempt1'
def mean(xs): return sum(xs)/len(xs)
def run(seed=20260802,n=200000,alpha=.8,sigma=.6,a=1.7):
 r=random.Random(seed); xs=[]; stars=[]
 for _ in range(n):
  stars.append(r.gauss(0,1)); xs.append(alpha*stars[-1]+sigma*r.gauss(0,1))
 u=[a*x for x in xs]; denom=mean([q*q for q in u]); direct=mean([q*(x-s) for q,x,s in zip(u,xs,stars)])/denom
 stein=((1-1/alpha)*mean([q*x for q,x in zip(u,xs)])+(sigma*sigma/alpha)*a)/denom
 return {'seed':seed,'n':n,'alpha':alpha,'sigma':sigma,'a':a,'direct_gamma_mc':direct,'stein_gamma_mc':stein,'absolute_difference':abs(direct-stein),'tolerance':.01}
def main(out=OUT):
 out=Path(out);out.mkdir(parents=True,exist_ok=True);d=run();d['pass']=d['absolute_difference']<d['tolerance'];(out/'summary.json').write_text(json.dumps(d,indent=2)+'\n')
 with open(out/'results.csv','w',newline='') as f:w=csv.DictWriter(f,fieldnames=d.keys());w.writeheader();w.writerow(d)
 (out/'PROTOCOL.md').write_text('Pre-execution fixed: seed 20260802; n=200000; alpha=.8; sigma=.6; u=1.7x; pass iff absolute direct-vs-Stein gamma difference below .01. Claim-1 formula toy only.\n')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',default=str(OUT));main(ap.parse_args().out)
