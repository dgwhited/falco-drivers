import json
import boto3

DRIVERVERSION="3.0.1+driver"

def load_json(filepath):
    """Loads json content from files
    Args:
        filepath (str): Path to a file containing json
    Returns:
        [dict]: JSON loaded from the file
    """
    with open(filepath) as f:
        data = json.load(f)
    return data


def create_session(profile=None, region="us-east-1"):
    """Creates a boto session

    Args:
        profile (string): AWS profile name

    Returns:
        [object]: Authenticated Boto3 session
    """
    if profile:
        return boto3.Session(profile_name="dgwhited", region_name=region)
    else:
        return boto3.Session()


def create_client(session, service):
    """Creates a service client from a boto session

    Args:
        session (object): Authenicated boto3 session
        service (string): service name to create the client

    Returns:
        [object]: client session for specific aws service (eg. accessanalyzer)
    """
    return session.client(service)


def build_driver_string(driver):

    base = f"{DRIVERVERSION}/x86_64/falco_{driver.get('target')}.{driver.get('kernelrelease')}_{driver.get('kernelversion')}."
    module = base + "ko"

    return module


def main():
    drivers = load_json("./kernels/amazonlinux2.json")

    s3 = create_client(create_session(), "s3")

    drivers_to_build = []
    for driver in drivers.get("AmazonLinux2"):
        driver_path = build_driver_string(driver)
        try:
            s3.head_object(
                Bucket="drivers-falco",
                Key=driver_path
            )
            continue
        except:
            drivers_to_build.append(driver)
    
    print(drivers_to_build)


if __name__ == '__main__':
    main()