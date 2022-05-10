***1.Какая команда позволяет установить задания планировщика?***
 ```bash
 at [options] time date
 ```
 ```bash
 crontab -e command
 ```
 
***2. Что сделает Команда atrm 7?***  
 Удалит задачу с id 7

***3. Какая команда позволяет установить планировщику crontab задания из файла jobs?***
```bash
crontab jobs
```

***4. Когда будет готово задание 19 */2 13 * 5 job.sh?***  
Каждую 13 пятницу на 19-ой минуте каждого второго часа

***5. Напишите cron строку установленной на выполнение скрипта job.sh с января по май, в 01:00 по воскресеньям***  
0 1 * 1-5 7 job.sh

***6. Просмотреть список всех смонтированных разделов можно командой?***
```bash
mount
```

*Практика*  

***Продемонстрировать работу at по запуску задачи записи в файл произвольной строки,
продемонстрировать работу cron по запуску задачи записи в файл произвольной строки***  
**at**
```bash
shaidertw@ubuntu:~$ at 17:51
warning: commands will be executed using /bin/sh
at> date > file
at> <EOT>
job 2 at Tue May 10 17:51:00 2022
```

***cron***
```bash
shaidertw@ubuntu:~$ cat jobs
* * * * * date > /home/shaidertw/date.txt
shaidertw@ubuntu:~$ crontab jobs
shaidertw@ubuntu:~$ crontab -l
* * * * * date > /home/shaidertw/date.txt
```
