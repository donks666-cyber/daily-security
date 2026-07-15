Title: Last Week in Security (LWiS) - 2021-11-08
Date: 2021-11-08 21:22
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-11-08
Author: Erik
Summary: DLL proxying helper BOFs (<a href="https://twitter.com/the_bit_diddler" target="_blank">@the_bit_diddler</a>), Cobalt Strike traffic decryption (<a href="https://twitter.com/DidierStevens" target="_blank">@DidierStevens</a>), CES/CEP on Linux (<a href="https://twitter.com/duff22b" target="_blank">@duff22b</a>), Kerberoasting OPSEC (<a href="https://twitter.com/DebugPrivilege" target="_blank">@DebugPrivilege</a>), certutil LOLbin replacement (<a href="https://twitter.com/ElliotKillick" target="_blank">@ElliotKillick</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-11-01 to 2021-11-08.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.state.gov/reward-offers-for-information-to-bring-darkside-ransomware-variant-co-conspirators-to-justice/" target="_blank">Reward Offers for Information to Bring DarkSide Ransomware Variant Co-Conspirators to Justice</a>. $10M USD for conviction of "individual(s) who hold(s) a key leadership position in the DarkSide" group. I think the goal of this is to sow distrust within DarkSide, and a potential $10M payout to snitch will certainly do that.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2021/11/1/pwn2ownaustin" target="_blank">Pwn2Own Austin 2021 - Schedule and Live Results</a>. It's always cool to see how many and what types of devices fall at Pwn2Own.</li>
<li><a href="https://hacks.mozilla.org/2021/05/introducing-firefox-new-site-isolation-security-architecture/" target="_blank">Introducing Firefox’s new Site Isolation Security Architecture</a>. Great news for the underdog browser. However, it may be <a href="https://madaidans-insecurities.github.io/firefox-chromium.html" target="_blank">too little too late</a>.</li>
<li><a href="https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cps-static-key-JmS92hNv" target="_blank">Cisco Policy Suite Static SSH Keys Vulnerability</a>. Cisco is the king of 9.0+ CVSS scores in critical networking hardware. This time it's SSH in the Policy Suite software and its Catalyst Passive Optical Network (PON) switches that could allow and attacker to log in a root.</li>
<li><a href="https://www.usnews.com/news/world/articles/2021-11-06/drone-attack-targets-iraq-pm-who-escapes-unhurt-iraq-military" target="_blank">Iraqi PM Safe After Drone Attack on Residence, Military Says</a>. Explosive laden assassination drones. "The <span class="strike">future</span> dystopia is already here — it’s just not very evenly distributed."</li>
<li><a href="https://support.kaspersky.com/general/vulnerability.aspx?el=12430#01112021_phishing" target="_blank">Phishing emails seemingly coming from a Kaspersky email address</a>. A better title might be, "oops someone used one of our AWS SES tokens to phish."</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://www.infosec.tirol/master-of-puppets-part-ii-how-to-tamper-the-edr/" target="_blank">Master of Puppets Part II – How to tamper the EDR?</a>. Tons of great ideas for how to disable EDR, even if it has a kernel driver. Great work.</li>
<li><a href="https://www.chadduffey.com/2021/11/CESCEP.html" target="_blank">Using Microsoft CES/CEP for Linux Workstation Certificate Enrollment with Kerberos Workstation Authentication</a>. While not a "red team" post, this shows how to set up CES/CEP with Linux which will give you an understanding to how that all works, and ideas for how it can be leveraged if you find yourself on a domain joined Linux machine.</li>
<li><a href="https://blog.nviso.eu/2021/11/03/cobalt-strike-using-process-memory-to-decrypt-traffic-part-3/" target="_blank">Cobalt Strike: Using Process Memory To Decrypt Traffic – Part 3</a>. If you're using for Cobalt Strike for serious operations, you're asking for trouble. Security through obscurity is a legitimate part of a larger security model.</li>
<li><a href="https://m365internals.com/2021/11/08/kerberoast-with-opsec/amp/" target="_blank">Kerberoast with OpSec</a>. Kerberoasting remains a powerful attack, but it's time to clean up how you go about searching for kerberoastable accounts.</li>
<li><a href="https://www.sentinelone.com/labs/tipc-remote-linux-kernel-heap-overflow-allows-arbitrary-code-execution/" target="_blank">CVE-2021-43267: Remote Linux Kernel Heap Overflow | TIPC Module Allows Arbitrary Code Execution</a>. Interesting bug and walk through (CodeQL again...). No PoC yet.</li>
<li><a href="https://medium.com/@omribaso/this-is-how-i-bypassed-almost-every-edr-6e9792cf6c44" target="_blank">This is how I bypassed almost every EDR!</a>. Userland unhooking and direct syscalls aren't novel, but the use of the PEB to find the clean functions in NTDLL without syscalls is a nice twist.</li>
<li><a href="https://www.romainthomas.fr/post/21-11-pgsharp-analysis/" target="_blank">PGSharp: Analysis of a Cheating App for PokemonGO</a>. This is an in-depth analysis of an Android cheat engine. Tons of good stuff if you are an android "tool" developer.</li>
<li><a class="m-text m-dim" href="https://attackerkb.com/topics/D41jRUXCiJ/cve-2021-22205/rapid7-analysis" target="_blank">CVE-2021-22205 Rapid7 Analysis</a>. Lots of Gitlab instances were used in a DDoS attack last week. This is how. Note that this was patched back in April 2021.</li>
<li><a href="http://muffsec.com/blog/pwn2own-xxe2rce/" target="_blank">Pwn2Own to Xxe2Rce</a>. XXE to RCE on an ICS controller - nice!</li>
<li><a href="https://twitter.com/ElliotKillick/status/1455897435063074824" target="_blank">Newly discovered #lolbin "C:WindowsSystem32Cmdl32.exe"</a>. Download files with a Microsoft signed binary. So long certutil.exe, hello cmdl32.exe!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/EspressoCake/DLL-Hijack-Search-Order-BOF" target="_blank">DLL-Hijack-Search-Order-BOF</a> is a Cobalt Strike BOF file, meant to use two arguments (path to begin, and a DLL filename of interest), that will traverse the SafeSearch order of DLL resolution. Optionally, this will also attempt to ascertain a HANDLE to the provided file (if found), and alert the operator of its mutability (WRITE access).</li>
<li><a href="https://github.com/EspressoCake/DLL-Exports-Extraction-BOF" target="_blank">DLL-Exports-Extraction-BOF</a> is a BOF for DLL export extraction with optional NTFS transactions.</li>
<li><a href="https://git.sr.ht/~prabhu/blint" target="_blank">blint</a> is a Binary Linter to check the security properties, and capabilities in your executables.</li>
<li><a href="https://github.com/Matheus-Garbelini/braktooth_esp32_bluetooth_classic_attacks" target="_blank">braktooth_esp32_bluetooth_classic_attacks</a> is a series of baseband &amp; LMP exploits against Bluetooth classic controllers.</li>
<li><a href="https://github.com/HexRabbit/CVE-writeup/tree/master/CVE-2021-34886" target="_blank">CVE-2021-34886</a> is a Linux kernel eBPF map type confusion that leads to EoP and affects Linux kernel 5.8 to 5.13.13. Writeup (CN) <a href="https://blog.hexrabbit.io/2021/11/03/CVE-2021-34866-writeup/" target="_blank">here</a>.</li>
<li><a href="https://github.com/gamozolabs/elfloader" target="_blank">elfloader</a> is an architecture-agnostic ELF file flattener for shellcode written in Rust.</li>
<li><a href="https://github.com/dsnezhkov/socksdll" target="_blank">socksdll</a> isa a loadable socks5 proxy via CGo/C bridge.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/bee-san/pyWhat" target="_blank">pyWhat</a>  easily lets you identify emails, IP addresses, and more. Feed it a .pcap file or some text and it'll tell you what it is! 🧙</li>
<li><a href="https://github.com/deepfence/ThreatMapper" target="_blank">ThreatMapper</a> is used to identify vulnerabilities in running containers, images, hosts and repositories and helps you to monitor and secure your running applications, in Cloud, Kubernetes, Docker, and Fargate Serverless.</li>
<li><a href="https://github.com/0xADE1A1DE/AssemblyLine" target="_blank">AssemblyLine</a> is a C library and binary for generating machine code of x86_64 assembly language and executing on the fly without invoking another compiler, assembler or linker. Could you build this into your RAT to execute shellcode modules without suspicious API calls?</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
