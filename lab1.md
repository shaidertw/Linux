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

***6. Какие разделы содержит вывод команды vmstat***  
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
+ Информация о загрузке процессора
```bash
shaidertw@ubuntu:~$ mpstat -P ALL
Linux 5.13.0-28-generic (ubuntu) 	15.02.2022 	_x86_64_	(2 CPU)

19:41:06     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
19:41:06     all    3,52    0,60    3,52    0,05    0,00    0,16    0,00    0,00    0,00   92,14
19:41:06       0    3,45    0,61    3,60    0,04    0,00    0,16    0,00    0,00    0,00   92,15
19:41:06       1    3,61    0,58    3,44    0,06    0,00    0,16    0,00    0,00    0,00   92,14
```  
+ Информация о процессоре
```bash
shaidertw@ubuntu:~$ lscpu
Архитектура:                     x86_64
CPU op-mode(s):                  32-bit, 64-bit
Порядок байт:                    Little Endian
Address sizes:                   43 bits physical, 48 bits virtual
CPU(s):                          2
On-line CPU(s) list:             0,1
Потоков на ядро:                 1
Ядер на сокет:                   1
Сокетов:                         2
NUMA node(s):                    1
ID прроизводителя:               GenuineIntel
Семейство ЦПУ:                   6
Модель:                          142
Имя модели:                      Intel(R) Core(TM) i3-7020U CPU @ 2.30GHz
Степпинг:                        10
CPU МГц:                         2303.997
BogoMIPS:                        4607.99
Разработчик гипервизора:         VMware
Тип виртуализации:               полный
L1d cache:                       64 KiB
L1i cache:                       64 KiB
L2 cache:                        512 KiB
L3 cache:                        6 MiB
NUMA node0 CPU(s):               0,1
Vulnerability Itlb multihit:     KVM: Mitigation: VMX unsupported
Vulnerability L1tf:              Mitigation; PTE Inversion
Vulnerability Mds:               Mitigation; Clear CPU buffers; SMT Host state unknown
Vulnerability Meltdown:          Mitigation; PTI
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and sec
                                 comp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitiz
                                 ation
Vulnerability Spectre v2:        Mitigation; Full generic retpoline, IBPB conditional, IBRS_FW, 
                                 STIBP disabled, RSB filling
Vulnerability Srbds:             Unknown: Dependent on hypervisor status
Vulnerability Tsx async abort:   Not affected
Флаги:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov p
                                 at pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp
                                  lm constant_tsc arch_perfmon nopl xtopology tsc_reliable nonst
                                 op_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid s
                                 se4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave a
                                 vx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault
                                  invpcid_single pti ssbd ibrs ibpb stibp fsgsbase tsc_adjust bm
                                 i1 avx2 smep bmi2 invpcid rdseed adx smap clflushopt xsaveopt x
                                 savec xsaves arat md_clear flush_l1d arch_capabilities

```


