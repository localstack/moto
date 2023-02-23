from moto.utilities.utils import get_partition


def make_arn(region, account_id, resource_type, resource_path):
    arn_template = "arn:{partition}:elasticbeanstalk:{region}:{account_id}:{resource_type}/{resource_path}"
    arn = arn_template.format(
        partition=get_partition(region),
        region=region,
        account_id=account_id,
        resource_type=resource_type,
        resource_path=resource_path,
    )
    return arn
