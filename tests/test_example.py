import pytest
import unittest
from example import calculate_bmi, is_valid_email, fibonacci_sequence, find_prime_factors, merge_dictionaries, calculate_distance, parse_json_safe, filter_and_sort_numbers, count_word_frequency, validate_password, calculate_age_from_birthdate, binary_search, generate_random_string, flatten_nested_list, calculate_compound_interest, BankAccount, celsius_to_fahrenheit, find_longest_common_substring


class TestExample(unittest.TestCase):

    def test_calculate_bmi_happy_path(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    def test_calculate_bmi_invalid_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)

    def test_calculate_bmi_invalid_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)

    def test_is_valid_email_valid(self):
        self.assertTrue(is_valid_email("test@example.com"))

    def test_is_valid_email_invalid(self):
        self.assertFalse(is_valid_email("invalid_email"))

    def test_fibonacci_sequence_happy_path(self):
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])

    def test_fibonacci_sequence_edge_case(self):
        self.assertEqual(fibonacci_sequence(1), [0])

    def test_find_prime_factors_happy_path(self):
        self.assertEqual(find_prime_factors(28), [2, 2, 7])

    def test_find_prime_factors_edge_case(self):
        self.assertEqual(find_prime_factors(1), [])

    def test_merge_dictionaries_happy_path(self):
        self.assertEqual(merge_dictionaries({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})

    def test_merge_dictionaries_type_error(self):
        with self.assertRaises(TypeError):
            merge_dictionaries({'a': 1}, [1, 2, 3])

    def test_calculate_distance_happy_path(self):
        self.assertEqual(calculate_distance((1, 1), (4, 5)), 5.0)

    def test_calculate_distance_invalid_points(self):
        with self.assertRaises(ValueError):
            calculate_distance((1, 1), (4, 5, 6))

    def test_parse_json_safe_valid(self):
        self.assertEqual(parse_json_safe('{"key": "value"}'), {'key': 'value'})

    def test_parse_json_safe_invalid(self):
        self.assertIsNone(parse_json_safe('invalid json string'))

    def test_filter_and_sort_numbers_happy_path(self):
        self.assertEqual(filter_and_sort_numbers([3, 1, 4, 1, 5, 9, 2], min_value=3, max_value=5), [3, 4, 5])

    def test_filter_and_sort_numbers_invalid_input(self):
        with self.assertRaises(TypeError):
            filter_and_sort_numbers("not a list")

    def test_count_word_frequency_happy_path(self):
        self.assertEqual(count_word_frequency("Hello world hello"), {'hello': 2, 'world': 1})

    def test_count_word_frequency_invalid_input(self):
        with self.assertRaises(TypeError):
            count_word_frequency(123)

    def test_validate_password_valid(self):
        self.assertEqual(validate_password("StrongP@ssw0rd"), (True, []))

    def test_validate_password_invalid(self):
        self.assertEqual(validate_password("weak"), (False, ['Password must be at least 8 characters long', 'Password must contain at least one uppercase letter', 'Password must contain at least one digit', 'Password must contain at least one special character']))

    def test_calculate_age_from_birthdate_happy_path(self):
        self.assertEqual(calculate_age_from_birthdate('1990-01-01'), 33)

    def test_calculate_age_from_birthdate_invalid_format(self):
        with self.assertRaises(ValueError):
            calculate_age_from_birthdate('01-01-1990')

    def test_binary_search_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_binary_search_invalid_input(self):
        with self.assertRaises(TypeError):
            binary_search("not a list", 3)

    def test_generate_random_string_happy_path(self):
        self.assertEqual(len(generate_random_string(10)), 10)

    def test_generate_random_string_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_random_string(-1)

    def test_flatten_nested_list_happy_path(self):
        self.assertEqual(flatten_nested_list([1, [2, [3, 4], 5]]), [1, 2, 3, 4, 5])

    def test_flatten_nested_list_empty_list(self):
        self.assertEqual(flatten_nested_list([]), [])

    def test_calculate_compound_interest_happy_path(self):
        self.assertEqual(calculate_compound_interest(1000, 0.05, 10), 1628.89)

    def test_calculate_compound_interest_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_compound_interest(-1000, 0.05, 10)

    def test_bank_account_deposit(self):
        account = BankAccount('12345')
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_bank_account_withdraw(self):
        account = BankAccount('12345', 100)
        self.assertTrue(account.withdraw(50))
        self.assertEqual(account.get_balance(), 50)

    def test_bank_account_invalid_deposit(self):
        account = BankAccount('12345')
        with self.assertRaises(ValueError):
            account.deposit(-100)

    def test_bank_account_invalid_withdraw(self):
        account = BankAccount('12345', 100)
        self.assertFalse(account.withdraw(150))

    def test_celsius_to_fahrenheit_happy_path(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_celsius_to_fahrenheit_below_absolute_zero(self):
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(-274.15)

    def test_find_longest_common_substring_happy_path(self):
        self.assertEqual(find_longest_common_substring('abcdef', 'zabqxcdpof'), 'abcd')

    def test_find_longest_common_substring_no_common_substring(self):
        self.assertEqual(find_longest_common_substring('abcdef', '123456'), '')


if __name__ == '__main__':
    unittest.main()