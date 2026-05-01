# CLAUDE.md — tech-news-aggregator

このファイルは Claude Code 用のプロジェクトガイドです。
新しい依頼を受けるたびに、このファイル → 該当する `docs/` 配下の仕様書 → 関連コードの順に読み込んでください。

## 1. プロジェクト概要

| 項目 | 内容 |
|------|------|
| 名称 | tech-news-aggregator |
| 目的 | 分散している技術情報を1箇所に集約し、日本語要約とジャンル別優先表示で効率よくキャッチアップする個人用 Web アプリ |
| 利用環境 | Web アプリ（PC・スマホ両対応のレスポンシブ） |

## 2. 技術スタック

| レイヤー | 技術 |
|---------|------|
| バックエンド | Python 3.12+ / FastAPI |
| 定期実行 | APScheduler |
| フロントエンド | React 18 + TypeScript + Vite + Tailwind CSS + TanStack Query + axios |
| データベース | PostgreSQL（Supabase 無料枠） |
| ORM | SQLAlchemy 2.x + Alembic |
| AI | Claude Haiku API（model: `claude-haiku-4-5-20251001`） |
| バックエンドデプロイ | Railway |
| フロントエンドデプロイ | Vercel |
| E2E テスト | Playwright MCP |

## 3. ディレクトリ構成

```
.
├── backend/                  # FastAPI バックエンド
│   ├── app/
│   │   ├── api/              # ルーター
│   │   ├── core/             # 設定・DB・共通ユーティリティ
│   │   ├── models/           # SQLAlchemy モデル
│   │   ├── schemas/          # Pydantic スキーマ
│   │   ├── services/         # ビジネスロジック（収集・要約・分類）
│   │   └── main.py           # FastAPI エントリポイント
│   ├── tests/                # pytest テスト
│   ├── alembic/              # マイグレーション
│   ├── pyproject.toml
│   └── requirements.txt
├── frontend/                 # React フロントエンド
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api/              # axios クライアント
│   │   ├── hooks/
│   │   └── App.tsx
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── tailwind.config.ts
├── docs/                     # API 仕様書・スプリント計画
│   ├── overview.md
│   ├── api/
│   ├── sprints/
│   └── feedback-history.md   # PlanReviewer / CodeReviewer の指摘履歴
├── .claude/
│   └── agents/               # サブエージェント定義（4種）
├── .mcp.json                 # GitHub MCP / Playwright MCP 設定
├── .env.example              # 環境変数のキー一覧（値は書かない）
└── CLAUDE.md                 # このファイル
```

## 4. コーディング規約

### 共通

- 関数・変数・ファイル名は意味の伝わる英語で書く
- コメントは日本語で書く
- 不要なコメントは書かない（命名と型で意図が伝わるなら不要）
- 1ファイルあたりの責務を1つに絞る

### Python（バックエンド）

- PEP 8 準拠
- フォーマッタ: `ruff format`
- リンタ: `ruff check`
- 型チェック: `mypy --strict`
- 関数・メソッドの引数と戻り値には**必ず型ヒントを付ける**
- Pydantic v2 のスキーマで API 入出力を定義する
- SQLAlchemy 2.x の typed mapping を使う

### TypeScript（フロントエンド）

- `tsconfig.json` で `"strict": true` を有効化する
- 型は `any` を禁止（明確に許可する場合のみ `unknown` を使う）
- フォーマッタ: `prettier`
- リンタ: `eslint`
- React コンポーネントは関数コンポーネント + Hooks のみ
- API レスポンスは Zod でランタイム検証する（任意・段階導入）

## 5. API 命名規則

- パス: スネークケース（例: `/articles/recent`, `/genres/{genre_id}`）
- HTTP メソッド: REST に従う
- ステータスコード: 標準に従う（200 / 201 / 204 / 400 / 401 / 403 / 404 / 409 / 422 / 500）

## 6. エラーハンドリング方針

### バックエンド

- 業務エラーは独自例外クラス（`AppError`）で表現し、FastAPI の `exception_handler` で JSON に変換する
- 想定外のエラーは 500 を返しつつログに stack trace を出力
- 入力検証は Pydantic に任せる（生 dict を直接触らない）

### フロントエンド

- API エラーはグローバルな axios interceptor で捕捉し、トースト等で表示
- 期待される業務エラー（404 など）は呼び出し側で個別に handling

## 7. 環境変数の管理方針

- すべての秘匿情報は `.env` に記載し、絶対にコミットしない
- `.env.example` にはキー名のみを書く
- `.mcp.json` はトークンを直接書かず `${ENV_VAR}` 形式で参照する
- 必要な環境変数:
  - `ANTHROPIC_API_KEY`: Claude Haiku API キー
  - `GITHUB_PERSONAL_ACCESS_TOKEN`: GitHub MCP 用
  - `DATABASE_URL`: Supabase PostgreSQL 接続文字列
  - `SUPABASE_URL` / `SUPABASE_ANON_KEY` / `SUPABASE_SERVICE_ROLE_KEY`: Supabase クライアント用

## 8. サブエージェント運用

開発フローは以下の通り。詳細は `.claude/agents/*.md` を参照。

```
Planner → PlanReviewer → Implementer → CodeReviewer
```

- **Planner**: 何を作るかを明確にしタスク分解する（実装はしない）
- **PlanReviewer**: Planner の計画をレビュー・差し戻し（修正提案はしない）
- **Implementer**: 設計・実装・ユニット/APIテスト・コミット
- **CodeReviewer**: コードレビュー・PR 作成・E2E テスト

## 9. コミット・PR

- コミット: Conventional Commits（`feat: ...`, `fix: ...`, `docs: ...`, `test: ...`, `refactor: ...`, `chore: ...`）
- PR は CodeReviewer がスプリント完了時に作成する
- マージは手動（ユーザーが確認してから）

## 10. テスト方針

- 各スプリントでユニットテスト・API テストをセットで作成（カバレッジ 80% 以上）
- 全スプリント完了後に E2E テストを Playwright で一括実施

## 11. 使用中スキル一覧

スキルを追加するたびに Implementer がこのセクションを更新する。

- （現時点で承認・インストール済みのスキルなし）

## 12. 過去の指摘履歴

PlanReviewer・CodeReviewer の指摘事項は `docs/feedback-history.md` に記録される。
Planner / Implementer は計画・実装の前にこのファイルを参照し、同じ指摘の再発を避けること。
