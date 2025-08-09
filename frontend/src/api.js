// frontend/src/api.js

const API_BASE = "http://localhost:8000/api"; // Update if deploying

export async function fetchJobs() {
  const res = await fetch(`${API_BASE}/jobs`);
  if (!res.ok) throw new Error("Failed to fetch jobs");
  return res.json();
}

export async function addJob(job) {
  const res = await fetch(`${API_BASE}/jobs`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(job),
  });
  if (!res.ok) throw new Error("Failed to save job");
  return res.json();
}

export async function generateCoverLetter(job, applicantName, skills) {
  const res = await fetch(`${API_BASE}/cover-letter/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ job, applicant_name: applicantName, skills }),
  });
  if (!res.ok) throw new Error("Failed to generate cover letter");
  return res.json();
}
