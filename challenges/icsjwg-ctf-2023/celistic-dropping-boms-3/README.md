# Dropping BOMs - 3
Category: Celistic

## Description
Looking at the differences between SBOMs as well as the actual packages, Celestic's development team has confirmed that the Magnezone SBOM is more accurate. However, unlike the Electivire SBOM, the Magnezone SBOM does not contain license or hash information. This is problematic, as the development team has received an additional request from security for the SHA256 hash of the `netdata` executable used in this router.

Attached (`celestic_router_firmware.bin`) is the firmware for the Celestic routers. The security team has requested that you please extract the filesystem from this firmware and provide them its hash.

What is the SHA256 hash of the `netdata` executable?

*Flag format: SHA256 hash. Example: **b9a5d4eff71b92c306ec3152f4c76f6094e395c1ff54aae26c28f10d9f7c5160***

Attachments: [celestic_router_firmware.bin](attachments/celestic_router_firmware.bin)

## Write-up
- We begin by extracting the files from the firmware using the `binwalk` tool. The command `binwalk -e celestic_router_firmware.bin` allows us to accomplish this.
- During the extraction process, we notice the presence of the file name `root`, which is a Squashfs filesystem. To extract its contents, we can use the command `binwalk -e root`.
- After accessing the extracted file system, we navigate into the extracted directory using the `cd` command. Then, we execute the following command to retrieve all files path containing the term `netdata`: `find . -type f -name "*netdata*" 2>/dev/null`.
- Among the results, we find the netdata executable located at `/usr/sbin/netdata`.
- To generate the SHA256 hash of the netdata executable, we can use the sha256sum command: `sha256sum /usr/sbin/netdata`.
- The resulting SHA256 hash is `1cb66aecf26f95d8d727e7508a85f5357737c88ab768380928a47b4df038db11`.

Flag: `1cb66aecf26f95d8d727e7508a85f5357737c88ab768380928a47b4df038db11`
