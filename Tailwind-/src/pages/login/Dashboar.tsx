import React, { useEffect, useState } from "react";

interface Post {
  id: number;
  title: string;
  summary: string;
}

export default function Dashboard() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchPosts = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        setError("未登录，请先登录");
        window.location.href = "/";
        return;
      }

      try {
        const res = await fetch(
          "https://improved-zebra-wrj5jrrqgq54cvgwq-8000.app.github.dev/posts/",
          {
            method: "GET",
            headers: {
              Authorization: `Token ${token}`,
            },
          }
        );

        if (!res.ok) {
          const text = await res.text();
          console.error("Server error:", res.status, text);
          throw new Error("请求失败");
        }

        const data: Post[] = await res.json();
        setPosts(data);
      } catch (err) {
        console.error("获取文章失败:", err);
        setError("获取文章失败，请先登录");
        // Clear token and redirect
        localStorage.removeItem("token");
        window.location.href = "/";
      }
    };

    fetchPosts();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">文章列表</h1>
      {error && <p className="text-red-500">{error}</p>}
      <ul className="space-y-4">
        {posts.map((post) => (
          <li key={post.id} className="p-4 border rounded-lg shadow">
            <h2 className="font-semibold">{post.title}</h2>
            <p>{post.summary}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
