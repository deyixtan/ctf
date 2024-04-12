# can you guess?
Category: Misc

## Description
Can you guess it right?

Note: the chall.py file is used for setup purposes only and is out of scope of the challenge.

Connect with `nc -v localhost port`

Attachments: [can-you-guess.zip](attachments/can-you-guess.zip)

## Write-up
- Our initial step was to conduct a quick manual taint analysis to understand the challenge's flow and where we want our input (i.e. source) to flow to.
- We began by examining `chall.py`, the entry point for the challenge. Our objective was to print the flag (i.e. our sink).
```
if guessed.value == True:
    with open('flag.txt') as f:
        print(f.read())
```
- Upon inspection, we noticed that guessed was initially set to `False` using the line: `guessed = mp.Value('b', False)`.
- Before checking the value of guessed, the code invoked `guess()` from the `jail` module as a subprocess.
- Here's an overview of the logic in `jail.py`:
```
def jail(inp):
    return eval(inp)

def guess(inp, guessed):
    import os, random

    os.setregid(65534, 65534), os.setreuid(65534, 65534)
    try:
        r = jail(inp)
        if random.random() == r:
            print('That\'s right, but you ain\'t get any flags')
            guessed.value = False
    except Exception as e:
        print("Don't break my jail")
```
- Our observation revealed that the control flow ultimately leads to `jail()` from `guess()`, which employs `eval()` on our input. However, we faced a challenge because `guess()` sets our effective and real UID and GID to `65534`, which corresponds to the `nobody` user with limited permissions.
- As `jail()` returns, it is compared against `random.random()`, and if the conditions are met, guessed is set to `False`.
- In summary, our goal was to manipulate `guessed` through input without causing an exception and without satisfying the condition `random.random() == r`, where `r` is the output from `eval()`.
- After conducting some research, we discovered that using the `inspect` module would enable us to view variables from other stack frames.
- Additionally, if variables are in the global scope, we can manipulate their values. However, manipulating local variables of other stack frames is not possible as they are read-only.
- Interestingly, `guessed` was initialized as an `mp.Value`, which allows sharing a ctypes variable across multiple processes. Consequently, we can consider `guessed` as a reference to shared memory.
- This implies that only the reference to guessed is read-only, while it can be used to dereference and the value itself can still be modified.
- With this understanding, we devised a payload that inspects the local variable `guessed` in `guess()` from our `eval()` in `jail()` and overwrites its value to `True`.
- To ensure a valid expression and avoid exceptions, our payload includes `== 0` at the end.
- The final payload is as follows:
```
setattr(__import__("inspect").currentframe().f_back.f_back.f_locals["guessed"], "value", True) == 0
```

Flag: `shellmates{PYTHOn_FR4mE_0bj3cTs_ARENT_s3CuR3_ARE_Th3y}`
