#!/bin/env python3
from region import get_region
get_user_type = input("Pref > ")
region = get_region(get_user_type)
print(region)