def check_eligibility(data):
    if data.family_in_us:
        return "Eligible: Family-Based"

    elif data.job_offer and data.education.lower() in ['bachelor', 'master', 'phd']:
        return "Eligible: Employment-Based"

    elif data.investment >= 800000:
        return "Eligible: Investor"

    elif data.refugee_status:
        return "Eligible: Refugee"

    elif data.country_in_dv_list:
        return "Eligible: Lottery"

    else:
        return "Not Eligible"