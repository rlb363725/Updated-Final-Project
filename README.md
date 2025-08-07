## College Football Matchup Analyzer

This tool compares two FBS teams' season stats using data from the [CollegeFootballData API](https://collegefootballdata.com/), predicts a score based on offensive/defensive yardage, and visualizes multiple stat comparisons using Plotly.

---

### Features

- Retrieves live team stats from the CollegeFootballData API  
- Predicts scores based on total offensive and defensive yards  
- Prints stat summaries and predicted win probabilities in the terminal  
- Visualizes:
  • Side-by-side stat comparison (bar chart)  
  • Win probability pie chart  
  • Interactive player headlines board  
- Command-line interface  
- Automated testing via Pytest

---

### How It Works

1. You input two FBS teams and a season year.
2. The app fetches season-long team stats from the API.
3. It calculates predicted scores based on yardage.
4. It prints each team’s key stats and win odds in the terminal.
5. It displays three visuals:  
   - A stat comparison bar chart  
   - A win probability pie chart  
   - An interactive "headline players" table

---

### Setup Instructions

#### 1. Clone the repo

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

### 2. Create and activate your virtual environment

conda create -n matchup-env python=3.11
conda activate matchup-env

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add your API key

CFB_API_KEY=your_actual_api_key_here

If this variable is not set, the application will prompt you for your key the
first time it runs.

### 5. Run the app

python main.py

### 6. Run the tests

pytest


### File Structure

.
├── data_fetcher.py     # API call logic
├── utils.py            # Stat extraction + prediction + win odds
├── matchup.py          # Core simulation and print logic
├── visuals.py          # Plotly visuals (bar, pie, table)
├── main.py             # User interaction and control
├── test_matchup.py     # Pytest-based tests
├── .env                # Your local API key (ignored by Git)
├── requirements.txt    # Dependencies
└── README.md           # This file


### License

MIT License. See LICENSE for details.

### Security Notes

API keys are securely stored in .env using python-dotenv

.env is excluded from Git tracking via .gitignore

Always use version control responsibly when working with API credentials



