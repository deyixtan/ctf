tshark -r chall.jpg.pcap -Y "icmp" -T fields -e data | tr -d '\n' | xxd -r -p > cat.jpg
