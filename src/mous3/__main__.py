# __main__.py

import boto3
import argparse

def print_bytes(direction, bucket_name, key, bytes_to_download=1000, aws_profile=None):
    """
    Print the first or last 'bytes_to_download' bytes of an object from an S3 bucket using a specified AWS profile.

    :param direction: The direction to read from the object. Can be "head" or "tail".
    :param bucket_name: Name of the S3 bucket.
    :param key: Key of the object.
    :param bytes_to_download: Number of bytes to download from the end of the object.
    :param aws_profile: Optional AWS profile to use for the session.
    """
    
    # If the direction is 'head', set the bytes to a range starting at 0
    if direction == 'head':
        bytes_to_download = f'0-{bytes_to_download}'
    # If the direction is 'tail', set the bytes to download to a negative number
    elif direction == 'tail':
        bytes_to_download = -bytes_to_download

    # Create a session using the specified AWS profile, if provided
    session = boto3.Session(profile_name=aws_profile) if aws_profile else boto3.Session()
    
    # Create an S3 client from the session
    s3_client = session.client('s3')
    
    # Specify the range of bytes to download (last 'bytes_to_download' bytes)
    byte_range = f"bytes={bytes_to_download}"

    try:
        # Get the object
        response = s3_client.get_object(Bucket=bucket_name, Key=key, Range=byte_range)
        
        # Read the response and decode it to a string
        content = response['Body'].read().decode('utf-8')
        
        # Print the content
        print(content)

        # Return 0 to indicate success
        return 0
    except Exception as e:
        print(f"Failed to download object: {e}")

        # Return 1 to indicate failure
        return 1

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Print the last bytes of an S3 object using a specific AWS profile.')
    parser.add_argument('direction', choices=['head', 'tail'], help='The direction to read from the object. Can be "head" or "tail".')
    parser.add_argument('bucket_name', help='The name of the S3 bucket.')
    parser.add_argument('key', help='The key of the object in the S3 bucket.')
    parser.add_argument('--bytes', type=int, default=1000, help='Number of bytes to download. Default is 1000. You do not need to specify positive or negative, as this is determined by the "direction" argument.')
    parser.add_argument('--profile', type=str, default=None, help='The AWS profile to use.')

    # Parse command line arguments
    args = parser.parse_args()

    # Call the function with provided arguments and exit with return code
    raise SystemExit(print_bytes(args.direction, args.bucket_name, args.key, args.bytes, args.profile))

if __name__ == '__main__':
    main()
