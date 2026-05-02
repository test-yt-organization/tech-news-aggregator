# tech-news-aggregator システム概要

## 目的

エンジニアとして必要な技術情報を集約し、日本語要約とジャンル別優先表示で効率よくキャッチアップするための個人用 Web アプリ。

## システム構成

```
[フロントエンド: React + Vite (Vercel)]
        │  HTTPS
        ▼
[バックエンド: FastAPI (Railway)]
        │  ├── 定期実行: APScheduler
        │  ├── AI 連携: Claude Haiku API
        │  └── データ永続化
        ▼
[PostgreSQL: Supabase]
```

## 全 API 一覧

スプリント進行に応じて随時追記する。

| メソッド | パス | 概要 | 仕様書 |
|---------|------|------|--------|
| GET | `/health` | ヘルスチェック | - |

（Sprint 2 以降で記事収集 API、Sprint 4 で記事一覧 API などを追加予定）

## 機能 ↔ API 対応表

| 機能 | 関連 API | 仕様書 |
|------|---------|--------|
| 情報収集 | （Sprint 2 で定義） | docs/api/articles.md |
| 要約・分類 | （Sprint 3 で定義） | docs/api/articles.md |
| ジャンル管理 | （Sprint 5 で定義） | docs/api/genres.md |
| 設定（保持期間） | （Sprint 9 で定義） | docs/api/settings.md |

## スプリント進捗

| Sprint | 状態 | 完了日 |
|--------|------|--------|
| Sprint 1 | 進行中 | - |
| Sprint 2〜10 | 未着手 | - |
