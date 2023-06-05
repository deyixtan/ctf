# An Alarming BAC(net) Pain - 2
Category: Jubilife

## Description
Jubilife's security team looked into the BACnet traffic involving that IP address (10.120.50.12) and noticed that write-property commands were sent to that device. It is possible the heat detectors are being triggered by these write-property commands.

What is the `BACnet object-name` on the fire suppression device that was written to using the write-property commands?

Note: the object-name itself is never written to via write-property commands

*Flag format: BACnet object-name. Example: **HVAC-ABC***

## Write-up
- To identify the device that was written to using the `write-property` commands, we can filter the logs in the `BACnet` dashboard using the filter `zeek.bacnet.pdu_service == write-property`.
- Upon applying the filter, we observe that the `write-property` commands were sent to the device with IP address `10.120.50.12` and `instance number 14`.
- Once we have identified the device, we can proceed to examine the `read-property-ack` logs of that particular device to find the `object-name`.
- We can further filter the logs using the following criteria: `destination.ip == 10.120.50.12`, `zeek.bacnet.pdu_service == read-property-ack`, `zeek.bacnet_property.property == object-name`, and `zeek.bacnet_property.instance_number == 14`.

Flag: `VENT-LB`
