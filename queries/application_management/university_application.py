from queries.generic_queries import *
from queries.executor import _execute_query

from datetime import datetime



def generate_application_token(user_id, intake_id):
    """
    Generates a unique application attempt token for the database layer.
    Format: USERID-INTAKEID-YYYYMMDD-HHMM
    Example Output: "42-1-20260531-2221"
    """

    clean_user_id = int(user_id)
    clean_intake_id = int(intake_id)

    timestamp_str = datetime.now().strftime("%Y%m%d-%H%M")
    
    token = f"{clean_user_id}-{clean_intake_id}-{timestamp_str}"
    
    return token



def check_university_application_exist(university_application_id):
    return check_entity_exists("university_applications", "university_application_id", university_application_id)


def check_univeristy_application_uniqueness(user_id, intake_id, status_id):

    exists = get_records("university_applications", filters={"user_id": user_id, "intake_id": intake_id, "status_id": status_id}, single=True)

    if exists:
        print("Program already exists.")

        return False

    return True


def create_university_application(user_id, intake_id, status_id, application_guidance_token, target_year, application_platform, platform_url, notes, applied_date):

    payload = {"user_id": user_id,
               "intake_id": intake_id,
               "status_id": status_id,
               "application_guidance_token": application_guidance_token,
               "target_year": target_year,
               "application_platform": application_platform,
               "platform_url": platform_url,
               "notes": notes,
               "applied_date": applied_date}

    new_row = insert_record("university_applications", payload)
    return new_row


def update_university_application(university_application_id, status_id, target_year, application_platform, platform_url, notes, applied_date):

    payload = {"status_id": status_id,
               "target_year": target_year,
               "application_platform": application_platform,
               "platform_url": platform_url,
               "notes": notes,
               "applied_date": applied_date}
    
    updated_row = update_record("university_applications", "university_application_id", university_application_id, payload)
    return updated_row


def delete_university_application(university_application_id):
    return delete_records("university_applications", filters={"university_application_id": university_application_id}, single=True)


def get_university_tracker(user_id, search_input=None):

    query = '''
    select ua.university_application_id, un.name as university_name, p.name as program_name, i.name as intake_name, ua.application_platform, ast.status_name, ua.applied_Date
    from university_applications as ua
    join intakes as i on
    ua.intake_id = i.intake_id
    join programs as p on
    i.program_id = p.program_id
    join universities as un on
    p.university_id = un.university_id
    join application_statuses as ast on
    ua.status_id = ast.application_status_id
    where ua.user_id = %s'''

    if not search_input or search_input.strip() == "":
        query += " ORDER BY ua.applied_date DESC;"
        params = (user_id,)
        rows = _execute_query(query, params, "fetchall")

    clean_input = search_input.strip()

    if clean_input.isdigit():
        query += " and ua.university_application_id = %s;"
        params = (user_id, int(clean_input))
        rows = _execute_query(query, params, "fetchall")

    try:
        valid_date = datetime.strptime(clean_input, "%Y-%m-%d").date()
        query += " and ua.applied_date = %s;"
        params = (user_id, valid_date)
        rows = _execute_query(query, params, "fetchall")

    except ValueError:
        pass

    else:
        query += '''
        AND (
            un.name ILIKE %s OR
            p.name ILIKE %s OR
            i.name ILIKE %s OR             -- Added: Intake name filter match
            ua.application_platform ILIKE %s OR
            ast.status_name ILIKE %s
        )
        ORDER BY ua.applied_date DESC;'''

        search_pattern = f"%{clean_input}%"
        params = (user_id, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern)
        rows = _execute_query(query, params, "fetchall")

    return rows



def get_university_pipeline_summary():

    query = '''select * from university_pipeline_summary'''
    result = _execute_query(query)
    return  {
        "total_historical_count": result[0],
        "current_active_total": result[1],
        "current_applied": result[2],
        "current_accepted": result[3],
        "success_rate_percentage": "0.00" if result[4] is None else f"{result[4]:.2f}"
    }


def get_strategic_target_overview():

    query = '''select * from v_dashboard_application_analytics_summary'''
    result = _execute_query(query)

    if not result or len(result) < 3:
        return []

    unis, programs, platforms = result[0], result[1], result[2]

    # Convert dictionaries to flat lists using standard for-loops
    uni_rows = []
    for u in unis:
        uni_rows.append([u['university_name'], u['total_submissions'], u['success_rate']])

    prog_rows = []
    for p in programs:
        prog_rows.append([p['program_name'], p['program_degree'], p['total_submissions'], p['success_rate']])

    plat_rows = []
    for pl in platforms:
        plat_rows.append([pl['standardized_platform'], pl['total_submissions'], pl['success_rate']])

    # Return a clean list containing the data and headers for each table
    return [
        {"title": "UNIVERSITIES:", "rows": uni_rows, "headers": ["University Name", "Submissions", "Success Rate"]},
        {"title": "PROGRAMS:", "rows": prog_rows, "headers": ["Program Name", "Degree", "Submissions", "Success Rate"]},
        {"title": "PLATFORMS:", "rows": plat_rows, "headers": ["Platform", "Submissions", "Success Rate"]}
    ]


def get_bottleneck_application():

    query = '''select * from v_dashboard_application_watchlist'''
    result = _execute_query(query, (), "fetchall")
    return result


def get_intake_milestones():

    query = '''select * from v_dashboard_intake_milestones'''
    result = _execute_query(query, (), "fetchall")
    return result