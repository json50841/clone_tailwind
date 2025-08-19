import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./Navbar";
import JobsPage from "./pages/JobsPage";
import LoginPage from "./pages/login/LoginPage";
import Dashboard from "./pages/login/Dashboar"; // ✅ 保证文件名一致
import TestLoginPage from "./TestLoginPage";

// 404 页面组件
function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center h-screen text-center">
      <h1 className="text-6xl font-bold text-red-500">404</h1>
      <p className="text-lg mt-4">抱歉，您访问的页面不存在。111</p>
      <a href="/" className="mt-6 text-blue-500 underline">
        返回首页
      </a>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <div className="p-6">
        <Routes>
          {/* 首页 */}
          <Route
            path="/"
            element={
              <>
                <h1 className="text-3xl font-bold">欢迎来到 DaisySite</h1>
                <JobsPage />
              </>
            }
          />
          {/* 登录页 */}
          <Route path="/login" element={<LoginPage />} />
          {/* 测试登录页 */}
          <Route path="/TestLoginPage" element={<TestLoginPage />} />
          {/* 仪表盘 */}
          <Route path="/dashboard" element={<Dashboard />} />
          {/* ✅ 兜底 404 */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
