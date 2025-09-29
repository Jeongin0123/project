import CommentBox from "./CommentBox.jsx";
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

export default function PostCard({ post }) {
  const [likes, setLikes] = useState(post.likes_count || 0);
  const [comments, setComments] = useState(post.comments || []);

  const addLike = async () => {
    try {
      await api(`/likes/${post.id}`, { method: "POST" });
      setLikes((l) => l + 1);
    } catch (e) {
      alert("좋아요 실패: " + e.message);
    }
  };

  const addComment = async (content) => {
    try {
      const newComment = await api(`/comments/${post.id}`, {
        method: "POST",
        body: { content },
      });
      setComments((prev) => [...prev, newComment]);
    } catch (e) {
      alert("댓글 실패: " + e.message);
    }
  };

  return (
    <div className="border rounded-2xl p-4 bg-white">
      <h3 className="font-bold text-lg">{post.title}</h3>
      <p className="text-gray-700 mt-2">{post.content}</p>

      <div className="flex items-center gap-4 mt-4">
        <button
          onClick={addLike}
          className="text-sm bg-indigo-500 text-white rounded-lg px-3 py-1"
        >
          ❤️ {likes}
        </button>
      </div>

      <div className="mt-4 space-y-2">
        <p className="font-semibold">댓글</p>
        {comments.map((c) => (
          <div key={c.id} className="text-sm border-b pb-1">
            {c.content}
          </div>
        ))}
        <CommentBox onSubmit={addComment} />
      </div>
    </div>
  );
}
