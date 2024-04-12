# Buried Treasure
Category: Reversing

## Description
Ready your masts and set sail! Thar be treasure here if we can figure out how to find it.

Follow the map and get the booty — a pirate’s work is never done.

[http://treasure.chal.pwni.ng/](http://treasure.chal.pwni.ng/)

Attachments: [buried-treasure.zip (Scrapped)](attachments/buried-treasure.zip)

## Write-up
- The flag, enclosed within braces, consists of 25 characters. Each character corresponds to a specific JavaScript index file, such as `100.js`.
- The correct combinations of characters (i.e., the flag) ultimately lead us to the `success.js` file, indicating successful completion.
- To solve this challenge, we can work backwards starting from `success.js` and proceed through each stage by brute-forcing all possible ASCII characters associated with the respective index.

The solve script can be found [here](solution/solve.js).

Flag: `PCTF{Need+a+map/How+about+200!}`
