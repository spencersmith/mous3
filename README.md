
# mous3
A python utility that allows you to print a number of bytes from either the beginning or end of an object stored on AWS S3 without downloading the entire file.

## Features
-  **AWS Profile Support**: Optionally specify an AWS profile to use for accessing the S3 bucket, making it easier to work with multiple AWS accounts or configurations.

-  **Flexible Byte Range**: Customize the number of bytes you want to read from the end of the object.

## Requirements
- Python 3.6+
- Boto3

## Installation
- `pip install mous3`

- Your AWS credentials will need to be stored in `~/.aws/credentials` or set as environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).

## Usage

`mous3 [-h] [--bytes BYTES] [--profile PROFILE] {direction} {bucket_name} {key}`

#### Positional arguments:
`direction` The direction to read from the object. Can be "head" or "tail".

`bucket_name` The name of the S3 bucket.

`key` The key of the object in the S3 bucket.

#### Optional arguments:

```
-h, --help show this help message and exit

--bytes BYTES Number of bytes to download. Default is 1000. You do not need to specify positive or negative, as this is determined by the "direction" argument.

--profile PROFILE The AWS profile to use. Optional.
```
  
  

## Examples:
- To print the first 1000 bytes (head) of an object using the AWS profile named `myProfile`:
  - `mous3 head my-bucket example.log --profile myProfile`
- To print the last 1000 bytes (tail) of an object named `example.log` in the bucket `my-bucket`:
  - `mous3 tail my-bucket example.log`
- To print the last 200 bytes of the object:
  - `mous3 tail my-bucket example.log --bytes 200`
