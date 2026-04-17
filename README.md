# Network Security ML Pipeline

## Overview

This project implements an **end-to-end machine learning pipeline** for detecting malicious network activity. It follows a production-style architecture with modular components, experiment tracking, and deployment on AWS.

The system is designed to simulate a real-world **Network Intrusion Detection System (IDS)**.

---

## Features

* Modular pipeline architecture (ingestion → validation → transformation → training)
* Data validation using schema rules
* Feature engineering and preprocessing pipeline
* Experiment tracking using MLflow
* Model deployment using Docker and AWS (S3, ECR, EC2)
* Batch prediction support
* Logging and custom exception handling

---

## Project Structure

```
network-security-ml-pipeline/
│
├── networksecurity/
│   ├── components/
│   ├── pipeline/
│   ├── entity/
│   ├── utils/
│   ├── logging/
│   ├── exception/
│
├── artifacts/
├── final_model/
├── logs/
├── templates/
│
├── app.py
├── main.py
├── requirements.txt
├── setup.py
├── Dockerfile
```

---

## Pipeline Flow

```
MongoDB → Data Ingestion → Data Validation → Data Transformation
        → Model Training → Model Evaluation → Model Pusher
        → Deployment (AWS)
```

---

## Tech Stack

* Python
* Scikit-learn
* MLflow
* MongoDB Atlas
* AWS (S3, ECR, EC2)
* Docker
* GitHub Actions (CI/CD)

---

## Installation

```bash
git clone https://github.com/your-username/network-security-ml-pipeline.git
cd network-security-ml-pipeline
pip install -r requirements.txt
```

---

## Run Training Pipeline

```bash
python main.py
```

---

## Run Application

```bash
python app.py
```

---

## Key Concepts Used

* ETL Pipeline
* Data Validation using Schema
* Feature Engineering
* Machine Learning Pipeline Design
* Experiment Tracking
* Containerization & Deployment

---

## Future Improvements

* Real-time data streaming
* Advanced models (XGBoost / Deep Learning)
* Monitoring dashboard
* API-based serving (FastAPI)

---

## Author

Vaibhav Sinha

---

## License

This project is for educational purposes.
