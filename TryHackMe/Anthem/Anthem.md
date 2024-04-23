# Anthem

## Description

This task involves you, paying attention to details and finding the 'keys to the castle'.

This room is designed for beginners, however, everyone is welcomed to try it out!

Enjoy the Anthem.

In this room, you don't need to brute force any login page. Just your preferred browser and Remote Desktop.

Please give the box up to 5 minutes to boot and configure.

## Challenges

### Website Analysis

1. Let's run nmap and check what ports are open.

`nmap -A 10.10.103.130`

```
Starting Nmap 7.60 ( https://nmap.org ) at 2024-04-23 03:14 BST
Nmap scan report for ip-10-10-103-130.eu-west-1.compute.internal (10.10.103.130)
Host is up (0.00041s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WIN-LU09299160F
| Not valid before: 2024-04-22T02:09:15
|_Not valid after:  2024-10-22T02:09:15
|_ssl-date: 2024-04-23T02:15:22+00:00; 0s from scanner time.
```

2. What port is for the web server?

Standart port for http server. Can find in Nmap results.

3. What port is for remote desktop service?

Standart port for RDP. Can find in Nmap results.

4. What is a possible password in one of the pages web crawlers check for?

Check robots.txt

5. What CMS is the website using?

You can find folders specific to CMS in robots.txt

6. What is the domain of the website?

Juxt check main page

7. What's the name of the Administrator

(HINT: Consult the Oracle.(your favourite search engine))

We have a poem in one of articles

```
Born on a Monday,
Christened on Tuesday,
Married on Wednesday,
Took ill on Thursday,
Grew worse on Friday,
Died on Saturday,
Buried on Sunday.
That was the end    
```

Check this poem in internet

8. Can we find find the email address of the administrator?

After checking two posts we find email of Jane Doe - `JD@anthem.com`

Looks like administrator is from question with poem. Pattern of email is first letter of Name and first letter of last name.

### Spot the flags

1. What is flag 1?
(Hint: Have we inspected the pages yet?)

Check `http://10.10.103.130/archive/we-are-hiring/` page with inspector

2. What is flag 2?
(Hint: Search for it)

Second flag is on the same page, try to use `Search` in `Inspector` tab. (HINT: All TryHackMe flags starts with THM)

3. What is flag 3?
(Hint: Profile)

Check Jane Doe profile - `http://10.10.103.130/authors/jane-doe/`

4. What is flag 4?
(Hint: Have we inspected all the pages yet?)

You need to check another page. To spend your time, here is hint - `http://10.10.103.130/archive/a-cheers-to-our-it-department/`

### Final stage

1. Let's figure out the username and password to log in to the box.(The box is not on a domain)

We already find username - part of email before @ and password from robots.txt, use this combination to connect via rdp. There is file `user` on Desktop

2. Can we spot the admin password?
(Hint: It is hidden.)

At first enable property to see hidden files for current user. Then go to hidden folder C:\backup and try to open restore.txt. There is no permissions. Let's try to change permissions for this file. Open properties and add `WIN-LU09299160F\Users` for read and edit. This allow all users on this workstation to edit and read this file.

3. Escalate your privileges to root, what is the contents of root.txt?

Go to `C:\Users\Administrator\Desktop` enter administrator password and read root.txt
