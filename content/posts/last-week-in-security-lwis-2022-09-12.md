Title: Last Week in Security (LWiS) - 2022-09-12
Date: 2022-09-12 19:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-09-12
Author: Erik
Summary: Avoiding memory scanners (<a href="https://twitter.com/kyleavery_" target="_blank">@kyleavery_</a>), EvilnoVNC critiques (<a href="https://twitter.com/TheXC3LL" target="_blank">@TheXC3LL</a>), Athena 0.2 (<a href="https://twitter.com/checkymander" target="_blank">@checkymander</a>), Monkey365 (<a href="https://twitter.com/tr1ana" target="_blank">@tr1ana</a>), reFlutter (<a href="https://twitter.com/lmpact_l" target="_blank">@lmpact_l</a>), gTunnel/SOCKS (<a href="https://twitter.com/greycatsecurity" target="_blank">@greycatsecurity</a> + <a href="https://twitter.com/hotnops" target="_blank">@hotnops</a>), cobaltstrike-headless (<a href="https://twitter.com/codex_tf2" target="_blank">@codex_tf2</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-09-06 to 2022-09-12.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2022/09/fuzzing-beyond-memory-corruption.html" target="_blank">Fuzzing beyond memory corruption: Finding broader classes of vulnerabilities automatically</a>. OSS-fuzz recently found a trivial <a href="https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=49053" target="_blank">Command injection</a> and its hungry for more vulnerability classes.</li>
<li><a href="https://www.sentinelone.com/labs/crimeware-trends-ransomware-developers-turn-to-intermittent-encryption-to-evade-detection/" target="_blank">Crimeware Trends | Ransomware Developers Turn to Intermittent Encryption to Evade Detection</a>. Why encrypt entire files or every file when encrypting parts of files still achieves the same effect with greater speed and fewer detections?</li>
<li><a href="https://www.mandiant.com/company/press-releases/google-completes-mandiant-acquisition" target="_blank">Google Completes Acquisition of Mandiant</a>. First FireEye, now Google. Kevin Mandia must be Scrooge McDuck-ing into a pool of gold coins at this point.</li>
<li><a href="https://blog.thinkst.com/2022/09/sensitive-command-token-so-much-offense.html" target="_blank">Sensitive Command Token - So much offense in my defense</a>. There is a new Canary token for commands executed on Windows.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.kyleavery.com/posts/avoiding-memory-scanners/" target="_blank">Avoiding Memory Scanners</a> This is a written version of the presentation/deck (<a href="https://media.defcon.org/DEF%20CON%2030/DEF%20CON%2030%20presentations/Kyle%20Avery%20-%20Avoiding%20Memory%20Scanners%20Customizing%20Malware%20to%20Evade%20YARA%20PE-sieve%20and%20More.pdf" target="_blank">[PDF] Avoiding Memory Scanners - Customizing Malware to Evade YARA, PE-sieve, and More</a>) and DEF CON presentation.</li>
<li><a href="https://adepts.of0x.cc/novnc-phishing/" target="_blank">Thoughts on the use of noVNC for phishing campaigns</a>. Last week's EvilnoVNC has some flaws. I think with some more customization and effort, "browser emulation phishing" has its place, especially as login portals get better and better at defeating malicious reverse proxies.</li>
<li><a href="https://bishopfox.com/blog/unredacter-winner" target="_blank">Solving the Unredacter Challenge</a>. This is your weekly reminder to only redact with black boxes.</li>
<li><a href="https://n4r1b.com/posts/2022/09/smart-app-control-internals-part-2/" target="_blank">Smart App Control Internals (Part 2)</a>. Deep dive into the internals of the new Windows Security feature: "Smart App Control."</li>
<li><a href="https://swarm.ptsecurity.com/fork-bomb-for-flutter/" target="_blank">Fork Bomb for Flutter</a>. This post discusses the creation of <a href="https://github.com/Impact-I/Reflutter" target="_blank">reFlutter</a>, the Flutter Reverse Engineering Framework.</li>
<li><a href="https://posts.specterops.io/get-your-socks-on-with-gtunnel-4a70a9b82b24" target="_blank">Get Your SOCKS on with gTunnel</a>. Steps to setup a wicked fast SOCKS proxy with a tool called gTunnel.</li>
<li><a href="https://posts.specterops.io/wmi-internals-part-3-38e5dad016be" target="_blank">WMI Internals Part 3</a>. This blog looks at what happens after the COM method ITaskServices:NewTask.</li>
<li><a href="https://www.trustedsec.com/blog/video-blog-using-dll-persist-to-avoid-detection/" target="_blank">Video Blog: Using DLL Persist to Avoid Detection</a>. "During an Incident Response case, the TrustedSec IR team came across a novel method used by an attacker to maintain access to the target's servers. After gaining access to the systems, the attacker then modified a DLL required by a service to include malicious code. This video demonstrates a similar process for embedding malicious code into a benign DLL to create a method of persistence that is not easily detected." Not sure I love the video blog format.</li>
<li><a href="https://unit42.paloaltonetworks.com/credential-gathering-third-party-software/" target="_blank">Credential Gathering From Third-Party Software</a>. A nice quick reference guide for red teamers.</li>
<li><a href="https://www.x86matthew.com/view_post?id=writeprocessmemory_apc" target="_blank">WriteProcessMemoryAPC - Write memory to a remote process using APC calls</a>. Does what it says on the tin.</li>
<li><a href="https://medium.com/@bobbyrsec/gifshell-covert-attack-chain-and-c2-utilizing-microsoft-teams-gifs-1618c4e64ed7" target="_blank">"GIFShell" — Covert Attack Chain and C2 Utilizing Microsoft Teams GIFs</a>. GIFShell allows an attacker to create a reverse shell that delivers malicious commands via base64 encoded GIFs in Teams, and exfiltrates the output through GIFs retrieved by Microsoft's own infrastructure. 3rd party C2 is on the rise and here to stay.</li>
<li><a href="https://github.com/parsdefense/CVE-2022-22629" target="_blank">CVE-2022-22629</a>. This post is about the poc for the WebGL bug that was patched in Safari 15.4 security updates. See related: <a href="https://starlabs.sg/blog/2022/09-step-by-step-walkthrough-of-cve-2022-32792/" target="_blank">Step-by-Step Walkthrough of CVE-2022-32792 - WebKit B3ReduceStrength Out-of-Bounds Write</a>.</li>
<li><a href="https://taggart-tech.com/quasar-electron/" target="_blank">Quasar: Compromising Electron Apps</a>. This post introduces a tool for backdooring electron app's ASAR archives: <a href="https://github.com/mttaggart/quasar" target="_blank">quASAR</a>.</li>
<li><a href="https://frame.work/products/ethernet-expansion-card" target="_blank">New 2.5G Ethernet Expansion Card for Framework Laptops</a>. If you haven't seen the framework laptop, check it out. I hope they can make it in the much attempted but never sustained reparable tech space.</li>
<li><a href="https://twitter.com/fce365/status/1568146652246036480" target="_blank">GeoSn0w demos his blizzard jailbreak on ios 15 and 16 booting from custom app</a>. This should allow iPhone X and older devices to boot into a jailbroken state on any iOS version, a boon for researchers.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://blog.checkymander.com/red%20team/c2/Athena-0-2/" target="_blank">Athena v0.2</a>. A big update to an up and coming Mythic C2 agent.</li>
<li><a href="https://www.ihteam.net/advisory/pfblockerng-unauth-rce-vulnerability/" target="_blank">pfBlockerNG Unauth RCE Vulnerability</a>. This is only vulnerable on the LAN side of the firewall, unless you have some strange WAN rules that allow access to the pfblockerNG pages from WAN. Patched in 2022-06, its still a bad vulnerability. Poc <a href="https://iht.li/paste.php?hash=WWATN" target="_blank">here</a>.</li>
<li><a href="https://labs.jumpsec.com/quest-kace-desktop-authority-pre-auth-remote-code-execution-cve-2021-44031/" target="_blank">QUEST KACE Desktop Authority Pre-Auth Remote Code Execution (CVE-2021-44031)</a>. Pre-Auth RCE is the flavor of the week it seems.</li>
<li><a href="https://research.nccgroup.com/2022/09/07/tool-release-monkey365/" target="_blank">Tool Release - Monkey365</a>. Monkey 365 is an Open Source security tool that can be used to easily conduct not only Microsoft 365, but also Azure subscriptions and Azure Active Directory security configuration reviews without the significant overhead of learning tool APIs or complex admin panels from the start.</li>
<li><a href="https://github.com/10TG/vulnerabilities/blob/main/Netgear/CVE-2022-30078/CVE-2022-30078.md" target="_blank">Command injection vulnerability in Netgear R6200_v2 and R6300v2 routers</a>. Authenticated and LAN side only it looks like.</li>
<li><a href="https://github.com/PayloadSecurity/Sandbox_Scryer" target="_blank">Sandbox_Scryer</a> is an open-source tool for producing threat hunting and intelligence data from public sandbox detonation output The tool leverages the MITRE ATT&amp;CK Framework to organize and prioritize findings, assisting in the assembly of IOCs, understanding attack movement and in threat hunting.</li>
<li><a href="https://github.com/CodeXTF2/cobaltstrike-headless" target="_blank">cobaltstrike-headless</a> - Aggressorscript that turns the headless aggressor client into a (mostly) functional cobalt strike client.</li>
<li><a href="https://github.com/mohamedbenchikh/CVE-2022-27925" target="_blank">CVE-2022-27925</a> - Zimbra Unauthenticated Remote Code Execution Exploit (CVE-2022-27925)</li>
<li><a href="https://github.com/daem0nc0re/TangledWinExec" target="_blank">TangledWinExec</a> - This repository is for investigation of Windows process execution techniques. Most of PoCs are given a name corresponding to the technique. WmiSpawn is brand new and looks very interesting.</li>
<li><a href="https://github.com/iustin24/chameleon" target="_blank">chameleon</a> provides better content discovery by using wappalyzer's set of technology fingerprints alongside custom wordlists tailored to each detected technologies.</li>
<li><a href="https://github.com/CravateRouge/autobloody" target="_blank">autobloody</a> - Tool to automatically exploit Active Directory privilege escalation paths shown by BloodHound. "Automatic" and "Exploit" are two words that when used together cause me great concern.</li>
<li><a href="https://github.com/fin3ss3g0d/evilgophish" target="_blank">evilgophish</a> - evilginx2 + gophish.</li>
<li><a href="https://github.com/janoglezcampos/rust_syscalls" target="_blank">rust_syscalls</a> Single stub direct and indirect syscalling with runtime SSN resolving for windows.</li>
<li><a href="https://github.com/ryan-weil/HideProcessHook" target="_blank">HideProcessHook</a> - DLL that hooks the NtQuerySystemInformation API and hides a process name.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://containerssh.io/" target="_blank">ContainerSSH: Launch containers on demand</a>. ContainerSSH launches a new container for each SSH connection in Kubernetes, Podman, or Docker. The user is transparently dropped in the container and the container is removed when the user disconnects. Authentication and container configuration are dynamic using webhooks, no system users required.</li>
<li><a href="https://github.com/Flangvik/TeamFiltration" target="_blank">TeamFiltration</a> is a cross-platform framework for enumerating, spraying, exfiltrating, and backdooring O365 AAD accounts.</li>
<li><a href="https://github.com/ktock/buildg" target="_blank">buildg</a> - Interactive debugger for Dockerfile, with support for IDEs (VS Code, Emacs, Neovim, etc.).</li>
<li><a href="https://github.com/projectdiscovery/wappalyzergo" target="_blank">wappalyzergo</a> - A high performance go implementation of Wappalyzer Technology Detection Library.</li>
<li><a href="https://github.com/IcebreakerSecurity/Ekko_CFG_Bypass" target="_blank">Ekko_CFG_Bypass</a> A PoC for adding NtContinue to CFG allowed list in order to make Ekko work in a CFG protected process</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 420 (+0)</p>
<p>Blogs monitored: 323 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
