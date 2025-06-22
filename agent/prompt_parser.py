def extract_domains(prompt: str) -> list[str]:
    import re
    # Matches domain names with optional www. or api. and supports multi-level TLDs like co.in
    pattern = r"(?:www\.|api\.)?[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)+"
    domains = re.findall(pattern, prompt.lower())
    return list(set(domains)) if domains else []