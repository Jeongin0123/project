import { useEffect, useState } from "react";
import PostCard from "../components/PostCard.jsx";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

async function api(path) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) throw new Error((await res.text()) || res.statusText);
  return res.json();
}

export default function Feed() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api("/posts/")
      .then(setPosts)
      .catch((e) => console.error(e))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>로딩 중...</p>;

  return (
    <div className="space-y-6">
      {posts.length === 0 && <p>아직 게시물이 없습니다.</p>}
      {posts.map((p) => (
        <PostCard key={p.id} post={p} onDelete={(id) => setPosts(posts.filter((p) => p.id !== id))} />
      ))}
    </div>
  );
}
