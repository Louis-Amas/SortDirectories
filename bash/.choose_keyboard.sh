choice=$(echo -e "us_qwerty-fr \nfr" | dmenu -i -p "Please type the keymap you wish to use") || exit 1
if [ -z $choice ]; then
    setxkbmap fr


else
    setxkbmap $choice
fi
