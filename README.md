# WebSecCheck

## Description

- WebSecCheck is your all-in-one tool for scanning websites using publicly available APIs and summarizing the results with AI-driven insights.
- Because who wouldn’t want a robot telling you how insecure your site might be? By leveraging multiple scanners and seamlessly consolidating their findings, WebSecCheck caters to both technical wizards and non-technical mortals—ensuring everyone can grasp the big picture of a site’s security posture.

---

## Quick Guide

1. **Configure VirusTotal**  
   - Open the `main.py` file.  
   - Insert your VirusTotal API key into the designated variable ```VTApiKey```.

2. **Register your email on "Qualys SSL Lab"**
   - Open your terminal
   - Insert this code, before changing it, more information can be found in [Qualys SSL Labs documentation](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v4.md#register-)
   ```
   curl --location 'https://api.ssllabs.com/api/v4/register'  --header 'Content-Type: application/json' --data '{ "firstName":"John", "lastName":"Doe", "email":"jdoe@someoraganizationemail.com", "organization":"Some Organization"}'
   ```

3. **Start the Scan**  
   - Run the `main.py` script.  
   - Enter the URL you wish to scan when prompted.  

---

## Use case example

- Non malicious example ```Google.com```

```
Website Security analysis
------------------------------------------------------------------
Website Title: Google
IP Address: 2607:f8b0:4005:80e:0:0:0:200e
Status Code: 200
SSL grade: B
VirusTotal Last analysis date: 2025-04-14 23:03:58
VirusTotal Community score: 2715
VirusTotal Security vendors' analysis : 0/97
VirusTotal Security vendors' that found it Malicious: []
```

- Malicious example ```coherentinflationescort[.]com```
  
```
Website Security analysis
------------------------------------------------------------------
Website Title: coherentinflationescort[.]com
IP Address: 103.224.182.242
Status Code: 200
SSL grade: A
VirusTotal Last analysis date: 2025-02-13 10:27:51
VirusTotal Community score: -30
VirusTotal Security vendors' analysis : 8/96
VirusTotal Security vendors' that found it Malicious: ['alphaMountain.ai', 'CRDF', 'CyRadar', 'Dr.Web', 'Fortinet', 'Kaspersky', 'Seclookup', 'Webroot']
```

## Ongoing Improvements

- [ ] Integrate a total of seven scanners for broader coverage.  
- [ ] Add detailed comments throughout the code for clarity.  
- [ ] Present the gathered data in a user-friendly format for non-technical audiences.  
- [ ] Automatically forward the retrieved information to AI for an insightful summary of results. 
