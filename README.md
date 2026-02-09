# Football Performance Decision Support API

A lightweight production-oriented backend service designed to demonstrate how applied AI concepts can be operationalised into real-time decision-support systems for football performance environments.

This project focuses on transforming analytical prototypes into deployable services using modern backend, containerisation, and cloud-ready engineering practices.

---

## Project Purpose

Football performance departments increasingly rely on AI-driven insights during live matches, training sessions, and tactical analysis workflows. However, many analytical models remain isolated notebooks or research prototypes.

This project demonstrates how such models can be converted into a **production-style API service** that:

- Accepts structured match context data  
- Applies decision logic representing AI-assisted reasoning  
- Returns interpretable tactical recommendations in real time  
- Is containerised and deployable in cloud environments  

The objective is not only prediction, but **operational decision support**, aligned with real-world performance science workflows.

---

## System Architecture

Client (Coach / Analyst System)  
→ FastAPI Backend Service  
→ Decision Logic Layer (AI reasoning / rules / model inference)  
→ JSON Response (Recommendation + Explanation + Confidence)

The design intentionally separates:

- API layer  
- Decision logic  
- Data schemas  

This mirrors real production engineering practices where models must be exposed reliably through backend services.

---

## Key Features

- Production-style REST API using **FastAPI**
- Structured request validation using **Pydantic**
- Modular system design separating API, schemas, and decision logic
- Containerised deployment using **Docker**
- Cloud-ready deployment compatible with **Google Cloud Run / AWS**
- Designed specifically for **football performance decision-support scenarios**

---

## Technology Stack

- Python 3.11  
- FastAPI  
- Pydantic  
- Uvicorn  
- Docker  
- Cloud-ready deployment architecture (GCP / AWS compatible)  
- GitHub Actions CI pipeline (build validation ready)

---

## Example Use Case

The service can support match-time reasoning scenarios such as:

- Tactical shape stability recommendations  
- Fatigue-based substitution alerts  
- Possession-trend contextual decisions  
- Game-state-aware performance adjustments  

Example API request:

```json
{
  "minute": 65,
  "score_diff": 1,
  "fatigue_level": 0.6,
  "possession_trend": 0.3
}
