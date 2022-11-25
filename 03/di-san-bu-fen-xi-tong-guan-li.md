# 第三部分：系统管理

本手册其余各章涵盖了 FreeBSD 系统管理的各个方面。每一章的开头都介绍了阅读本章后将会学到的东西，并详细说明了读者在阅读这些材料之前应该具有的背景知识。

这些章节的设计是为了在需要时查阅这些信息。它们无需按照任何特定的顺序来阅读，也不需要在开始使用 FreeBSD 之前阅读所有的章节。

## 第十三章 配置与优化
```toc
:maxdepth: 1

di-13-zhang-pei-zhi-yu-you-hua/13.1.-gai-shu
di-13-zhang-pei-zhi-yu-you-hua/13.2.-qi-dong-fu-wu
di-13-zhang-pei-zhi-yu-you-hua/13.3.-pei-zhi-cron8
di-13-zhang-pei-zhi-yu-you-hua/13.4.-guan-li-freebsd-zhong-de-fu-wu
di-13-zhang-pei-zhi-yu-you-hua/13.5.-she-zhi-wang-ka
di-13-zhang-pei-zhi-yu-you-hua/13.6.-xu-ni-zhu-ji
di-13-zhang-pei-zhi-yu-you-hua/13.7.-pei-zhi-xi-tong-ri-zhi
di-13-zhang-pei-zhi-yu-you-hua/13.8.-pei-zhi-wen-jian
di-13-zhang-pei-zhi-yu-you-hua/13.9.-shi-yong-sysctl8-jin-hang-you-hua
di-13-zhang-pei-zhi-yu-you-hua/13.10.-ci-pan-you-hua
di-13-zhang-pei-zhi-yu-you-hua/13.11.-nei-he-can-shu-you-hua
di-13-zhang-pei-zhi-yu-you-hua/13.12.-tian-jia-jiao-huan-kong-jian
di-13-zhang-pei-zhi-yu-you-hua/13.13.-dian-yuan-he-zi-yuan-guan-li
```
## 第十四章 FreeBSD 的引导过程
```toc
:maxdepth: 1

di-14-zhang-freebsd-de-yin-dao-guo-cheng/14.1.-gai-shu
di-14-zhang-freebsd-de-yin-dao-guo-cheng/14.2.freebsd-de-yin-dao-guo-cheng
di-14-zhang-freebsd-de-yin-dao-guo-cheng/14.3.device-hints
di-14-zhang-freebsd-de-yin-dao-guo-cheng/14.4.-guan-ji-liu-cheng
```
## 第十五章 安全
```toc
:maxdepth: 1

di-15-zhang-an-quan/15.1.-gai-shu
di-15-zhang-an-quan/15.2.-jian-jie
di-15-zhang-an-quan/15.3.-yi-ci-xing-mi-ma
di-15-zhang-an-quan/15.4.tcp-wrapper
di-15-zhang-an-quan/15.5.kerberos
di-15-zhang-an-quan/15.6.openssl
di-15-zhang-an-quan/15.7.ipsec-vpn
di-15-zhang-an-quan/15.8.openssh
di-15-zhang-an-quan/15.9.-wen-jian-xi-tong-fang-wen-kong-zhi-lie-biao
di-15-zhang-an-quan/15.10.-jian-ce-di-san-fang-an-quan-wen-ti
di-15-zhang-an-quan/15.11.freebsd-an-quan-gong-gao
di-15-zhang-an-quan/15.12.-jin-cheng-shen-ji
di-15-zhang-an-quan/15.13.-zi-yuan-pei-e
di-15-zhang-an-quan/15.14.-shi-yong-sudo-guan-li-quan-xian
di-15-zhang-an-quan/15.15.-shi-yong-doas-lai-dai-ti-sudo
```
## 第十六章 Jail
```toc
:maxdepth: 1

di-16-zhang-jail/16.1.-gai-shu
di-16-zhang-jail/16.2.-yu-jail-you-guan-de-shu-yu
di-16-zhang-jail/16.3.-jian-li-he-kong-zhi-jail
di-16-zhang-jail/16.4.-wei-tiao-he-guan-li
di-16-zhang-jail/16.5.-geng-xin-duo-ge-jail
di-16-zhang-jail/16.6.-shi-yong-ezjail-guan-li-jail
```
## 第十七章 强制访问控制
```toc
:maxdepth: 1

di-17-zhang-qiang-zhi-fang-wen-kong-zhi/17.1.-gai-shu
di-17-zhang-qiang-zhi-fang-wen-kong-zhi/17.2.-guan-jian-shu-yu
di-17-zhang-qiang-zhi-fang-wen-kong-zhi/17.3.-le-jie-mac-biao-qian
di-17-zhang-qiang-zhi-fang-wen-kong-zhi/17.4.-gui-hua-an-quan-pei-zhi
di-17-zhang-qiang-zhi-fang-wen-kong-zhi/17.5.-ke-yong-de-mac-ce-lve
di-17-zhang-qiang-zhi-fang-wen-kong-zhi/17.6.-yong-hu-suo-ding
di-17-zhang-qiang-zhi-fang-wen-kong-zhi/17.7.mac-jail-zhong-de-nagios
di-17-zhang-qiang-zhi-fang-wen-kong-zhi/17.8.mac-kuang-jia-de-gu-zhang-pai-chu
```
## 第十八章 安全事件审计
```toc
:maxdepth: 1

di-18-zhang-an-quan-shi-jian-shen-ji/18.1.-gai-shu
di-18-zhang-an-quan-shi-jian-shen-ji/18.2.-guan-jian-shu-yu
di-18-zhang-an-quan-shi-jian-shen-ji/18.3.-shen-ji-pei-zhi
di-18-zhang-an-quan-shi-jian-shen-ji/18.4.-shi-yong-shen-ji-gen-zong
```
## 第十九章 存储
```toc
:maxdepth: 1

di-19-zhang-cun-chu/19.1.-gai-shu
di-19-zhang-cun-chu/19.2.-tian-jia-ci-pan
di-19-zhang-cun-chu/19.3.-tiao-zheng-he-zeng-jia-ci-pan-da-xiao
di-19-zhang-cun-chu/19.4.usb-cun-chu-she-bei
di-19-zhang-cun-chu/19.5.-chuang-jian-he-shi-yong-cd
di-19-zhang-cun-chu/19.6.-chuang-jian-he-shi-yong-dvd
di-19-zhang-cun-chu/19.7.-chuang-jian-he-shi-yong-ruan-pan
di-19-zhang-cun-chu/19.8.-shi-yong-ntfs-ci-pan
di-19-zhang-cun-chu/19.9.-bei-fen-de-ji-chu-zhi-shi
di-19-zhang-cun-chu/19.10.-nei-cun-pan
di-19-zhang-cun-chu/19.11.-wen-jian-xi-tong-kuai-zhao
di-19-zhang-cun-chu/19.12.-ci-pan-pei-e
di-19-zhang-cun-chu/19.13.-jia-mi-ci-pan-fen-qu
di-19-zhang-cun-chu/19.14.-jia-mi-jiao-huan-fen-qu
di-19-zhang-cun-chu/19.15.-gao-ke-yong-xing-cun-chu-hast
```
## 第二十章 GEOM: 模块化磁盘转换框架
```toc
:maxdepth: 1

di-20-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/20.1.-gai-shu
di-20-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/20.2.raid0-tiao-dai
di-20-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/20.3.raid1-jing-xiang
di-20-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/20.4.raid3-dai-you-zhuan-yong-qi-ou-xiao-yan-de-zi-jie-ji-tiao-dai
di-20-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/20.5.-ruan-jian-raid-she-bei
di-20-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/20.6.geom-gate-wang-luo-she-bei
di-20-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/20.7.-wei-ci-pan-she-bei-tian-jia-juan-biao
di-20-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/20.8.-tong-guo-geom-shi-xian-ufs-ri-zhi
```
## 第二十一章 Z 文件系统（ZFS）
```toc
:maxdepth: 1

di-21-zhang-z-wen-jian-xi-tong-zfs/21.1.-shi-shi-mo-shi-zfs-yu-zhong-bu-tong
di-21-zhang-z-wen-jian-xi-tong-zfs/21.2.-kuai-su-ru-men-zhi-nan
di-21-zhang-z-wen-jian-xi-tong-zfs/21.3.zpool-guan-li
di-21-zhang-z-wen-jian-xi-tong-zfs/21.4.zfs-guan-li
di-21-zhang-z-wen-jian-xi-tong-zfs/21.5.-wei-tuo-guan-li
di-21-zhang-z-wen-jian-xi-tong-zfs/21.6.-gao-ji-zhu-ti
di-21-zhang-z-wen-jian-xi-tong-zfs/21.7.-geng-duo-zi-yuan
di-21-zhang-z-wen-jian-xi-tong-zfs/21.8.zfs-te-xing-he-shu-yu
```
## 第二十二章 其他文件系统
```toc
:maxdepth: 1

di-22-zhang-qi-ta-wen-jian-xi-tong/22.1.-gai-shu
di-22-zhang-qi-ta-wen-jian-xi-tong/22.2.linux-wen-jian-xi-tong
```
## 第二十三章 虚拟化
```toc
:maxdepth: 1

di-23-zhang-xu-ni-hua/23.1.-gai-shu
di-23-zhang-xu-ni-hua/23.2.-shi-yong-macos-shang-de-parallels-desktop-an-zhuang-freebsd
di-23-zhang-xu-ni-hua/23.3.-shi-yong-macos-shang-de-vmware-fusion-an-zhuang-freebsd
di-23-zhang-xu-ni-hua/23.4.-shi-yong-virtualbox-an-zhuang-freebsd
di-23-zhang-xu-ni-hua/23.5.-zai-freebsd-shang-an-zhuang-virtualbox
di-23-zhang-xu-ni-hua/23.6.-shi-yong-freebsd-shang-de-bhyve-xu-ni-ji
di-23-zhang-xu-ni-hua/23.7.-shi-yong-freebsd-shang-de-xen-xu-ni-ji
```
## 第二十四章 本地化——i18n/L10n 的使用和设置
```toc
:maxdepth: 1

di-24-zhang-ben-di-hua-i18nl10n-de-shi-yong-he-she-zhi/24.1.-gai-shu
di-24-zhang-ben-di-hua-i18nl10n-de-shi-yong-he-she-zhi/24.2.-shi-yong-ben-di-hua
di-24-zhang-ben-di-hua-i18nl10n-de-shi-yong-he-she-zhi/24.3.-xun-zhao-i18n-ying-yong-cheng-xu
di-24-zhang-ben-di-hua-i18nl10n-de-shi-yong-he-she-zhi/24.4.-te-ding-yu-yan-de-qu-yu-pei-zhi
```
## 第二十五章 FreeBSD 更新与升级
```toc
:maxdepth: 1

di-25-zhang-freebsd-geng-xin-yu-sheng-ji/25.1.-gai-shu
di-25-zhang-freebsd-geng-xin-yu-sheng-ji/25.2.-geng-xin-freebsd
di-25-zhang-freebsd-geng-xin-yu-sheng-ji/25.3.-geng-xin-bootcode
di-25-zhang-freebsd-geng-xin-yu-sheng-ji/25.4.-geng-xin-wen-dang
di-25-zhang-freebsd-geng-xin-yu-sheng-ji/25.5.-zhui-zong-kai-fa-fen-zhi
di-25-zhang-freebsd-geng-xin-yu-sheng-ji/25.6.-cong-yuan-dai-ma-geng-xin-freebsd
di-25-zhang-freebsd-geng-xin-yu-sheng-ji/25.7.-duo-tai-ji-qi-de-zhui-zong
```
## 第二十六章 DTrace
```toc
:maxdepth: 1

di-26-zhang-dtrace/26.1.-gai-shu
di-26-zhang-dtrace/26.2.-shi-xian-shang-de-cha-yi
di-26-zhang-dtrace/26.3.-kai-qi-dtrace-zhi-chi
di-26-zhang-dtrace/26.4.-shi-yong-dtrace
```
## 第二十七章 USB 设备模式/USB OTG
```toc
:maxdepth: 1

di-27-zhang-usb-she-bei-mo-shi-usb-otg/27.1.-gai-shu
di-27-zhang-usb-she-bei-mo-shi-usb-otg/27.2.usb-xu-ni-chuan-hang-duan-kou
di-27-zhang-usb-she-bei-mo-shi-usb-otg/27.3.usb-she-bei-mo-shi-wang-luo-jie-kou
di-27-zhang-usb-she-bei-mo-shi-usb-otg/27.4.usb-xu-ni-cun-chu-she-bei

```