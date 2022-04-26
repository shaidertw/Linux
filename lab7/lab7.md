***1. Как отобразить 4 последних выполненных команды?***
```bash
history 4
```  

***2. Перевести задание в фоновый режим в bash можно командой***  
```bash
nohup command & или command &
```

***3. Какая комбинация клавиш переключит вас на 4-ю виртуальную консоль?***
alt + 4

***4. Какая переменная среды содержит путь к домашнему каталогу?***  
PWD

***5. Установить в bash переменную MYVAR в качестве системной можно командой?***
MYVAR=value

***6. Какие комбинации клавиш позволят выделить несколько файлов в Midnight Commander?***
CTRL + T

***7. Что выведет на экран этот сценарий?***
```bash
shaidertw@ubuntu:~$ VAR=`echo 'test'`
shaidertw@ubuntu:~$ VAR2=`echo '$VAR'`
shaidertw@ubuntu:~$ echo $VAR2
$VAR
```

***8. Что выведет на экран это сценарий?***
```bash
shaidertw@ubuntu:~$ VAR="$PWD"
shaidertw@ubuntu:~$ if [ -n "$VAR" ]; then
>  echo "$VAR"
> else
>  echo '$VAR'
> fi 
/home/shaidertw
```

***9. Что выведет на экран этот сценарий?***
```bash
shaidertw@ubuntu:~$ A=1
shaidertw@ubuntu:~$ B=2
shaidertw@ubuntu:~$ if [ $A -eq $B  ]; then
>  echo '$A'
> else
>  echo "$B"
> fi 
2
```






