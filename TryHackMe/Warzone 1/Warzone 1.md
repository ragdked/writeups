# Warzone 1

You received an IDS/IPS alert. Time to triage the alert to determine if its a true positive.

## Your shift just started and your first network alert comes in.

You work as a Tier 1 Security Analyst L1 for a Managed Security Service Provider (MSSP). Today you're tasked with monitoring network alerts.

A few minutes into your shift, you get your first network case: Potentially Bad Traffic and Malware Command and Control Activity detected.  Your race against the clock starts. Inspect the PCAP and retrieve the artifacts to confirm this alert is a true positive. 

Your tools:

Brim
Network Miner
Wireshark
Deploy the machine attached to this task; it will be visible in the split-screen view once it is ready.

If you don't see a virtual machine load then click the Show Split View button.

Answer the questions below

### What was the alert signature for Malware Command and Control Activity Detected?

![alt text](image.png)
![alt text](image-1.png)

ET Malware MirrorBlast CnC Activity M3

### What is the source IP address? Enter your answer in a defanged format.

![alt text](image-2.png)

172[.]16[.]1[.]102

### What IP address was the destination IP in the alert? Enter your answer in a defanged format. 

169[.]239[.]128[.]11

### Still in VirusTotal, under Community, what threat group is attributed to this IP address?

![alt text](image-3.png)

TA505

### What is the malware family?

MirrorBlast

### Do a search in VirusTotal for the domain from question 4. What was the majority file type listed under Communicating Files?

![alt text](image-4.png)

Windows Installer

### Inspect the web traffic for the flagged IP address; what is the user-agent in the traffic?

![alt text](image-5.png)

![alt text](image-6.png)

REBOL View 2.7.8.3.1

### Retrace the attack; there were multiple IP addresses associated with this attack. What were two other IP addresses? Enter the IP addressed defanged and in numerical order. (format: IPADDR,IPADDR)

![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)

185[.]10[.]68[.]235,192[.]36[.]27[.]92

### What were the file names of the downloaded files? Enter the answer in the order to the IP addresses from the previous question. (format: file.xyz,file.xyz)

![alt text](image-10.png)
![alt text](image-11.png)

filter.msi,10opd3r_load.msi

### Inspect the traffic for the first downloaded file from the previous question. Two files will be saved to the same directory. What is the full file path of the directory and the name of the two files? (format: C:\path\file.xyz,C:\path\file.xyz)

![alt text](image-12.png)
![alt text](image-13.png)

C:\ProgramData\001\arab.bin,C:\ProgramData\001\arab.exe

### Now do the same and inspect the traffic from the second downloaded file. Two files will be saved to the same directory. What is the full file path of the directory and the name of the two files? (format: C:\path\file.xyz,C:\path\file.xyz)

![alt text](image-14.png)
![alt text](image-15.png)

C:\ProgramData\Local\Google\rebol-view-278-3-1.exe,C:\ProgramData\Local\Google\exemple.rb
