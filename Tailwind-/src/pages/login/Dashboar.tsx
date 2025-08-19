import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

interface Post {
  id: number;
  title: string;
  summary: string;
}

export default function Dashboard() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      navigate("/", { replace: true });
      return;
    }

    const fetchPosts = async () => {
      try {
        const res = await fetch(
          "https://improved-zebra-wrj5jrrqgq54cvgwq-8000.app.github.dev/posts",
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );

        if (res.ok) {
          const data = await res.json();
          setPosts(data);
        } else {
          localStorage.removeItem("token");
          navigate("/", { replace: true });
        }
      } catch {
        setError("网络错误");
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, [navigate]);

  if (loading) return <p>加载中...</p>;
  if (error) return <p className="text-red-500">{error}</p>;

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/", { replace: true });
  };

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">后台文章管理</h1>
        <button className="btn btn-outline" onClick={handleLogout}>
          退出
        </button>
      </div>
      <ul className="space-y-4">
        {posts.map((post) => (
          <li key={post.id} className="p-4 border rounded shadow bg-white">
            <h2 className="text-lg font-semibold">{post.title}</h2>
            <p className="text-sm text-gray-600">{post.summary}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
