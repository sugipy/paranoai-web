#!/usr/bin/env python3
"""運営者（杉田）のこの100日のコミット数を日ごとに数え、トップの「積み上げ」マスのデータにする。

使い方: python3 tools/gen_activity.py  → src/data/activity.json を上書き
対象は ~/Desktop 直下の git リポジトリ。同じコミットが複数リポジトリ（複製・worktree）に出ても1回と数える。
出すのは日付と件数だけ（リポジトリ名・メッセージは出さない）。
"""
import json, subprocess
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

AUTHORS = {"hunterpresident@gmail.com", "36855334+sugipy@users.noreply.github.com", "sugipy@sugipynoMacBook-Pro.local"}
end = date.today()
DAYS = 100
start = end - timedelta(days=DAYS - 1)
seen, per_day = set(), Counter()
for repo in sorted(Path.home().joinpath("Desktop").iterdir()):
    if not (repo / ".git").exists():
        continue
    out = subprocess.run(["git", "-C", str(repo), "log", "--all", f"--since={start.isoformat()}", "--format=%H|%ae|%ad", "--date=short"],
                         capture_output=True, text=True).stdout
    for line in out.splitlines():
        h, email, d = line.split("|")
        if email in AUTHORS and h not in seen and start.isoformat() <= d <= end.isoformat():
            seen.add(h)
            per_day[d] += 1
days = [{"date": (start + timedelta(days=i)).isoformat(), "count": per_day.get((start + timedelta(days=i)).isoformat(), 0)} for i in range(DAYS)]
Path(__file__).resolve().parent.parent.joinpath("src/data/activity.json").write_text(json.dumps({"generated": end.isoformat(), "days": days}, ensure_ascii=False))
print(f"{start}〜{end}: コミット {sum(per_day.values())} 件 / 記録のある日 {sum(1 for d in days if d['count'])} 日 / 最多 {max(per_day.values())} 件")
