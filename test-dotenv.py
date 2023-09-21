#!/usr/bin/env python3

import os
from dotenv import load_dotenv

load_dotenv()

# dotenv isn't working in Jupyter, but it seems to work here
print('this is the ehc folder from your .env: {}'.format(os.getenv('EHCFOLDER')))
