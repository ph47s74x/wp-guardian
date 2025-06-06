#!/usr/bin/env python3

import argparse
import logging
import os
import sys

import api_combined
import wp_version_scanner as wvs
import jsontomd
import page_fuzzer

logger = logging.getLogger(__name__)
def main():
    parser = argparse.ArgumentParser(description="WordPress vulnerability scanner")
    parser.add_argument('url', help='Target WordPress site')
    parser.add_argument('--report-dir', default=os.path.join(os.path.dirname(__file__), 'reports'), help='Directory to store reports')
    args = parser.parse_args()

    url = args.url

    logging.basicConfig(level=logging.INFO)

    logger.info('IS BUILDING YOUR REPORT. PLEASE WAIT...')


    logger.info('[+] Running report on %s', url)
    soup = wvs.url_input(url)
    logger.info('[+] Scanning WordPress version')
    wp_version = wvs.wp_version_finder(soup)
    logger.info('[+] Scanning server version')
    server_version = page_fuzzer.getserverversion(url)
    logger.info('[+] Fuzzing pages for data exposure')
    update_page = page_fuzzer.fuzzupdatepage(url)
    install_page = page_fuzzer.fuzzinstallpage(url)
    logger.info('[+] Building vulnerability profile')
    filename = api_combined.report_builder(wp_version, url)
    logger.info('[+] Creating report')
    jsontomd.jsontomd(filename, server_version, install_page, update_page)

    logger.info('[+] WP GUARDIAN SCAN COMPLETE! Report saved to %s', args.report_dir)

if __name__ == "__main__":
    main()


