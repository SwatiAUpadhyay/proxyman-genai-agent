from .prompt_parser import extract_domains
from .proxyman_cli_handler import capture_logs_with_proxyman, filter_logs

def run_agent(prompt: str) -> str:
    domains = extract_domains(prompt)
    if not domains:
        return "❌ No domains found in the prompt."

    output_path = capture_logs_with_proxyman(domains)
    if not output_path:
        return "❌ Proxyman CLI failed to export logs."

    return filter_logs(output_path, domains[0])