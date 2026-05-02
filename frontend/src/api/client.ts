import axios from "axios";

/** バックエンド API クライアント。Vite の /api プロキシ経由で FastAPI に接続する。 */
export const apiClient = axios.create({
  baseURL: "/api",
  timeout: 10_000,
});
