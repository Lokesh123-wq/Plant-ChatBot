import os
import time

#create a unique output directory
def unique_output_directory():
    curr_time = time.strftime("%Y%m%d%H%M%S")
    output_dir = f"output_{curr_time}"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir