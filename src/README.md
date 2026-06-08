# 🤖 Line Follower Simulator

A software-based line follower robot simulator built in Python using Pygame.

This project simulates a differential-drive robot moving along a track and serves as a foundation for implementing robotics concepts such as:

- Robot kinematics
- Virtual sensors
- PID control
- Autonomous navigation
- Robotics simulation

---

## Features

### Current Features
- 2D simulation environment
- Differential-drive robot model
- Track visualization
- Robot movement and orientation display

### Planned Features
- Virtual IR sensor array
- PID-based line following
- Curved and complex tracks
- Sensor noise simulation
- Performance metrics
- ROS 2 integration

---

## Project Structure

```text
line-follower-sim/
│
├── src/
│   ├── simulator.py
│   ├── robot.py
│   ├── environment.py
│   ├── sensors.py
│   └── pid.py
│
├── tracks/
├── results/
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/line-follower-sim.git
cd line-follower-sim
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

---

## Running the Simulator

```bash
cd src
python3 simulator.py
```

---

## Technologies Used

- Python 3
- Pygame
- NumPy
- Matplotlib

---

## Learning Goals

This project is intended to explore:

- Mobile robot kinematics
- Sensor modeling
- Feedback control systems
- PID tuning
- Autonomous robot navigation

---

## Future Roadmap

- [ ] Virtual IR sensor array
- [ ] Line detection
- [ ] PID controller
- [ ] Closed-loop track
- [ ] Performance graphs
- [ ] ROS 2 version
- [ ] Gazebo integration

---

## License

MIT License
