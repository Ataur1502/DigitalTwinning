# DigitalTwinning
This project implements a Digital Twin for a titration experiment, allowing students to seamlessly transition between a physical and virtual lab environment. The system collects real-time data from an ESP32 microcontroller and stores it in a Ganache blockchain server to ensure data integrity and security.
🔹 Features:
Physical & Virtual Lab Integration – Students can start the experiment in a real lab and continue in the virtual simulation.
Real-time Data Collection – Sensor readings from the ESP32 are logged and analyzed.
Blockchain-Powered Data Storage – Secure and tamper-proof data logging using Ganache.
Interactive Visualization – A web-based interface for monitoring titration progress dynamically.
AI Assistance – Voice-enabled interaction for guidance during the experiment.
🔹 Tech Stack:
Frontend: HTML, CSS, JavaScript
Backend: Django
Hardware: ESP32
Data Storage: Ganache (Blockchain)
🔹 How It Works:
Physical Experiment: ESP32 collects titration data (e.g., liquid volume).
Data Transmission: The collected data is sent to the blockchain server (Ganache).
Virtual Twin: The web interface updates in real-time, reflecting physical changes.
Analysis & Insights: Users can analyze trends and predict titration completion.
