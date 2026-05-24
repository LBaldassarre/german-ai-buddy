# German AI Tutor

An AI-powered German conversation tutor designed to help learners improve fluency through natural conversation, adaptive corrections, and personalized learning memory.

This project combines:

* Conversational AI
* Language learning
* Speech technologies
* Learning analytics
* Full-stack engineering

The goal is to create a tutor that feels more like a real conversational partner than a traditional exercise app.

---

# Features (Planned)

## MVP

* Text-based German conversations
* Grammar corrections
* Natural phrasing suggestions
* Context-aware follow-up questions
* Conversation history

## Phase 2

* Persistent learner memory
* Recurring mistake tracking
* Vocabulary tracking
* Personalized tutoring prompts

## Phase 3

* Voice input
* Speech-to-text
* Text-to-speech
* Realtime conversations

## Future Ideas

* Electron desktop app
* React Native mobile app
* Spaced repetition system
* Learning analytics dashboard
* Pronunciation feedback
* CEFR progression tracking

---

# Tech Stack

## Frontend

* React
* Vite
* TypeScript

## Backend

* FastAPI
* Python

## Database

* SQLite

## AI

* OpenAI API

---

# Repository Structure

```text
german-ai-tutor/
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── german_tutor.db
│
└── docs/
```

---

# Architecture Overview

```text
Frontend
   ↓
FastAPI API
   ↓
Tutor Service
   ↓
Memory Service
   ↓
OpenAI Service
   ↓
Response
```

## Core Design Principles

* Fluency over perfection
* Lightweight corrections
* Adaptive learning
* Separation of concerns
* Progressive complexity
* Fast iteration

---

# Development Philosophy

This project intentionally starts simple.

The initial focus is:

* validating the tutoring experience
* creating useful conversational flows
* building sustainable learning loops

Complexity such as:

* realtime infrastructure
* advanced memory systems
* distributed services
* vector databases

will only be added once the product justifies them.

---

# Current Status

🚧 Early development / MVP phase

Initial milestone:

* User sends German text
* AI returns:

  * correction
  * explanation
  * natural response
  * follow-up question

---

# Getting Started

## Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate
# Windows:
# venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Environment Variables

Create a `.env` file in the backend folder:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# Long-Term Vision

The long-term goal is to build a personalized conversational language-learning system that:

* adapts to the learner
* tracks recurring weaknesses
* encourages speaking confidence
* provides realistic conversational practice
* combines AI tutoring with learning analytics

---

# Why This Project Exists

Most language-learning apps:

* overfocus on drills
* interrupt too often
* lack personalization
* do not adapt to recurring learner mistakes

This project aims to create a more natural and motivating learning experience using modern AI capabilities.

---

# License

MIT License
