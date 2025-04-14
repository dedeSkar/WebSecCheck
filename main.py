from Scanners.VirusTotal import VT_Main

VTApiKey = ""

website_url = input("Enter hostname of website :")

print(VT_Main(VTApiKey, website_url))
