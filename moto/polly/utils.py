from moto.utilities.utils import get_partition


def make_arn_for_lexicon(account_id, name, region_name):
    return f"arn:{get_partition(region_name)}:polly:{region_name}:{account_id}:lexicon/{name}"
