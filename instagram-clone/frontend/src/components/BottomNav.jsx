import { Link } from "react-router-dom";
import { Home, Search, PlusCircle, Heart, User } from "lucide-react";

export default function BottomNav() {
  return (
    <nav
      style={{
        position: "fixed",
        bottom: 0,
        left: 0,
        width: "100%",
        background: "white",
        borderTop: "1px solid #e5e7eb",
        display: "flex",
        justifyContent: "space-around",
        padding: "8px 0",
        boxShadow: "0 -1px 5px rgba(0,0,0,0.1)",
        zIndex: 1000,
      }}
    >
      <Link to="/" style={{ textAlign: "center", color: "#111" }}>
        <Home size={24} />
        <div style={{ fontSize: 12 }}>홈</div>
      </Link>
      <Link to="/search" style={{ textAlign: "center", color: "#111" }}>
        <Search size={24} />
        <div style={{ fontSize: 12 }}>검색</div>
      </Link>
      <Link to="/upload" style={{ textAlign: "center", color: "#111" }}>
        <PlusCircle size={24} />
        <div style={{ fontSize: 12 }}>업로드</div>
      </Link>
      <Link to="/likes" style={{ textAlign: "center", color: "#111" }}>
        <Heart size={24} />
        <div style={{ fontSize: 12 }}>좋아요</div>
      </Link>
      <Link to="/profile" style={{ textAlign: "center", color: "#111" }}>
        <User size={24} />
        <div style={{ fontSize: 12 }}>프로필</div>
      </Link>
    </nav>
  );
}
