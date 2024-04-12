# Irreductible
Category: Misc

## Description
A Python deserialization challenge ? Easy ! I'll just copy-paste a generic payload and ... oh, oh no.

\> Deploy on [deploy.heroctf.fr](https://deploy.heroctf.fr/)

Format : **Hero{flag}**

Author : **Alol**

Attachments: [chall.zip](attachments/chall.zip)

## Write-up
- This challenge involves Python deserialization using the `pickle` module.
- Upon examining the source code, we can see that it is not a simple pickle2rce problem. The program only loads our serialized input if it iterates through the opcodes and does not encounter a REDUCE (`R`) opcode. Since remote code execution (RCE) using `pickle` heavily relies on `__reduce__`, this approach won't work. We need to find an alternative solution.
- While inspecting the `pickle` module's source code, we discovered an intriguing function called [`_instantiate`](https://github.com/python/cpython/blob/b378d991f8cd41c33416e590cb83472cce1d6b98/Lib/pickle.py#L1477).
This function attempts to instantiate a class from the `klass` parameter using the arguments from `args`.
```
def _instantiate(self, klass, args):
    if (args or not isinstance(klass, type) or
        hasattr(klass, "__getinitargs__")):
        try:
            value = klass(*args)
        except TypeError as err:
            raise TypeError("in constructor for %s: %s" %
                            (klass.__name__, str(err)), err.__traceback__)
    else:
        value = klass.__new__(klass)
    self.append(value)
```
- The object is created at this line: `value = klass(*args)`.
- Instead of passing a class to `klass`, we can specify our own function along with the necessary arguments in `args`, leading to an RCE.
- Both `load_inst` and `load_obj` functions call `_instantiate`, as seen [here](https://github.com/python/cpython/blob/b378d991f8cd41c33416e590cb83472cce1d6b98/Lib/pickle.py#L1489) and [here](https://github.com/python/cpython/blob/b378d991f8cd41c33416e590cb83472cce1d6b98/Lib/pickle.py#L1496) respectively.
- Let's examine the `load_obj` function:
```
def load_obj(self):
    # Stack is ... markobject classobject arg1 arg2 ...
    args = self.pop_mark()
    cls = args.pop(0)
    self._instantiate(cls, args)
dispatch[OBJ[0]] = load_obj
```
- According to the comment, we can prepare our payload using opcodes in the specified sequence.
- To simplify the process of writing Pickle assembly, we can utilize the `pickleassem` Python package.
- The written payload (with comments) can be found [here](solution/solve.py).

![](solution/image.png)

Flag: `Hero{Ins3cur3_d3s3ri4liz4tion_tickl3s_my_pickl3}`
