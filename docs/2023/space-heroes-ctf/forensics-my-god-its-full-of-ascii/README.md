# My God, it's full of .- ... -.-. .. .. 
Category: Forensics

## Description
If sound can't travel in a vacuum then how did a microphone pick this up in space unless space is a made up concept designed to make us fear leaving Earth and joining with Xenu and the Galactic Confederacy?

MD5 (signal.wav) = d6c4e284c970d03cb6aa71acd27b4f4d

Attachments: [signal.wav](attachments/signal.wav)

## Write-up
- In the challenge title, the Morse code `.- ... -.-. .. ..` converts to ASCII characters.
- Open the WAV file in Audacity, somewhere along the audio's spectogram view we see a pattern of big and small rectangles that may resemble morse codes.
- These shapes appear to be grouped into sets of 8 per group.
- Each block of 8 shapes likely represents an ASCII character, as hinted by the challenge title. It cannot be Morse code since 1 ASCII character wouldn't be 8 Morse digits long.
- Since each block consists of 8 shapes, it suggests that each shape represents 1 bit in the ASCII character.
- Here is the binary mapping obtained from the WAV file:
```
01110011 01101000 01100011 01110100 01100110 01111011 01001110 00110000 00100000 00110001 00100000 01100011 00110100 01101110 00100000 01001000 00110011 00110100 01110010 00100000 01110101 00100000 00111000 00110011 00110011 01010000 01011111 00111000 00110000 00110000 01110000 00101000 01001001 01101110 00101001 00100000 00111100 00100000 00101111 01100100 01100101 01110110 00101111 01101110 01110101 01101100 01101100 01110011 01110000 01100001 01100011 01100101 01111101
```

Flag: `shctf{N0 1 c4n H34r u 833P_800p(In) < /dev/nullspace}`
