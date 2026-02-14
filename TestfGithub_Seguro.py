import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Function to validate input

def validate_input(data):
    if not isinstance(data, (int, str)):
        logging.error('Invalid input: Must be int or str')
        raise ValueError('Invalid input: Must be int or str')
    logging.info('Input validated: {}'.format(data))
    return True

# Function to mask sensitive data

def mask_data(data):
    if isinstance(data, str):
        masked = '*' * len(data[:-4]) + data[-4:]
        logging.info('Data masked: {}'.format(masked))
        return masked

# Function to demonstrate error handling

def process_data(data):
    try:
        validate_input(data)
        masked_data = mask_data(data)
        logging.info('Data processed successfully: {}'.format(masked_data))
    except Exception as e:
        logging.error('Error processing data: {}'.format(e))
        raise

# Example usage
if __name__ == '__main__':
    try:
        process_data('1234-5678-9101')
    except Exception as e:
        print('Error:', e)