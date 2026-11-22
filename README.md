# 𖠚 Cafe & Wifi Directory

A full-stack web application built with **Python**, **Flask**, and **SQLite** that helps remote workers and students find laptop-friendly cafes. Users can browse cafes, search by name or location, filter by essential work amenities, and manage cafe listings with full CRUD functionality.

## ✨ Features

- **Search & Multi-Filter Discovery:** Search cafes dynamically by name or neighborhood, and filter results by **Wi-Fi**, **Power Sockets**, and **Toilet** availability.
- **Detailed Cafe Cards:** Displays cafe photos, seating capacity, coffee pricing, map links (`View on Map`), and amenity indicators (Wi-Fi, Sockets, Toilet, Calls).
- **Full CRUD Management:**
  - **Add Cafe:** Submit new laptop-friendly cafes via a dedicated form.
  - **Edit Cafe:** Update existing cafe details and amenities seamlessly.
  - **Smooth Async Deletion:** Delete cafes with a confirmation prompt and instant DOM removal via JavaScript `fetch()` without resetting page scroll position.
- **Responsive UI:** Built with **Bootstrap 5** and custom CSS for clean card layouts across desktop and mobile screens.

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Database:** SQLite (`cafes.db`)
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (`fetch` API), Jinja2 Templates

## 📂 Project Structure

```text
cafe-and-wifi-website/
├── static/
│   └── style.css         # Custom styling
├── templates/
│   ├── index.html        # Home page with search, filters, and cafe cards
│   ├── add.html          # Form to add a new cafe
│   └── edit.html         # Form to edit an existing cafe
├── cafes.db              # SQLite database
├── main.py               # Flask routes, database models, and app logic
├── .gitignore            # Ignored virtual environment and cache files
└── README.md             # Project documentation
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/cafe-and-wifi-website.git](https://github.com/priya-veejay11/cafe-and-wifi-website.git)
cd cafe-and-wifi-website
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install flask flask-sqlalchemy
```

### 4. Run the application
```bash
python main.py
```
Open your browser and visit `http://127.0.0.1:5000` to explore the app.

## 🔮 Future Improvements

- User authentication for community-submitted reviews and ratings
- Interactive map view integration
- Pagination for larger cafe directories