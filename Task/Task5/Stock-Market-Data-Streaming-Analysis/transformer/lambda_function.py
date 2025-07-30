import base64
import json
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    output = []
    logger.info(f"Received event: {json.dumps(event)}")
    
    for record in event['records']:
        try:
            logger.info(f"Processing recordId: {record['recordId']}")
            logger.info(f"Raw data: {record['data']}")
            

            decoded_data = base64.b64decode(record['data']).decode('utf-8')
            logger.info(f"Decoded data: {decoded_data}")
            

            payload = json.loads(decoded_data)
            logger.info(f"Parsed payload: {json.dumps(payload)}")
            

            dt = datetime.strptime(payload['timestamp'], "%Y-%m-%d %H:%M:%S")
            
            # Transform data
            transformed = {
                'symbol': payload['symbol'],
                'datetime': payload['timestamp'],
                'open': payload['open'],
                'high': payload['high'],
                'low': payload['low'],
                'close': payload['close'],
                'volume': payload['volume'],
                'date': dt.date().isoformat(),
                'hour': dt.hour
            }
            

            encoded_data = base64.b64encode(json.dumps(transformed).encode('utf-8')).decode('utf-8')
            
            output.append({
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': encoded_data,
                'metadata': {
                    'partitionKeys': {
                        'symbol': payload['symbol'],
                        'date': dt.date().isoformat(),
                        'hour': dt.hour
                    }
                }
            })
            
        except Exception as e:
            logger.error(f"Error processing record {record['recordId']}: {str(e)}", exc_info=True)
            output.append({
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data'],
                'message': str(e)  # Include error message for debugging
            })
    
    print(output)
    logger.info(f"Returning {len(output)} records")
    return {'records': output}


