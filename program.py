import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class ProcessAttributes:
    pid: int
    arrivalTime: int
    burstTime: int
    priority: int = 0
    WaitingTime: int = 0
    TurnAroundTime: int = 0

class ProcessGanttChart:
    def __init__(self):
        self._Color = ['skyblue', 'salmon', 'lightgreen', 'orange', 'pink']

    def Create_Step_GanttChart(self, steps, algorithm_name):
        """Creates a Gantt chart dynamically based on the steps."""
        fig, ax = plt.subplots(figsize=(8, 2))
        current_time = 0

        for step in steps:
            pid, exec_time = step
            ax.barh(["Time"], exec_time, left=current_time, color=self._Color[pid % len(self._Color)])
            ax.text(current_time + exec_time / 2, 0, f"P{pid}", ha='center', va='center', color='black', fontsize=10)
            current_time += exec_time

        plt.xlabel("Time")
        plt.title(algorithm_name)
        plt.show()

# Scheduling Algorithms
def FCFS(processes):
    processes.sort(key=lambda x: x.arrivalTime)
    current_time = 0
    steps = []

    for process in processes:
        if current_time < process.arrivalTime:
            current_time = process.arrivalTime

        process.WaitingTime = current_time - process.arrivalTime
        process.TurnAroundTime = process.WaitingTime + process.burstTime
        steps.append((process.pid, process.burstTime))
        current_time += process.burstTime

    return processes, steps

def Round_Robin(processes, quantum):
    processes.sort(key=lambda x: x.arrivalTime)  # Sort by arrival time
    remaining_time = [process.burstTime for process in processes]
    current_time = 0
    steps = []
    completed = [False] * len(processes)

    while not all(completed):
        made_progress = False
        for i, process in enumerate(processes):
            if remaining_time[i] > 0 and process.arrivalTime <= current_time:
                made_progress = True
                exec_time = min(quantum, remaining_time[i])
                steps.append((process.pid, exec_time))
                current_time += exec_time
                remaining_time[i] -= exec_time

                if remaining_time[i] == 0:
                    process.TurnAroundTime = current_time - process.arrivalTime
                    process.WaitingTime = process.TurnAroundTime - process.burstTime
                    completed[i] = True

        if not made_progress:  
            current_time += 1

    return processes, steps

def Non_Preemptive_SJF(processes):
    processes.sort(key=lambda x: (x.arrivalTime, x.burstTime))
    return FCFS(processes)

def Preemptive_SJF(processes):
    processes.sort(key=lambda x: x.arrivalTime)
    remaining_time = [process.burstTime for process in processes]
    current_time = 0
    steps = []
    completed = 0

    while completed < len(processes):
        available_processes = [p for i, p in enumerate(processes) if remaining_time[i] > 0 and p.arrivalTime <= current_time]
        if not available_processes:
            current_time += 1
            continue

        shortest_process = min(available_processes, key=lambda p: remaining_time[p.pid - 1])
        steps.append((shortest_process.pid, 1))
        remaining_time[shortest_process.pid - 1] -= 1
        current_time += 1

        if remaining_time[shortest_process.pid - 1] == 0:
            shortest_process.TurnAroundTime = current_time - shortest_process.arrivalTime
            shortest_process.WaitingTime = shortest_process.TurnAroundTime - shortest_process.burstTime
            completed += 1

    return processes, steps

def Non_Preemptive_Priority(processes):
    processes.sort(key=lambda x: (x.priority, x.arrivalTime))
    return FCFS(processes)

def Preemptive_Priority(processes):
    processes.sort(key=lambda x: x.arrivalTime)
    remaining_time = [process.burstTime for process in processes]
    current_time = 0
    steps = []
    completed = 0

    while completed < len(processes):
        available_processes = [p for i, p in enumerate(processes) if remaining_time[i] > 0 and p.arrivalTime <= current_time]
        if not available_processes:
            current_time += 1
            continue

        highest_priority_process = min(available_processes, key=lambda p: p.priority)
        steps.append((highest_priority_process.pid, 1))
        remaining_time[highest_priority_process.pid - 1] -= 1
        current_time += 1

        if remaining_time[highest_priority_process.pid - 1] == 0:
            highest_priority_process.TurnAroundTime = current_time - highest_priority_process.arrivalTime
            highest_priority_process.WaitingTime = highest_priority_process.TurnAroundTime - highest_priority_process.burstTime
            completed += 1

    return processes, steps

def run_scheduler(algorithm, processes, quantum=0):
    if algorithm == "FCFS":
        return FCFS(processes)
    elif algorithm == "Round Robin":
        return Round_Robin(processes, quantum)
    elif algorithm == "Non-Preemptive SJF":
        return Non_Preemptive_SJF(processes)
    elif algorithm == "Preemptive SJF":
        return Preemptive_SJF(processes)
    elif algorithm == "Non-Preemptive Priority":
        return Non_Preemptive_Priority(processes)
    elif algorithm == "Preemptive Priority":
        return Preemptive_Priority(processes)

def gui_interface():
    processes = []

    def add_process():
        try:
            arrival_time = int(arrival_entry.get())
            burst_time = int(burst_entry.get())
            priority = int(priority_entry.get()) if priority_entry.get() else 0
            pid = len(processes) + 1
            processes.append(ProcessAttributes(pid, arrival_time, burst_time, priority))
            process_list.insert(tk.END, f"P{pid}: Arrival={arrival_time}, Burst={burst_time}, Priority={priority}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integer values.")

    def clear_processes():
        processes.clear()
        process_list.delete(0, tk.END)

    def run():
        algorithm = algorithm_var.get()
        quantum = int(quantum_entry.get()) if quantum_entry.get() else processes[0].burstTime if processes else 0
        if not processes:
            messagebox.showerror("No Processes", "Add at least one process.")
            return
        gantt_chart = ProcessGanttChart()
        completed_processes, steps = run_scheduler(algorithm, processes, quantum)
        total_waiting_time = sum(p.WaitingTime for p in completed_processes)
        total_turnaround_time = sum(p.TurnAroundTime for p in completed_processes)
        avg_waiting_time = total_waiting_time / len(completed_processes)
        avg_turnaround_time = total_turnaround_time / len(completed_processes)
        
        result_text.delete(1.0, tk.END)
        for p in completed_processes:
            result_text.insert(tk.END, f"P{p.pid}: Waiting Time={p.WaitingTime}, Turnaround Time={p.TurnAroundTime}\n")
        result_text.insert(tk.END, f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
        result_text.insert(tk.END, f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
        
        gantt_chart.Create_Step_GanttChart(steps, algorithm)

    root = tk.Tk()
    root.title("CPU Scheduling Simulator")

    # Input Frame
    input_frame = ttk.LabelFrame(root, text="Process Inputs")
    input_frame.grid(row=0, column=0, padx=10, pady=10)

    ttk.Label(input_frame, text="Arrival Time:").grid(row=0, column=0)
    arrival_entry = ttk.Entry(input_frame)
    arrival_entry.grid(row=0, column=1)

    ttk.Label(input_frame, text="Burst Time:").grid(row=1, column=0)
    burst_entry = ttk.Entry(input_frame)
    burst_entry.grid(row=1, column=1)

    ttk.Label(input_frame, text="Priority:").grid(row=2, column=0)
    priority_entry = ttk.Entry(input_frame)
    priority_entry.grid(row=2, column=1)

    ttk.Button(input_frame, text="Add Process", command=add_process).grid(row=3, column=0)
    ttk.Button(input_frame, text="Clear", command=clear_processes).grid(row=3, column=1)

    process_list = tk.Listbox(input_frame, width=40)
    process_list.grid(row=4, column=0, columnspan=2)

    # Algorithm Frame
    algo_frame = ttk.LabelFrame(root, text="Scheduling Algorithm")
    algo_frame.grid(row=1, column=0, padx=10, pady=10)

    algorithm_var = tk.StringVar(value="FCFS")
    ttk.Radiobutton(algo_frame, text="FCFS", variable=algorithm_var, value="FCFS").grid(row=0, column=0)
    ttk.Radiobutton(algo_frame, text="Round Robin", variable=algorithm_var, value="Round Robin").grid(row=1, column=0)
    ttk.Radiobutton(algo_frame, text="Non-Preemptive SJF", variable=algorithm_var, value="Non-Preemptive SJF").grid(row=2, column=0)
    ttk.Radiobutton(algo_frame, text="Preemptive SJF", variable=algorithm_var, value="Preemptive SJF").grid(row=3, column=0)
    ttk.Radiobutton(algo_frame, text="Non-Preemptive Priority", variable=algorithm_var, value="Non-Preemptive Priority").grid(row=4, column=0)
    ttk.Radiobutton(algo_frame, text="Preemptive Priority", variable=algorithm_var, value="Preemptive Priority").grid(row=5, column=0)

    ttk.Label(algo_frame, text="Time Quantum (RR):").grid(row=6, column=0)
    quantum_entry = ttk.Entry(algo_frame)
    quantum_entry.grid(row=7, column=0)

    ttk.Button(algo_frame, text="Run Scheduler", command=run).grid(row=8, column=0)

    # Result Frame
    result_frame = ttk.LabelFrame(root, text="Results")
    result_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
    result_text = tk.Text(result_frame, width=40, height=20)
    result_text.grid(row=0, column=0)

    root.mainloop()


if __name__ == "__main__":
    gui_interface()
