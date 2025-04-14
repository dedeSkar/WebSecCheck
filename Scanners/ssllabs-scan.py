import requests

sslLabs_email = "test4@testing-sorry.lt"
website_url = "lrt.lt"

def sslLabs_register(sslLabs_email):
    # Should be used only once
    data = {
        "firstName" : "test",
        "lastName" : "test",
        "email" : sslLabs_email,
        "organization" : "Home use"
}
    headers = {"Content-Type": "application/json"}
    url = "https://api.ssllabs.com/api/v4/register"
    response = requests.post(url, headers=headers, data=data)
    return response.text

# print(sslLabs_register())

def sslLabs_start_assesment(website_url, sslLabs_email):
    url = f"https://api.ssllabs.com/api/v4/analyze?host={website_url}"
    headers = {"email": sslLabs_email}
    response = requests.get(url, headers=headers)
    return response.text

sslLabs_register(sslLabs_email)
print(sslLabs_start_assesment(website_url, sslLabs_email))
