from typing import Tuple

def parse_line(s: str) -> Tuple[str]:
    parsed = s.split('=')
    if len(parsed) > 1:
        return  tuple(parsed)
    else:
        return None