// frontend/src/pages/UploadPage.js
import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const UploadPage = () => {
  const [file, setFile] = useState(null);
  const [jobRole, setJobRole] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file || !jobRole) {
      setError("Please upload your resume and select a job role.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);
    formData.append("job_role", jobRole);

    try {
      setLoading(true);
      const res = await axios.post("/api/upload", formData);
      const { user_id } = res.data;

      navigate(`/results/${user_id}`);
    } catch (err) {
      console.error(err);
      setError("Failed to upload resume. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-8 max-w-xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">📤 Upload Your Resume</h1>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-1">Select Resume (PDF or DOCX)</label>
          <input
            type="file"
            accept=".pdf,.doc,.docx"
            onChange={handleFileChange}
            className="block w-full border p-2 rounded"
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">Target Job Role</label>
          <input
            type="text"
            value={jobRole}
            onChange={(e) => setJobRole(e.target.value)}
            placeholder="e.g., Backend Developer"
            className="w-full border p-2 rounded"
          />
        </div>

        {error && <p className="text-red-600">{error}</p>}

        <button
          type="submit"
          disabled={loading}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {loading ? "Uploading..." : "Analyze Resume"}
        </button>
      </form>
    </div>
  );
};

export default UploadPage;
