// frontend/src/pages/ReEvaluation.js
import React, { useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

const ReEvaluation = () => {
  const { userId } = useParams(); // URL pattern: /re-evaluation/:userId
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setMessage("");
    setError("");
  };

  const handleReupload = async () => {
    if (!file) {
      setError("Please select a resume file.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);
    formData.append("user_id", userId);

    try {
      setIsUploading(true);
      const response = await axios.post("/api/upload/re-evaluate", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setMessage("✅ Re-evaluation successful! Skill gaps and roadmap updated.");
      setError("");
    } catch (err) {
      setError("❌ Re-evaluation failed. Please try again.");
      setMessage("");
      console.error(err);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">♻️ Re-Evaluate Your Resume</h1>

      <div className="bg-white p-6 rounded shadow-md max-w-xl">
        <label className="block mb-4">
          <span className="text-gray-700 font-medium">Upload your updated resume (PDF):</span>
          <input
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
            className="mt-2 block w-full border p-2 rounded"
          />
        </label>

        <button
          onClick={handleReupload}
          disabled={isUploading}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
        >
          {isUploading ? "Uploading..." : "Re-Analyze"}
        </button>

        {message && <p className="mt-4 text-green-600">{message}</p>}
        {error && <p className="mt-4 text-red-600">{error}</p>}
      </div>
    </div>
  );
};

export default ReEvaluation;
