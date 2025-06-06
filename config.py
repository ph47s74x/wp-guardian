# API KEY https://wpvulndb.com/api (50 free daily requests per token)
import os

wpvulndb_api_key = os.getenv('WPVULNDB_API_KEY', '')

# API KEY https://vulners.com/ (1,000 free monthly requests per token)
vulners_api_key = os.getenv('VULNERS_API_KEY', '')

