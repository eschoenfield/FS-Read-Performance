#subprocess reference: https://realpython.com/python-subprocess/
#regular expression refrence: https://docs.python.org/3/library/re.html
import subprocess
import re

#read/write up to # bytes at a time
blockSizes = [1, 10, 20, 50, 100]
#copy only # input blocks
countSizes = [1, 10, 20, 50, 100]
#number of iterations
iterations = 1000

#output file
output_file = "myout.csv"

#open output file with write permission
with open(output_file, "w") as f:
    #CSV file header
    f.write(f"bs, count, timevalue\n")
    for bs in blockSizes:
        for count in countSizes:
            for i in range(iterations):
                #craft call to dd
                command = f"dd if=/dev/random of=sample.txt bs={bs}K count={count}"
                #call dd and capture the output
                result = subprocess.run(command, shell=True, capture_output=True, text=True)

                #copy bs, count, and time value to file
                time_match = re.search(r"copied, (.+?) s,", result.stderr)
                if time_match:
                    time_value = time_match.group(1)
                    f.write(f"{bs},{count},{time_value}\n")
                    #to watch the code brrr
                    print(f"iteration {i} for bs={bs}K, count={count}, Time: {time_value}")
#exit print
print(f"DONE")
