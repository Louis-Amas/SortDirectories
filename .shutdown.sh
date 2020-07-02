choice=$(echo -e "suspend\nhibernate\nreboot\npoweroff" | dmenu -i -p "Please type the action to use" || exit 1)

systemctl $choice
