// frontend/src/App.js
import React, { useEffect, useState } from "react";
import { fetchJobs, addJob, generateCoverLetter } from "./api";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedJob, setSelectedJob] = useState(null);
  const [coverLetter, setCoverLetter] = useState("");
  const [applicantName, setApplicantName] = useState("");
  const [skills, setSkills] = useState("");

  useEffect(() => {
    loadJobs();
  }, []);

  async function loadJobs() {
    setLoading(true);
    try {
      const data = await fetchJobs();
      setJobs(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  async function handleGenerateCoverLetter(job) {
    if (!applicantName || !skills) {
      alert("Please enter your name and skills first.");
      return;
    }
    setSelectedJob(job);
    setLoading(true);
    try {
      const result = await generateCoverLetter(job, applicantName, skills);
      setCoverLetter(result.cover_letter || result);
    } catch (error) {
      console.error(error);
      alert("Error generating cover letter.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="App">
      <h1>ApplyMate — Job Application Tracker</h1>

      <div className="input-section">
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

      {loading && <p>Loading...</p>}

      <h2>Available Jobs</h2>
      <ul className="job-list">
        {jobs.map((job) => (
          <li key={job.id} className="job-item">
            <strong>{job.title}</strong> — {job.company} ({job.location})
            <div>
              <button onClick={() => handleGenerateCoverLetter(job)}>
                Generate Cover Letter
              </button>
            </div>
          </li>
        ))}
      </ul>

      {selectedJob && coverLetter && (
        <div className="cover-letter-section">
          <h3>Cover Letter for {selectedJob.title}</h3>
          <pre>{coverLetter}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
