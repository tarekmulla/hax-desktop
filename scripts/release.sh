#!/bin/sh
if [[ "$OSTYPE" == "linux"* ]]; then
  echo "Releasing Linux version"
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Releasing MacOS version (.dmg)"
  ./scripts/release-os/macos.sh
elif [[ "$OSTYPE" == "msys" ]]; then
  echo "Releasing Windows version (.exe)"
fi
