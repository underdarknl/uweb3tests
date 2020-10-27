#!/bin/bash
gunicorn3 'base:main()' --workers=1
