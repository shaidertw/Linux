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
