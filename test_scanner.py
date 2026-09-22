from pathlib import Path
import json, subprocess, sys
root=Path(r"C:\BrainIX\Arc Early Intelligence")
files=[root/"live_fixture.json",root/"live_fixture_2.json"]
rows=[]
for f in files:
    x=json.loads(f.read_text(encoding="utf-8-sig"))
    holders=int(x["token"].get("holders_count") or 0)
    assert holders >= 0
    assert x["block_number"] > 0
    assert x["tx_hash"].startswith("0x")
print("TEST_PASS fixtures=2 read_only=true")
