import os
import subprocess

asm_num = [
    ('১', 'এক '),
    ('২', 'দুই '),
    ('৩', 'তিনি '),
    ('৪', 'চাৰি '),
    ('৫', 'পাঁচ '),
    ('৬', 'ছয় '),
    ('৭', 'সাত '),
    ('৮', 'আঠ '),
    ('৯', 'ন '),
    ('০', 'শূন্য '),
]

def uromanize(input_string, uroman_path):
    """Convert non-Roman strings to Roman using the `uroman` perl package."""
    script_path = os.path.join(uroman_path, "bin", "uroman.pl")

    command = ["perl", script_path]
    for src, dst in asm_num:
        inputs = input_string.replace(src, dst)

    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Execute the perl command
    stdout, stderr = process.communicate(input=inputs.encode())

    if process.returncode != 0:
        raise ValueError(f"Error {process.returncode}: {stderr.decode()}")

    # Return the output as a string and skip the new-line character at the end
    return stdout.decode()[:-1]
