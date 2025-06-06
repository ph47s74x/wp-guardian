# WP Guardian
Wordpress vulnerability scanner and reporting tool. 

## Installation
- API keys required
    https://www.wpvulndb.com - 50 free daily requests per token
    Set the environment variables `WPVULNDB_API_KEY` and `VULNERS_API_KEY` before running.

    https://www.vulnersdb.com - 1,000 free monthly requests per token


- Clone github repo

        git clone https://github.com/ricardolopezg/wp-guardian


- Install dependencies

        pip install -r requirements.txt

- Set the environment variables `WPVULNDB_API_KEY` and `VULNERS_API_KEY` with your API tokens

- Usage

        python3 wp_guardian.py http(s)://www.example.com/

Markdown report will be generated and saves to the reports folder, along with with a json formatted report.

Use your favorite Markdown viewer to view the .md file. You can also use google chrome extension Markdownviewer.

## Future Features
- [ ] plugin fuzzing
- [ ] theme fuzzing
- [ ] md5sum version fingerprinting 

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
