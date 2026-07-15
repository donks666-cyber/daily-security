Title: Last Week in Security (LWiS) - 2021-12-07
Date: 2021-12-07 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-12-07
Author: Erik
Summary: Windows LPE 0day (<a href="https://twitter.com/KLINIX5" target="_blank">@KLINIX5</a>), Windows 10 URI handler "RCE" (<a href="https://twitter.com/positive_sec" target="_blank">@positive_sec</a>), detect anomalous TLS certs with ML (<a href="https://twitter.com/NCCGroupInfosec" target="_blank">@NCCGroupInfosec</a>), USB-over-ethernet vuln (<a href="https://twitter.com/kasifdekel" target="_blank">@kasifdekel</a>), bitlocker key leak (<a href="https://twitter.com/theluemmel" target="_blank">@theluemmel</a>), Linux TIPC LPE (<a href="https://twitter.com/bl4sty" target="_blank">@bl4sty</a>), Tartarus' Gate (<a href="https://twitter.com/trickster012" target="_blank">@trickster012</a>), abusing SecLogon (<a href="https://twitter.com/splinter_code" target="_blank">@splinter_code</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-11-22 to 2021-12-07.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.cnn.com/2021/12/05/politics/us-cyber-command-disrupt-ransomware-operations/index.html" target="_blank">US military's hacking unit publicly acknowledges taking offensive action to disrupt ransomware operations</a>. Consider the hounds released.</li>
<li><a href="https://www.justice.gov/usao-sdny/pr/former-employee-technology-company-charged-stealing-confidential-data-and-extorting" target="_blank">Former Employee Of Technology Company Charged With Stealing Confidential Data And Extorting Company For Ransom While Posing As Anonymous Attacker</a>. The Ubiquiti hack/breach/whatever from last year was actually an insider who demanded 50 bitcoin as ransom during the attack. He now faces up to 37 years in prison.</li>
<li><a href="https://techcommunity.microsoft.com/t5/articles/introducing-buy-now-pay-later-in-microsoft-edge/m-p/2967030" target="_blank">Introducing Buy now, pay later in Microsoft Edge</a>. Predatory lending coming to a browser near you by default!</li>
<li><a href="https://www.sec.gov/Archives/edgar/data/1609711/000160971121000122/gddyblogpostnov222021.htm" target="_blank">GoDaddy Announces Security Incident Affecting Managed WordPress Service</a>. GoDaddy has been riding the high of its first mover advantage for about two decades now. Don't worry breach bingo players, "GoDaddy leadership and employees take our responsibility to protect our customers’ data very seriously."</li>
<li><a href="https://www.vice.com/en/article/5dggxk/us-state-department-employees-targeted-with-nso-group-malware" target="_blank">US State Department Employees Targeted with NSO Group Malware</a>. After being heavily sanctioned, details about US based attacks are coming out. NSO groups woes continue to mount with <a href="https://www.apple.com/newsroom/2021/11/apple-sues-nso-group-to-curb-the-abuse-of-state-sponsored-spyware/" target="_blank">Apple suing them</a>.</li>
<li><a href="https://nusenu.medium.com/is-kax17-performing-de-anonymization-attacks-against-tor-users-42e566defce8" target="_blank">Is “KAX17” performing de-anonymization Attacks against Tor Users?</a>. Someone spend a fair amount of money to run a lot of Tor middle nodes, but have since been subject to a mass <a href="https://lists.torproject.org/pipermail/tor-relays/2021-November/019980.html" target="_blank">rejection of relays</a>. Tin foil hats on to guess who may be behind this.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://aptw.tf/2021/11/25/c2-redirectors-using-caddy.html" target="_blank">Carrying the Tortellini's golf sticks - Using Caddy to spin up fast and reliable C2 redirectors.</a> While Apache and Nginx are the most common redirectors, Caddy is a light weight web server that can be used as a redirector as well. This post details some helpful configuration options you should look into if you go down this route. Be care of the more unique JA3S hash though. Since caddy is written in Go and open source, this can be changed (with something like <a href="https://github.com/CUCyber/ja3transport" target="_blank">this</a> for the server side).</li>
<li><a href="https://positive.security/blog/ms-officecmd-rce" target="_blank">Windows 10 RCE: The exploit is in the link</a>. Fabian and Lukas found that the default handler for <cite>ms-officecmd:</cite> URIs allows argument injection. Typical bug bounty payment shenanigans followed. There are great details about the process of finding the bug and exploiting it in this post - don't skip it.</li>
<li><a href="https://blog.fox-it.com/2021/12/07/encryption-does-not-equal-invisibility-detecting-anomalous-tls-certificates-with-the-half-space-trees-algorithm/" target="_blank">Encryption Does Not Equal Invisibility – Detecting Anomalous TLS Certificates with the Half-Space-Trees Algorithm</a>. Much like JA3 and JA3S, TLS metadata about certificates can be extremely useful for detecting anomalies.</li>
<li><a href="https://www.gosecure.net/blog/2021/12/03/trickbot-leverages-zoom-work-from-home-interview-malspam-heavens-gate-and-spamhaus/" target="_blank">TrickBot Leverages Zoom Work from Home Interview Malspam, Heaven’s Gate and… Spamhaus?</a>. Trickbot is back with a nifty LNK+loader campaign. Threat emulator take note.</li>
<li><a href="https://security.googleblog.com/2021/12/exploring-container-security-storage.html" target="_blank">Exploring Container Security: A Storage Vulnerability Deep Dive</a>. Containers are taking over the DevOps world, best learn how to exploit them.</li>
<li><a href="https://www.sentinelone.com/labs/usb-over-ethernet-multiple-privilege-escalation-vulnerabilities-in-aws-and-other-major-cloud-services/" target="_blank">USB Over Ethernet | Multiple Vulnerabilities in AWS and Other Major Cloud Services</a>. Some base libraries used in many remote desktop services has a vulnerability that can be triggered from sandboxes (i.e. web browsers).</li>
<li><a href="https://luemmelsec.github.io/Go-away-BitLocker-you-are-drunk/" target="_blank">Go away BitLocker, you´re drunk</a>. You've read some stories about leaking bitlocker keys, but they lacked memes and snark. I believe this is the third bitlocker hardware hack post on LWiS. Have you added a second factor to your bitlocker deployment yet?</li>
<li><a href="https://trickster0.github.io/posts/Halo's-Gate-Evolves-to-Tartarus-Gate/" target="_blank">Halo's Gate Evolves -&gt; Tartarus' Gate</a>. This new "gate" adds a check for a different type of hook used by an EDR vendor. Code <a href="https://github.com/trickster0/TartarusGate" target="_blank">here</a>.</li>
<li><a href="https://posts.specterops.io/azure-privilege-escalation-via-azure-api-permissions-abuse-74aee1006f48" target="_blank">Azure Privilege Escalation via Azure API Permissions Abuse</a>. At this point I'm convinced that each "cloud" is it's own entire security research domain.</li>
<li><a href="https://splintercod3.blogspot.com/p/the-hidden-side-of-seclogon-part-2.html" target="_blank">The hidden side of Seclogon part 2: Abusing leaked handles to dump LSASS memory</a>. This is a fresh take on credential dumping with a PoC available: <a href="https://github.com/antonioCoco/MalSeclogon" target="_blank">MalSeclogon</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/klinix5/InstallerFileTakeOver" target="_blank">InstallerFileTakeOver</a> is a Windows LPE 0day for all supported Windows version. RIP.</li>
<li><a href="https://github.com/shmuelamar/cracken" target="_blank">cracken</a> is a fast password wordlist generator, Smartlist creation and password hybrid-mask analysis tool written in pure safe Rust.</li>
<li><a href="https://haxx.in/posts/pwning-tipc/" target="_blank">Exploiting CVE-2021-43267</a>. This is a walkthrough and full exploit for Linux <a href="https://www.sentinelone.com/labs/tipc-remote-linux-kernel-heap-overflow-allows-arbitrary-code-execution/" target="_blank">TIPC vulnerabilitiy</a> that affects kernels between 5.10-rc1 and 5.15.</li>
<li><a href="https://github.com/wavestone-cdt/EDRSandblast" target="_blank">EDRSandblast</a> is a tool written in C that weaponize a vulnerable signed driver to bypass EDR detections (Kernel callbacks and ETW TI provider) and LSASS protections. Multiple userland unhooking techniques are also implemented to evade userland monitoring.</li>
<li><a href="https://github.com/skahwah/SSHClient" target="_blank">SSHClient</a> is a small SSH client written in C#. May be useful for pivoting from Windows to Linux.</li>
<li><a href="https://github.com/cedowens/EntitlementCheck" target="_blank">EntitlementCheck</a> is a Python3 script for macOS to recursively check /Applications and also check /usr/local/bin, /usr/bin, and /usr/sbin for binaries with problematic/interesting entitlements. Also checks for hardened runtime enablement.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/cyberdefenders/DetectionLabELK" target="_blank">DetectionLabELK</a> is a fork of <a href="https://github.com/clong/DetectionLab" target="_blank">DetectionLab</a> with ELK stack instead of Splunk.</li>
<li><a href="https://github.com/nodauf/GoMapEnum" target="_blank">GoMapEnum</a> is a user enumeration (Linkedin) and password bruteforcer for Azure, ADFS, OWA, O365, and Teams.</li>
<li><a href="https://github.com/redherd-project/redherd-framework" target="_blank">redherd-framework</a> is a collaborative and serverless framework for orchestrating a geographically distributed group of assets capable of simulating complex offensive cyberspace operations.</li>
<li><a href="https://github.com/emalderson/ThePhish#installation" target="_blank">ThePhish</a> is an automated phishing email analysis tool based on TheHive, Cortex and MISP. It is a web application written in Python 3 and based on Flask that automates the entire analysis process starting from the extraction of the observables from the header and the body of an email to the elaboration of a verdict which is final in most cases.</li>
<li><a href="https://github.com/FalconForceTeam/BOF2shellcode" target="_blank">BOF2shellcode</a> is a POC tool to convert CobaltStrike BOF files to raw shellcode.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
