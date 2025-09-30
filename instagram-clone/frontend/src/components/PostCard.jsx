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

export default function PostCard({ post, onDelete }) {
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

  const deletePost = async () => {
    if (!window.confirm("이 게시물을 삭제할까요?")) return;
    try {
      await api(`/posts/${post.id}`, { method: "DELETE" });
      onDelete?.(post.id);
    } catch (e) {
      alert("삭제 실패: " + e.message);
    }
  };

  return (
    <div className="bg-white rounded-2xl shadow-md p-4 space-y-3">
      {/* 헤더: 작성자/삭제 */}
      <div className="flex justify-between items-center">
        <span className="font-bold text-gray-800">{post.user_name || "익명"}</span>
        <button
          onClick={deletePost}
          className="text-red-500 text-sm hover:underline"
        >
          삭제
        </button>
      </div>

      {/* 게시글 내용 */}
      <div>
        <h3 className="font-semibold text-gray-900">{post.title}</h3>
        <p className="text-gray-700 mt-1">{post.content}</p>
      </div>

      {/* 좋아요 버튼 */}
      <div className="flex items-center gap-4">
        <button
          onClick={addLike}
          className="text-sm bg-indigo-500 text-white rounded-lg px-3 py-1 hover:bg-indigo-600"
        >
          ❤️ {likes}
        </button>
      </div>

      {/* 댓글 */}
      <div className="space-y-2">
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
