# WebSecCheck

## Description

- WebSecCheck allows you to scan a website using publicly available APIs and then obtain an AI-generated analysis of the results.
- By incorporating multiple scanners and summarizing the findings, WebSecCheck aims to provide both technical and non-technical audiences with a comprehensive overview of a website’s security posture.

---

## Quick Guide

1. **Configure VirusTotal**  
   - Open the `main.py` file.  
   - Insert your VirusTotal API key into the designated variable ```VTApiKey```.

2. **Register your email on "Qualys SSL Lab"**
   - Open your terminal
   - Insert this code, before changing it, more information can be found here: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v4.md#register-
   ```
   curl --location 'https://api.ssllabs.com/api/v4/register'  --header 'Content-Type: application/json' --data '{ "firstName":"John", "lastName":"Doe", "email":"jdoe@someoraganizationemail.com", "organization":"Some Organization"}'
   ```

3. **Start the Scan**  
   - Run the `main.py` script.  
   - Enter the URL you wish to scan when prompted.  

---

## Ongoing Improvements

- [ ] Integrate a total of seven scanners for broader coverage.  
- [ ] Add detailed comments throughout the code for clarity.  
- [ ] Present the gathered data in a user-friendly format for non-technical audiences.  
- [ ] Automatically forward the retrieved information to AI for an insightful summary of results. 
