"""FastAPI エントリポイント。"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings


def create_app() -> FastAPI:
    """FastAPI アプリケーションを生成する。"""
    settings = get_settings()
    app = FastAPI(
        title="tech-news-aggregator",
        version="0.1.0",
        description="技術情報を収集・要約・ジャンル分類するアプリのバックエンド",
    )

    # CORS（フロントエンド開発サーバ向けに開発時のみ広く開ける）
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health", tags=["meta"])
    def health() -> dict[str, str]:
        """ヘルスチェック用エンドポイント。"""
        return {"status": "ok"}

    return app


app = create_app()
