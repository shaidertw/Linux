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
