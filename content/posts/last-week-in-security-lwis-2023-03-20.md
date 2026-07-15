Title: Last Week in Security (LWiS) - 2023-03-20
Date: 2023-03-20 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-03-20
Author: Erik
Summary: RCE any Samsung phone (<a href="https://twitter.com/itswillis" target="_blank">@itswillis</a>), Parallels escape (<a href="https://twitter.com/the_impalabs" target="_blank">@the_impalabs</a>), AD trust issues (<a href="https://twitter.com/exploitph" target="_blank">@exploitph</a>), glitching past all ESP32 defenses (<a href="https://twitter.com/raelizecom" target="_blank">@raelizecom</a>), PPL defeated again (<a href="https://twitter.com/itm4n" target="_blank">@itm4n</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-03-07 to 2023-03-20.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><p><a href="https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html" target="_blank">Multiple Internet to Baseband Remote Code Execution Vulnerabilities in Exynos Modems</a>. RCE with no user interaction to basically any modern Samsung phone. All you need is the phone number, no user interaction. Wild. Turn off Wifi Calling and VoLTE until you are sure this one is patched.</p>
</li>
<li><p>AI news</p>
<blockquote>
<ul>
<li><a href="https://gynvael.coldwind.pl/?id=764" target="_blank">LLM + Clean Room: Will LLMs be the death of code copyrights?</a>. Find code you want to use, but isn't licensed right, and just have GPT4 re-write it for you.</li>
<li><a href="https://www.vice.com/en/article/jg5ew4/gpt4-hired-unwitting-taskrabbit-worker" target="_blank">GPT-4 Hired Unwitting TaskRabbit Worker By Pretending to Be 'Vision-Impaired' Human</a>. Remember, at its core GPT-4 is just a model that predicts what should come next in a sequence. It's just scarily good at that task. If you feed it bad instructions it will do bad things. The "novel" part of the article is that GPT-4 "lied" on purpose. But all it really did was predict (correctly) what it should say next based on the context. What's really going to bake your noodle later on is wondering - are you doing anything different? Daniel Miessler <a href="https://danielmiessler.com/blog/ai-is-eating-the-software-world/" target="_blank">thinks GPT-4 understands</a>.</li>
<li><a href="https://github.com/morpheuslord/GPT_Vuln-analyzer" target="_blank">GPT_Vuln-analyzer</a> - Uses ChatGPT API and Python-Nmap module to use the GPT3 model to create vulnerability reports based on Nmap scan data.</li>
<li><a href="https://cocktailpeanut.github.io/dalai/#/" target="_blank">Dalai - Run LLaMA and Alpaca on your computer.</a>. The the 7B and 13B models are quick and easy to install. Models up to 64B parameters are available.</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://www.politico.com/news/2023/03/07/privacy-loophole-ring-doorbell-00084979" target="_blank">The privacy loophole in your doorbell</a>. Ring, like every cloud connected camera/smart speaker is trading security for convenience. People pull out slippery slope arguments about government overreach because governments have a history of collecting as much data as possible and sorting it out later. Plus Ring maybe <a href="https://www.vice.com/en/article/qjvd9q/ransomware-group-claims-hack-of-amazons-ring" target="_blank">got hacked recently</a>.</p>
</li>
<li><p><a href="https://www.kali.org/blog/kali-linux-2023-1-release/#kali-purple" target="_blank">Kali Purple</a>. The Offensive Security team is taking on defense with the release of Kali Purple.</p>
</li>
<li><p><a href="https://arstechnica.com/tech-policy/2023/03/rising-scams-use-ai-to-mimic-voices-of-loved-ones-in-financial-distress/" target="_blank">Thousands scammed by AI voices mimicking loved ones in emergencies</a>. I called this years ago (LWiS 2021-06-21). Next up: your IT guy or boss telling you to click the link and run the exe.</p>
</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.impalabs.com/2303_advisory_parallels-desktop_toolgate.html" target="_blank">Parallels Desktop Toolgate Vulnerability</a>. A guest with Parallels tools installed can write crash dumps to the host, and there existed a path traversal vulnerability that allowed an escape and code execution via the shell login script.</li>
<li><a href="https://blog.scrt.ch/2023/03/17/bypassing-ppl-in-userland-again/" target="_blank">Bypassing PPL in Userland (again)</a>. The PPL master delivers yet again: <a href="https://github.com/itm4n/PPLmedic" target="_blank">PPLmedic</a> - Dump the memory of any PPL with a Userland exploit chain.</li>
<li><a href="https://www.mdsec.co.uk/2023/03/exploiting-cve-2023-23397-microsoft-outlook-elevation-of-privilege-vulnerability/" target="_blank">Exploiting CVE-2023-23397: Microsoft Outlook Elevation of Privilege Vulnerability</a>. Leak NTLM hashes from targets as soon as the Outlook thick client processes an email (they don't even have to open it!). The patch <a href="https://twitter.com/wdormann/status/1636741880674222081" target="_blank">does not prevent UNC paths without dots</a>, so internal assessors can still make use of this on fully patched Outlook clients. PoC <a href="https://github.com/api0cradle/CVE-2023-23397-POC-Powershell" target="_blank">here</a>.</li>
<li><a href="https://adepts.of0x.cc/vba-exports-runtime/" target="_blank">VBA: resolving exports in runtime without NtQueryInformationProcess or GetProcAddress</a>. I once coded an entire personnel intake validation pipeline in Access and VBA. It was painful. Low level programming in VBA is insane.</li>
<li><a href="https://www.cobaltstrike.com/blog/revisiting-the-udrl-part-1-simplifying-development/" target="_blank">Revisiting the User-Defined Reflective Loader Part 1: Simplifying Development</a>. UDRL developmet just got a bit easier.</li>
<li><a href="https://exploit.ph/external-trusts-are-evil.html" target="_blank">External Trusts Are Evil</a>. There is no such thing - in reality - as non-transitive trust. Any domain in a forrest can authenticate and create machine accounts in any other domain in the forrest unless special precautions are taken. Microsoft Active Directory is the ultimate job security for cybersecurity professionals.</li>
<li><a href="https://thalpius.com/2023/03/13/microsoft-defender-for-identity-sensor-identification/" target="_blank">Microsoft Defender for Identity Sensor Identification</a>. Defender for Identity seemingly always opens two uniquely named pipes that can be remotely enumerated.</li>
<li><a href="https://research.nccgroup.com/2023/03/01/making-new-connections-leveraging-cisco-anyconnect-client-to-drop-and-run-payloads/" target="_blank">Making New Connections - Leveraging Cisco AnyConnect Client to Drop and Run Payloads</a>. This tool was in last LWiS, but this walks thorough it in detail.</li>
<li><a href="https://research.nccgroup.com/2023/03/15/a-race-to-report-a-toctou-analysis-of-a-bug-collision-in-intel-smm/" target="_blank">A Race to Report a TOCTOU: Analysis of a Bug Collision in Intel SMM</a>. Intel BIOS bug!</li>
<li><a href="https://medium.com/@zenmoviefornotification/saidov-maxim-cve-2023-26604-c1232a526ba7" target="_blank">CVE-2023-26604</a>. Get root on a systemd Linux machine with... less?! Yes.</li>
<li><a href="https://raelize.com/blog/espressif-systems-esp32-glitching-otp-transfer/" target="_blank">Espressif ESP32: Glitching The OTP Data Transfer</a>. Very cool glitching hacks. Hundreds of thousands of trials to find just the right location and power and time!</li>
<li><a href="https://blog.scrt.ch/2023/03/14/producing-a-poc-for-cve-2022-42475-fortinet-rce/" target="_blank">Producing a POC for CVE-2022-42475 (Fortinet RCE)</a>. A great start to finish walk through of a vulnerability.</li>
<li><a href="https://posts.specterops.io/uncovering-windows-events-b4b9db7eac54" target="_blank">Uncovering Windows Events</a>. How does ETW work? Find out in this post.</li>
<li><a href="https://www.trustedsec.com/blog/red-vs-blue-kerberos-ticket-times-checksums-and-you/" target="_blank">Red vs. Blue: Kerberos Ticket Times, Checksums, and You!</a>. Up your kerberos opsec or detection skills with this post.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/ab2pentest/MacOSThreatTrack" target="_blank">MacOSThreatTrack</a> - Bash tool used for proactive detection of malicious activity on macOS systems.</li>
<li><a href="https://github.com/outflanknl/C2-Tool-Collection" target="_blank">Updates to C2-Tool-Collection</a> - Psm: BOF to show detailed information on a specific process ID; ReconAD: BOF that uses ADSI to query Active Directory (AD and GC) objects and attributes.</li>
<li><a href="https://github.com/rvrsh3ll/Azure-App-Tools" target="_blank">Azure-App-Tools</a> - Collection of tools to use with Azure Applications. Just updated with an IPFS dropper.</li>
<li><a href="https://github.com/memN0ps/ekko-rs" target="_blank">ekko-rs</a> - Rusty Ekko - Sleep Obfuscation in Rust.</li>
<li><a href="https://github.com/gtworek/PSBits/tree/master/OfflineSAM/OfflineAddAdmin2" target="_blank">PSBits</a> - Windows 10 offline admin creation? 😈 Why not?! Everything happens through built-in offlinelsa and offlinesam DLLs. Official, but not very documented.</li>
<li><a href="https://github.com/Mr-Un1k0d3r/Elevate-System-Trusted-BOF" target="_blank">Elevate-System-Trusted-BOF</a> - This BOF can be used to elevate the current beacon to SYSTEM and obtain the TrustedInstaller group privilege. The impersonation is done through the SetThreadToken API.</li>
<li><a href="https://github.com/XaFF-XaFF/Black-Angel-Rootkit" target="_blank">Black-Angel-Rootkit</a> - Black Angel is a Windows 11/10 x64 kernel mode rootkit. Rootkit can be loaded with enabled DSE while maintaining its full functionality.</li>
<li><a href="https://github.com/realoriginal/bootdoor" target="_blank">bootdoor</a> - An initial proof of concept of a bootkit based on Cr4sh's DMABackdoorBoot.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/RoseSecurity/ScrapPY" target="_blank">ScrapPY</a> is a Python utility for scraping manuals, documents, and other sensitive PDFs to generate wordlists that can be utilized by offensive security tools to perform brute force, forced browsing, and dictionary attacks against targets. The tool dives deep to discover keywords and phrases leading to potential passwords or hidden directories.</li>
<li><a href="https://alexplaskett.github.io/demystifying-security-research-part1/" target="_blank">Demystifying Security Research - Part 1</a>. This resonated with me, with a heavy emphasis on blog posts and tweets.</li>
<li><a href="https://github.com/ValtteriL/UPnProxyChain" target="_blank">UPnProxyChain</a> - A tool to create a SOCKS proxy server out of UPnProxy vulnerable device(s).</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 337 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
