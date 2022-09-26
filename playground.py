#!/bin/env python3
pref = input("pref -> ")

if pref.endswith("府"):
    print(pref.removesuffix("府"))
elif pref.endswith("都"):
    print(pref.removesuffix("都"))
elif pref.endswith("県"):
    print(pref.removesuffix("県"))
else:
    print(pref)