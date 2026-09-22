import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(r"C:\BrainIX\Arc Early Intelligence")
FIX=Path(__import__("sys").argv[1]) if len(__import__("sys").argv)>1 else ROOT/"live_fixture.json"
OUT=ROOT/"signals.jsonl"

def score(x):
    pts=0; reasons=[]
    holders=int(x["token"].get("holders_count") or 0)
    if 0 < holders < 5000: pts+=2; reasons.append("low_holder_count")
    if int(x.get("token_transfer_count",0)) >= 6: pts+=2; reasons.append("dense_transfer_activity")
    if len(x.get("unique_wallets",[])) >= 4: pts+=2; reasons.append("coordinated_multi_wallet")
    if x.get("userop"): pts+=1; reasons.append("account_abstraction_bundle")
    vol=float(x["token"].get("volume_24h") or 0)
    if vol >= 100000: pts+=1; reasons.append("meaningful_volume")
    return pts,reasons

def main():
    x=json.loads(FIX.read_text(encoding="utf-8-sig"))
    pts,reasons=score(x)
    row={
      "signal_at":datetime.now(timezone.utc).isoformat(),
      "source_observed_at":x["observed_at"],
      "block_number":x["block_number"],
      "tx_hash":x["tx_hash"],
      "token":x["token"],
      "score":pts,
      "reasons":reasons,
      "candidate":pts>=5,
      "economic_edge_proven":False,
      "lead_time_vs_public_tools_sec":0,
      "read_only":True
    }
    with OUT.open("a",encoding="utf-8") as f: f.write(json.dumps(row)+"\n")
    print(json.dumps(row,indent=2))

if __name__=="__main__": main()

