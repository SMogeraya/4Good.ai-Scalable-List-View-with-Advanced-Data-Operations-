import { TextField, MenuItem, Box } from "@mui/material";

export default function Filters({ filters, setFilters }) {
  return (
    <Box sx={{ display: "flex", gap: 2, mb: 3, flexWrap: "wrap" }}>
      <TextField
        label="Search"
        onChange={(e) =>
          setFilters({ ...filters, search: e.target.value, page: 1 })
        }
      />

      <TextField
        label="Location"
        onChange={(e) =>
          setFilters({ ...filters, location: e.target.value, page: 1 })
        }
      />

      <TextField
        label="Employment Type"
        select
        onChange={(e) =>
          setFilters({ ...filters, employment_type: e.target.value, page: 1 })
        }
      >
        <MenuItem value="">All</MenuItem>
        <MenuItem value="Full-time">Full-time</MenuItem>
        <MenuItem value="Part-time">Part-time</MenuItem>
      </TextField>

      <TextField
        type="date"
        label="From"
        InputLabelProps={{ shrink: true }}
        onChange={(e) =>
          setFilters({ ...filters, start_date: e.target.value, page: 1 })
        }
      />

      <TextField
        type="date"
        label="To"
        InputLabelProps={{ shrink: true }}
        onChange={(e) =>
          setFilters({ ...filters, end_date: e.target.value, page: 1 })
        }
      />
    </Box>
  );
}
