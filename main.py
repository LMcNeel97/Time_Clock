import tkinter as tk
import datetime

#  List to store clock in and clock out data
work_data = []


def clock_in():
    current_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M")
    start_time.set(current_time)
    work_data.append({"action": "Clock In", "timestamp": current_time})


def clock_out():
    current_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M")
    end_time.set(current_time)
    work_data.append({"action": "Clock Out", "timestamp": current_time})


def calculate_total_hours():
    # Initialize total_hours as a time delta
    total_hours = datetime.timedelta()

    # Sort the work_data by timestamp to ensure clock-in/clock-out pairs are in order
    sorted_work_data = sorted(work_data, key=lambda item: item["timestamp"])

    # Initialize variables to keep track of clock in and clock out times
    in_time = None
    out_time = None

    for item in sorted_work_data:
        if item["action"] == "Clock In":
            in_time = datetime.datetime.strptime(item["timestamp"], "%m-%d-%Y %H:%M")
        elif item["action"] == "Clock Out":
            out_time = datetime.datetime.strptime(item["timestamp"], "%m-%d-%Y %H:%M")
            if in_time:
                work_duration = out_time - in_time
                total_hours += work_duration
                in_time = None  # Resets the in_time for the next clock in/clock out

    total_hours_str = str(total_hours)
    total_hours_label.config(text="Total Hours Worked: " + total_hours_str)


root = tk.Tk()
root.title("Time Tracking App")

start_time = tk.StringVar()
end_time = tk.StringVar()

clock_in_button = tk.Button(root, text="Clock In", command=clock_in)
clock_in_button.pack()

clock_out_button = tk.Button(root, text="Clock Out", command=clock_out)
clock_out_button.pack()

start_label_text = tk.Label(root, text="Start Time: ")
start_label_text.pack()

start_label = tk.Label(root, textvariable=start_time)
start_label.pack()

end_label_text = tk.Label(root, text="End Time: ")
end_label_text.pack()

end_label = tk.Label(root, textvariable=end_time)
end_label.pack()

calculate_button = tk.Button(root, text="Calculate Total Hours", command=calculate_total_hours)
calculate_button.pack()

total_hours_label = tk.Label(root, text="Total Hours Worked: ")
total_hours_label.pack()

root.mainloop()
