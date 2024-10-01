# Home Safety System Using LLM Agents

## Motivation
The windows in any house are considered to be one of the weak spots in the house, due to the ease of access they offer. Instead of giving a chance to a skilled professional to break in the house, an intruder would possibly take advantage of these windows and many other uncovered entrances. All the systems predicates on the sensors are for identification rather than recognition of the latent errors. The purpose of this research is to build detection in all system approaches to how anomalies magnitude of playing losing is achieved even when cluster algorithms have not settled the inhomogeneity problem in isolation of null data. Detection of attempts to make windows irrelevant can be done using different ways including visual in remote systems, mechanics in the local advanced control systems and even software. Technology powered by image processors and AI algorithms is proposed to deliver high accuracy real-time performances to an end user.


## Design Goals:
- Create a smart monitoring system for windows, capable of detecting abnormalities in real time from live video feeds.
- Track intruders or actions that may not be lawful as a result of disrupting the normal system by analyzing the motion of objects adjacent to the windows using OpenCV.
- Minimize the number of unnecessary alarms by applying an artificial intelligence approach such that pets/script blocking or other forms of activity do not result in an alarm.
- Introduce features for homeowners that will swiftly inform them of anything unusual happening at their place, thereby allowing for quick response.

## Deliverables
- Fully functional window tampering detection system using OpenCV and LLM agents.
- Evaluation of the system on multiple datasets, covering different scenarios.
- Real time alerts via SMS or email when tampering is detected.
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

## Hardware/Software Requirements
## Software Requirements
- **Python**: Core programming language.
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

