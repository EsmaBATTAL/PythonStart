import time
current_time = time.time()

formatted_time = f"{current_time:,.4f}"

scientific_notation = f"{current_time:.2e}"

print(f"Seconds since January 1, 1970: {formatted_time} or {scientific_notation} in scientific notation")