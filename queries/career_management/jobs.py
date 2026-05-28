from queries.executor import _execute_query
from queries.generic_queries import *

from datetime import date, timedelta


def get_all_jobs():
    return get_records("jobs")


def get_job_by_id(job_id):
    return get_records("jobs", filters={"job_id": job_id}, single=True)


def check_job_exists(job_id):
    return check_entity_exists("jobs", "job_id", job_id)


def create_job(company_id, title, location, description, work_mode, job_type, salary_min, salary_max, currency, posted_date, application_deadline, source_url):
    
    payload = {"company_id": company_id,
               "title": title,
               "location": location,
               "description": description,
               "work_mode": work_mode,
               "job_type": job_type,
               "salary_min": salary_min,
               "salary_max": salary_max,
               "currency": currency,
               "posted_date": posted_date,
               "application_deadline": application_deadline,
               "source_url": source_url
               }
    
    new_row = insert_record("jobs",payload)
    return new_row


def update_job(job_id, title, location, description, work_mode, job_type, salary_min, salary_max, currency, posted_date, application_deadline, source_url):

    payload = {"title": title,
               "location": location,
               "description": description,
               "work_mode": work_mode,
               "job_type": job_type,
               "salary_min": salary_min,
               "salary_max": salary_max,
               "currency": currency,
               "posted_date": posted_date,
               "application_deadline": application_deadline,
               "source_url": source_url}
    
    updated_row = update_record("jobs","job_id",job_id,payload)
    return updated_row


def search_jobs_by_title(keyword):
    return get_records("jobs", search_columns=["title"], search_query=keyword, partial_match=True)


def search_jobs_by_location(keyword):
    return get_records("jobs", search_columns=["location"], search_query=keyword, partial_match=True)


def search_jobs_by_company(keyword):
    query = '''
    select c.company_id, c.name, j.*
    from companies as c 
    left join jobs as j on c.company_id = j.company_id
    where c.name ILIKE %s
    order by c.company_id'''

    params = (f"%{keyword}%")

    return _execute_query(query, params, "fetchall")


def get_jobs_by_job_type(job_type):
    return get_records("jobs", filters={"job_type":job_type})


def get_recent_job_listings():

    cutoff_date = (
        date.today() - timedelta(days=30)
    )

    query = """
        SELECT
            j.job_id,
            c.name AS company_name,
            j.title,
            j.location,
            j.work_mode,
            j.job_type,
            j.posted_date
        FROM jobs j
        JOIN companies c
            ON j.company_id = c.company_id
        WHERE j.posted_date >= %s
        ORDER BY j.posted_date DESC;
    """

    return _execute_query(
        query,
        (cutoff_date,),
        fetch="all"
    )



def get_job_market_summary():


    query = """
        SELECT

            COUNT(*) AS total_jobs,

            COUNT(DISTINCT company_id)
            AS total_companies_hiring,

            COUNT(*) FILTER (
                WHERE job_type = 'Full-time'
            ) AS full_time_jobs,

            COUNT(*) FILTER (
                WHERE job_type = 'Part-time'
            ) AS part_time_jobs,

            COUNT(*) FILTER (
                WHERE job_type = 'Working Student'
            ) AS working_student_jobs,

            COUNT(*) FILTER (
                WHERE job_type = 'Internship'
            ) AS internship_jobs,

            COUNT(*) FILTER (
                WHERE job_type = 'Contract'
            ) AS contract_jobs,

            (
                SELECT location
                FROM jobs
                WHERE location IS NOT NULL
                GROUP BY location
                ORDER BY COUNT(*) DESC
                LIMIT 1
            ) AS top_hiring_location,

            COUNT(*) FILTER (
                WHERE posted_date >= CURRENT_DATE - INTERVAL '30 days'
            ) AS recent_jobs_last_30_days

        FROM jobs;
    """

    return _execute_query(
        query,
        fetch="one"
    )

