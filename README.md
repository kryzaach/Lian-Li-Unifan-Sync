# Lian-Li-Unifan-Sync
Just a quick hack to allow the use of the unifan hub in linux, as a synced device

This only applies to the LianLi-UNI FAN-SL V2-v0.5

Imagine my disgust when I bought these amazing fans only to find out that;
1) The control software is windows or mac only
2) The hub has no persistent state through a power off, unlike the corsair commander pro
3) It can't even sync to the dedicated inputs unless the control software tells it to on every reboot

So, after dumping the commands in windows with wireshark, here is a dirty hack script that you can run on startup to sync the lighting and fans.
Could it be prettier? Yes.
Do I care enough to fix it? No.
