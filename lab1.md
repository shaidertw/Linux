***1. Основные принципы Unix-way***
+ Одна задача - одна программа
+ все есть файл
+ есть множество путей решения

***2. Линус Торвальдс является разработчиком чего?***  
Создал Linux-ядро операционной системы GNU/Linux  

***3. Как посмотреть название ядра системы из консоли***  
```bash
uname -rs
```  

***4. Промежутки измерения загрузки системы для команды uptime следующие***  
1,5 и 15 минут  

***5. Какой командой узнать сколько место занято на HDD***  
```bash
df -h
```  

***6. Какие разделы содержит вывод команды vmstat ***  
+ procs
+ memory
+ swap
+ io
+ system
+ cpu  

***7. Описать работу своего Linux дистрибутива***
+ Ядро и архитектура 
```bash
shaidertw@ubuntu:~$ uname -a
Linux ubuntu 5.13.0-28-generic #31~20.04.1-Ubuntu SMP Wed Jan 19 14:08:10 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```  
+ Размеры HDD  
```bash
shaidertw@ubuntu:~$ df -h
Файл.система   Размер Использовано  Дост Использовано% Cмонтировано в
udev             3,9G            0  3,9G            0% /dev
tmpfs            792M         2,2M  790M            1% /run
/dev/sda5         49G          44G  2,5G           95% /
tmpfs            3,9G            0  3,9G            0% /dev/shm
tmpfs            5,0M         4,0K  5,0M            1% /run/lock
tmpfs            3,9G            0  3,9G            0% /sys/fs/cgroup
/dev/loop0       128K         128K     0          100% /snap/bare/5
/dev/loop2        66M          66M     0          100% /snap/gtk-common-themes/1515
/dev/loop1        56M          56M     0          100% /snap/core18/2128
/dev/loop3       723M         723M     0          100% /snap/intellij-idea-community/323
/dev/loop4       100M         100M     0          100% /snap/core/11606
/dev/loop5        51M          51M     0          100% /snap/snap-store/547
/dev/loop6       219M         219M     0          100% /snap/gnome-3-34-1804/72
/dev/loop7       655M         655M     0          100% /snap/intellij-idea-community/324
/dev/loop8        33M          33M     0          100% /snap/snapd/13170
/dev/loop9        33M          33M     0          100% /snap/snapd/12883
/dev/loop10       66M          66M     0          100% /snap/gtk-common-themes/1519
/dev/sda1        511M         4,0K  511M            1% /boot/efi
overlay           49G          44G  2,5G           95% /var/lib/docker/overlay2/b0d076c075946791b36ba369c5fe34df00bcc97e14b0cb90965074948fa2e907/merged
overlay           49G          44G  2,5G           95% /var/lib/docker/overlay2/6780897e6e685520ff89f770c20a2b4e0e9d4eeabefd116cba3f88a07c3811a8/merged
overlay           49G          44G  2,5G           95% /var/lib/docker/overlay2/5b3799da2e9038f92dd0f5cc667554361a34cff90592ce937d61bf71daed22b9/merged
shm               64M            0   64M            0% /var/lib/docker/containers/3ce7a02b72ca65376d4e38f2c6748e7c300697b6f046789494e1313a41cf2961/mounts/shm
tmpfs            792M          64K  792M            1% /run/user/1000
```  

+ Информаци ОЗУ  
```bash
shaidertw@ubuntu:~$ free -h
              всего        занято        свободно      общая  буф./врем.   доступно
Память:       7,7Gi       3,8Gi       694Mi        35Mi       3,2Gi       3,6Gi
Подкачка:       2,0Gi          0B       2,0Gi
```


