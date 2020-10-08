import os

# this tool can be used to translate `mode2` output into a lircd.conf

recording_dir = "/home/bij81sgp/Desktop/recordings"

conf_file = """# This config file written manually by Jan!

begin remote

  name  mitsubishi_ac
  flags RAW_CODES
  eps     30
  aeps   100

  ptrail   0
  repeat 0 0
  gap 28205

    begin raw_codes
"""

# Detect all recordings
recordings = []
for file in os.listdir(recording_dir):
    # recordings.append(file)
    with open(f'{recording_dir}/{file}', 'r') as file_reader:
        # print({file})
        raw_data = file_reader.read().replace("pulse", "").replace(
            "space", "").replace("\n", "").lstrip().split(" ")

        cleansed_raw_data = []
        for entry in raw_data:
            if int(entry) > 10000:
                continue
            else:
                cleansed_raw_data.append(entry)

        x = "           "
        for index, entry in enumerate(cleansed_raw_data):
            if index == 0:
                continue
            if int(entry) > 10000:
                continue
            if index % 6 == 0:
                x += f"{entry} "
                x += "\n"
                x += "           "
            else:
                x += f"{entry} "

        # print(raw_data)
        conf_file += f"        name {file}"
        conf_file += "\n"
        conf_file += x
        conf_file += "\n\n"

conf_file += """    end raw_codes

end remote
"""

print(conf_file)
