# OpenPirate
Category: OSINT

## Description
A pirate runs a website that sells counterfeit goods, it is available under the name `heroctf.pirate`. However, we can't get our hands on it, can you help us? Your goal is to find a way to access this website.

Format : **Hero{flag}**

Author : **xanhacks**

## Write-up
- It appears that the hostname `heroctf.pirate` was not found on commonly used DNS servers such as Google or Cloudflare.
- The challenge involved finding a DNS server that would allow us to perform a lookup for the target hostname.
- After conducting some research, we discovered that we could use the OpenNIC DNS server at `134.195.4.2` for our lookup.
- The command we used to perform the lookup was: `dig @134.195.4.2 heroctf.pirate`.
```
; <<>> DiG 9.18.12-0ubuntu0.22.04.1-Ubuntu <<>> @134.195.4.2 heroctf.pirate
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 19246
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: d5c17ec228ee94820100000064602304c6db48f49c6fbc79 (good)
;; QUESTION SECTION:
;heroctf.pirate.			IN	A

;; ANSWER SECTION:
heroctf.pirate.		86400	IN	A	13.38.112.148

;; Query time: 235 msec
;; SERVER: 134.195.4.2#53(134.195.4.2) (UDP)
;; WHEN: Sun May 14 07:53:44 +08 2023
;; MSG SIZE  rcvd: 87
```
- From the output of the command, we obtained the IP address associated with `heroctf.pirate`, which is `13.38.112.148`.
- By navigating to [http://13.38.112.148](http://13.38.112.148), we were able to access the website and obtain the flag.

Flag: `Hero{OpenNIC_is_free!!!3586105739}`
