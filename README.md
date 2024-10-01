# Home Safety System Using LLM Agents

## Motivation
Windows are one of the most vulnerable entry points in any home. Many home security systems rely on hardware sensors for window security, which may result in false alarms. This project aims to build a software-based solution using OpenCV and Large Language Models (LLMs) to detect tampering attempts on windows. By leveraging modern image processing techniques and AI reasoning, the system will identify suspicious activity in real-time and notify homeowners, offering a more intelligent and scalable, security solution.


## Design Goals
- **Real-Time Monitoring**: Continuously monitor windows using video feeds.
- **Intelligent Detection**: Use OpenCV for motion detection and LLM agents to classify movements as normal or suspicious.
- **Instant Alerts**: Notify homeowners immediately via SMS or email upon detecting tampering.
- **Minimize False Positives**: Reduce false alarms by differentiating between harmless and suspicious movements.

## Deliverables
- Fully functional window tampering detection system using OpenCV and LLM agents.
- Evaluation of the system on multiple datasets, covering different scenarios.
- Real-time alerts via SMS or email when tampering is detected.
- Performance analysis including accuracy, false positive rates, and adaptability across datasets.
- Comprehensive user documentation for setup and usage.

## System Blocks
- **LLM Reasoning Engine**: The heart of the system, responsible for analyzing real-time inputs and making decisions.
- **Sensor Integration**: Modules that process data from cameras or sensors (like motion detectors, smoke alarms) and feed this data to the LLM.
- **Night Vision**: Enhances video processing for low-light conditions, ensuring 24/7 monitoring.
- **Dataset Integration**: Trains and tests the system on multiple datasets to handle various conditions like lighting and environment.
- **Notification System**: Alerts the user via phone or other devices when a threat is detected
- **Recording Module**: Records and stores footage of suspicious activity for later review.
- **Data Processing**: Handles the incoming data from various sensors and prepares it for analysis by the LLM.

## Software Requirements
- **Python**: programming language.
- **OpenCV**: For video and image processing.
- **TensorFlow Object Detection API**: For object detection models.
- **Langchain**: LLM agent integration.
- **smtp**: Sending real-time alerts.

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

