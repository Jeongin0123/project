import { Link, Outlet, useLocation } from "react-router-dom";
import "./App.css";

export default function App() {
  const { pathname } = useLocation();

  return (
    <div>
      {/* 상단 네비게이션 */}
      <nav
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          padding: "12px 24px",
          background: "#4f46e5",
          color: "white",
        }}
      >
        <Link to="/" style={{ color: "white", textDecoration: "none", fontWeight: 700, fontSize: 18 }}>
          Instagram Clone
        </Link>

        <div style={{ display: "flex", gap: 16 }}>
          <Link
            to="/"
            style={{
              color: "white",
              textDecoration: pathname === "/" ? "underline" : "none",
              fontWeight: 500,
            }}
          >
            피드
          </Link>
          <Link
            to="/upload"
            style={{
              color: "white",
              textDecoration: pathname === "/upload" ? "underline" : "none",
              fontWeight: 500,
            }}
          >
            업로드
          </Link>
        </div>
      </nav>

      {/* 라우트가 그려질 자리 */}
      <main style={{ padding: 24, maxWidth: 960, margin: "0 auto" }}>
        <Outlet />
      </main>
    </div>
  );
}
