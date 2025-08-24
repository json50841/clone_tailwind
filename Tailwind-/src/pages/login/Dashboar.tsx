import React, { useEffect, useState } from "react";

interface Post {
  id: number;
  title: string;
  summary: string;
}

export default function Dashboard() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      setError("未登录，请先登录");
      setLoading(false);
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
          const errMsg = await res.text();
          setError(`获取文章失败: ${res.status} ${errMsg}`);
        }
      } catch (err: any) {
        setError("网络错误: " + err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setError("已退出，请重新登录");
    setPosts([]);
  };

  if (loading) return <p>加载中...</p>;
  if (error)
    return (
      <div className="p-6">
        <p className="text-red-500 mb-4">{error}</p>
        <button className="btn btn-primary" onClick={handleLogout}>
          退出
        </button>
      </div>
    );

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
