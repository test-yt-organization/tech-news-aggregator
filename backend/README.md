# tech-news-aggregator backend

FastAPI 製のバックエンド。

## セットアップ

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example ../.env  # 値を埋める
```

## 起動

```bash
uvicorn app.main:app --reload --port 8000
```

ヘルスチェック: <http://localhost:8000/health>

## テスト

```bash
pytest
```
