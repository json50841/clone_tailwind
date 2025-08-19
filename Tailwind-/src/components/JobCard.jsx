import { useState } from "react";

export default function JobCard({ job }) {
  const [expanded, setExpanded] = useState(false);
  const [fullDesc, setFullDesc] = useState(job.shortDescription); // 初始是短描述
  const [loading, setLoading] = useState(false);

  const handleExpand = () => {
    if (!expanded) {
      setLoading(true);
      // 模拟 API 请求
      setTimeout(() => {
        setFullDesc(job.fullDescription);
        setExpanded(true);
        setLoading(false);
      }, 800);
    } else {
      setExpanded(false);
      setFullDesc(job.shortDescription);
    }
  };

  return (
    <div className="card bg-base-100 shadow-md hover:shadow-lg transition">
      <div className="card-body">
        <h2 className="card-title">{job.title}</h2>
        <p className="text-sm text-gray-500">{job.company}</p>
        <p className="text-sm">{job.location}</p>

        <div className="mt-2 transition-all duration-500 ease-in-out">
          {loading ? (
            <span className="loading loading-dots loading-sm text-primary"></span>
          ) : (
            <p className="text-sm leading-relaxed">{fullDesc}</p>
          )}
        </div>

        <div className="mt-3">
          <button
            className="btn btn-sm btn-outline"
            onClick={handleExpand}
            disabled={loading}
          >
            {expanded ? "收起内容" : "展开更多"}
          </button>
        </div>
      </div>
    </div>
  );
}
