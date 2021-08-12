if ( Test-Path "$HOME\scoop\shims\scoop" ) {
    scoop install git
    scoop update
} else {
    Set-ExecutionPolicy RemoteSigned -scope CurrentUser
    iwr -useb get.scoop.sh | iex
}
scoop bucket add java
scoop bucket add extras
scoop install git openjdk11 vscode
code --install-extension vscjava.vscode-java-pack 
code --install-extension wpilibsuite.vscode-wpilib