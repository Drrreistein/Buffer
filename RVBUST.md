#### Linux

##### difference between`dpkg`, `apt`, `apt-get`, `aptitude`

(I just came up with this question from the experience when I try to install a *.deb package using `apt`, but failed, then Chengji tried `dpkg -i *.deb` and worked perfectly)

- `dpkg`, only installs current *.deb package, it will also notify you which dependencies should be installed, but won't install them automatically
- `apt-get`, is a `Package Management System`, that handles *install*, *remove*, *change* packages easily, it's a clever `dpkg`
- `apt` integrate only the very often used functions of `apt-get` and `apt-cache`, which has tons of command options
- `aptitude`, a little bit smart than `apt-get`

ref: [askubuntu](https://askubuntu.com/questions/309113/what-is-the-difference-between-dpkg-and-aptitude-apt-get), [its Foss](https://itsfoss.com/apt-vs-apt-get-difference/)

### /etc/apt/sources.list
```shell
## debian tsinghua source 
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster/updates main contrib non-free

## and run in terminal
sudo apt install apt-transport-https ca-certificates
sudo apt update


## ubuntu iamges source 
# https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
```

