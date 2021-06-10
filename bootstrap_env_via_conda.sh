#!/bin/bash

set -e

conda env create -f environment.yml
conda activate udacity-data-engineer-postgres-data-modeling-env
