/** アプリケーションのルートコンポーネント。Sprint 4 で本実装する想定。 */
function App(): JSX.Element {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <header className="border-b bg-white">
        <div className="mx-auto max-w-5xl px-4 py-4">
          <h1 className="text-xl font-bold">tech-news-aggregator</h1>
          <p className="text-sm text-slate-500">技術情報を集約してジャンル別に表示する個人用アプリ</p>
        </div>
      </header>
      <main className="mx-auto max-w-5xl px-4 py-8">
        <p className="text-slate-700">Sprint 1 初期化完了。記事一覧画面は Sprint 4 で実装予定です。</p>
      </main>
    </div>
  );
}

export default App;
