import React from "react";
import { Link } from "react-router-dom"; // ⭐ 引入 Link

export default function GenericHeader() {
  return (
    <header className="bg-base-100 shadow sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4 flex items-center justify-between h-14">
        {/* 左侧 Logo 和 搜索 */}
        <div className="flex items-center space-x-4">
          {/* 通用 Logo */}
          <div className="flex-shrink-0 text-xl font-bold text-primary">
            MyApp
          </div>

          {/* 搜索框 */}
          <label className="input input-bordered flex items-center gap-2 h-9">
            <input
              type="text"
              placeholder="搜索内容"
              className="grow text-sm"
            />
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-4 w-4 opacity-70"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth="2"
            >
              <circle cx="11" cy="11" r="7" />
              <line x1="16.65" y1="16.65" x2="21" y2="21" />
            </svg>
          </label>
        </div>

        {/* 中间导航菜单 */}
        <nav className="hidden md:flex space-x-6">
          {["首页", "人脉", "职位", "消息", "通知", "我"].map((item, index) => (
            <a
              key={index}
              href="#"
              className="text-sm text-base-content hover:text-primary"
            >
              {item}
            </a>
          ))}
        </nav>

        {/* 右侧操作按钮 */}
        <div className="hidden md:flex items-center space-x-2">
          <button className="btn btn-ghost btn-sm">商务</button>
          <button className="btn btn-outline btn-sm">免费试用</button>

          {/* 登录按钮 👉 改成 Link */}
          <Link to="/login">
            <button className="btn btn-primary btn-sm">登录</button>
          </Link>
        </div>
      </div>
    </header>
  );
}
