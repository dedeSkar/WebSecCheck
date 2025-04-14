import requests
import time

def sslLabs_register(sslLabs_email):
    data = {
        "firstName": "test",
        "lastName": "test",
        "email": sslLabs_email,
        "organization": "Testing usecase"
    }
    url = "https://api.ssllabs.com/api/v4/register"
    response = requests.post(url, json=data) 
    
    return response.text

# sslLabs_register(sslLabs_email)
# Gonna leave this for testing, will clean this later

def sslLabs_start_assessment(website_url, sslLabs_email):
    url = f"https://api.ssllabs.com/api/v4/analyze?host={website_url}"
    headers = {"email": sslLabs_email}
    response = requests.get(url, headers=headers)
    data = response.json()
    ip_address = data.get("endpoints", [{}])[0].get("ipAddress", "N/A")
    status = data.get("status", "N/A")
    
    return ip_address, status

def sslLabs_get_analysis(website_url, ip_address, sslLabs_email):
    url = f"https://api.ssllabs.com/api/v4/getEndpointData?host={website_url}&s={ip_address}"
    headers = {"email": sslLabs_email}
    response = requests.get(url, headers=headers)
    data = response.json()
    grade = data.get("grade", "N/A")
    return grade

def main_sslLabs(sslLabs_email, website_url):
    ip_address, assessment_status = sslLabs_start_assessment(website_url, sslLabs_email)
    while assessment_status != "READY":
        print(f"Current assessment status: {assessment_status}. Waiting for status to be READY...")
        time.sleep(15)
        ip_address, assessment_status = sslLabs_start_assessment(website_url, sslLabs_email)
    grade = sslLabs_get_analysis(website_url, ip_address, sslLabs_email)
    SSL_Report = {
        "ip_address": ip_address,
        "grade": grade,
        "assessment_status": assessment_status 
    }
    return SSL_Report
