from django.test import testcases
import unittest
from unittest.mock import patch, MagicMock
from ..src.spotify.spotify import get_spotify_data
from ..src.youtube.youtube import download_song_from_youtube
from main import tracks, logger

class TestMain(unittest.TestCase):

    @patch('src.spotify.spotify.get_spotify_data')
    def test_valid_spotify_track_url(self, mock_get_spotify_data):
        """Test processing a valid Spotify track URL"""
        mock_get_spotify_data.return_value = [
            {
                "title": "Never Gonna Give You Up",
                "artist": "Rick Astley",
                "album": "Whenever You Need Somebody",
                "release_date": "1987-07-27",
                "spotify_url": "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT"
            }
        ]

        result = get_spotify_data("https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Never Gonna Give You Up")
        self.assertEqual(result[0]["artist"], "Rick Astley")

    @patch('src.spotify.spotify.get_spotify_data')
    def test_valid_spotify_playlist_url(self, mock_get_spotify_data):
        """Test processing a valid Spotify playlist URL"""
        mock_get_spotify_data.return_value = [
            {"title": "Song 1", "artist": "Artist 1"},
            {"title": "Song 2", "artist": "Artist 2"},
        ]

        result = get_spotify_data("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["title"], "Song 1")
        self.assertEqual(result[1]["title"], "Song 2")

    @patch('src.spotify.spotify.get_spotify_data')
    def test_invalid_spotify_url(self, mock_get_spotify_data):
        """Test handling of an invalid Spotify URL"""
        mock_get_spotify_data.return_value = {"error": "Invalid Spotify URL"}

        result = get_spotify_data("https://example.com/invalid")

        self.assertIn("error", result)
        self.assertEqual(result["error"], "Invalid Spotify URL")

    @patch('src.youtube.youtube.download_song_from_youtube')
    def test_download_song_success(self, mock_download):
        """Test successful song download from YouTube"""
        mock_download.return_value = "Never Gonna Give You Up - Rick Astley.mp3"

        result = download_song_from_youtube("Never Gonna Give You Up", "Rick Astley")

        self.assertEqual(result, "Never Gonna Give You Up - Rick Astley.mp3")

    @patch('src.youtube.youtube.download_song_from_youtube')
    def test_download_song_failure(self, mock_download):
        """Test failed song download from YouTube"""
        mock_download.return_value = None

        result = download_song_from_youtube("Fake Song", "Fake Artist")

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
