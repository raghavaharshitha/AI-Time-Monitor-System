import time

entry_times = {}

if track_id not in entry_times:

    entry_times[track_id] = time.time()

time_spent = time.time() - entry_times[track_id]

minutes = int(time_spent // 60)
seconds = int(time_spent % 60)