# Python's REPL (read-eval-print loop) is a perfect place for quick test of statements, as well as for some calculations

# Simple expressions
val = 12 + 34 * (56 + 78)

# Utility code
list1 = ['apple', 'melon']
list2 = ['apple', 'banana']

set(list1) - set(list2)
set(list2) - set(list1)

# Checking some Python functions
a = sorted([2, 4, 1, 6], reverse=True)
a.sort(reverse=False)

# Finding public methods and constants of classes
import datetime
dir(datetime)
datetime.MAXYEAR

import requests
dir(requests)
requests.__cake__
