import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

interface Post {
  id: number;
  title: string;
  summary: string;
}

export default function InfoPage() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token"); // 或直接写死 token: const token = "admin_token";
    if (!token) {
      // 没有 token，重定向到首页
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

        if (!res.ok) {
          const data = await res.json();
          throw new Error(data.error || `请求失败: ${res.status}`);
        }

        const data: Post[] = await res.json();
        setPosts(data);
      } catch (err: any) {
        setError("获取文章失败: " + err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, [navigate]);

  if (loading) return <p className="text-center mt-10">加载中...</p>;
  if (error) return <p className="text-center text-red-500 mt-10">{error}</p>;

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-6 bg-gray-50">
      <h1 className="text-2xl font-bold mb-6">服务器返回文章列表</h1>
      <ul className="w-full max-w-3xl space-y-4">
        {posts.map((post) => (
          <li
            key={post.id}
            className="p-4 border rounded shadow bg-white text-left"
          >
            <h2 className="text-lg font-semibold">{post.title}</h2>
            <p className="text-sm text-gray-600">{post.summary}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
