#!/bin/bash
#instalacion
#autor bunkerwallx


green='\e[0;34m'
white='\e[1;37m'
red='\e[1;31m'
BlueF='\e[1;34m'


echo -e $white"============================================"
echo -e $BlueF"  __  ___             _ "
echo -e $BlueF"  \ \/ / |_ __ ___  _(_)___  "
echo -e $BlueF"   \  /| __/ _' \ \/ / / __|  "
echo -e $BlueF"   /  \| || (_| |>  <| \__ \  "
echo -e $BlueF"  /_/\_\\__\__,_/_/\_\_|___/  "
echo -e $BlueF"                               "
echo -e $white"============================================"
echo -e $red"www.lapestenegra.com by.Bunkerwallx"
echo -e $green"============================================"
echo -e $white" modifica tu archivo sources.list con mirrors de diferentes paises y proyectos de kali linux"        
echo""       
echo""       
       
       
       echo >> "/etc/apt/sources.list.r"

       cp /etc/apt/sources.list /etc/apt/sources.list.r
       rm /etc/apt/sources.list 
       echo >> /etc/sources.list
       echo "#!/etc/apt/sources.list"
       echo "deb http://http.kali.org/kali/ kali-rolling non-free contrib main" >> /etc/apt/sources.list
       echo "deb-src http://http.kali.org/kali/ kali-rolling non-free contrib main" >> /etc/apt/sources.list
       echo "deb http://mir.linux.kg/debian buster main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://mirror.kku.ac.th/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://kali.mirror.garr.it/mirrors/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://distro.ibiblio.org/debian bullseye main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://ftp.linux.org.tr/debian/ bullseye main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirror.zetup.net/debian bullseye main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://download.nus.edu.sg/mirror/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list

       echo "deb https://mirrors.tuna.tsinghua.edu.cn/kali kali-debian-picks main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling-only main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirrors.tuna.tsinghua.edu.cn/kali kali-dev main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirrors.tuna.tsinghua.edu.cn/kali kali-dev-only main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirrors.tuna.tsinghua.edu.cn/kali debian-testing main non-free contrib" >> /etc/apt/sources.list

       echo "deb https://wlglam.fsmg.org.nz/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://wlglam.fsmg.org.nz/kali kali-rolling-only main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://wlglam.fsmg.org.nz/kali kali-dev main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://wlglam.fsmg.org.nz/kali kali-experimental main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://ftp2.nluug.nl/os/Linux/distr/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://kali.download/kali/ kali-rolling-only non-free contrib" >> /etc/apt/sources.list
       echo "deb https://ftp.halifax.rwth-aachen.de/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://ftp1.nluug.nl/os/Linux/distr/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirror.pyratelan.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb-src https://mirror.pyratelan.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list

       echo "deb http://debian.xtdv.net/debian buster main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://mirror.positive-internet.com/debian buster main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://mirror.linux.org.au/debian testing main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://ftp.mx.debian.org/debian testing main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://ftp.harukasan.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirrors.bfsu.edu.cn/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirrors.bfsu.edu.cn/kali debian-testing main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://mirror.cedia.org.ec/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://mirrors.psu.ac.th/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://mirror1.ku.ac.th/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://tux.rainside.sk/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://ftp.icm.edu.pl/pub/Linux/dist/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://mirror.truenetwork.ru/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
       echo "deb http://mirrors.163.com/debian bullseye main non-free contrib" >> /etc/apt/sources.list
       echo "deb https://mirror.zetup.net/debian buster main non-free contrib" >> /etc/apt/sources.list
       
apt-get update && apt-get dist-upgrade -y
apt autoremove
reboot
