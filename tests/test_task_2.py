from unittest import TestCase
from ya_loader import YaUploader

TOKEN_YADISK = '*******'


class TestCreateFolder(TestCase):
    def test_create_folder(self):
        disk_file_path = '/test_folder/'
        uploader = YaUploader(TOKEN_YADISK)
        expected = 201
        response = uploader._create_folder(disk_file_path)
        self.assertEqual(response, expected)

    def test_exists_folder(self):
        disk_file_path = '/test_folder/'
        uploader = YaUploader(TOKEN_YADISK)
        expected = 200
        response = uploader._folder_exists(disk_file_path)
        self.assertEqual(response, expected)
