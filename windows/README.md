To compile, use **Microsoft keyboard Layout Creator**.

To disbable `CAPS`, change the file
```
C:\Program Files (x86)\Microsoft Keyboard Layout Creator 1.4\inc\kbd.h
```
by replacing the key definition:
```
> #define T3A _EQ(                           CAPITAL                   )
< #define T3A _EQ(                           _none_                    )
```
