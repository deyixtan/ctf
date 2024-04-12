# attack-strategies
Category: Web

## Description
The StarCraft III Interplanetary Newbie Championship is almost live and I was assigned to take care of teaching everyone in the Newbie-84 planet how to play. I made a blog so each individual can choose their favorite races and strategies to learn before the tournament. I will secretly participate and to give them a change, I hid my go to strategy somewhere on the website. Wanna try finding it?

[http://vespene-gas.hackers.best:31337/](http://vespene-gas.hackers.best:31337/)

Author: Bal

## Write-up
- The first input field is used to specify the folder to navigate to, while the second input field is used to specify the file to read within that folder.
- Cicking the button triggers a POST request to retrieve the contents of the specified file.
- It is possible to exploit these fields and read arbitrary files by injecting malicious input.
- Also, leaving the second input field empty will display the files in the directory.
- Through experimentation, it is likely to discover the `/app/strategies` directory, containing a file named `flag.txt`.

Flag: `shctf{get_zerg_rushed_nb}`
