// src/api.js
const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export default async function api(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    credentials: "include", // 세션 쿠키/토큰 쓰는 경우 필요
    ...options,
  });
  if (!res.ok) throw new Error((await res.text()) || res.statusText);
  return res.json();
}
