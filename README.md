# paranoai-web

https://parano-ai.com/ の公開ファイル（GitHub Pages）。ParanoAI 導入支援のLP。

- 見た目の正本: ParanoAI Design System https://claude.ai/artifact/RybqLTfsoDZ2QeSwMLuFuw （控え: ~/Desktop/Claude/03_projects/ParanoAI/design-system/）
- 文章の元: ~/Desktop/ai-training-lp/index.html（2026-10-09 に移植。旧URLはこちらへ転送）
- DNS: parano-ai.com（Cloudflare Registrar・DNS）→ GitHub Pages（A 185.199.108-111.153 ／ www CNAME sugipy.github.io、プロキシはオフ＝灰色雲）

## 作り（2026-10-10〜 Astro）

- **Astro 5 ＋ React の島**。トップは `src/pages/index.astro`。研修・LINE・お問い合わせは `public/` の素のHTMLをそのまま配信。
- **Arc UI（https://uiarc.dev 無料部品）** を `src/components/arc/` にソースごと同梱（in-view-title・activity-heatmap）。追加は `npx shadcn@latest add @uiarc/<名前>`。色は `src/styles/brand.css` 末尾で Arc のトークンをブランドの深緑に差し替え。activity-heatmap は表示文字を日本語化済み（再インストールすると英語に戻る）。Pro部品は未購入。
- **積み上げマス**のデータ = `python3 tools/gen_activity.py`（~/Desktop 直下リポジトリのこの100日のコミット数。日付と件数だけ）。更新したら commit。
- **公開**: main に push → GitHub Actions（`.github/workflows/deploy.yml`）がビルドして Pages へ。手元確認は `npm run build && npx astro preview`。
- **戻し方**: `gh api -X PUT repos/sugipy/paranoai-web/pages -f build_type=legacy -f source[branch]=main -f source[path]=/` ＋ 4842c4b の状態に revert。

## Slackアプリ「世界のAI同僚」（2026-10-10〜）

- 一覧 `public/doryo/index.html` → /doryo/ （インド・タイのLPと同じ装飾の素のHTML）。各LPは `public/doryo/<slug>/`（remind＝リマインド人／kintai＝勤タイ人／tsunagana＝ツナガーナ人／nippo＝ニッポー人・未作成）。
- 旧URLは転送のみ: `public/kintaijin/`、`public/line-flow/`（→ /doryo/tsunagana/）、ai-training-lp の `slack-remind/`。
- シリーズの正本表は `~/Desktop/Claude/03_projects/世界の同僚/README.md`。
