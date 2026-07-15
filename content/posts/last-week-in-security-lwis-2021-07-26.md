Title: Last Week in Security (LWiS) - 2021-07-26
Date: 2021-07-26 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-07-26
Author: Erik
Summary: User readable SAM hives (<a href="https://twitter.com/jonasLyk" target="_blank">@jonasLyk</a> and <a href="https://twitter.com/cube0x0" target="_blank">@cube0x0</a>), PetitPotam takes off (<a href="https://twitter.com/topotam77" target="_blank">@topotam77</a>), Smart AD bruteforcing (<a href="https://twitter.com/_nwodtuhs" target="_blank">@_nwodtuhs</a> and <a href="https://twitter.com/podalirius_" target="_blank">@podalirius_</a>), automated advanced maldocs (<a href="https://twitter.com/33y0re" target="_blank">@33y0re</a>), Windows command line obfuscation (<a href="https://twitter.com/wietze" target="_blank">@Wietze</a>), dockerized Android (<a href="https://twitter.com/sickcodes" target="_blank">@sickcodes</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-07-19 to 2021-07-26.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.kaseya.com/potential-attack-on-kaseya-vsa/" target="_blank">Updates Regarding VSA Security Incident</a>. Kaseya got their hands on a universal decrpytor for the randomsware that hit thousands of their customers on the Friday before the July 4th holiday in the US. They state that, "in no uncertain terms that Kaseya did not pay a ransom – either directly or indirectly through a third party – to obtain the decryptor." This leaves two possibilities: Someone found a flaw in the encryption scheme a professional ransomware crew with years of experience was using, or someone acquired the universal decryptor key without paying for it (leak, hack, deal to not get arrested by the FSB, etc). If there was a flaw in the encryption, have researchers been sitting on it like the allies allowed ships to be sunk after breaking the Enigma cypher in WWII? Was the Kaseya incident big enough to "burn" the technique? With the disappearance of REvil's public infrastructure, I suspect the FSB came knocking, demanded the key, and told them to take a nice vacation on the Black Sea while things cool off.</li>
<li><a href="https://blog.windscribe.com/openvpn-security-improvements-and-changes-7b04ea49222" target="_blank">OpenVPN Security Improvements and Changes</a>. Two Ukrainian Windscribe VPN servers were seized and since they were unencrypted and had persistent disks, the authorities got hold of the OpenVPN private keys. In the age of ubiquitous HTTPS and HSTS preloading VPNs are effective against a very specific threat model, and are probably unnecessary for most people (despite what the YouTube ads will tell you).</li>
<li><a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934" target="_blank">CVE-2021-36934 aka HiveNightmare aka SeriousSAM</a>. For some reason, Windows 10 starting with 1909 and Server 2019 modified the SAM database access control lists to allow regular users to read the contents. While the files are locked by lsass normally, if the system has volume shadow copies (VSS), they will be available there. Check out <a href="https://github.com/cube0x0/CVE-2021-36934" target="_blank">CVE-2021-36934</a> to check for shadow copies and read them all in memory, and <a href="https://docs.velociraptor.app/exchange/artifacts/pages/windows.ntfs.mft.hivenightmare/" target="_blank">this Velociraptor query</a> to hunt for it.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><dl>
<dt><a href="https://github.com/topotam/PetitPotam" target="_blank">PetitPotam</a>. While this was in last week's Tool/Exploits section, it has hit the news this week. Besides the classic Unconstrained Delegation method, there was talk of the following ways to leverage PetitPotam.</dt>
<dd><ul>
<li><a href="https://isc.sans.edu/diary/27668" target="_blank">Active Directory Certificate Services (ADCS - PKI) domain admin vulnerability</a>. SANS covers the PetitPotam + ADCS + Impaket + Rebeus route.</li>
<li><a href="https://twitter.com/tifkin_/status/1418855927575302144" target="_blank">WebDAV + NTLM is also an option</a></li>
<li><a href="https://twitter.com/_wald0/status/1418077997051957252" target="_blank">Find a computer with a path to AD and SMB relay</a></li>
<li><a href="https://twitter.com/gentilkiwi/status/1418660994931376136" target="_blank">Mimikatz + Kekeo + Impacket</a></li>
<li><a href="https://support.microsoft.com/en-us/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429" target="_blank">Microsoft's response: Won't fix</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://labs.sentinelone.com/cve-2021-3438-16-years-in-hiding-millions-of-printers-worldwide-vulnerable/" target="_blank">CVE-2021-3438: 16 Years In Hiding – Millions of Printers Worldwide Vulnerable</a>. A sloppy strncopy with a size parameter controlled by the user in this driver from 2005 can lead an unprivileged user to SYSTEM. Look for the SSPORT.sys driver on your next engagement.</li>
<li><a href="https://blog.qualys.com/vulnerabilities-threat-research/2021/07/20/sequoia-a-local-privilege-escalation-vulnerability-in-linuxs-filesystem-layer-cve-2021-33909" target="_blank">Sequoia: A Local Privilege Escalation Vulnerability in Linux’s Filesystem Layer (CVE-2021-33909)</a>. A size_t-to-int type conversion vulnerability in the Linux Kernel’s filesystem layer affecting most Linux operating systems (3.16 through 5.13.x before 5.13.4). Any unprivileged user can gain root privileges on a vulnerable host by exploiting this vulnerability in a default configuration. You can use <a href="https://www.qualys.com/research/security-advisories/" target="_blank">cve-2021-33909-crasher.c</a> to test if the vulnerability exists on systems, but a user to root PoC isn't in the wild yet. This could be the <a href="https://dirtycow.ninja/" target="_blank">Dirty COW</a> of 2021.</li>
<li><a href="https://research.securitum.com/fail2ban-remote-code-execution/" target="_blank">fail2ban – Remote Code Execution</a>. While not exploitable without MiTM or the ability to set whois information, the <cite>~!</cite> feature of the <cite>mail</cite> binary can be abused to inject commands to any program that passes attacker controlled input to <cite>mail</cite>.</li>
<li><a href="https://hackerone.com/reports/1234406" target="_blank">Exfiltrating a victim's exact location (to within 5m)</a>. This is a great example of getting inside the mind of the defender to speculate what they did to "fix" a vulnerability, and then exploiting that "fix."</li>
<li><a href="https://www.wietzebeukema.nl/blog/windows-command-line-obfuscation" target="_blank">Windows Command-Line Obfuscation</a>. "Many Windows applications have multiple ways in which the same command line can be expressed, usually for compatibility or ease-of-use reasons. As a result, command-line arguments are implemented inconsistently making detecting specific commands harder due to the number of variations. This post shows how more than 40 often-used, built-in Windows applications are vulnerable to forms of command-line obfuscation, and presents a tool for analyzing other executables." Check out <a href="https://github.com/wietze/windows-command-line-obfuscation" target="_blank">windows-command-line-obfuscation</a> for the scripts and raw data.</li>
<li><a href="https://blog.ret2.io/2021/07/21/wtf-snapshot-fuzzing/" target="_blank">All Your Base Are [Still] Belong To Us: Fuzzing Modern UDP Game Protocols With Snapshot-based Fuzzers</a>. Ever wanted to discover a potential RCE against a AAA multiplayer game without all that hardcore reverse engineering? Hit it with a well tuned fuzzer and let the vulnerabilities fall out!</li>
<li><a href="https://www.solomonsklash.io/devils-in-the-details.html" target="_blank">On Disk, The Devil’s In The Details</a>. When persisting, or otherwise dropping files to disk, professionals will do the extra work to make their exes and dlls blend in. You should too! One tool not mentioned that I find useful: <a href="https://github.com/obscuritylabs/PeFixup" target="_blank">PeFixup</a>.</li>
<li><a href="https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575" target="_blank">Guide to Named Pipes and Hunting for Cobalt Strike Pipes</a>. It's probably worth going through your profiles to ensure your pipe names aren't in the table of default and common profile pipe names.</li>
<li><a href="https://security.humanativaspa.it/openssh-ssh-agent-shielded-private-key-extraction-x86_64-linux/" target="_blank">OpenSSH ssh-agent Shielded Private Key Extraction (x86_64 Linux)</a>. This is a nice post on how to extract private keys from the memory space of OpenSSH after the introduction of "shielded private keys."</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/capt-meelo/Beaconator" target="_blank">Beaconator</a> is an aggressor script for Cobalt Strike used to generate a raw stageless shellcode and packing the generated shellcode using <a href="https://github.com/phra/PEzor" target="_blank">PEzor</a>.</li>
<li><a href="https://github.com/ShutdownRepo/smartbrute" target="_blank">smartbrute</a> is a smart password spraying and bruteforcing tool for Active Directory Domain Services. Supports NTML over SMB or LDAP as well as Kerberos pre-authentication bruteforcing. It can also intelligently bruteforce a domain to prevent user lockouts.</li>
<li><a href="https://github.com/DarkCoderSc/inno-shellcode-example/" target="_blank">inno-shellcode-example</a> is an InnoSetup template to that runs shellcode! How easy is it to convince a user they need to install Zoom, Adobe Reader XYZ, or whatever-app to join your meeting, read your document, etc? Now you can have a legit installer with some extra shellcode injection!</li>
<li><a href="https://github.com/MythicAgents/Medusa" target="_blank">Medusa</a> is a cross-platform C2 agent compatible with Python 2.7 and 3.8, compatible with Mythic. This new agent has some nice features, but does require Python (just a base install) on the target to run.</li>
<li><a href="https://github.com/connormcgarr/LittleCorporal" target="_blank">LittleCorporal</a> is a C# automated maldoc generator. It uses a two step process to first self-inject into Word via an AutoOpen macro, and then inject the real payload from word into a running process. The use of InlineShape and automated building is just the cherry on top.</li>
<li><a href="https://github.com/kleiton0x00/ppmap" target="_blank">ppmap</a> is a scanner/exploitation tool written in Go, which leverages Prototype Pollution to XSS by exploiting known gadgets. Use this on your next web app assessment or bug bounty.</li>
<li><a href="https://github.com/sickcodes/dock-droid" target="_blank">dock-droid</a> is dockerized android. Run QEMU Android x86 and Android ARM in a Docker with X11 Forwarding. This could be useful for CI/CD for Android or for poking at Android apps "live."</li>
<li><a href="https://github.com/Inf0secRabbit/BadAssMacros" target="_blank">BadAssMacros</a> is an automated malicious macro generator written in C# with capabilities like VBA purging, sandbox detections, and shellcode obfuscation.</li>
<li><a href="https://github.com/antonioCoco/RemotePotato0/releases/tag/1.1" target="_blank">RemotePotato0 Cross Session Activation</a>. Version 1.1 drops the requirement for the victim to be in session 0. Now you can coerce and relay NTLM authentication from any user in any session!</li>
<li><a href="https://github.com/anthemtotheego/Detect-Hooks" target="_blank">Detect-Hooks</a> is a proof of concept Beacon Object File (BOF) that attempts to detect userland API hooks in place by AV/EDR. The BOF will return a list of detected API hooks or let the operator know no hooks were detected. This can be useful knowledge to have before performing certain post-exploitation actions.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/banga/git-split-diffs" target="_blank">git-split-diffs</a> brings GitHub style split diffs to your terminal.</li>
<li><a href="https://github.com/elastic/dorothy" target="_blank">dorothy</a> is a tool to test security monitoring and detection for Okta environments.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
