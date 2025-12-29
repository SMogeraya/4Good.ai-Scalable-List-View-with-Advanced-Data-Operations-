import {
  Card,
  CardContent,
  Typography,
  Chip,
  Stack,
  Divider,
  Box
} from "@mui/material";

export default function JobCard({ job }) {
  return (
    <Card
      elevation={3}
      sx={{
        m: 3,
        width:'20%',
        display:'inline-block',
        borderRadius: 3,
        transition: "0.2s",
        "&:hover": {
          transform: "translateY(-2px)",
          boxShadow: 6
        }
      }}
    >
      <CardContent sx={{ p: 3 }}>

        {/* Title */}
        <Typography variant="h6" fontWeight={600}>
          {job.job_title || "No Title"}
        </Typography>

        {/* Company & Location */}
      <Typography
  variant="body2"
  color="text.secondary"
  sx={{
    mt: 0.5,
    display: "-webkit-box",
    WebkitLineClamp: 2,
    WebkitBoxOrient: "vertical",
    overflow: "hidden"
  }}
>
  {job.company} • {job.location}
</Typography>


        {/* Meta chips */}
        <Stack
          direction="row"
          spacing={1}
          sx={{ mt: 1.5, flexWrap: "wrap" }}
        >
          {job.industry && (
            <Chip
              label={job.industry}
              size="small"
              color={job.industry === "IT" ? "primary" : "default"}
            />
          )}
          {job.employment_type && (
            <Chip label={job.employment_type} size="small" />
          )}
          {job.posted_date && (
            <Chip
              label={`Posted: ${job.posted_date}`}
              size="small"
              variant="outlined"
            />
          )}
        </Stack>

        <Divider sx={{ my: 2 }} />

        {/* Description */}
        {/* <Box>
          <Typography
            variant="body2"
            sx={{
              color: "text.primary",
              display: "-webkit-box",
              WebkitLineClamp: 4,
              WebkitBoxOrient: "vertical",
              overflow: "hidden"
            }}
          >
            {job.description || "No description available."}
          </Typography>
        </Box> */}

      </CardContent>
    </Card>
  );
}
