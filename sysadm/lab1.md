***1. Демонстрация работы программ***
```bash
shaidertw@my-virtual-machine:~$ cat ~/.vimrc
syntax on
set number
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set noswapfile
set noshowmode

" plugins
call plug#begin()

" On-demand loading
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }

Plug 'neoclide/coc.nvim', {'branch': 'release'}

" Initialize plugin system
call plug#end()


" mapping(open folder)
map <C-n> :NERDTreeToggle<CR>
```

```bash
shaidertw@my-virtual-machine:~$ cd ~/kaleva.fi.auth/
```

```bash
shaidertw@my-virtual-machine:~$ ls ~/kaleva.fi.auth/ -R
/home/shaidertw/kaleva.fi.auth/:
app  Dockerfile  main.py  README.md  requirements.txt

/home/shaidertw/kaleva.fi.auth/app:
__init__.py  models.py  parser.py  settings.py
```

```bash
shaidertw@my-virtual-machine:~/kaleva.fi.auth$ cp requirements.txt{,.backup}
shaidertw@my-virtual-machine:~/kaleva.fi.auth$ mv requirements.txt.backup requirements.txt
```

```bash
shaidertw@my-virtual-machine:~$ rm -rf ~/kaleva.fi.auth
```

```bash
shaidertw@my-virtual-machine:~$ touch file.txt
```


```bash
shaidertw@my-virtual-machine:~$ echo 1 > /proc/sys/net/ipv4/ip_forward
```

```bash
shaidertw@my-virtual-machine:/etc/postgresql$ pwd
/etc/postgresql
```

```bash
shaidertw@my-virtual-machine:~$ mkdir temp_dir
shaidertw@my-virtual-machine:~$ rmdir temp_dir/
```

```bash
shaidertw@my-virtual-machine:~$ sudo ss -tulnp | grep ssh
tcp     LISTEN   0        128               0.0.0.0:1337          0.0.0.0:*      users:(("sshd",pid=782,fd=3))

tcp     LISTEN   0        128                  [::]:1337             [::]:*      users:(("sshd",pid=782,fd=4))
```

```bash
shaidertw@my-virtual-machine:~$ docker ps -a | less
CONTAINER ID   IMAGE          COMMAND                  CREATED       STATUS                     PORTS
                    NAMES
a44153d7a5b3   balancer       "./main"                 10 days ago   Exited (1) 10 days ago
                    balancer
18ac2102a4aa   page_parser    "./main"                 11 days ago   Exited (255) 5 days ago    0.0.0.0:6000->5000/tcp, :::6000->5000/tcp   page_parser
152f55c5da90   98ff60bf8db6   "/bin/sh -c 'pyinsta…"   12 days ago   Exited (2) 12 days ago
                    vigilant_mahavira
25abe6b16a7b   ab70cfeebd42   "/bin/sh -c 'pyinsta…"   12 days ago   Exited (2) 12 days ago
                    sweet_swirles
4dc2aa9afc3b   k-crm          "bash"                   2 weeks ago   Exited (255) 5 days ago
                    k-crm
f4f64bc43cc3   eff9125f374d   "/bin/sh -c 'cd / &&…"   2 weeks ago   Exited (1) 2 weeks ago
                    focused_borg
b4d57c9be482   02b85a5e4c26   "/bin/sh -c 'cd / &&…"   2 weeks ago   Exited (1) 2 weeks ago
                    relaxed_gould
6fc53dd87583   e3f813fc8614   "/bin/sh -c 'git clo…"   2 weeks ago   Exited (127) 2 weeks ago
                    sweet_sutherland
be43f3d96bda   4952337b55f6   "/bin/sh -c 'git clo…"   2 weeks ago   Exited (1) 2 weeks ago
                    vigilant_jemison
a305e5b7c06a   313124940cde   "/bin/sh -c 'apt upd…"   2 weeks ago   Exited (255) 2 weeks ago
                    dreamy_nobel
ff61ec5aba1c   654261a86208   "/bin/sh -c 'git clo…"   2 weeks ago   Exited (1) 2 weeks ago
                    adoring_joliot
4697ab7c31d8   e35bdbe6c986   "/bin/sh -c 'wget ht…"   2 weeks ago   Exited (1) 2 weeks ago
                    youthful_feistel
(END)
```

```bash
shaidertw@my-virtual-machine:~$ find / -type d -name shaidertw
/home/shaidetw
```
```bash
shaidertw@my-virtual-machine:~$ tail -f /var/log/syslog
Oct  9 19:09:00 my-virtual-machine systemd[1]: phpsessionclean.service: Succeeded.
Oct  9 19:09:00 my-virtual-machine systemd[1]: Finished Clean php session files.
Oct  9 19:09:01 my-virtual-machine CRON[96816]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
Oct  9 19:12:10 my-virtual-machine systemd[1]: Starting Ubuntu Advantage Timer for running repeated jobs...
Oct  9 19:12:10 my-virtual-machine systemd[1]: ua-timer.service: Succeeded.
Oct  9 19:12:10 my-virtual-machine systemd[1]: Finished Ubuntu Advantage Timer for running repeated jobs.
Oct  9 19:15:01 my-virtual-machine CRON[96845]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
Oct  9 19:17:01 my-virtual-machine CRON[96888]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Oct  9 19:25:02 my-virtual-machine CRON[96959]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
Oct  9 19:25:50 my-virtual-machine nordvpnd[697]: 2022/10/09 19:25:50 quic transport needs reconnect, err: timeout: no recent network activity
```

```bash
shaidertw@my-virtual-machine:~/asterisk$ ls -l | sort -k9
total 4
drwxr-xr-x 2 root root 4096 Mar  4  2022 configs
-rw-r--r-- 1 root root    0 Mar  4  2022 Dockerfile
```

```bash
shaidertw@my-virtual-machine:~$ which python
/usr/bin/python
```

```bash
shaidertw@my-virtual-machine:~$ curl https://github.com/mozilla/geckodriver/tags | grep -Po 'v[0]+.[0-9]+.[0-9]+'| head -1
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  183k    0  183k    0     0   178k      0 --:--:--  0:00:01 --:--:--  178k
v0.31.0
```

```bash
shaidertw@my-virtual-machine:~$ file docker-compose.yaml
docker-compose.yaml: ASCII text
```

***2. Показать содержимое path, добавить в path дополнительный путь***  
```bash
shaidertw@my-virtual-machine:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

shaidertw@my-virtual-machine:~$ export PATH=$PATH:/opt/local/bin
```

***3. Продемонстрировать перенаправление вывода в файл ***  
```bash
shaidertw@my-virtual-machine:~$ echo "some text" > file.txt
```

***4. вызвать команду с ошибкой и перенаправить вывод ошибки в файл ***  
```bash
shaidertw@my-virtual-machine:~$ ls -lz 2> error.txt
```

***5. Перенаправить стандартный ввод в программу ***  
```bash
shaidertw@my-virtual-machine:~$ cat < error.txt
ls: invalid option -- 'z'
Try 'ls --help' for more information.
```

***6. Cоздать архив, распаковать архив
```bash
shaidertw@my-virtual-machine:~$ tar -cf archive.tar temp/
shaidertw@my-virtual-machine:~$ tar -xvf archive.tar
```
