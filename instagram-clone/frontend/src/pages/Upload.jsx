import { useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

async function api(path, { method = "GET", body } = {}) {
  const headers = { "Content-Type": "application/json" };
  const res = await fetch(`${API_BASE}${path}`, {
    method,
    headers,
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) throw new Error((await res.text()) || res.statusText);
  return res.json();
}

export default function Upload() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) return alert("제목과 내용을 입력하세요.");
    setLoading(true);
    try {
      await api("/posts/", {
        method: "POST",
        body: { title: title.trim(), content: content.trim() },
      });
      alert("게시글이 등록되었습니다.");
      setTitle("");
      setContent("");
    } catch (e) {
      alert("등록 실패: " + e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-lg">
      <form onSubmit={submit} className="space-y-4 bg-white border rounded-2xl p-6">
        <input
          className="w-full border rounded-lg px-3 py-2"
          placeholder="제목"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          className="w-full border rounded-lg p-3 h-40"
          placeholder="내용"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <button
          className="w-full bg-indigo-600 text-white rounded-lg py-2 disabled:opacity-50"
          disabled={loading}
        >
          {loading ? "등록 중..." : "등록"}
        </button>
      </form>
    </div>
  );
}
