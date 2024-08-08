from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from threading import Lock

@dataclass
class Event:
    timestamp: datetime
    data: str

@dataclass
class Job:
    result: str
    status: str
    events: List[Event]

job_lock = Lock()
jobs: Dict[str, 'Job'] = {}

def append_event(job_id:str, event_data:str):
    with job_lock:
        if job_id not in jobs:
            print(f'Job Started {job_id}')
            jobs[job_id] = Job(result='',status='running',events=[])
        else:
            print("Appending event for job")
        jobs[job_id].events.append(Event(timestamp=datetime.now(),data=event_data))   