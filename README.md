# CPU Scheduling Simulator

A comprehensive desktop application for visualizing and comparing different CPU scheduling algorithms with interactive Gantt charts and performance metrics.
---

## 🖥️ Overview

This project provides an intuitive GUI-based simulator for understanding and comparing various CPU scheduling algorithms used in operating systems. Perfect for students, educators, and anyone learning about process scheduling.

**Key Features:**
- 🎨 **Interactive GUI** with Tkinter
- 📊 **Real-time Gantt Chart** visualization
- 📈 **Performance Metrics** (waiting time, turnaround time)
- ⚡ **6 Scheduling Algorithms** implemented
- 🔄 **Dynamic Process Management**

## 🛠️ Supported Algorithms

| Algorithm | Type | Description |
|-----------|------|-------------|
| **FCFS** | Non-Preemptive | First Come First Serve |
| **Round Robin** | Preemptive | Time quantum-based rotation |
| **SJF (Non-Preemptive)** | Non-Preemptive | Shortest Job First |
| **SJF (Preemptive)** | Preemptive | Shortest Remaining Time |
| **Priority (Non-Preemptive)** | Non-Preemptive | Priority-based scheduling |
| **Priority (Preemptive)** | Preemptive | Dynamic priority scheduling |

## 🚀 Quick Start

### Prerequisites
```bash
pip install tkinter matplotlib
```

### Running the Application
```bash
python cpu_scheduler.py
```

## 💻 How to Use

1. **Add Processes:**
   - Enter arrival time, burst time, and priority
   - Click "Add Process" to add to the queue
   - Use "Clear" to reset all processes

2. **Select Algorithm:**
   - Choose from 6 available scheduling algorithms
   - Set time quantum for Round Robin (if selected)

3. **Run Simulation:**
   - Click "Run Scheduler" to execute
   - View results in the text area
   - Gantt chart opens automatically

4. **Analyze Results:**
   - Individual process metrics (waiting/turnaround time)
   - Average performance statistics
   - Visual timeline representation

## 📊 Features

### Interactive GUI
- **Process Input Panel:** Easy process creation and management
- **Algorithm Selection:** Radio buttons for algorithm choice
- **Results Display:** Comprehensive performance metrics
- **Real-time Updates:** Dynamic process list management

### Visualization
- **Gantt Charts:** Color-coded process execution timeline
- **Performance Metrics:** Waiting time and turnaround time analysis
- **Comparative Analysis:** Easy algorithm comparison

### Technical Implementation
- **Object-Oriented Design:** Clean, modular code structure
- **Dataclass Integration:** Efficient process attribute management
- **Matplotlib Integration:** Professional chart visualization
- **Error Handling:** Input validation and user feedback

## 📈 Output Examples

**Sample Results:**
```
P1: Waiting Time=0, Turnaround Time=5
P2: Waiting Time=5, Turnaround Time=8
P3: Waiting Time=8, Turnaround Time=12

Average Waiting Time: 4.33
Average Turnaround Time: 8.33
```

## 🏗️ Code Structure

```
cpu-scheduler-visualizer/
├── cpu_scheduler.py          # Main application
├── ProcessAttributes         # Process data structure
├── ProcessGanttChart        # Visualization class
├── Scheduling Algorithms/
│   ├── FCFS()
│   ├── Round_Robin()
│   ├── SJF (Preemptive/Non-Preemptive)
│   └── Priority (Preemptive/Non-Preemptive)
└── GUI Interface
```

## 🎓 Educational Value

Perfect for:
- **Operating Systems Courses:** Understanding process scheduling
- **Algorithm Learning:** Comparing time complexities and behaviors
- **Performance Analysis:** Measuring algorithm efficiency
- **Interactive Learning:** Visual understanding of concepts

## 🔧 Technical Highlights

- **Custom Gantt Chart Implementation:** Dynamic visualization generation
- **Preemptive Algorithm Logic:** Time-slice and priority interruption handling
- **Performance Calculation:** Accurate waiting and turnaround time computation
- **GUI Event Handling:** Responsive user interface design

## 🚀 Future Enhancements

- [ ] Export Gantt charts as images
- [ ] Save/load process sets
- [ ] Multilevel queue scheduling
- [ ] Process arrival time simulation
- [ ] Batch process comparison

## 🤝 Contributing

Contributions welcome! Please feel free to submit issues and pull requests.

---

⭐ **Perfect for learning CPU scheduling algorithms!** ⭐
