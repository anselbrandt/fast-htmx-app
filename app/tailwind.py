from subprocess import Popen, PIPE
import logging
import os

from app.constants import ENV_MODE

log = logging.getLogger("uvicorn")


def tailwind():
    if ENV_MODE != "DEV":
        return None
    if ENV_MODE == "DEV":
        try:
            if not os.path.isfile("./tailwindcss"):
                raise FileNotFoundError("tailwindcss executable not found.")
            process = Popen(
                ["./tailwindcss", "-o", "static/tailwind.css"], stdout=PIPE, stderr=PIPE
            )
            log.info("TailwindCSS successfully started.")
            return process
        except FileNotFoundError as error:
            log.error(f"{error} TailwindCSS process not started.")
            log.error(
                "Download the executable from https://github.com/tailwindlabs/tailwindcss/releases/latest"
            )
