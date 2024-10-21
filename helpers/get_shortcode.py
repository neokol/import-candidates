def get_shortcode_for_job_title(job_title, job_title_to_shortcode):
    # First, try to get the shortcode with exact match
    shortcode = job_title_to_shortcode.get(job_title)
    if shortcode:
        return shortcode
    else:
        # If exact match not found, try case-insensitive match
        normalized_job_title = job_title.strip().lower()
        for title, code in job_title_to_shortcode.items():
            if title.strip().lower() == normalized_job_title:
                return code
        # If still not found, return None
        return None