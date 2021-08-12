#!/bin/bash
has() { type -p "$1" &> /dev/null; }
if has brew ; then
    brew update
    brew upgrade
else
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
brew install openjdk@11 git visual-studio-code
if has code ; then
    code --install-extension vscjava.vscode-java-pack
    code --install-extension wpilibsuite.vscode-wpilib
else
    echo "ERROR: vscode failed to install"
