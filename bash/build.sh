#!/bin/bash -x

SUFFIX="-haptic-poc"
make LOCALVERSION=$SUFFIX ARCH=arm64 -j8
doas make LOCALVERSION=$SUFFIX ARCH=arm64 modules_install
doas cp arch/arm64/boot/Image /boot/vmlinuz-linux-asahi$SUFFIX
doas mkinitcpio -k 6.18.15-ARCH$SUFFIX -g /boot/initramfs-linux-asahi$SUFFIX.img
# grub-mkconfig -o /boot/grub/grub.cfg
doas update-grub
doas grub-reboot "Arch Linux (haptic-poc kernel)"
