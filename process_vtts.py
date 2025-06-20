import os
import re
from pathlib import Path

###############################################
# GENERATION AI SUPPORTED  
# CARMELO C. - LABORATORIO SPERIMENTALE LILEC
# UNIVERSITA' DI BOLOGNA
###############################################

# FROM THIS: 
"""
e371828e-7f70-4cb4-a3fb-18243967b8ca/30-0
00:00:03.332 --> 00:00:12.192
<v Tommaso Pellin>Ti senti vero? Non sentiamo lei,
non sentiamo noi, però ***** c'ha primis.</v>
"""

# TO THIS:
"""
# tommaso pellin	00:00:03	00:00:09	ti senti vero? non sentiamo lei, non sentiamo noi, però ***** c'ha primis.
"""

def clean_timestamp(ts):
    """Removes milliseconds from timestamp."""
    return ts.split('.')[0]

def process_vtt_file(file_path, output_dir):
    output_lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if '-->' in line:
            # Timestamp line
            timestamp_line = line
            prev_line = lines[i - 1].strip() if i > 0 else ''
            text_lines = []
            i += 1

            # Collect all subtitle text lines
            while i < len(lines) and lines[i].strip():
                text_lines.append(lines[i].strip())
                i += 1

            match = re.match(r'<v ([^>]+)>(.*?)</v>', ' '.join(text_lines))
            if match:
                speaker = match.group(1)
                text = match.group(2)
            else:
                speaker = 'UNKNOWN'
                text = ' '.join(text_lines)

            start_raw, end_raw = timestamp_line.split('-->')
            start_time = clean_timestamp(start_raw.strip())
            end_time = clean_timestamp(end_raw.strip())

            # Convert output line to lowercase
            output_line = f"# {speaker}\t{start_time}\t{end_time}\t{text}".lower()
            output_lines.append(output_line)

        i += 1

    # Save to .txt file
    output_path = os.path.join(output_dir, Path(file_path).stem + ".txt")
    with open(output_path, 'w', encoding='utf-8') as out_f:
        out_f.write('\n'.join(output_lines))

def process_all_vtt_files(folder_path):
    output_dir = os.path.join(folder_path, "output_txt")
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.vtt'):
            file_path = os.path.join(folder_path, file_name)
            process_vtt_file(file_path, output_dir)

# Run the script
if __name__ == "__main__":
    folder = "../VTT-to-TXT-For-Elan"  # ← Replace with the actual folder path
    process_all_vtt_files(folder)
