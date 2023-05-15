# An Alarming BAC(net) Pain - 1
Category: Jubilife

## Description
Jubilife has a chemical processing facility to create chemicals used in the water purification process. In this facility, Jubilife produces compounds such as ferric sulfate and aluminum sulfate, which are involved in the coagulation process of water purification. The chemical processing facility uses both heat detectors and smoke detectors as part of their fire suppression system. Recently, the heat detectors have been triggered a number of times, causing building evacuations and halts in production.

None of these events have triggered the smoke detectors, and Jubilife employees have not noticed a substantial increase in temperature corresponding to the heat detector alarms. Therefore, they believe that either the heat detectors are malfunctioning or the building management system itself is misconfigured. Employees are unable to ignore these alarms because the heat detectors are connected to the building management system. When an alarm goes off, the fire suppression and ventilation systems activate, forcing employees to evacuate and cease production until the system can be reset.

Your goal is to help Jubilife determine what is causing the alarms and how to fix the problem, whatever it may be. The building management system uses the BACnet protocol for its communication, and network traffic from Jubilife’s chemical processing facility has been ingested into Malcolm.

The fire suppression BACnet device contains binary sensors for all heat detectors, smoke detectors, and ventilation systems. This fire suppression device has BACnet identifier/instance number 257 which can be found on the `BACnet Dashboard` in the `BACnet - Discovery logs` pane.

What is the IP address of the BACnet fire suppression device?

*Flag format: IP Address. Example: **192.168.1.20***

Note: Working through the `Introduction to Malcolm` challenges will help provide a tutorial/introduction to Malcolm.

## Write-up
- To proceed with the task, we navigate to the `BACnet` dashboard in Malcomm.
- Upon inspecting the `BACnet - Read and Write Property` section, we discover a device identified by the `object-name` as `fire-suppression`.
- The IP address associated with this device is `10.120.50.12`.

Flag: `10.120.50.12`
