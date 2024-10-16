import json
import sys


def update_test_values(tests, values_dict):
    for test in tests:
        if test['id'] in values_dict:
            test['value'] = values_dict[test['id']]

        if 'values' in test:
            update_test_values(test['values'], values_dict)
    return tests


def main():
    tests_path = sys.argv[1]
    values_path = sys.argv[2]
    report_path = sys.argv[3]

    with open(tests_path, 'r') as f:
        tests_data = json.load(f)
        tests = tests_data['tests']

    with open(values_path, 'r') as f:
        values_data = json.load(f)
        values = values_data['values']

    values_dict = {item['id']: item['value'] for item in values}
    updated_tests = update_test_values(tests, values_dict)

    with open(report_path, 'w') as f:
        json.dump(updated_tests, f, indent=4)


if __name__ == "__main__":
    main()

