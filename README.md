# migrate_data_dynamodb_to_dynamodb
Migrate data from a dynamodb table to another dynamodb table

Install requirements (boto3):

    pip install -r requirements.txt

Prepare some vars below

Source info
    SOURCE_REGION = 'eu-west-1'
    SOURCE_TABLE_NAME = 'table1'
    SOURCE_AWS_PROFILE = 'aws_profile1'

Des info
    DES_REGION = 'eu-west-2'
    DES_TABLE_NAME = 'table2'
    DES_AWS_PROFILE = 'des_profile2'

Then run:

    python3 migrate_dynamodb_data.py