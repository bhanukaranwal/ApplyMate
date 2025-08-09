// frontend/src/App.js

import React, { useState, useEffect } from "react";
import { fetchJobs, addJob, generateCoverLetter } from "./api";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);
  const [formData, setFormData] = useState({ title: "", company: "", location: "", summary: "" });
  const [applicantName, setApplicantName] = useState("");
  const [skills, setSkills] = useState("");
  const [coverLetter, setCoverLetter] = useState("");
  const [loadingLetter, setLoadingLetter] = useState(false);

  // Load jobs on mount
  useEffect(() => {
    fetchJobs()
      .then(data => setJobs(data))
      .catch(err => console.error(err));
  }, []);

  const handleAddJob = async (e) => {
    e.preventDefault();
    try {
      const newJob = await addJob(formData);
      setJobs([...jobs, newJob]);
      setFormData({ title: "", company: "", location: "", summary: "" });
    } catch (err) {
      console.error(err);
    }
  };

  const handleGenerateLetter = async (job) => {
    setLoadingLetter(true);
    try {
      const { cover_letter } = await generateCoverLetter(job, applicantName, skills);
      setCoverLetter(cover_letter);
    } catch (err) {
      console.error(err);
    }
    setLoadingLetter(false);
  };

  return (
    <div className="app-container">
      <h1>ApplyMate — Job Tracker & Cover Letter Generator</h1>

      {/* Applicant Info */}
      <div className="applicant-info">
        <input
          type="text"
          placeholder="Your Name"
          value={applicantName}
          onChange={(e) => setApplicantName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Your Skills (comma separated)"
          value={skills}
          onChange={(e) => setSkills(e.target.value)}
        />
      </div>

      {/* Add Job Form */}
      <form className="job-form" onSubmit={handleAddJob}>
        <input
          type="text"
          placeholder="Job Title"
          value={formData.title}
          onChange={(e) => setFormData({ ...formData, title: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Company"
          value={formData.company}
          onChange={(e) => setFormData({ ...formData, company: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Location"
          value={formData.location}
          onChange={(e) => setFormData({ ...formData, location: e.target.value })}
        />
        <textarea
          placeholder="Job Summary"
          value={formData.summary}
          onChange={(e) => setFormData({ ...formData, summary: e.target.value })}
        />
        <button type="submit">Add Job</button>
      </form>

      {/* Job List */}
      <div className="job-list">
        {jobs.map((job, idx) => (
          <div className="job-card" key={idx}>
            <h3>{job.title} — {job.company}</h3>
            <p><strong>Location:</strong> {job.location}</p>
            <p>{job.summary}</p>
            <button onClick={() => handleGenerateLetter(job)}>
              {loadingLetter ? "Generating..." : "Generate Cover Letter"}
            </button>
          </div>
        ))}
      </div>

      {/* Cover Letter Output */}
      {coverLetter && (
        <div className="cover-letter">
          <h2>Your Tailored Cover Letter</h2>
          <pre>{coverLetter}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
