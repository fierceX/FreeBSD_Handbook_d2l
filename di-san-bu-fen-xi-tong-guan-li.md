# 第三部分：系统管理

本手册其余各章涵盖了 FreeBSD 系统管理的各个方面。每一章的开头都介绍了阅读本章后将会学到的东西，并详细说明了读者在阅读这些材料之前应该具有的背景知识。

这些章节的设计是为了在需要时查阅这些信息。它们无需按照任何特定的顺序来阅读，也不需要在开始使用 FreeBSD 之前阅读所有的章节。

## 第十四章 配置与优化
```toc
:maxdepth: 1

di-14-zhang-pei-zhi-yu-you-hua/14.1.-gai-shu
di-14-zhang-pei-zhi-yu-you-hua/14.2.-qi-dong-fu-wu
di-14-zhang-pei-zhi-yu-you-hua/14.3.-pei-zhi-cron8
di-14-zhang-pei-zhi-yu-you-hua/14.4.-guan-li-freebsd-zhong-de-fu-wu
di-14-zhang-pei-zhi-yu-you-hua/14.5.-pei-zhi-xi-tong-ri-zhi
di-14-zhang-pei-zhi-yu-you-hua/14.6.-pei-zhi-wen-jian
di-14-zhang-pei-zhi-yu-you-hua/14.7.-shi-yong-sysctl8-jin-hang-you-hua
di-14-zhang-pei-zhi-yu-you-hua/14.8.-ci-pan-you-hua
di-14-zhang-pei-zhi-yu-you-hua/14.9.-nei-he-can-shu-you-hua
di-14-zhang-pei-zhi-yu-you-hua/14.10.-tian-jia-jiao-huan-kong-jian
di-14-zhang-pei-zhi-yu-you-hua/14.11.-dian-yuan-he-zi-yuan-guan-li
```
## 第十五章 FreeBSD 的引导过程
```toc
:maxdepth: 1

di-15-zhang-freebsd-de-yin-dao-guo-cheng/15.1.-gai-shu
di-15-zhang-freebsd-de-yin-dao-guo-cheng/15.2.-freebsd-de-yin-dao-guo-cheng
di-15-zhang-freebsd-de-yin-dao-guo-cheng/15.3.-device-hints
di-15-zhang-freebsd-de-yin-dao-guo-cheng/15.4.-guan-ji-liu-cheng
```
## 第十六章 安全
```toc
:maxdepth: 1

di-16-zhang-an-quan/16.1.-gai-shu
di-16-zhang-an-quan/16.2.-jian-jie
di-16-zhang-an-quan/16.3.-tcp-wrapper
di-16-zhang-an-quan/16.4.-kerberos
di-16-zhang-an-quan/16.5.-openssl
di-16-zhang-an-quan/16.6.-ipsec-vpn
di-16-zhang-an-quan/16.7.-openssh
di-16-zhang-an-quan/16.8.-wen-jian-xi-tong-fang-wen-kong-zhi-lie-biao
di-16-zhang-an-quan/16.9.-jian-ce-di-san-fang-an-quan-wen-ti
di-16-zhang-an-quan/16.10.-freebsd-an-quan-gong-gao
di-16-zhang-an-quan/16.11.-jin-cheng-shen-ji
di-16-zhang-an-quan/16.12.-zi-yuan-pei-e
di-16-zhang-an-quan/16.13.-shi-yong-sudo-guan-li-quan-xian
di-16-zhang-an-quan/16.14.-shi-yong-doas-lai-dai-ti-sudo
```
## 第十七章 Jail
```toc
:maxdepth: 1

di-17-zhang-jail/17.1.-gai-shu
di-17-zhang-jail/17.2.-yu-jail-you-guan-de-shu-yu
di-17-zhang-jail/17.3.-jian-li-he-kong-zhi-jail
di-17-zhang-jail/17.4.-wei-tiao-he-guan-li
di-17-zhang-jail/17.5.-geng-xin-duo-ge-jail
di-17-zhang-jail/17.6.-shi-yong-ezjail-guan-li-jail
```
## 第十八章 强制访问控制
```toc
:maxdepth: 1

di-18-zhang-qiang-zhi-fang-wen-kong-zhi/18.1.-gai-shu
di-18-zhang-qiang-zhi-fang-wen-kong-zhi/18.2.-guan-jian-shu-yu
di-18-zhang-qiang-zhi-fang-wen-kong-zhi/18.3.-le-jie-mac-biao-qian
di-18-zhang-qiang-zhi-fang-wen-kong-zhi/18.4.-gui-hua-an-quan-pei-zhi
di-18-zhang-qiang-zhi-fang-wen-kong-zhi/18.5.-ke-yong-de-mac-ce-lve
di-18-zhang-qiang-zhi-fang-wen-kong-zhi/18.6.-yong-hu-suo-ding
di-18-zhang-qiang-zhi-fang-wen-kong-zhi/18.7.-mac-jail-zhong-de-nagios
di-18-zhang-qiang-zhi-fang-wen-kong-zhi/18.8.-mac-kuang-jia-de-gu-zhang-pai-chu
```
## 第十九章 安全事件审计
```toc
:maxdepth: 1

di-19-zhang-an-quan-shi-jian-shen-ji/19.1.-gai-shu
di-19-zhang-an-quan-shi-jian-shen-ji/19.2.-guan-jian-shu-yu
di-19-zhang-an-quan-shi-jian-shen-ji/19.3.-shen-ji-pei-zhi
di-19-zhang-an-quan-shi-jian-shen-ji/19.4.-shi-yong-shen-ji-gen-zong
```
## 第二十章 存储
```toc
:maxdepth: 1

di-20-zhang-cun-chu/20.1.-gai-shu
di-20-zhang-cun-chu/20.2.-tian-jia-ci-pan
di-20-zhang-cun-chu/20.3.-tiao-zheng-he-zeng-jia-ci-pan-da-xiao
di-20-zhang-cun-chu/20.4.-usb-cun-chu-she-bei
di-20-zhang-cun-chu/20.5.-chuang-jian-he-shi-yong-cd
di-20-zhang-cun-chu/20.6.-chuang-jian-he-shi-yong-dvd
di-20-zhang-cun-chu/20.7.-chuang-jian-he-shi-yong-ruan-pan
di-20-zhang-cun-chu/20.8.-shi-yong-ntfs-ci-pan
di-20-zhang-cun-chu/20.9.-bei-fen-de-ji-chu-zhi-shi
di-20-zhang-cun-chu/20.10.-nei-cun-pan
di-20-zhang-cun-chu/20.11.-wen-jian-xi-tong-kuai-zhao
di-20-zhang-cun-chu/20.12.-ci-pan-pei-e
di-20-zhang-cun-chu/20.13.-jia-mi-ci-pan-fen-qu
di-20-zhang-cun-chu/20.14.-jia-mi-jiao-huan-fen-qu
di-20-zhang-cun-chu/20.15.-gao-ke-yong-xing-cun-chu-hast
```
## 第二一章 GEOM: 模块化磁盘转换框架
```toc
:maxdepth: 1

di-21-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/21.1.-gai-shu
di-21-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/21.2.-raid0-tiao-dai
di-21-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/21.3.-raid1-jing-xiang
di-21-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/21.4.-raid3-dai-you-zhuan-yong-qi-ou-xiao-yan-de-zi-jie-ji-tiao-dai
di-21-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/21.5.-ruan-jian-raid-she-bei
di-21-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/21.6.-geom-gate-wang-luo-she-bei
di-21-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/21.7.-wei-ci-pan-she-bei-tian-jia-juan-biao
di-21-zhang-geom-mo-kuai-hua-ci-pan-zhuan-huan-kuang-jia/21.8.-tong-guo-geom-shi-xian-ufs-ri-zhi
```
## 第二十二章 Z 文件系统（ZFS）
```toc
:maxdepth: 1

di-22-zhang-z-wen-jian-xi-tong-zfs/22.1.-shi-shi-mo-shi-zfs-yu-zhong-bu-tong
di-22-zhang-z-wen-jian-xi-tong-zfs/22.2.-kuai-su-ru-men-zhi-nan
di-22-zhang-z-wen-jian-xi-tong-zfs/22.3.-zpool-guan-li
di-22-zhang-z-wen-jian-xi-tong-zfs/22.4.-zfs-guan-li
di-22-zhang-z-wen-jian-xi-tong-zfs/22.5.-wei-tuo-guan-li
di-22-zhang-z-wen-jian-xi-tong-zfs/22.6.-gao-ji-zhu-ti
di-22-zhang-z-wen-jian-xi-tong-zfs/22.7.-geng-duo-zi-yuan
di-22-zhang-z-wen-jian-xi-tong-zfs/22.8.-zfs-te-xing-he-shu-yu
```
## 第二十三章 其他文件系统
```toc
:maxdepth: 1

di-23-zhang-qi-ta-wen-jian-xi-tong/23.1.-gai-shu
di-23-zhang-qi-ta-wen-jian-xi-tong/23.2.-linux-wen-jian-xi-tong
```
## 第二十四章 虚拟化
```toc
:maxdepth: 1

di-24-zhang-xu-ni-hua/24.1.-gai-shu
di-24-zhang-xu-ni-hua/24.2.-shi-yong-macos-shang-de-parallels-desktop-an-zhuang-freebsd
di-24-zhang-xu-ni-hua/24.3.-shi-yong-macos-shang-de-vmware-fusion-an-zhuang-freebsd
di-24-zhang-xu-ni-hua/24.4.-shi-yong-virtualbox-an-zhuang-freebsd
di-24-zhang-xu-ni-hua/24.5.-zai-freebsd-shang-an-zhuang-virtualbox
di-24-zhang-xu-ni-hua/24.6.-shi-yong-freebsd-shang-de-bhyve-xu-ni-ji
di-24-zhang-xu-ni-hua/24.7.-shi-yong-freebsd-shang-de-xen-xu-ni-ji
```
## 第二十五章 本地化——i18n/L10n 的使用和设置
```toc
:maxdepth: 1

di-25-zhang-ben-di-hua-i18nl10n-de-shi-yong-he-she-zhi/25.1.-gai-shu
di-25-zhang-ben-di-hua-i18nl10n-de-shi-yong-he-she-zhi/25.2.-shi-yong-ben-di-hua
di-25-zhang-ben-di-hua-i18nl10n-de-shi-yong-he-she-zhi/25.3.-xun-zhao-i18n-ying-yong-cheng-xu
di-25-zhang-ben-di-hua-i18nl10n-de-shi-yong-he-she-zhi/25.4.-te-ding-yu-yan-de-qu-yu-pei-zhi
```
## 第二十六章 FreeBSD 更新与升级
```toc
:maxdepth: 1

di-26-zhang-freebsd-geng-xin-yu-sheng-ji/26.1.-gai-shu
di-26-zhang-freebsd-geng-xin-yu-sheng-ji/26.2.-geng-xin-freebsd
di-26-zhang-freebsd-geng-xin-yu-sheng-ji/26.3.-geng-xin-bootcode
di-26-zhang-freebsd-geng-xin-yu-sheng-ji/26.4.-geng-xin-wen-dang
di-26-zhang-freebsd-geng-xin-yu-sheng-ji/26.5.-zhui-zong-kai-fa-fen-zhi
di-26-zhang-freebsd-geng-xin-yu-sheng-ji/26.6.-cong-yuan-dai-ma-geng-xin-freebsd
di-26-zhang-freebsd-geng-xin-yu-sheng-ji/26.7.-duo-tai-ji-qi-de-zhui-zong
```
## 第二十七章 DTrace
```toc
:maxdepth: 1

di-27-zhang-dtrace/27.1.-gai-shu
di-27-zhang-dtrace/27.2.-shi-xian-shang-de-cha-yi
di-27-zhang-dtrace/27.3.-kai-qi-dtrace-zhi-chi
di-27-zhang-dtrace/27.4.-shi-yong-dtrace
```
## 第二十八章 USB 设备模式/USB OTG
```toc
:maxdepth: 1

di-28-zhang-usb-she-bei-mo-shi-usb-otg/28.1.-gai-shu
di-28-zhang-usb-she-bei-mo-shi-usb-otg/28.2.-usb-xu-ni-chuan-hang-duan-kou
di-28-zhang-usb-she-bei-mo-shi-usb-otg/28.3.-usb-she-bei-mo-shi-wang-luo-jie-kou
di-28-zhang-usb-she-bei-mo-shi-usb-otg/28.4.-usb-xu-ni-cun-chu-she-bei

```