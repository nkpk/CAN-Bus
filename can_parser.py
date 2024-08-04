
#### **2. can_parser.py**
##This script contains the logic for parsing and analyzing CAN bus messages.

```python
import re
from collections import defaultdict

class CANParser:
    def __init__(self):
        self.message_counts = defaultdict(int)
        self.data_store = defaultdict(list)

    def parse_line(self, line):
        """Parse a line from the CAN bus log."""
        match = re.match(r'(\w+)\s+(\w+)\s+(\w+)\s+(.*)', line)
        if match:
            timestamp, can_id, dlc, data = match.groups()
            return {'timestamp': timestamp, 'can_id': can_id, 'dlc': dlc, 'data': data.split()}
        return None

    def process_file(self, filepath):
        """Process a CAN bus log file."""
        with open(filepath, 'r') as f:
            for line in f:
                parsed_message = self.parse_line(line.strip())
                if parsed_message:
                    self.message_counts[parsed_message['can_id']] += 1
                    self.data_store[parsed_message['can_id']].append(parsed_message)

    def get_message_counts(self):
        """Get the count of each CAN message."""
        return dict(self.message_counts)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python can_parser.py <log_file>")
        sys.exit(1)
    
    parser = CANParser()
    parser.process_file(sys.argv[1])
    counts = parser.get_message_counts()

    for can_id, count in counts.items():
        print(f"CAN ID: {can_id}, Count: {count}")
