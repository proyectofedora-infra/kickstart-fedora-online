#version=DEVEL

# System bootloader configuration
bootloader --location=none

%packages
@books
@lxde-apps
-autofs
-coolkey
-hpijs
-hplip
-isdn4k-utils
-mpage
-numactl
-sane-backends
-sox
-wget
-xsane
-xsane-gimp

%end
