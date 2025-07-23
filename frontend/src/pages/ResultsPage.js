// frontend/src/pages/ResultsPage.js
import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

const ResultsPage = () => {
  const { userId } = useParams(); // URL pattern: /results/:userId
  const [userSkills, setUserSkills] = useState([]);
  const [missingSkills, setMissingSkills] = useState([]);
  const [roadmap, setRoadmap] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchResults = async () => {
      try {
        const res = await axios.get(`/api/analyze/results/${userId}`);
        const data = res.data;

        setUserSkills(data.user_skills || []);
        setMissingSkills(data.missing_skills || []);
        setRoadmap(data.roadmap || []);
      } catch (err) {
        setError("Failed to fetch analysis results.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchResults();
  }, [userId]);

  if (loading) return <p className="p-8 text-lg">Loading results...</p>;
  if (error) return <p className="p-8 text-red-600">{error}</p>;

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-4">📊 Skill Gap Analysis Results</h1>

      <div className="mb-6">
        <h2 className="text-xl font-semibold mb-2 text-green-700">✅ Your Current Skills</h2>
        <ul className="list-disc ml-6">
          {userSkills.map((skill, index) => (
            <li key={index}>{skill}</li>
          ))}
        </ul>
      </div>

      <div className="mb-6">
        <h2 className="text-xl font-semibold mb-2 text-red-700">⚠️ Missing Skills</h2>
        {missingSkills.length > 0 ? (
          <ul className="list-disc ml-6">
            {missingSkills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>
        ) : (
          <p>No major skill gaps detected. Great job!</p>
        )}
      </div>

      <div>
        <h2 className="text-xl font-semibold mb-2 text-blue-700">🗺️ Personalized Roadmap</h2>
        {roadmap.length > 0 ? (
          <ol className="list-decimal ml-6 space-y-2">
            {roadmap.map((step, index) => (
              <li key={index}>{step}</li>
            ))}
          </ol>
        ) : (
          <p>No roadmap needed — you’re all set!</p>
        )}
      </div>
    </div>
  );
};

export default ResultsPage;
