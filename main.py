import gifos, colorama
from colorama import Fore

colorama.init()

t = gifos.Terminal(width=800, height=600, xpad=5, ypad=5, font_size=15)

t.set_fps(15)

# Function to print a line of reg text with color
def reg_line(text, row, delay=2, color="white", contin=False, save=True):
    t.set_txt_color(color)
    t.gen_text(text=text, row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")

def shell(row, delay=0, color="white", contin=False, save=True):
    t.set_txt_color(color)
    t.gen_text(text="[reggie@gentoo ~]$ ", row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")

def typetext(text, row, delay=1, color="white", contin=True, save=True):
    t.clone_frame(3)
    for char in text:
        t.set_txt_color(color)
        t.gen_text(text=char, row_num=row, contin=contin)
        t.clone_frame(delay)
        if save:
            t.save_frame(base_file_name=f"frame_{row}")
        t.set_txt_color("white")

def blankspace(row, delay=0, color="white", contin=False, save=True):
    t.set_txt_color(color)
    t.gen_text(text="     ", row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")

def openrc_line(text, row, delay=2, color="white", contin=False, save=True):
    t.gen_text(text=Fore.GREEN + "* " + Fore.WHITE + text, row_num=row, contin=contin)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")

def openrc_line_ok(text, row, max_width=72, delay=2, color="white", contin=False, save=True):
    padding = max_width - len(text) -  1  # Subtract  1 for the space before "OK"
    if padding <  0:
        padding =  0
    padded_text = text + " " * padding
    
    t.gen_text(text=Fore.GREEN + "* " + Fore.WHITE + padded_text, row_num=row, contin=contin)
    t.clone_frame(delay)
    t.gen_text("[ " + Fore.GREEN + "ok" + Fore.WHITE + " ]", row_num=row, contin=True)
    t.clone_frame(delay)
    if save:
        t.save_frame(base_file_name=f"frame_{row}")
    t.set_txt_color("white")






reg_line("Loading Linux 6.8.1-zen1-1-zen ...", 1, delay=0)
reg_line("Loading initial ramdisk ...", 2, delay=5)
t.clone_frame(30)

#begin openrc clone lol

t.clear_frame()
reg_line("Freeing unused kernel memory: 980K (ffffffff81bcf000 - ffffffff81cc4000)", 1, delay=0)
reg_line("INIT: version 3.08 booting", 2, delay=0)
blankspace(3)
reg_line("     " + Fore.LIGHTGREEN_EX + "OpenRC 0.53" + Fore.WHITE + " Is starting up " + Fore.BLUE + "Gentoo Linux (x86_64)" + Fore.WHITE, 4, delay=0)
blankspace(5)
openrc_line_ok("Mounting /proc ...", 6, delay=2)
openrc_line_ok("Mounting /run ...", 7, delay=2)
openrc_line("/run/openrc: creating directory", 8, delay=0)
openrc_line("/run/lock: creating directory", 9, delay=0)
openrc_line("/run/lock: correcting owner", 10, delay=0)
openrc_line_ok("Caching service dependencies ...", 11, delay=0)
openrc_line_ok("Mounting devtmpfs on /dev ...", 12, delay=0)
openrc_line_ok("Mounting /dev/mqueue ...", 13, delay=7)
openrc_line_ok("Mounting /dev/pts ...", 14, delay=0)
openrc_line_ok("Mounting /dev/shm ...", 15, delay=0)
openrc_line_ok("Creating list of required static device nodes for the current kernel . ", 16, delay=0)
openrc_line_ok("Mounting /sys ...", 17, delay=0)
openrc_line_ok("Mounting debug filesystem ...", 18, delay=4)
openrc_line_ok("Mounting config filesystem ...", 19, delay=2)
openrc_line_ok("Mounting cgroup filesystem ...", 20, delay=1)
openrc_line_ok("Mounting fuse control filesystem ...", 21, delay=0)
openrc_line_ok("Setting up tmpfiles.d entries for /dev ...", 22, delay=0)
openrc_line_ok("Starting udev ...", 23, delay=0)
openrc_line_ok("Generating a rule to create a /dev/root symlink ...", 24, delay=0)
openrc_line_ok("Populating /dev with existing devices through uevents ...", 25, delay=0)
openrc_line_ok("Waiting for uevents to be processed ...", 26, delay=0)
openrc_line_ok("Setting system clock using the hardware clock [Local Time] ...", 27, delay=3)
openrc_line("Configuring kernel parameters ...", 28, delay=0)
openrc_line("Activating swap devices ...", 29, delay=0)
openrc_line_ok("Setting hostname to gentoo ...", 30, delay=0)
openrc_line("Autoloaded 18 module(s)", 31, delay=2)
openrc_line_ok("Checking local filesystems ...", 32, delay=5)
reg_line("Gentoo_x86: clean, 786432/786432 files... ", 33, delay=0)
openrc_line_ok("Remounting root filesystem read/write ...", 34, delay=0)
openrc_line_ok("Remounting filesystems ...", 35, delay=2)
openrc_line("Skipping mtab update (mtab is a symbolic link)", 36, delay=0)
openrc_line_ok("Mounting local filesystems ...", 37, delay=2)
openrc_line("setting up tmpfiles.d entries ...", 38, delay=0)
openrc_line("Initializing random number generator ...", 39, delay=0)
openrc_line("Activating additional swap space ...", 40, delay=0)
openrc_line_ok("Mounting misc binary format filesystem ...", 41, delay=0)
reg_line("tmpfiles: ignoring invalid entry on line 15 of `/usr/lib/tmpfiles.d//tmp.conf`", 42, delay=0)
reg_line("tmpfiles: ignoring invalid entry on line 16 of `/usr/lib/tmpfiles.d//tmp.conf`", 43, delay=0)
openrc_line("Creating user login records ...", 44, delay=0)
openrc_line_ok("Loading custom binary format handlers ...", 45, delay=0)
openrc_line_ok("Clearing /var/run ...", 46, delay=0)
openrc_line_ok("Wiping /tmp directory ...", 47, delay=0)
openrc_line("Setting terminal encoding [UTF-8] ...", 48, delay=0)
openrc_line_ok("Bringing up interface lo", 49, delay=0)
openrc_line_ok("Setting keyboard mode [UTF-8] ...", 50, delay=0)
openrc_line_ok("Loading key mappings [en_US] ...", 51, delay=0)
openrc_line_ok("   127.0.0.1/8 ...", 52, delay=0)
openrc_line("   Adding routes", 53, delay=0)
openrc_line_ok("      127.0.0.0/8 via 127.0.0.1 ...", 54, delay=0)
reg_line("INIT: Entering runlevel: 3", 55, delay=0)
openrc_line_ok("Starting D-BUS system messagebus ...", 56, delay=0)
openrc_line_ok("Starting syslog-ng ...", 57, delay=0)
openrc_line("Starting DHCP Client Daemon ...", 58, delay=0)
openrc_line("Starting ConsoleKit daemon ...", 59, delay=0)
openrc_line_ok("Starting vixie-cron ...", 60, delay=0)
openrc_line_ok("Starting local ...", 61, delay=0)
blankspace(62)
blankspace(63)
blankspace(64)
reg_line("Gentoo Linux 6.8.1-zen1-1-zen (tty1)", 65, delay=0)
blankspace(66)
reg_line("gentoo login: ", 66, delay=0)
typetext("reggie", 66)
reg_line("password: ", 67, delay=0)
typetext("*************************", 67)
blankspace(68)
blankspace(69)
shell(70)
typetext("pfetch", 70, contin=True)
blankspace(71)


# _-----_      reggie@gentoo
#(       \     os     Gentoo Linux
#\    0   \    kernel 6.8.1-zen1-1-zen
# \        )   uptime 10s
# /      _/    pkgs   1288
#(     _-      memory 7834M / 31242M
#\____-        
reg_line(Fore.MAGENTA + " _-----_      " + Fore.BLUE + "reggie" + Fore.WHITE + "@" + Fore.BLUE + "gentoo", 72, delay=0)
reg_line(Fore.MAGENTA + "(       \     os" + Fore.WHITE + "     Gentoo Linux", 73, delay=0)
reg_line(Fore.MAGENTA + "\    0   \    kernel" + Fore.WHITE + " 6.8.1-zen1-1-zen", 74, delay=0)
reg_line(" \        )   " + Fore.MAGENTA + "uptime" + Fore.WHITE + " 10s", 75, delay=0)
reg_line(" /      _/    " + Fore.MAGENTA + "pkgs" + Fore.WHITE + "   1288", 76, delay=0)
reg_line("(     _-      " + Fore.MAGENTA + "memory" + Fore.WHITE + " 7834M / 31242M", 77, delay=0)
reg_line("\____-        ", 78, delay=0)
blankspace(79)
shell(80)
t.clone_frame(15)

typetext("ghfetch -u reggietorres", 80)

gh_stats = gifos.utils.fetch_github_stats("reggietorres")
details_lines = f"""\x1b[96mUser Rating: \x1b[93m{gh_stats.user_rank.level}\x1b[0m
\x1b[96mTotal Stars Earned: \x1b[93m{gh_stats.total_stargazers}\x1b[0m
\x1b[96mTotal Commits (2023): \x1b[93m{gh_stats.total_commits_last_year}\x1b[0m
\x1b[96mTotal PRs: \x1b[93m{gh_stats.total_pull_requests_made}\x1b[0m
\x1b[96mMerged PR %: \x1b[93m{gh_stats.pull_requests_merge_percentage}\x1b[0m
\x1b[96mTotal Contributions: \x1b[93m{gh_stats.total_repo_contributions}\x1b[0m
"""
blankspace(81)
reg_line(text=details_lines, row=82, delay=0)

blankspace(83)
shell(84)

typetext("cat /proc/languages | head -n 6", 84)

blankspace(85)

t.gen_text(text="\x1b[34mHTML", row_num=86)
t.gen_text(text="\x1b[35mCSS", row_num=87)
t.gen_text(text="\x1b[33mJavaScript", row_num=88)
t.gen_text(text="\x1b[34mPython", row_num=89)
t.gen_text(text="\x1b[32mC", row_num=90)
t.gen_text(text="\x1b[31mC++", row_num=91)

blankspace(86)
shell(87)
typetext("cat /proc/frameworks | head -n 3", 87)
blankspace(88)

t.gen_text(text="\x1b[32mpyFlask", row_num=89)
t.gen_text(text="\x1b[36mTailwindCSS", row_num=90)
t.gen_text(text="\x1b[32mpyQT5", row_num=91)

blankspace(92)
shell(93)
typetext('echo "thanks for stopping by!" | cowsay', 94)
blankspace(95)

reg_line(" _________________________ ",96, delay=0)
reg_line("< thanks for stopping by! >",97, delay=0)
reg_line(" ------------------------- ",98, delay=0)
reg_line("        \   ^__^",99, delay=0)
reg_line("         \  (oo)\_______",100, delay=0)
reg_line("            (__)\       )\/",101, delay=0)
reg_line("                ||----w |",102, delay=0)
reg_line("                ||     ||",103, delay=0)



blankspace(102)
shell(103)
t.clone_frame(60)
typetext("poweroff", 104)
openrc_line("Stopping local ...", 105, delay=0)
openrc_line("Saving random seed ...", 106, delay=0)
openrc_line("Unmounting network filesystems ...", 107, delay=0)
openrc_line("Stopping cronie ...", 108, delay=0)
openrc_line("Stopping NetworkManager ...", 109, delay=0)
openrc_line("Stopping elogind ...", 110, delay=0)
openrc_line("Stopping dbus ...", 111, delay=0)
openrc_line("Unmounting loop devices ...", 112, delay=0)
openrc_line("Unmounting filesystems ...", 113, delay=0)
openrc_line("   Unmounting /efi ...", 114, delay=0)
openrc_line("Deactivating swap devices ...", 115, delay=0)
openrc_line("Setting hardware clock using the system clock [Local Time]...", 116, delay=0)
openrc_line("Stopping udev ...", 117, delay=0)
openrc_line("Terminating remaining processes ...", 118, delay=2)
openrc_line("Killing remaining processes ...", 119, delay=0)
openrc_line("Saving dependency cache ...", 120, delay=0)
openrc_line("Remounting remaining filesystems read-only ...", 121, delay=0)
openrc_line("   Remounting / read only ...", 122, delay=0)
reg_line("Sending the final term signal", 123, delay=30)
reg_line("Sending the final term signal", 124, delay=0)
t.clear_frame()
t.clone_frame(60)

t.gen_gif()