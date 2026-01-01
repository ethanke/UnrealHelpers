import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Install mock unreal module if running in CI (without real Unreal Engine)
try:
    import unreal
except ImportError:
    # Running outside Unreal Engine - install mock module
    from tests import mock_unreal
    sys.modules['unreal'] = mock_unreal 