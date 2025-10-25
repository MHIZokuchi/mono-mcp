import os

REQUIRED_ENV = ("MONO_SECRET_KEY", "WEBHOOK_SECRET")


def validate_env() -> None:
    missing = [k for k in REQUIRED_ENV if not os.getenv(k)]
    if missing:
        raise RuntimeError(
            "Missing required environment variables: "
            + ", ".join(missing)
            + ". Copy .env and set values before starting the server."
        )
