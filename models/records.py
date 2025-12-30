from playwright.sync_api import Page, expect, TimeoutError
from config import dns_hostname
from datetime import datetime
from pathlib import Path
from browser_config import SCREENSHOT_DIR
from logger import get_logger

log = get_logger("records")


class RecordsPage:
    def __init__(self, page: Page):
        self.page = page
        self.expiration_banner = page.locator(
            f'[id="expiration-banner-hostname-{dns_hostname}"]'
        )
        self.confirm_button = page.get_by_role("button", name="Confirm")

        try:
            log.debug(f"Checking for expiration banner for '{dns_hostname}'...")
            expect(self.expiration_banner).to_be_visible(timeout=10000)
            log.info(f"Expiration banner found for hostname '{dns_hostname}'")
        except TimeoutError:
            log.warning(f"Expiration banner not found for '{dns_hostname}'")
            raise Exception(
                f"Expiration banner not found for hostname '{dns_hostname}'. "
                "The hostname might already be renewed or not expiring within 7 days."
            )

    def renew_hostname(self):
        """Renew hostname with error handling"""
        try:
            log.debug("Clicking confirm button to renew hostname...")
            self.confirm_button.click()
            self.page.wait_for_load_state("networkidle", timeout=15000)
            log.info("Hostname renewal confirmed")
        except TimeoutError:
            log.error("Confirm button timeout")
            raise Exception("Failed to confirm hostname renewal - page timeout")
        except Exception as e:
            log.error(f"Confirm button click failed: {e}")
            raise Exception(f"Failed to click confirm button: {e}")

        try:
            self._capture_screenshot()
        except Exception as e:
            log.warning(f"Screenshot capture failed: {e}")

    def _capture_screenshot(self):
        """Capture screenshot"""
        try:
            screenshot_dir = Path(SCREENSHOT_DIR)
            if not screenshot_dir.is_absolute():
                screenshot_dir = Path(__file__).parent.parent / screenshot_dir

            timestamp: str = datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M")
            screenshot_path = screenshot_dir / f"dns_renewal_{timestamp}.png"

            screenshot_path.parent.mkdir(parents=True, exist_ok=True)

            log.debug(f"Saving screenshot to: {screenshot_path}")
            self.page.screenshot(path=str(screenshot_path))
            log.info(f"Screenshot saved: {screenshot_path.name}")

        except Exception as e:
            log.error(f"Screenshot save failed: {e}")
            raise Exception(f"Screenshot save failed: {e}")
