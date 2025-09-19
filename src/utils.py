# Placeholder for helpers (expandable)
def safe_get(d, key, default=''):
    return d.get(key, default) if isinstance(d, dict) else default
