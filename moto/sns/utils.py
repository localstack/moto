from moto.utilities.utils import get_partition
import re
from moto.moto_api._internal import mock_random

E164_REGEX = re.compile(r"^\+?[1-9]\d{1,14}$")


def make_arn_for_topic(account_id, name, region_name):
    return f"arn:{get_partition(region_name)}:sns:{region_name}:{account_id}:{name}"


def make_arn_for_subscription(topic_arn):
    subscription_id = mock_random.uuid4()
    return f"{topic_arn}:{subscription_id}"


def is_e164(number):
    return E164_REGEX.match(number) is not None
