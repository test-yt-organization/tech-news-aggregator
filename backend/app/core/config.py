"""アプリケーション設定。環境変数から読み込む。"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """環境変数から読み込む設定値。"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # アプリケーション
    app_env: str = Field(default="development")
    log_level: str = Field(default="INFO")

    # CORS（カンマ区切り文字列を受け取り、リストに変換するのは利用側）
    cors_allow_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173"])

    # 外部 API
    anthropic_api_key: str = Field(default="")
    github_personal_access_token: str = Field(default="")

    # データベース
    database_url: str = Field(default="")
    supabase_url: str = Field(default="")
    supabase_anon_key: str = Field(default="")
    supabase_service_role_key: str = Field(default="")

    # アプリケーション動作設定
    article_retention_days: int = Field(default=30)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """設定をキャッシュ付きで取得する。"""
    return Settings()
