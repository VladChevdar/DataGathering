# 🌧️ Is It Raining in Portland?

This Python script checks if it's currently raining in Portland, OR and whether rain is forecasted in the next 3 days using the OpenWeatherMap API.

## 🔧 Setup

1. Clone the repo and navigate into the folder:
git clone https://github.com/your-username/your-repo-name.git cd your-repo-name

2. Create and activate a virtual environment:
python3 -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install requirements:
pip install -r requirements.txt

4. Set your API key:
- Copy `.env.example` to `.env`:
  ```
  cp .env.example .env
  ```
- Edit `.env` and replace the placeholder with your actual OpenWeatherMap API key:
  ```
  API_KEY=your_api_key_here
  ```

5. Run the script:
python3 is_it_raining.py

## 📁 Files

- `is_it_raining.py` – Main script that checks the weather
- `requirements.txt` – List of Python packages needed
- `.env.example` – Template for your `.env` file
- `.gitignore` – Excludes `venv/` and `.env` from Git
