                              ARCH LINUX #VERSION#
                     SHORT & SWEET INSTALL INSTRUCTIONS
                 ==========================================

1.  Make your swap/root partitions
      # fdisk /dev/discs/disc0/disc

2.  Make your target filesystems
      # mkswap /dev/discs/disc0/partX
      # mkreiserfs /dev/discs/disc0/partY

3.  Activate your swap partition
      # swapon /dev/discs/disc0/partX

4.  Mount your target root filesystem under /mnt
      # mount /dev/discs/disc0/partX /mnt

5.  Initialize the pacman database
      # mkdir -p /mnt/var/lib/pacman
      # touch /mnt/var/lib/pacman/pacman.db

6.  Add the filesystem package from /arch/pkg/filesystem-0.X-Y.tar.gz
      # cd /arch/pkg
      # pacman --add -r /mnt filesystem-0.X-Y.tar.gz

7.  Mount any other data partitions you may have created
      # mount /dev/discs/disc0/partX /mnt/home
      # mount /dev/discs/disc0/partY /mnt/usr
      
8.  Install some base packages
      # cd /arch
      # ./installworld /mnt
      
9.  Uncompress the linux source to /mnt/usr/src
      # cd /mnt/usr/src && tar zxvf /arch/linux-2.4.XX.tar.gz
      
10. Mount a dev and proc under your new system and chroot
      # mount -t devfs none /mnt/dev
      # mount -t proc none /mnt/proc
      # chroot /mnt /bin/bash
      
11. Build & install your new kernel from /usr/src/linux
      NOTE: make sure you ask for "/dev file system support" and
            "Automatically mount at boot", since we use DevFS.

12. Install a lilo bootloader
      # vi /etc/lilo.conf
      # lilo

13. Edit settings
      # vi /etc/rc.conf
      # vi /etc/resolv.conf
      # vi /etc/fstab
      # vi /etc/modules.conf (if needed)

14. Exit your chroot shell
      # exit

15. Reboot!

16. Verify success and install any additional packages you want.
      # pacman -A /mnt/cd/arch/pkg/whatever-1.1-1.pkg.tar.gz

