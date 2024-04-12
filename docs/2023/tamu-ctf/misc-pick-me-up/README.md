# Pick Me Up
Category: Misc

## Description
Author: `bit`

You're supposed to pick your friend up at the airport, but she didn't send you any information! When does this flight actually arrive and where should you pick her up? This screenshot was taken on 4/20.

The flag format is `gigem{HH:MM-Gate}` in CDT with HH being hour in 24 hour time and MM for the minutes. Gate represents the gate that the plane arrives at. For example, if you were picking your friend up at 4:20 PM CDT at gate A1 would yield the flag `gigem{16:20-A1}`.

Attachments: [pick-me-up.zip](attachments/pick-me-up.zip)

## Write-up
- After extracting the file, we discovered an image containing a conversation in Mandarin. We used Google Translate to translate the text into English.
- The image features an airplane from EVA Air, suggesting it is related to a flight.
- By examining the conversation, we determined that the flight is between Taipei (TPE) and Houston (IAH) airports.
- Further research revealed that a flight from Taipei to Houston typically takes approximately 14 hours.
- Assuming the author's timezone is related to Houston's, based on the image showing that their friend is departing on approximately April 20th at 08:50, we can estimate that their friend should arrive around April 20th at 23:00.
- To confirm this, we searched the arrival history for IAH airport on FlightAware and found that the only EVA Air flight arriving around that time period is on `April 21st at 00:28`.
- Additionally, within the same FlightAware page, we were able to locate the gate number `D7` for the arrival.

You can find the flight details and more information [here](https://flightaware.com/live/flight/EVA52/history/20230420/1410Z/RCTP/KIAH) or in the provided [`solution/scrapped.zip`](solution/scrapped.zip) scrapped file. 

Flag: `gigem{00:28-D7}`
