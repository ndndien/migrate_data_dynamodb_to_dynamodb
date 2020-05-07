import boto3

# source info
SOURCE_REGION = 'eu-west-1'
SOURCE_TABLE_NAME = 'table1'
SOURCE_AWS_PROFILE = 'aws_profile1'

# des info
DES_REGION = 'eu-west-2'
DES_TABLE_NAME = 'table2'
DES_AWS_PROFILE = 'des_profile2'


class DynamoObj:
    def __init__(self, session: boto3.Session, table_name: str):
        self._session = session
        self._table_name = table_name
        self._resource = self._session.resource('dynamodb')
        self._table = self._resource.Table(self._table_name)

    def get_all_items(self):
        return self._table.scan().get('Items')

    def write_all_item_to_table(self, item_list: list):
        _response_list = list()
        with self._table.batch_writer() as batch:
            for r in item_list:
                batch.put_item(Item=r)
                _res = {
                    'Status': 'Success',
                    'Payload': r
                }
                _response_list.append(_res)
        return _response_list


if __name__ == '__main__':
    source_session = boto3.Session(region_name=SOURCE_REGION, profile_name=SOURCE_AWS_PROFILE)
    source_db = DynamoObj(session=source_session, table_name=SOURCE_TABLE_NAME)
    source_items = source_db.get_all_items()

    des_session = boto3.Session(region_name=DES_REGION, profile_name=DES_AWS_PROFILE)
    des_db = DynamoObj(session=des_session, table_name=DES_TABLE_NAME)
    print(des_db.write_all_item_to_table(item_list=source_items))
