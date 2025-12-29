from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from database import jobs_collection

app = FastAPI(title="Job Listings Dashboard API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/jobs")
def get_jobs(
    page: int = 1,
    limit: int = 10,

    search: Optional[str] = None,
    location: Optional[str] = None,
    employment_type: Optional[str] = None,

    start_date: Optional[str] = None,
    end_date: Optional[str] = None,

    sort: Optional[str] = None
):
    skip = (page - 1) * limit
    query = {}


    if search:
        query["$or"] = [
            {"Title": {"$regex": search, "$options": "i"}},
            {"Company": {"$regex": search, "$options": "i"}},
            {"JobDescription": {"$regex": search, "$options": "i"}},
            {"jobpost": {"$regex": search, "$options": "i"}},
        ]

  
    if location:
        query["Location"] = location

    if employment_type:
        query["Term"] = employment_type

 
    if start_date or end_date:
        query["OpeningDate"] = {}
        if start_date:
            query["OpeningDate"]["$gte"] = start_date
        if end_date:
            query["OpeningDate"]["$lte"] = end_date

   
    sort_query = []
    if sort:
       
        for field in sort.split(","):
            key, direction = field.split("_")
            sort_query.append((key, -1 if direction == "desc" else 1))

    total = jobs_collection.count_documents(query)

    cursor = jobs_collection.find(query)

    if sort_query:
        cursor = cursor.sort(sort_query)

    raw_jobs = list(cursor.skip(skip).limit(limit))

  
    jobs = []
    for job in raw_jobs:
        jobs.append({
            "id": str(job.get("_id")),
            "job_title": job.get("Title"),
            "company": job.get("Company"),
            "location": job.get("Location"),
            "employment_type": job.get("Term"),
            "industry": "IT" if job.get("IT") == "TRUE" else "Non-IT",
            "posted_date": job.get("OpeningDate") or job.get("date"),
            "description": job.get("JobDescription"),
            "full_post": job.get("jobpost") 
        })

    return {
        "data": jobs,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": total,
            "pages": (total + limit - 1) // limit
        }
    }

# from fastapi import FastAPI, Query
# from typing import Optional
# from datetime import datetime
# from database import jobs_collection
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI(title="Job Listings Dashboard API")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/api/jobs")
# def get_jobs(
#     page: int = 1,
#     limit: int = 10,

#     search: Optional[str] = None,
#     location: Optional[str] = None,
#     employment_type: Optional[str] = None,
#     industry: Optional[str] = None,

#     start_date: Optional[str] = None,   # YYYY-MM-DD
#     end_date: Optional[str] = None,     # YYYY-MM-DD

#     sort: Optional[str] = None
# ):
#     skip = (page - 1) * limit
#     query = {}

#     # 🔍 Case-insensitive search
#     if search:
#         query["$or"] = [
#             {"job_title": {"$regex": search, "$options": "i"}},
#             {"company": {"$regex": search, "$options": "i"}},
#             {"description": {"$regex": search, "$options": "i"}}
#         ]

#     # 🎯 Categorical filters
#     if location:
#         query["location"] = location

#     if employment_type:
#         query["employment_type"] = employment_type

#     if industry:
#         query["industry"] = industry

#     # 📅 Date range filter
#     if start_date or end_date:
#         query["posted_date"] = {}
#         if start_date:
#             query["posted_date"]["$gte"] = start_date
#         if end_date:
#             query["posted_date"]["$lte"] = end_date

#     # 🔃 Sorting
#     sort_query = []
#     if sort:
#         # Example: sort=posted_date_desc,company_asc
#         for field in sort.split(","):
#             key, direction = field.split("_")
#             sort_query.append(
#                 (key, -1 if direction == "desc" else 1)
#             )

#     total = jobs_collection.count_documents(query)

#     cursor = jobs_collection.find(query)

#     if sort_query:
#         cursor = cursor.sort(sort_query)

#     jobs = list(cursor.skip(skip).limit(limit))

#     for job in jobs:
#         job["_id"] = str(job["_id"])

#     return {
#         "data": jobs,
#         "pagination": {
#             "page": page,
#             "limit": limit,
#             "total": total,
#             "pages": (total + limit - 1) // limit
#         }
#     }
