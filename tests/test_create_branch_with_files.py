import pytest
import unittest
from unittest.mock import patch, Mock
from create_branch_with_files import create_branch_with_files


class TestCreateBranchWithFiles(unittest.TestCase):
    @patch('requests.get')
    @patch('requests.post')
    @patch('requests.put')
    def test_create_branch_with_files_happy_path(self, mock_put, mock_post, mock_get):
        # Setup mock responses
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'object': {'sha': 'base_sha'}}
        mock_post.return_value.status_code = 201
        mock_put.return_value.status_code = 201

        # Call the function
        result = create_branch_with_files(
            token='test_token',
            owner='test_owner',
            repo='test_repo',
            branch_name='test_branch',
            files={'test_file.txt': 'content'}
        )

        # Assertions
        self.assertTrue(result)
        mock_get.assert_called_once()
        mock_post.assert_called_once()
        mock_put.assert_called_once()

    @patch('requests.get')
    def test_create_branch_with_files_base_branch_error(self, mock_get):
        # Setup mock response for error
        mock_get.return_value.status_code = 404

        # Call the function
        result = create_branch_with_files(
            token='test_token',
            owner='test_owner',
            repo='test_repo',
            branch_name='test_branch',
            files={'test_file.txt': 'content'}
        )

        # Assertion
        self.assertFalse(result)
        mock_get.assert_called_once()

    @patch('requests.get')
    @patch('requests.post')
    def test_create_branch_with_files_branch_already_exists(self, mock_post, mock_get):
        # Setup mock responses
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'object': {'sha': 'base_sha'}}
        mock_post.return_value.status_code = 422

        # Call the function
        result = create_branch_with_files(
            token='test_token',
            owner='test_owner',
            repo='test_repo',
            branch_name='test_branch',
            files={'test_file.txt': 'content'}
        )

        # Assertion
        self.assertTrue(result)
        mock_get.assert_called_once()
        mock_post.assert_called_once()

    @patch('requests.get')
    @patch('requests.post')
    @patch('requests.put')
    def test_create_branch_with_files_add_file_error(self, mock_put, mock_post, mock_get):
        # Setup mock responses
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'object': {'sha': 'base_sha'}}
        mock_post.return_value.status_code = 201
        mock_put.return_value.status_code = 400

        # Call the function
        result = create_branch_with_files(
            token='test_token',
            owner='test_owner',
            repo='test_repo',
            branch_name='test_branch',
            files={'test_file.txt': 'content'}
        )

        # Assertion
        self.assertFalse(result)
        mock_get.assert_called_once()
        mock_post.assert_called_once()
        mock_put.assert_called_once()

    @patch('requests.get')
    @patch('requests.post')
    @patch('requests.put')
    def test_create_branch_with_files_request_exception(self, mock_put, mock_post, mock_get):
        # Setup mock responses to raise exception
        mock_get.side_effect = requests.exceptions.RequestException('Test exception')

        # Call the function
        result = create_branch_with_files(
            token='test_token',
            owner='test_owner',
            repo='test_repo',
            branch_name='test_branch',
            files={'test_file.txt': 'content'}
        )

        # Assertion
        self.assertFalse(result)
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()