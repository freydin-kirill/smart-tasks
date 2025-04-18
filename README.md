# SmartTasks Project Documentation

## Overview

### Project Idea

> **SmartTasks** is a task management system designed to automate task-related workflows and notifications. 
> It helps users and teams efficiently track tasks by automating routine operations based on defined rules and conditions.

---

## MVP Feature List

- [ ] User registration and login functionality
- [ ] Task management: creating, updating, viewing, and deleting tasks
- [ ] Task assignment and deadline management
- [ ] Automation rule setup (e.g., "send notification if a task deadline has passed")
- [ ] Notification system integration (email notifications)
- [ ] Simple API with comprehensive documentation

---

## Microservice Architecture

### Services and Responsibilities

| Service                  | Description                                                 | Communication Method  |
|--------------------------|-------------------------------------------------------------|-----------------------|
| **User Service**         | Manages user accounts, authentication, and authorization    | HTTP (REST)           |
| **Task Service**         | Handles task creation, management, and assignment           | HTTP (REST), RabbitMQ |
| **Automation Service**   | Executes automation rules and workflows                     | RabbitMQ              |
| **Notification Service** | Sends out notifications (email/webhook)                     | RabbitMQ              |
| **API Gateway**          | Centralized API access, request routing, and JWT validation | HTTP (REST)           |

### Architectural Diagram

                             +---------------------+
                             |     API Gateway     |
                             | (Authentication,    |
                             |   Routing, Logging) |
                             +----------+----------+
                                        |
                         HTTP/REST      |     HTTP/REST (Internal)
                                        V
           +-------------------+  +---------------+  +-----------------------+
           |   User Service    |  |  Task Service |  | Automation Service    |
           | (Registration,    |  | (CRUD Tasks)  |  | (Rule Processing:     |
           |  Login, Profiles) |  |               |  |  Overdue Check)       |
           +-------------------+  +-------+-------+  +----------+------------+
                                        |                        |
                                        |                        | Publishes events  
                                        |                        | (via RabbitMQ)
                                        V                        V
                               +-----------------+     +-----------------------+
                               |  Message Broker |<----| Notification Service  |
                               |   (RabbitMQ)    |     | (Email/Webhook, etc.) |
                               +-----------------+     +-----------------------+

---

## Technology Stack

| Category             | Technology Choices                            |
|----------------------|-----------------------------------------------|
| Programming Language | Python 3.x                                    |
| Web Framework        | FastAPI                                       |
| Authentication       | OAuth2 with JWT                               |
| Databases            | PostgreSQL (primary), Redis (cache)           |
| Message Broker       | RabbitMQ                                      |
| Logging              | Loguru or structlog                           |
| Monitoring           | Prometheus + Grafana                          |
| Containerization     | Docker, docker-compose                        |
| Testing              | Pytest                                        |
| CI/CD                | GitHub Actions                                |

---

## User Stories & Scenarios

### Scenario 1: Task Creation and Automation Trigger
- User logs in and creates a new task with a specified deadline.
- Task Service stores task details and publishes an event to RabbitMQ.
- Automation Service subscribes to the event and schedules automation checks.

### Scenario 2: Overdue Task Notification
- Automation Service detects a task as overdue.
- Automation Service sends a notification request to Notification Service via RabbitMQ.
- Notification Service sends an email notification to the task owner and logs the notification delivery.

---
