# 📚 VocabU — Fun-Powered Vocabulary Learning Platform

VocabU is a Django-based web portal designed to make vocabulary learning more engaging and memorable using AI-generated funny images and interactive quizzes. The platform helps users learn complex words through humor, visual context, and adaptive multiple-choice questions.

---

## 🚀 Features

- 🧠 **Word Understanding**: Users can explore definitions, synonyms, and usage examples.
- ❓ **MCQ Quizzes**: Contextual multiple-choice questions powered by GPT or pre-written logic.
- 🎯 **Personalized Learning**: Uses K-Nearest Neighbors (KNN) algorithm from `scikit-learn` to adapt question difficulty based on user performance.
- 📊 **Performance Tracking**: Stores user scores and progress history.
- 🔍 **Search & Bookmarking**: Save favorite words or revisit tricky ones.

---

## 🛠 Tech Stack

- **Backend**: Django, Python 3
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: SQLite (default), PostgreSQL (optional)
- **ML & NLP**: `scikit-learn`, `pandas`, `NumPy`
- **AI Integration**: OpenAI GPT & DALL·E APIs
- **Deployment**: (Optional) Heroku, Render, or Docker

---

## 🧪 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/vocab-u.git
cd vocab-u
