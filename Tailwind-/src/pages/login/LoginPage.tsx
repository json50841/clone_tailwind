import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

interface LoginResponse {
  message?: string;
  token?: string;
  error?: string;
}

export default function LoginPage() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    try {
      const res = await fetch(
        "https://improved-zebra-wrj5jrrqgq54cvgwq-8000.app.github.dev/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ username, password }),
        }
      );

      const data: LoginResponse = await res.json();

      if (res.ok && data.token) {
        // 保存 token
        localStorage.setItem("token", data.token);
        // 跳转到 Dashboard 并通过 URL 传 token
        navigate(`/dashboard?token=${data.token}`);
      } else {
        setError(data.error || "登录失败");
      }
    } catch (err) {
      console.error(err);
      setError("网络或服务器错误");
    }
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="card w-96 bg-base-100 shadow-xl">
        <div className="card-body">
          <h2 className="card-title">登录</h2>
          <form onSubmit={handleLogin} className="flex flex-col gap-4">
            <input
              type="text"
              placeholder="用户名"
              className="input input-bordered"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <input
              type="password"
              placeholder="密码"
              className="input input-bordered"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            {error && <p className="text-red-500 text-sm">{error}</p>}
            <button type="submit" className="btn btn-primary">
              登录
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
