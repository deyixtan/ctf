# Broken Inside
Category: Forensics

## Description
Elliot got this broken data, seemed to contain some hidden information, possibly related to the havoc he had been investigating. Fixing this could lead him to valuable clues in his pursuit of the rogue group responsible for the chaos in the cyber world.

Flag Format: CHCTF{}

Attachments: [Broken Elliot](attachments/Broken%20Elliot)

## Write-up
- The file header was corrupted, and using the `file` command indicates that it contains generic data without any specific file format or type.
- Upon performing a hex edit, it was observed that the file has the following trailing bytes: `49 45 4E 44 AE 42 60 82`, which correspond to a PNG file.
- To fix restore the image, update the magic number to indicate that it is a PNG file, and upload it to a suitable tool or platform like [compress-or-die.com](https://compress-or-die.com/repair) for the rest of the image to be repaired.

[`Broken Elliot (fixed)`](solution/Broken%20Elliot%20(fixed))
![](solution/Broken%20Elliot%20(fixed))

Flag: `CHCTF{P30PL3_4R3_7H3_3451357_7H1N6_70_M4N1PU1473}`
