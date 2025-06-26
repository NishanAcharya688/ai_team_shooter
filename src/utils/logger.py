# ai_team_shooter/src/utils/logger.py
from pathlib import Path
import json
import time

def setup_logging(session_name=None):
    """Initialize logging system with timestamped folder"""
    logs_dir = Path(__file__).parent.parent.parent / "logs"
    logs_dir.mkdir(exist_ok=True)
    
    session_name = session_name or f"session_{int(time.time())}"
    session_dir = logs_dir / "sessions" / session_name
    session_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Logging initialized at: {session_dir}")
