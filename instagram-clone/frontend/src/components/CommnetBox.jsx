import { useState } from "react";

export default function CommentBox({ onSubmit }) {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    const v = text.trim();
    if (!v) return;
    setLoading(true);
    try {
      await onSubmit?.(v);
      setText("");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={submit} className="flex items-center gap-2">
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="댓글 달기..."
        className="flex-1 rounded-lg border px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
      />
      <button
        disabled={loading || !text.trim()}
        className="px-3 py-2 text-sm rounded-lg bg-indigo-600 text-white disabled:opacity-40"
      >
        등록
      </button>
    </form>
  );
}
