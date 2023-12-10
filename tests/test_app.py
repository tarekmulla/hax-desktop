from haxdesktop.app import App


def test_app():
  """Test creating the application"""
  app = App()
  app.is_ready
  assert app.is_ready
