import pytest
from can_parser import CANParser

def test_parse_line():
    parser = CANParser()
    line = "12345678 1F334455 8 11 22 33 44 55 66 77 88"
    expected_output = {
        'timestamp': '12345678',
        'can_id': '1F334455',
        'dlc': '8',
        'data': ['11', '22', '33', '44', '55', '66', '77', '88']
    }
    assert parser.parse_line(line) == expected_output

def test_parse_line_invalid():
    parser = CANParser()
    line = "Invalid line"
    assert parser.parse_line(line) is None

def test_process_file():
    parser = CANParser()
    parser.process_file('data/example_can_log.txt')
    counts = parser.get_message_counts()
    assert counts['1F334455'] == 1
    assert counts['1F223344'] == 1

def test_get_message_counts():
    parser = CANParser()
    parser.message_counts = {'1F334455': 2, '1F223344': 1}
    counts = parser.get_message_counts()
    assert counts == {'1F334455': 2, '1F223344': 1}

if __name__ == "__main__":
    pytest.main()
