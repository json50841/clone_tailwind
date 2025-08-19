import JobCard from "../components/JobCard";

export default function JobsPage() {
  const jobs = [
    {
      id: 1,
      title: "Data Analyst",
      company: "Example Inc.",
      location: "San Francisco, CA",
      shortDescription: "负责日常数据分析和报表制作，协助业务部门制定决策。",
      fullDescription:
        "负责日常数据分析和报表制作，协助业务部门制定决策。工作包括收集、清洗、分析和可视化数据，运用统计方法和数据挖掘技术识别业务趋势，为公司战略提供数据支持。"
    },
    {
      id: 2,
      title: "Junior Data Scientist",
      company: "Tech Co.",
      location: "Oakland, CA",
      shortDescription: "参与机器学习模型训练与数据处理。",
      fullDescription:
        "参与机器学习模型训练与数据处理，协助资深数据科学家进行特征工程、模型优化与结果解读。需要具备一定的 Python 编程能力，熟悉 Pandas、NumPy、Scikit-learn 等工具。"
    }
  ];

  return (
    <div className="p-6 grid gap-4">
      {jobs.map((job) => (
        <JobCard key={job.id} job={job} />
      ))}
    </div>
  );
}
