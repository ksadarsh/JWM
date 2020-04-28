yad --center --borders=20 \
	--image=/usr/share/icons/Surfn/scalable/apps/scalable/vym.svg --image-on-top \
    --title="Shutdown options" \
    --button="🌙 Logout":"jwm -exit" \
    --button="🍵 Suspend":"systemctl suspend" \
    --button="🌙 Hibernate":"systemctl hibernate" \
    --button="🛑 Shutdown":"systemctl shutdown" \
   	--button=gtk-cancel \
# --close-on-unfocus \
