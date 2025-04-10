import unittest
from unittest.mock import patch
import unittest.mock
from src.api_client import get_location
import requests
import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class ApiClientTest(unittest.TestCase):
    
    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "Florida",
            "cityName" : "Miami",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"),"USA")
        self.assertEqual(result.get("region"),"Florida")
        self.assertEqual(result.get("city"),"Miami")
        
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")
        
        
    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code = 200,
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "Florida",
                    "cityName" : "Miami",    
                }
            )       
        ]

        with self.assertRaises(
            requests.exceptions.RequestException):
            get_location("8.8.8.8")
        
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"),"USA")
        self.assertEqual(result.get("region"),"Florida")
        self.assertEqual(result.get("city"),"Miami")
        
        