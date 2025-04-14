from Scanners.VirusTotal import VT_Main
from Scanners.ssllabs import main_sslLabs

# Prereq vars
VTApiKey = "changeme"
sslLabs_email = "changeme@changeme.lt"
website_url = input("Enter hostname of website :")

def main():
    VT_Data = VT_Main(VTApiKey, website_url)
    SSL_Data = main_sslLabs(sslLabs_email, website_url)
    Report = f"""
    Website Security analysis
    ------------------------------------------------------------------
    Website Title: {VT_Data["title"]}
    IP Address: {SSL_Data["ip_address"]}
    Status Code: {VT_Data["status_code"]}
    SSL grade: {SSL_Data["grade"]}
    VirusTotal Last analysis date: {VT_Data["last_analysis_date"]}
    VirusTotal Community score: {VT_Data["community_score"]}
    VirusTotal Security vendors' analysis : {VT_Data["score_overall"]}
    VirusTotal Security vendors' that found it Malicious: {VT_Data["Scanners_that_found_it_malicious"]}
    """
    print(Report)

if __name__ == "__main__":
    main()
