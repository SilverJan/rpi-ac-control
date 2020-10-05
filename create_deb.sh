#!/bin/bash

####################
# This script builds .deb packages
####################

function print_help() {
    echo "
This script / container creates a .deb package

Usage (as script):
----------------------------
build_deb.sh -v <version> -n <name> -b <base_dir>

Hint: Run this script in a osd-*-package directory.

Options:
  -b BASE_DIR  : project base directory to be used for build (needs to contain src/ and .git/)
  -d DIST_DIR  : target directory to be used for storing .deb package (default: ./dist/)
  -n NAME      : name of package
  -r VERSION   : version to be used for build
  -h           : print this help
"
}

SCRIPT_PATH=$(dirname "$0")
SCRIPT_PATH=$(cd "$SCRIPT_PATH" && pwd)
DIST_DIR="dist"
VERSION="$(cat VERSION)"
NAME="rpi-ac-control"
EXPERIMENTAL_SUFFIX=""
BASE_DIR="$(pwd)"

while getopts ":b:d:n:v:h" opt; do
    case $opt in
    b) BASE_DIR=$OPTARG ;;
    d) DIST_DIR=$OPTARG ;;
    n) NAME=$OPTARG ;;
    v) VERSION=$OPTARG ;;
    h)
        print_help
        exit 0
        ;;
    *)
        error "Invalid option: $opt"
        print_help
        exit 1
        ;;
    esac
done

SRC_DIR="src"

if [[ ! -d $BASE_DIR ]]; then
    echo "Base directory does not exist. Please run script / container with '-b <path_to_base_dir>'"
    exit 128
fi
if [[ ! -d $BASE_DIR/$SRC_DIR ]]; then
    echo "Base directory does not contain src/. Are you sure your base directory is correct?"
    exit 128
fi
if [[ -z $NAME ]]; then
    echo "No package name has been passed as an argument. Please run script / container with '-n <package_name>'"
    exit 128
fi
if [[ -z $VERSION ]]; then
    echo "No version has been passed as an argument. Please run script / container with '-v <package_version>'"
    exit 128
fi

cd "$BASE_DIR" || exit

GIT_BRANCH=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)
GIT_COMMIT_SHA=$(git rev-parse --short HEAD)

# prepare result folder
DIST_SRC_DIR="dist_src"
rm -rf "$DIST_DIR" "$DIST_SRC_DIR"
mkdir -p "$DIST_DIR" "$DIST_SRC_DIR"
# create source copy
cp -rfp $SRC_DIR/* "$DIST_SRC_DIR"

# replaces all wildcards in src/
for file in $(find $DIST_SRC_DIR -type f); do
    sed -i "s/%PACKAGE_NAME%/$NAME/g" "$file"
    sed -i "s/%PACKAGE_VERSION%/$VERSION/g" "$file"
done

# build DEBIAN/changelog
git log -n 10 >>"$DIST_SRC_DIR/DEBIAN/changelog"

# build the package
dpkg-deb -b "$DIST_SRC_DIR/" "$DIST_DIR/${NAME}_${VERSION}_all.deb"
