import re

DICE_RE = re.compile(r'(?P<count>\d{1,2})([kK]|[dD])(?P<dice>\d{1,3})(?P<bonus>\+\d{1,2})?$')

CRITICAL_RE = re.compile(r'((?P<low_range>\d{2})-(?P<high_range>\d{2}))?/?([xX](?P<multiplier>\d))$')

HANDLING_RE = re.compile(r'(?P<hand>[12])[rRhH]')
