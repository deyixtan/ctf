# An Alarming BAC(net) Pain - 4
Category: Jubilife

## Description
Based on the observed temperature readings, it appears that the heat detector’s setpoint was changed, causing it to go off while still within the range of normal operating temperatures, nowhere close to the temperature that should trigger the alarm.

Setpoints are defined in BACnet configuration files. These configuration files are stored in zip files that are encrypted with password `jubilife_BMS_configuration!` before being sent over BACnet.

It appears that someone uploaded a configuration file to the fire suppression BACnet device that changed its temperature setpoint.

Jubilife would like you to extract this configuration file from the BACnet traffic and report the password listed for the misconfigured binary sensor so they can revert the setpoint to its correct value.

*Flag format: password for the misconfigured binary sensor. Example: **37ab38cb4f***

## Write-up
- Upon examining Malcomm's `Files` dashboard, we observe that only one ZIP file is logged in the `Files - MIME Type` table. The ZIP archive is named `BACNET-FraRoA4cyfHy1i2ix6-ChxepzFTHt0PwAOXe-20230504165355.zip` which can be found in the `Files - Logs` table.
- To access files in Malcomm, we can navigate to [https://malcolm.icsjwgctf.com/extracted-files/](https://malcolm.icsjwgctf.com/extracted-files/). Specifically, the ZIP archive can be retrieved from [https://malcolm.icsjwgctf.com/extracted-files/preserved/BACNET-FraRoA4cyfHy1i2ix6-ChxepzFTHt0PwAOXe-20230504165355.zip](https://malcolm.icsjwgctf.com/extracted-files/preserved/BACNET-FraRoA4cyfHy1i2ix6-ChxepzFTHt0PwAOXe-20230504165355.zip). You can refer to the file [here](solution/BACNET-FraRoA4cyfHy1i2ix6-ChxepzFTHt0PwAOXe-20230504165355.zip).
- We proceeded to download the ZIP file and extracted its contents using the provided password: `jubilife_BMS_configuration!`.
- We discovered a file named `fire_suppresion_config.txt` after the extraction process, which contained the `Lab B Heat detector` password: `927ab89245`.

Flag: `927ab89245`
