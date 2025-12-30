import os
from dotenv import load_dotenv

load_dotenv()


class ConfigurationError(Exception):
    """Raised when required configuration is missing or invalid"""


def _get_required_env(var_name: str) -> str:
    """Get a required environment variable or raise an error"""
    value = os.getenv(var_name, "").strip()
    if not value:
        raise ConfigurationError(
            f"Missing required environment variable: {var_name}\n"
            f"Please ensure your .env file or environment contains {var_name}"
        )
    return value


# Export configuration variables with validation
try:

    dns_hostname: str = _get_required_env("DNS_HOSTNAME")
    noip_username: str = _get_required_env("NOIP_USERNAME")
    noip_password: str = _get_required_env("NOIP_PASSWORD")
    otp_secret: str = _get_required_env("OTP_SECRET")
except ConfigurationError as e:
    print(f"Configuration Error: {e}")
    raise


def print_config_summary():
    """Print config summary (without sensitive data)"""
    print("Configuration loaded successfully:")
    print(f"    - DNS Hostname: {dns_hostname}")
    print(f"    - Username: {noip_username}")
    print(f"    - Password: {'*' * len(noip_password)}")
    print(f"    - OTP Secret: {'*' * len(otp_secret)}")
