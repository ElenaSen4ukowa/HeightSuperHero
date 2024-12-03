import pytest
from unittest.mock import patch
from height_hero import get_height_hero


class TestGetHeightHero:

    @patch('requests.get')
    def test_tallest_male_with_job(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {'name': 'Hero1', 'gender': 'Male', 'height': 180, 'work': {'occupation': 'Engineer'}},
            {'name': 'Hero2', 'gender': 'Male', 'height': 190, 'work': {'occupation': 'Doctor'}},
            {'name': 'Hero3', 'gender': 'Male', 'height': 175, 'work': {'occupation': ''}},
        ]

        result = get_height_hero('Male', True)
        assert result['name'] == 'Hero2'

    @patch('requests.get')
    def test_tallest_female_with_job(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {'name': 'Hero4', 'gender': 'Female', 'height': 170, 'work': {'occupation': 'Teacher'}},
            {'name': 'Hero5', 'gender': 'Female', 'height': 165, 'work': {'occupation': ''}},
            {'name': 'Hero6', 'gender': 'Female', 'height': 180, 'work': {'occupation': 'Writer'}},
        ]

        result = get_height_hero('Female', True)
        assert result['name'] == 'Hero6'

    @patch('requests.get')
    def test_tallest_male_without_job(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {'name': 'Hero7', 'gender': 'Male', 'height': 205, 'work': {'occupation': ''}},
            {'name': 'Hero8', 'gender': 'Male', 'height': 190, 'work': {'occupation': 'Mechanic'}},
        ]

        result = get_height_hero('Male', False)
        assert result['name'] == 'Hero7'

    @patch('requests.get')
    def test_no_heroes_found(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []

        result = get_height_hero('Male', True)
        assert result is None

    @patch('requests.get')
    def test_api_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        with pytest.raises(Exception, match='Failed to fetch data from API'):
            get_height_hero('Male', True)
