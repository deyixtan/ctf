f = open("print_flag.py.enc", "rb")
content = f.read()
content_parts = content.split(b"\n")
doc = content_parts.pop(0)
encoded_content = b"\n".join(content_parts)

sub_map = {
    # part 1
    b"\x2e": "#",
    b"\x3d": "!",
    b"\x5a": " ",
    b"\x34": "/",
    b"\x25": "u",
    b"\x5c": "s",
    b"\x45": "r",
    b"\x47": "b",
    b"\x44": "i",
    b"\x65": "n",
    b"\x20": "e",
    b"\x61": "v",
    b"\x6f": "p",
    b"\x0c": "y",
    b"\x50": "t",
    b"\x70": "h",
    b"\x55": "o",
    b"\x3a": "3",
    # part 2
    b"\x62": "\n",
    b"\x5e": "(",
    b"\x67": ")",
    b"\x4d": "m",
    b"\x74": "a",
    b"\x41": "6",
    b"\x77": "4",
    b"\x2f": ":",
    b"\x58": "_",
    b"\x5d": "\"",
    b"\x4a": "=",
    b"\x40": "f",
    b"\x59": "d",
    b"\x53": "c",
    b"\x3e": ".",
    b"\x6c": "k",
    b"\x58": "_",
    b"\x09": "q",
    b"\x0b": "w",
    b"\x24": "x",
    b"\x7a": "j",
    b"\x57": "l",
    b"\x6b": "z",
    b"\x7b": "g",
    b"\x38": "'",
    b"\x79": "{",
    b"\x52": "1",
    b"\x6d": "2",
    b"\x68": "5",
    b"\x7e": "7",
    b"\x5f": "8",
    b"\x33": "9",
    b"\x36": "0",
    b"\x27": ",",
    b"\x6a": "[",
    b"\x3f": "]",
    b"\x56": "}",
    b"\x2c": "N",
    # part 3
    b"\x46": "G",
    b"\x2b": "O",
    b"\x0a": "D",
    b"\x66": "Y",
    b"\x35": "Z",
    b"\x7d": "A",
    b"\x49": "L",
    b"\x37": "E",
    b"\x7c": "H",
    b"\x30": "T",
    b"\x31": "R",
    b"\x37": "E",
    b"\x73": "V",
    b"\x2b": "O",
    b"\x42": "S",
    b"\x26": "P",
    b"\x4e": "M",
    b"\x29": "U",
    b"\x4b": "J",
    b"\x6e": "X",
    b"\x2b": "O",
    b"\x28": "F",
    b"\x2d": "N",
    b"\x4f": "W",
    b"\x2b": "O",
    b"\x31": "R",
    b"\x71": "B",
    b"\x43": "K",
    b"\x51": "C",
    b"\x2a": "I",
    b"\x29": "U",
    b"\x60": "Q",
}

for c in encoded_content:
    c = c.to_bytes(1, byteorder="big")
    if c in sub_map:
        print(sub_map[c], end="")
    else:
        print('#', end="")

# {'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}

# 00000000  7b 27 74 68 65 5f 71 75  69 63 6b 5f 62 72 6f 77  |{'the_quick_brow|
# 00000010  6e 5f 66 6f 78 5f 6a 75  6d 70 73 5f 6f 76 65 72  |n_fox_jumps_over|
# 00000020  5f 74 68 65 5f 6c 61 7a  79 5f 64 6f 67 27 3a 20  |_the_lazy_dog': |
# 00000030  31 32 33 34 35 36 37 38  39 2e 30 2c 20 27 69 74  |123456789.0, 'it|
# 00000040  65 6d 73 27 3a 5b 5d 7d  0a 2e 3d 5a 34 25 5c 45  |ems':[]}..=Z4%\E|
# 00000050  34 47 44 65 34 20 65 61  5a 6f 0c 50 70 55 65 3a  |4GDe4 eaZo.PpUe:|
# 00000060  62 44 4d 6f 55 45 50 5a  47 74 5c 20 41 77 62 62  |bDMoUEPZGt\ Awbb|
# 00000070  53 55 59 20 59 58 40 57  74 7b 5a 4a 5a 5d 53 6d  |SUY YX@Wt{ZJZ]Sm|
# 00000080  31 7a 59 46 35 7e 73 73  33 52 47 57 4b 70 59 7a  |1zYF5~ss3RGWKpYz|
# 00000090  2c 5c 35 4f 31 40 59 37  7b 6b 6e 3a 2c 25 4e 6d  |,\5O1@Y7{kn:,%Nm|
# 000000a0  5c 70 40 60 4a 4a 5d 62  62 59 20 40 5a 45 20 61  |\p@`JJ]bbY @ZE a|
# 000000b0  20 45 5c 20 5e 5c 67 2f  62 5a 5a 5a 5a 45 20 50  | E\ ^\g/bZZZZE P|
# 000000c0  25 45 65 5a 5d 5d 3e 7a  55 44 65 5e 45 20 61 20  |%EeZ]]>zUDe^E a |
# 000000d0  45 5c 20 59 5e 5c 67 67  62 62 59 20 40 5a 53 70  |E\ Y^\ggbbY @ZSp|
# 000000e0  20 53 6c 5e 67 2f 62 5a  5a 5a 5a 5d 5d 5d 46 2b  | Sl^g/bZZZZ]]]F+|
# 000000f0  0a 58 66 35 7d 49 58 37  7c 30 58 31 37 73 2b 58  |.Xf5}IX7|0X17s+X|
# 00000100  42 26 4e 29 4b 58 6e 2b  28 58 2c 4f 2b 31 71 58  |B&N)KXn+(X,O+1qX|
# 00000110  43 51 2a 29 60 58 37 7c  30 5d 5d 5d 62 5a 5a 5a  |CQ*)`X7|0]]]bZZZ|
# 00000120  5a 74 5c 5c 20 45 50 5a  59 20 53 55 59 20 58 40  |Zt\\ EPZY SUY X@|
# 00000130  57 74 7b 3e 58 58 59 55  53 58 58 5a 44 5c 5a 65  |Wt{>XXYUSXXZD\Ze|
# 00000140  55 50 5a 2c 55 65 20 5a  74 65 59 5a 59 20 53 55  |UPZ,Ue ZteYZY SU|
# 00000150  59 20 58 40 57 74 7b 3e  58 58 59 55 53 58 58 3e  |Y X@Wt{>XXYUSXX>|
# 00000160  25 6f 6f 20 45 5e 67 6a  6d 2f 77 68 3f 5a 4a 4a  |%oo E^gjm/wh?ZJJ|
# 00000170  5a 45 20 61 20 45 5c 20  5e 53 70 20 53 6c 3e 58  |ZE a E\ ^Sp Sl>X|
# 00000180  58 59 55 53 58 58 67 62  62 59 20 40 5a 59 20 53  |XYUSXXgbbY @ZY S|
# 00000190  55 59 20 58 40 57 74 7b  5e 53 55 59 20 67 2f 62  |UY X@Wt{^SUY g/b|
# 000001a0  5a 5a 5a 5a 5d 5d 5d 79  38 50 70 20 58 09 25 44  |ZZZZ]]]y8Pp X.%D|
# 000001b0  53 6c 58 47 45 55 0b 65  58 40 55 24 58 7a 25 4d  |SlXGEU.eX@U$Xz%M|
# 000001c0  6f 5c 58 55 61 20 45 58  50 70 20 58 57 74 6b 0c  |o\XUa EXPp XWtk.|
# 000001d0  58 59 55 7b 38 2f 5a 52  6d 3a 77 68 41 7e 5f 33  |XYU{8/ZRm:whA~_3|
# 000001e0  3e 36 27 5a 38 44 50 20  4d 5c 38 2f 6a 3f 56 5d  |>6'Z8DP M\8/j?V]|
# 000001f0  5d 5d 62 5a 5a 5a 5a 45  20 50 25 45 65 5a 47 74  |]]bZZZZE P%EeZGt|
# 00000200  5c 20 41 77 3e 47 41 77  59 20 53 55 59 20 5e 53  |\ Aw>GAwY SUY ^S|
# 00000210  55 59 20 67 3e 59 20 53  55 59 20 5e 67 62 62 44  |UY g>Y SUY ^gbbD|
# 00000220  40 5a 58 58 65 74 4d 20  58 58 5a 4a 4a 5a 5d 58  |@ZXXetM XXZJJZ]X|
# 00000230  58 4d 74 44 65 58 58 5d  2f 62 5a 5a 5a 5a 53 70  |XMtDeXX]/bZZZZSp|
# 00000240  20 53 6c 5e 67 62 5a 5a  5a 5a 6f 45 44 65 50 5e  | Sl^gbZZZZoEDeP^|
# 00000250  59 20 53 55 59 20 58 40  57 74 7b 5e 53 55 59 20  |Y SUY X@Wt{^SUY |
# 00000260  59 58 40 57 74 7b 67 67  62                       |YX@Wt{ggb|
# 00000269
