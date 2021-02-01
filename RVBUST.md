#### Linux

##### difference between`dpkg`, `apt`, `apt-get`, `aptitude`

(I just came up with this question from the experience when I try to install a *.deb package using `apt`, but failed, then Chengji tried `dpkg -i *.deb` and worked perfectly)

- `dpkg`, only installs current *.deb package, it will also notify you which dependencies should be installed, but won't install them automatically
- `apt-get`, is a `Package Management System`, that handles *install*, *remove*, *change* packages easily, it's a clever `dpkg`
- `apt` integrate only the very often used functions of `apt-get` and `apt-cache`, which has tons of command options
- `aptitude`, a little bit smart than `apt-get`

ref: [askubuntu](https://askubuntu.com/questions/309113/what-is-the-difference-between-dpkg-and-aptitude-apt-get), [its Foss](https://itsfoss.com/apt-vs-apt-get-difference/)

