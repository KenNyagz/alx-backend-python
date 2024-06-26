#!/usr/bin/env python3
'''
Testing client.GithubOrgClient class
'''
import unittest
import fixtures
from requests import HTTPError
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
         '''Test public repos method'''
         mock_get_json.return_value = [
             {'name': 'repo1'},
             {'name': 'repo2'}
         ]
         with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
            client = GithubOrgClient('test_org')

            result = client.public_repos()
            self.assertEqual(result, ['repo1', 'repo2'])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
        ({}, 'my_license', False),
        ({'license': {}}, 'my_licence', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        '''test GithubOrgClient.has_license method'''
        client = GithubOrgClient('test_org')
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': fixtures.TEST_PAYLOAD[0][0], 
        'repos_payload': fixtures.TEST_PAYLOAD[0][1],
        'expected_repos': fixtures.TEST_PAYLOAD[0][2],
        'apache2_repos': fixtures.TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''test the GithubOrgClient.public_repos method in an integration test'''
    @classmethod
    def setUpClass(cls):
        '''setup class'''
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_json(url):
            '''queries url'''
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_json)
        cls.get_patcher.start()
        # cls.mock_get.return_value.json.side_effect = get_json

    @classmethod
    def tearDownClass(cls):
        '''stops the patcher'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''integrated testing for GithubOrgClient.public_repos method'''
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)
    

if __name__ == '__main__':
    unittest.main()
