#!/usr/bin/env python3
'''
Testing client.GithubOrgClient class
'''
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Testing github org client'''
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock_get_json):
        '''Testing org method'''
        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(result, {'key': 'value'})

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        '''testing _public_repos_url method'''
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/test_org/repos'
        }
        client = GithubOrgClient('test_org')
        result = client._public_repos_url

        self.assertEqual(result, 'https://api.github.com/orgs/test_org/repos')


if __name__ == '__main__':
    unittest.main()
