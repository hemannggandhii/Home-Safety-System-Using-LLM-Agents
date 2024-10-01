# Home Safety System Using LLM Agents

## Motivation
Windows are one of the most vulnerable entry points in any home. Many home security systems rely on hardware sensors for window security, which may result in false alarms. This project aims to build a software-based solution using OpenCV and Large Language Models (LLMs) to detect tampering attempts on windows. By leveraging modern image processing techniques and AI reasoning, the system will identify suspicious activity in real-time and notify homeowners, offering a more intelligent and scalable, security solution.


## Design Goals
- Live video feeds monitor windows using OpenCV for real-time motion detection.

- Machine learning LLM agents will classify detected motion as normal (e.g., wind or pets) or suspicious (e.g., tampering). These models learn and improve over time.

- Alerts will be sent to homeowners via SMS or email if suspicious activity is detected.

- Advanced ML algorithms reduce false alarms by distinguishing between harmless movements and real threats.


## Deliverables
- Window tampering detection system using OpenCV for real-time motion detection and LLM agents for activity classification. 

- Real time alert system that alerts homeowners via SMS or email when activity is detected.

- Modular codebase for easy addition of more entry points. 

- Low light detection and night vision for 24/7 monitoring.

- Automatic recording of tampering events for review or evidence. 

- Adapts to data over time, gets better and reduces false positives.

## System Blocks
- **LLM Reasoning Engine**: The heart of the system, responsible for analyzing real-time inputs and making decisions.
  
- **Sensor Integration**: Modules that process data from cameras or sensors (like motion detectors, smoke alarms) and feed this data to the LLM.
  
- **Night Vision**: Enhances video processing for low-light conditions, ensuring 24/7 monitoring.
  
- **Dataset Integration**: Trains and tests the system on multiple datasets to handle various conditions like lighting and environment.
  
- **Notification System**: Alerts the user via phone or other devices when a threat is detected
  
- **Recording Module**: Records and stores footage of suspicious activity for later review.
  
- **Data Processing**: Handles the incoming data from various sensors and prepares it for analysis by the LLM.

## Hardware/Software Requirements
- **Python**: programming language.
- Laptop with CUDA-enabled GPU

## Team Members Responsibilities
- **Hemang Gandhi**:
  - **Role**: Software implementation, algorithm design and networking
  
- **Manay Gala**:
  - **Role**: Setup, technical research and documentation.

## Project Timeline

### Week 1:
- Research OpenCV, LLM, and finalize architecture.

### Week 2:
- Start motion detection module and basic video feed testing.

### Week 3:
- Integrate LLM for tampering detection.
- **Check-in 1**: Present progress.

### Week 4:
- Refine motion detection, reduce false positives.

### Week 5:
- Add SMTP for real-time email alerts.
- Test in different conditions.

### Week 6:
- Full system testing with datasets.
- **Check-in 2**: Present system for feedback.

### Week 7:
- Finalize night vision and ensure stability.

### Week 8:
- Finalize documentation and record demo.

### Week 9:
- Final system tests.
- **Check-in 3**: Present completed project.

### Week 10:
- Review all deliverables.

### Week 11:
- Submit final project.

## References
- Langchain Documentation: [Langchain Framework](https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/)
- **Understanding LLM Agents and Tool Integration**: (https://arxiv.org/pdf/2303.17580)

