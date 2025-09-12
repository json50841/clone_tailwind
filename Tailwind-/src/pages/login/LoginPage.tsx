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
        "https://improved-zebra-wrj5jrrqgq54cvgwq-8000.app.github.dev/login/",
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
        // Save token
        localStorage.setItem("token", data.token);
        // Redirect to dashboard
        navigate("/dashboard");
      } else {
        setError(data.error  || "Login failed");
      }
    } catch (err) {
      console.error(err);
      setError("Network or server error");
    }
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="card w-96 bg-base-100 shadow-xl">
        <div className="card-body">
          <h2 className="card-title">Login</h2>
          <form onSubmit={handleLogin} className="flex flex-col gap-4">
            <input
              type="text"
              placeholder="Username"
              className="input input-bordered"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <input
              type="password"
              placeholder="Password"
              className="input input-bordered"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            {error && <p className="text-red-500 text-sm">{error}</p>}
            <button type="submit" className="btn btn-primary">
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
