Regex_Pattern = r'^[a-zA-Z]*s$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())