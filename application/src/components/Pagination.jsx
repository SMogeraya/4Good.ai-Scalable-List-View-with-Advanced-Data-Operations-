import { Button, Box } from "@mui/material";

export default function Pagination({ page, pages, setPage }) {
  return (
    <Box sx={{ display: "flex", justifyContent: "center", mt: 3 }}>
      <Button disabled={page === 1} onClick={() => setPage(page - 1)}>
        Prev
      </Button>
      <Button disabled={page === pages} onClick={() => setPage(page + 1)}>
        Next
      </Button>
    </Box>
  );
}
