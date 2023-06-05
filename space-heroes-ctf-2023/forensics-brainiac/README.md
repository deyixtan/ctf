# Brainiac
Category: Forensics

## Description
Brainiac has exploited a binary running on our server on the space station, thankfully the binary is still running but our data was stolen. We also were able to get a network traffic capture when Brainiac exploited our server. He also defaced the binary as well.

The flag is on the server that is running.

Author: SolarDebris

MD5 (exploit.pcap) = 980f66b08cf17c929c442fb98a893d23

Attachments: [exploit.pcap](attachments/exploit.pcap)

## Write-up
- Upon observing the DNS packets, we noticed that an IP address, `10.154.1.94`, was requesting to resolve `0.chals.io`. We made note of this IP address.
- We filtered the packets based on the source address matching the recorded IP address.
- One of the packets revealed an unusual interaction between our noted IP address and `165.227.210.30:16306`.
- We proceeded to follow the TCP stream, which revealed that a `Remote Code Execution (RCE)` was performed using a binary over the network.
- The RCE involved providing certain input, resulting in the listing of directory files, among which `flag.txt` was included.
- We can replicate this request using `pwntools`, but with slight modifications to the user input in order to retrieve the contents of `flag.txt`.

The script to replicate the request can be found [here](solution/solve.py).

Flag: `shctf{1_4m_n0t_pr0gr4mm3d_t0_3xp3r13nc3_hum0r}`
