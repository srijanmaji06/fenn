import requests

from fenn.notification.service import Service

# from fenn.settings import settings


class Slack(Service):
    """Slack notification service using webhooks."""

    def __init__(self):
        """Initialize Slack service."""
        super().__init__()
        self._slack_webhook_url = self._keystore.get_key("SLACK_WEBHOOK_URL")
        # self._slack_webhook_url = settings.slack_webhook_url

    def send_notification(self, message: str) -> None:
        """Send notification to Slack channel.

        Args:
            message: The message to send.

        Raises:
            requests.exceptions.RequestException: If the request fails.
        """
        data = {"text": message}

        try:
            result = requests.post(self._slack_webhook_url, json=data, timeout=10)
            result.raise_for_status()
        except requests.exceptions.RequestException as err:
            raise requests.exceptions.RequestException(
                f"Failed to send Slack notification: {err}"
            ) from err


# if __name__ == "__main__":
#     s = Slack()
#     message = "hello"
#     s.send_notification(message)
#     print(f"sent: {message}")
