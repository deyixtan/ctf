# An Alarming BAC(net) Pain - 3
Category: Jubilife

## Description
It turns out those write-property commands were used by the building management system to open the vents after the alarms were triggered, rather than what set the heat detectors off in the first place. As the heat detector alarms are designed to be triggered by high temperature values, Jubilife would like your help finding the temperature values for Lab B each time the heat detector alarm was triggered.

What was the lowest temperature value that **triggered the heat detector alarm** in `Lab B`?

Note: this is not the same as the lowest overall temperature value in Lab B, just the lowest value that triggered an alarm.

Flag format: temperature value rounded to two decimal places. *Example: if the reported temperature was 71.22999, the flag would be **71.23***

## Write-up
- By examining the `BACnet` dashboard, we discover that the `Lab B Temperature Sensor` is located at IP address `10.120.50.18 with Instance 1`, while the `Lab B Heat Detector Alarm` is at IP address `10.120.50.12 with Instance 4`.
- To filter the logs and focus on the heat detector alarm being triggered at Lab B, we use the following filter: `destination.ip == 10.120.50.12` and `zeek.bacnet_property.instance_number == 4` and `zeek.bacnet_property.value == 1`. This provides us with the log entries that represent instances of the heat detector alarm being triggered.
- The following timestamps correspond to the moments when the heat detector alarm was triggered:
```
May 5, 2023 @ 03:10:10:883
May 5, 2023 @ 02:10:04:135
May 5, 2023 @ 01:29:59:644
May 5, 2023 @ 01:07:57:209
May 5, 2023 @ 00:56:55:959
```
- To determine the corresponding temperature readings from the sensor near those timestamps, we use the filter `destination.ip == 10.120.50.18`. The associated temperature readings are as follows:
```
72.459999 degrees Celsius
72.470001 degrees Celsius
72.449997 degrees Celsius
72.459999 degrees Celsius
72.419998 degrees Celsius
```
- The lowest temperature recorded when the alarm was triggered occurred at `May 5, 2023 @ 00:56:55:959, with a temperature of 72.419998 degrees Celsius`.

Flag: `72.42`
