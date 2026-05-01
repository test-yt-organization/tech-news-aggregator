# Sprint 1 計画 — プロジェクト初期化・環境構築

## 1. 機能要件

依頼書の Sprint 1 として、以下を整備する。

- リポジトリ直下に開発の土台となる構成を整える
- Claude Code のサブエージェント方式（Planner / PlanReviewer / Implementer / CodeReviewer）の定義ファイルを揃える
- `CLAUDE.md` をプロジェクトの規約・ガイドとして整備
- `.mcp.json` で GitHub MCP / Playwright MCP を設定（トークンは `.env` 参照）
- `.env.example` で必要な環境変数キーを列挙
- バックエンド（FastAPI）と フロントエンド（React + TS + Vite + Tailwind）の最小雛形を生成
- `docs/` 配下に仕様書とスプリント計画・指摘履歴ファイルの土台を用意

## 2. 受け入れ条件

- `.claude/agents/` に 4 ファイル（planner.md / plan-reviewer.md / implementer.md / code-reviewer.md）が存在し、各ファイルの frontmatter で `tools` が依頼書通りに制限されていること
- `CLAUDE.md` がプロジェクト直下に存在し、技術スタック・規約・環境変数方針・サブエージェントフローを含むこと
- `.mcp.json` がトークンを直接含まず `${ENV_VAR}` 参照で書かれていること
- `.env.example` が存在し、`.env` が `.gitignore` に含まれていること（既存の Python テンプレートでカバー済み）
- `backend/` 配下に FastAPI アプリの最小雛形があり `GET /health` が `{"status": "ok"}` を返すユニットテストが存在すること
- `frontend/` 配下に Vite + React + Tailwind の最小雛形があり `npm install && npm run build` で成立する形になっていること（実際の install は別途）
- `docs/overview.md` / `docs/feedback-history.md` / `docs/sprints/` / `docs/api/` が存在すること
- `feature/sprint-1-init` ブランチで初回コミットされ、リモートに push されていること

## 3. 技術的制約

- 依頼書で明記された技術スタックから逸脱しない
- フロントエンドは UI ライブラリを入れず Tailwind + 自前コンポーネントで構築（追加は Sprint 4 以降に必要が出てから検討）
- 環境変数は `.env` で管理。コミットしない
- `.mcp.json` も同様に値を直接含めない

## 4. タスク一覧

| # | タスク | 依存 |
|---|--------|------|
| 1 | 作業ブランチ `feature/sprint-1-init` を作成 | - |
| 2 | `.claude/agents/` の 4 ファイルを作成 | 1 |
| 3 | `CLAUDE.md` を作成 | 1 |
| 4 | `.mcp.json` / `.env.example` を作成 | 1 |
| 5 | `backend/` 雛形を作成（FastAPI + /health + テスト） | 1 |
| 6 | `frontend/` 雛形を作成（Vite + React + Tailwind） | 1 |
| 7 | `docs/` 構造と `feedback-history.md` を作成 | 1 |
| 8 | `.gitignore` 拡張（frontend 用）→ コミット → push | 2-7 |

## 5. リスクと不明点

- Supabase / Anthropic API キーは Sprint 1 完了時点で未取得（ユーザー回答済み）。実利用は Sprint 2 以降で必要になる
- `npm install` / `pip install` の実行は Sprint 1 範囲外。設定ファイルだけ揃える
- 初回 push は `feature/sprint-1-init` ブランチに対して行い、main への merge はユーザー判断
