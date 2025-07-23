// frontend/src/pages/Dashboard.js
import React, { useEffect, useState } from "react";
import { getDashboardData } from "../services/dashboardService";
import { useParams } from "react-router-dom";

const Dashboard = () => {
  const { userId } = useParams(); // Assuming URL like /dashboard/:userId
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const data = await getDashboardData(userId);
        setDashboardData(data);
      } catch (err) {
        setError("Failed to load dashboard data.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchDashboard();
  }, [userId]);

  if (loading) return <div className="p-4">Loading dashboard...</div>;
  if (error) return <div className="p-4 text-red-500">{error}</div>;

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">📊 SkillGapAnalyzer Dashboard</h1>

      <section className="mb-10">
        <h2 className="text-xl font-semibold mb-2">👤 Your Profile Overview</h2>
        <div className="bg-white p-4 rounded shadow">
          <p><strong>Name:</strong> {dashboardData.name}</p>
          <p><strong>Branch:</strong> {dashboardData.branch}</p>
          <p><strong>Registered Skills:</strong> {dashboardData.user_skills.join(", ")}</p>
          <p><strong>Total Skill Gaps:</strong> {dashboardData.skill_gaps.length}</p>
        </div>
      </section>

      <section className="mb-10">
        <h2 className="text-xl font-semibold mb-2">🚀 Recommended Roadmap</h2>
        <div className="bg-white p-4 rounded shadow">
          <ul className="list-disc pl-6">
            {dashboardData.recommended_roadmap.map((step, index) => (
              <li key={index}>{step}</li>
            ))}
          </ul>
        </div>
      </section>

      <section>
        <h2 className="text-xl font-semibold mb-2">🏫 Institute Summary (Anonymized)</h2>
        <div className="bg-white p-4 rounded shadow">
          <p><strong>Average Skill Gaps:</strong> {dashboardData.institute_summary.avg_gaps}</p>
          <p><strong>Top In-Demand Skills:</strong> {dashboardData.institute_summary.in_demand_skills.join(", ")}</p>
        </div>
      </section>
    </div>
  );
};

export default Dashboard;
