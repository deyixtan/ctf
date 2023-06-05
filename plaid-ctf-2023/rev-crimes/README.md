# crimes
Category: Reversing

## Description
I found this locked chest at the bottom o’ the ocean, but the lock seems downright… criminal. Think you can open it? We recommend chrome at 100% zoom. Other browsers may be broken.

[https://plaidctf.com/files/css.74486b61b22e49b3d8c5afebee1269e37b50071afbf1608b8b4563bf8d09ef92.html](https://plaidctf.com/files/css.74486b61b22e49b3d8c5afebee1269e37b50071afbf1608b8b4563bf8d09ef92.html)

Attachments: [css.html (Scrapped)](attachments/css.html)

## Write-up
- Each group of 3 characters corresponds to an SVG with a small transparent rectangle
- Utilize JavaScript to perform a brute force attack on each group of 3 characters and ensure that all transparent rectangles align with the "Correct" div tag

The solve script can be found [here](solution/solve.js).

Flag: `PCTF{youre_lucky_this_wasnt_a_threesat_instance}`
