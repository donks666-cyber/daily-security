Title: Last Week in Security (LWiS) - 2024-12-09
Date: 2024-12-09 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2024-12-09
Author: Erik
Summary: Vuln finding with graphs (<a href="https://x.com/two06" target="_blank">@two06</a>), review of Postex kit (<a href="https://x.com/_RastaMouse" target="_blank">@_RastaMouse</a>), OpenWRT firmware upgrade vuln (<a href="https://x.com/ryotkak" target="_blank">@ryotkak</a>), iOS decompilation tool (<a href="https://x.com/lauriewired" target="_blank">@lauriewired</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2024-12-02 to 2024-12-09.</p>
<aside class="m-note m-success">
<h3>400 Security Blogs Monitored!</h3>
<p>As of this week, we now monitor 400 security blogs for content - all by hand. We have sponsorship slots available for next year, get in touch if you are interested! blog (at) badsectorlabs.com.</p>
<p>Curious what they are? <a href="https://blog.badsectorlabs.com/files/blogs.txt">Here's the list</a>.</p>
</aside>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.nbcnews.com/tech/security/us-officials-urge-americans-use-encrypted-apps-cyberattack-rcna182694" target="_blank">U.S. officials urge Americans to use encrypted apps amid unprecedented cyberattack</a> - "Encryption is your friend, whether it’s on text messaging or if you have the capacity to use encrypted voice communication" is not a sentence I would expect from the <a href="https://www.fbi.gov/about/mission/lawful-access" target="_blank">notoriously encryption unfriendly</a> FBI. To be fair the quote is from Jeff Green, executive assistant director for cybersecurity at the Cybersecurity and Infrastructure Security Agency, but the article said that Jeff and, "a senior FBI official who asked not to be named" recommend using encryption.</li>
<li><a href="https://learn.trustedsec.com/courses/cd84409a-36af-4507-be2c-ca7ad1e9fd2d" target="_blank">Beacon Object File (BOF) Development Course</a> - The first on-demand course from Trusted Sec, this course looks like a good one stop shop for BOF knowledge.</li>
<li><a href="https://llmailinject.azurewebsites.net/" target="_blank">LLMail-Inject: Adaptive Prompt Injection Challenge</a> - Microsoft invites you to try your hand at prompt injecting a simulated LLM-integrated email client. The goal is to get the email client to execute commands the email client "user" did not intend.</li>
<li><a href="https://msrc.microsoft.com/blog/2024/12/mitigating-ntlm-relay-attacks-by-default/" target="_blank">Mitigating NTLM Relay Attacks by Default</a> - Microsoft is enabling Extended Protection for Authentication (EPA) by default for Active Directory Certificate Services (AD CS) as well as the Light-Weight Directory Access Protocol (LDAP) service. NTLM is viewed as a legacy protocol, and is being phased out. Get those relay attacks in while you can!</li>
<li><a href="https://search.libraryofleaks.org/" target="_blank">Library of Leaks</a> - Distributed Denial of Secrets (DDoSecrets), a non-profit whistleblower organization, is commemorating its sixth anniversary with the unveiling of a search engine: the Library of Leaks. This searchable database provides access to millions of documents from numerous leaks, with an new entries being added daily.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://labs.watchtowr.com/where-theres-smoke-theres-fire-mitel-micollab-cve-2024-35286-cve-2024-41713-and-an-0day/" target="_blank">Where There’s Smoke, There’s Fire - Mitel MiCollab CVE-2024-35286, CVE-2024-41713 And An 0day</a> - A fun journey from CVE description to arbitrary file read (fresh 0day). Since its watchtowr, of course there is a nice PoC: <a href="https://github.com/watchtowrlabs/Mitel-MiCollab-Auth-Bypass_CVE-2024-41713?ref=labs.watchtowr.com" target="_blank">Mitel-MiCollab-Auth-Bypass_CVE-2024-41713</a>.</li>
<li><a href="https://blog.doyensec.com/2024/12/03/cspt-with-eval-villain.html" target="_blank">CSPT the Eval Villain Way!</a> - Client side path traversal (CSPT) can lead to cross site request forgery (CSRF) (<a href="https://blog.doyensec.com/2024/07/02/cspt2csrf.html" target="_blank">here</a> is a referesher if you need it), and now there is a playground and browser extension to play around with a vulnerable app.</li>
<li><a href="https://www.mdsec.co.uk/2024/12/extracting-account-connectivity-credentials-accs-from-symantec-management-agent-aka-altiris/" target="_blank">Extracting Account Connectivity Credentials (ACCs) from Symantec Management Agent (aka Altiris)</a> - This kind of deep dive is what separates a real red team from a penetration test. When faced with a hardened client, the team at MDSec dug into software on the endpoint, challenged assumptions, and ended up with a sweet privilege escalation. They even shared the tool: <a href="https://github.com/mdsecactivebreach/evilaltiris" target="_blank">evilaltiris</a>.</li>
<li><a href="https://www.rapid7.com/globalassets/_pdfs/research/pwn2own-iot-2024-lorex-2k-indoor-wi-fi-security-camera-research.pdf" target="_blank">[PDF] Pwn2Own IoT 2024 -Lorex 2K Indoor Wi-FiSecurityCamera</a> - A very in-depth exploit development whitepaper for an IoT device. Exploit: <a href="https://github.com/sfewer-r7/LorexExploit" target="_blank">LorexExploit</a>.</li>
<li><a href="https://trustedsec.com/blog/discovering-a-deserialization-vulnerability-in-linqpad" target="_blank">Discovering a Deserialization Vulnerability in LINQPad</a> - While the exploit itself is standard fare, the discovery method is novel. Mapping function calls into a graph database and using it to find callers is a novel approach to vulnerability identification.</li>
<li><a href="https://swarm.ptsecurity.com/new-dog-old-tricks-damagecard-attack-targets-memory-directly-thru-sd-card-reader/" target="_blank">New dog, old tricks: DaMAgeCard attack targets memory directly thru SD card reader</a> - A great history of direct memory attacks and a new method using the SD card.</li>
<li><a href="https://rastamouse.me/cobalt-strike-postex-kit/" target="_blank">Cobalt Strike Postex Kit</a> - Another post from Rasta about a newer feature in Cobalt Strike, the Postex kit that allows you to create your own reflective DLLs and communicate with them via pipes.</li>
<li><a href="https://flatt.tech/research/posts/compromising-openwrt-supply-chain-sha256-collision/" target="_blank">Compromising OpenWrt Supply Chain via Truncated SHA-256 Collision and Command Injection</a> - Using just the first 8 characters of a SHA256 hash allowed for the build cache to be poisoned and potentially malicious builds to be delivered to users requesting upgrades. This was patched and no malicious requests were found in build logs.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Teach2Breach/snapinject_rs" target="_blank">snapinject_rs</a> - A process injection using process snapshotting based on <a href="https://gitlab.com/ORCA000/snaploader" target="_blank">SnapLoader</a>, in rust.</li>
<li><a href="https://github.com/ricardojoserf/NativeBypassCredGuard" target="_blank">NativeBypassCredGuard</a> - Bypass Credential Guard by patching WDigest.dll using only NTAPI functions. More info in the <a href="https://ricardojoserf.github.io/nativebypasscredguard/" target="_blank">blog post</a>.</li>
<li><a href="https://github.com/Slowerzs/CryptDecryptMemory" target="_blank">CryptDecryptMemory</a> - A proof of concept that encrypts memory using CryptProtectMemory with the CRYPTPROTECTMEMORY_SAME_PROCESS flag, and then decrypts it without calling the API again. Must be run with SeDebugPrivilege. See the <a href="https://blog.slowerzs.net/posts/cryptdecryptmemory/" target="_blank">blog post</a> for more details.</li>
<li><a href="https://github.com/almounah/superdeye" target="_blank">superdeye</a> - Indirect Syscall with TartarusGate Approach in Go</li>
<li><a href="https://github.com/ZephrFish/QoL-BOFs" target="_blank">QoL-BOFs</a> - Curated list of public Beacon Object Files(BOFs) build in as submodules for easy cloning</li>
<li><a href="https://github.com/referefref/Rusty-Telephone" target="_blank">Rusty-Telephone</a> - Exfiltrate data over audio output from remote desktop sessions - Covert channel PoC</li>
<li><a href="https://github.com/tehstoni/LexiCrypt" target="_blank">LexiCrypt</a> - Shellcode encryptor using a substitution cipher with a randomly generated key.</li>
<li><a href="https://github.com/rad9800/BootExecuteEDR" target="_blank">BootExecuteEDR</a> - Boot Execute allows native applications—executables with the NtProcessStartup entry point and dependencies solely on ntdll.dll—to run prior to the complete initialization of the Windows operating system. This occurs even before Windows services are launched. Historically, attackers have exploited this mechanism as a rudimentary persistence method. However, utilizing this feature requires administrative privileges, both to modify the corresponding registry key and to place the executable within the %SystemRoot%System32 directory.</li>
<li><a href="https://github.com/LaurieWired/Malimite" target="_blank">Malimite</a> - iOS Decompiler.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/zh54321/SnafflerParser" target="_blank">SnafflerParser</a> - Parses Snaffler output file and generate beautified outputs.</li>
<li><a href="https://github.com/C5Hackr/c_syscalls" target="_blank">c_syscalls</a> - Single stub direct and indirect syscalling with runtime SSN resolving for windows.</li>
<li><a href="https://github.com/zh54321/EntraTokenAid" target="_blank">EntraTokenAid</a> - A pure PowerShell solution for Entra OAuth authentication, enabling easy retrieval of access and refresh tokens</li>
<li><a href="https://github.com/Aegrah/PANIX" target="_blank">PANIX</a> - Customizable Linux Persistence Tool for Security Research and Detection Engineering.</li>
<li><a href="https://github.com/tjnull/TJ-OPT" target="_blank">TJ-OPT</a> - This repo contains a pentesting template used in PWK and for current assessments. The template has been formatted to be used in Obsidian.</li>
<li><a href="https://github.com/markkcc/crxaminer" target="_blank">crxaminer</a> - Examine Chrome extensions for security issues.</li>
<li><a href="https://github.com/hfiref0x/WinDepends" target="_blank">WinDepends</a> - Windows Dependencies.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 441 (+0)</p>
<p>Blogs monitored: 400 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
