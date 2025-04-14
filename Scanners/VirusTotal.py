import requests
import datetime

def Submit_URL_VT(VTApiKey, website_url):
    url = "https://www.virustotal.com/api/v3/urls"
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "x-apikey": VTApiKey
    }
    data = {"url": website_url}
    response = requests.post(url, headers=headers, data=data)
    URL_ID = response.json()["data"]["id"]
    if URL_ID.startswith("u-"):
        URL_ID = URL_ID[2:]
    if "-" in URL_ID:
        URL_ID = URL_ID.split("-")[0]
    return URL_ID

def Get_URL_VT(VTApiKey, website_id):
    url = f"https://www.virustotal.com/api/v3/urls/{website_id}"
    headers = {
        "accept": "application/json",
        "x-apikey": VTApiKey
    }
    response = requests.get(url, headers=headers)
    return response.json()

def Parse_VT_Report(report):
    try:
        attributes = report["data"]["attributes"]
    except KeyError:
        print("Error: Could not find attributes in the report.")
        return None
    analysis_results = attributes.get("last_analysis_results", {})
    malicious_scanners = [
        details.get("engine_name", scanner)
        for scanner, details in analysis_results.items()
        if details.get("result", "").lower() == "malicious" or details.get("category", "").lower() == "malicious"
    ]
    community_score = attributes.get("reputation", "N/A")
    analysis_stats = attributes.get("last_analysis_stats", {})
    malicious_count = analysis_stats.get("malicious", 0)
    suspicious = analysis_stats.get("suspicious", 0)
    undetected = analysis_stats.get("undetected", 0)
    harmless = analysis_stats.get("harmless", 0)
    total_engines = malicious_count + suspicious + undetected + harmless
    score_overall = f"{malicious_count}/{total_engines}" if total_engines > 0 else "N/A"
    last_analysis_ts = attributes.get("last_analysis_date")
    if last_analysis_ts:
        last_analysis_date = datetime.datetime.fromtimestamp(last_analysis_ts).strftime("%Y-%m-%d %H:%M:%S")
    else:
        last_analysis_date = "N/A"
    final_url = attributes.get("last_final_url", "N/A")
    status_code = attributes.get("last_http_response_code", "N/A")
    title = attributes.get("title", "N/A")
    body_length_bytes = attributes.get("last_http_response_content_length", 0)
    body_length_kb = round(body_length_bytes / 1024, 2) if body_length_bytes else "N/A"
    parsed_report = {
        "community_score": community_score,
        "score_overall": score_overall,
        "last_analysis_date": last_analysis_date,
        "final_url": final_url,
        "status_code": status_code,
        "title": title,
        "body_length_kb": body_length_kb,
        "Scanners_that_found_it_malicious": malicious_scanners
    }
    return parsed_report

def VT_Main(VTApiKey, website_url):
    VT_ID = Submit_URL_VT(VTApiKey, website_url)
    Report = Get_URL_VT(VTApiKey, VT_ID)
    parsed_report = Parse_VT_Report(Report)
    return parsed_report
