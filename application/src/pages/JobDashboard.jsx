import { useEffect, useState } from "react";
import { fetchJobs } from "../api";
import JobCard from "../components/JobCard";
import Filters from "../components/Filters";
import Pagination from "../components/Pagination";
import { CircularProgress, Typography } from "@mui/material";

export default function JobDashboard() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [pagination, setPagination] = useState({});
  const [filters, setFilters] = useState({ page: 1, limit: 10 });

  useEffect(() => {
    setLoading(true);
    fetchJobs(filters)
      .then((res) => {
        setJobs(res.data);
        setPagination(res.pagination);
      })
      .finally(() => setLoading(false));
  }, [filters]);

  if (loading) return <CircularProgress />;

  return (
    <>
      <Typography variant="h4" sx={{ mb: 3 }}>
        Job Listings Dashboard
      </Typography>

      <Filters filters={filters} setFilters={setFilters} />

      {jobs.length === 0 && <Typography>No jobs found.</Typography>}

      {jobs.map((job) => (
        <JobCard key={job._id} job={job} />
      ))}

      <Pagination
        page={pagination.page}
        pages={pagination.pages}
        setPage={(p) => setFilters({ ...filters, page: p })}
      />
    </>
  );
}
