# TryHack3M: TriCipher Summit

Step into the realm of TryHackM3 as we approach 3 million users, where '3 is the magic number'! Embark on the TryHackM3 challenge, intercepting credentials, cracking custom crypto, hacking servers, and breaking into smart contracts to steal the 3 million. Are you ready for the cryptography ultimate challenge?

In this challenge, you will be expected to:

Perform supply chain attacks
Reverse engineer cryptography
Hack a crypto smart contract
Press the Start Machine button and wait at least 5 minutes for the VM to boot up properly.

# What is Flag 1?

```
nmap -Pn -T4 -vv -p- 10.10.199.11
Starting Nmap 7.80 ( https://nmap.org ) at 2025-06-20 05:38 BST
Initiating ARP Ping Scan at 05:38
Scanning 10.10.199.11 [1 port]
Completed ARP Ping Scan at 05:38, 0.03s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 05:38
Completed Parallel DNS resolution of 1 host. at 05:38, 0.00s elapsed
Initiating SYN Stealth Scan at 05:38
Scanning 10.10.199.11 [65535 ports]
Discovered open port 22/tcp on 10.10.199.11
Discovered open port 80/tcp on 10.10.199.11
Discovered open port 443/tcp on 10.10.199.11
Discovered open port 8000/tcp on 10.10.199.11
Discovered open port 9444/tcp on 10.10.199.11
Discovered open port 5000/tcp on 10.10.199.11
Completed SYN Stealth Scan at 05:38, 4.08s elapsed (65535 total ports)
Nmap scan report for 10.10.199.11
Host is up, received arp-response (0.0056s latency).
Scanned at 2025-06-20 05:38:32 BST for 4s
Not shown: 65529 closed ports
Reason: 65529 resets
PORT     STATE SERVICE         REASON
22/tcp   open  ssh             syn-ack ttl 64
80/tcp   open  http            syn-ack ttl 64
443/tcp  open  https           syn-ack ttl 63
5000/tcp open  upnp            syn-ack ttl 64
8000/tcp open  http-alt        syn-ack ttl 63
9444/tcp open  wso2esb-console syn-ack ttl 63
MAC Address: 02:8B:B3:A6:49:49 (Unknown)
```

Хз что дальше делать)