# acquire_data.py
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Create a rich, simulated dataset for our investigation
def generate_raw_evidence(num_records=100):
    timestamps = [datetime.now() - timedelta(minutes=random.randint(1, 100)) for _ in range(num_records)]
    users = [f'user_{random.randint(1, 10)}' for _ in range(num_records)]
    event_types = ['login', 'logout', 'file_access', 'network_connection', 'email_sent']
    events = [random.choice(event_types) for _ in range(num_records)]
    
    # Generate a mix of messages, some with potential entities
    messages = []

    for event in events:
        if event == 'login':
            messages.append(f'User logged in from IP 192.168.1.{random.randint(1, 254)}')
        elif event == 'network_connection':
            messages.append(f'Connection to www.suspicious-site-{random.randint(1, 5)}.com on port 8080')
        elif event == 'file_access':
            messages.append(f'Accessed sensitive document path: /home/{users[-1]}/docs/private_file_{random.randint(1, 5)}.txt')
        elif event == 'email_sent':
            messages.append(f'Email sent from Jane Doe to John Doe about Project X and the London office.')
        else:
            messages.append(f'{event} event.')

    # Simulate some missing data
    df = pd.DataFrame({
        'timestamp': timestamps,
        'user_id': users,
        'event_type': events,
        'message': messages
    })

    # Introduce NaN values in the dataset
    df.loc[df.sample(frac=0.1).index, 'user_id'] = np.nan
    df.loc[df.sample(frac=0.05).index, 'message'] = None

    # Save to CSV
    df.to_csv('raw_evidence.csv', index=False)
    print("Successfully generated 'raw_evidence.csv' with simulated forensic data.")

if __name__ == '__main__':
    generate_raw_evidence()
