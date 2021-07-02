#!/bin/bash
# This script sets up the application

SRC_DIR=$(cd "$(dirname "$0")"; pwd -P)

$SRC_DIR/setup_app/migrate_database.sh
# $SRC_DIR/setup_app/add_admin.sh
# $SRC_DIR/setup_app/add_seed_data.sh