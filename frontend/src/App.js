// frontend/src/api.js

const API_BASE_URL = "http://127.0.0.1:8000"; // Change if deployed

// Fetch all jobs from the backend
export async function fetchJobs() {
  const res = await fetch(`${API_BASE_URL}/jobs`);
  if (!res.ok) throw new Error("Failed to fetch jobs");
  return res.json();
}

// Add a new job to the database
export async function addJob(job) {
  const res = await fetch(`${API_BASE_URL}/jobs`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(job),
  });
  if (!res.ok) throw new Error("Failed to add job");
  return res.json();
}

// Generate a tailored cover letter using backend AI endpoint
export async function generateCoverLetter(job, applicantName, skills) {
  const res = await fetch(`${API_BASE_URL}/cover-letter`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      job: job,
      applicant_name: applicantName,
      skills: skills,
    }),
  });
  if (!res.ok) throw new Error("Failed to generate cover letter");
  return res.json();
}
