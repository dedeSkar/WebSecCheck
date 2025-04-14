from Scanners.VirusTotal import VT_Main
from Scanners.ssllabs import main_sslLabs

VTApiKey = "changeme"
sslLabs_email = "changeme@changeme.lt"

website_url = input("Enter hostname of website :")

print(VT_Main(VTApiKey, website_url))
print(main_sslLabs(sslLabs_email, website_url))
